from TObjectTable import TObjectTable, TObjectEntry
################################################################################
def process_line(line) :
    """
    Process a single 'line' of TObjTable output and returns it as a single tuple.
    """
    newline = line.split()

    object = str(newline[0])
    countTot = int(newline[1])
    countHeap = int(newline[2])
    sizeSingle = int(newline[3])
    sizeTot = int(newline[4])
    sizeHeap = int(newline[5])

    return TObjectEntry(object=object,countTot=countTot, countHeap=countHeap, sizeSingle=sizeSingle, sizeTot=sizeTot, sizeHeap=sizeHeap)
################################################################################
def check_start(line,file) :
    """
    Checks if current (and few subsequent) 'line' in input 'file' is start of TObjTable output.
    Return True if so, False otherwise.
    """
    if not line.startswith('Object statistics') :
        return False

    line = next(file)
    if not line.startswith('class') :
        return False

    line = next(file)
    if not line.startswith('======') :
        return False

    return True
################################################################################
def check_end(line,file) :
    """
    Checks if current (and few subsequent) 'line' in input 'file' is end of TObjTable output.
    Returns True if so, False othrewise.
    """
    if not line.startswith('-------') :
        return False, 0

    line = next(file)
    if not line.startswith('Total:') :
        return False, 0

    obj = process_line(line)

    line = next(file)
    if not line.startswith('=======') :
        return False, 0

    return True, obj
################################################################################
def parse_file(filepath,stats=False,debug=False) :
    """
    Takes a single file and parse it looking for TObjTable contents.
    Each TObjTable output (instance) is processed into single dictionary.
    Returns a list (of dictionaries) of parsed TObjTable instances.
    """

    print("=====  Parsing file '%s' content  ======================================" % str(filepath))

    with open(filepath, 'r') as file :
        within = False
        listInstances = []

        line = next(file)
        while line :
            if not within :
                if check_start(line,file) :
                    if debug : print(' --- Start found!')
                    within = True
                    newInstance = TObjectTable()
                    line = next(file)

            if within :
                is_end, obj = check_end(line,file)
                if is_end :
                    if debug : print(' --- End found!')
                    within = False
                    newInstance.set_summary(obj)
                    listInstances.append(newInstance)
                    line = next(file)

            if within :
                obj = process_line(line)
                newInstance.append(obj.object,obj)
                if debug :
                    print(line,end='')
                    print(obj)

            line = next(file,None)

        print("=====  Parsing finised! ", end='')
        print("Found %d instance(s) " % len(listInstances))
        if stats :
            for i,ins in enumerate(listInstances) :
                print("Instance %d (entries %d) : " %(i,len(ins)), end='');
                print(ins)
        print("================================================================")


        if debug :
            print("=====  Instances   ============================================")
            for i,ins in enumerate(listInstances) :
                print("\n----- Printing instance (index %d) with %d entries ----------------" % (i,len(ins)))
                print(ins)

    return listInstances

################################################################################
