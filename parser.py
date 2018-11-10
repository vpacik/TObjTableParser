from collections import namedtuple

TObject = namedtuple("TObject", ['object','countTot','countHeap','sizeSingle','sizeTot','sizeHeap'] ,verbose=False)

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

    return TObject(object=object,countTot=countTot, countHeap=countHeap, sizeSingle=sizeSingle, sizeTot=sizeTot, sizeHeap=sizeHeap)
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
        return False

    line = next(file)
    if not line.startswith('Total:') :
        return False

    line = next(file)
    if not line.startswith('=======') :
        return False

    return True
################################################################################
def parse_file(filepath) :
    """
    Takes a single file and parse it looking for TObjTable contents.
    Each TObjTable output (instance) is processed into single dictionary.
    Returns a list (of dictionaries) of parsed TObjTable instances.
    """

    print("=====  Parsing file content  ======================================")

    with open(filepath, 'r') as file :
        within = False
        listInstances = []

        line = next(file)
        while line :
            if not within :
                if check_start(line,file) :
                    print(' --- Start found!')
                    within = True
                    newInstance = dict()
                    line = next(file)

            if within :
                if check_end(line,file) :
                    print(' --- End found!')
                    within = False
                    listInstances.append(newInstance)
                    line = next(file)

            if within :
                obj = process_line(line)
                newInstance[obj.object] = obj
                # print(line,end='')
                # print(obj)

            line = next(file,None)

        print("=====  Parsing finised  =======================================")
        print("Found %d instances" % len(listInstances))
        # print(listInstances)


        print("=====  Instances   ============================================")
        for i,ins in enumerate(listInstances) :
            print("\n----- Printing instance %d with %d entries ----------------" % (i,len(ins)))
            print(ins)

    return listInstances

################################################################################
def print_inst(instance) :
    """
    Print out content of TObjectTable instance in 'user-friendly' way
    """

    print("=====  Printing instance with %d entries ============================================" % len(instance))

    for keys,values in  instance.items() :
        print(values)

    print("=====================================================================")

################################################################################
print("=== Parser ===")
filepath = "test/single.txt"
# filepath = "test/out"
instances = parse_file(filepath)

print("Parsing finished!")
print("Found %d instance(s)" % len(instances))

# print(instances)

firstInst = instances[0];
print("Printing first instance with %d entries" % len(firstInst))
# print(firstInst)
print_inst(firstInst)

print("Printing TFile TObject")
firstObj = firstInst['TFile'];
print(firstObj)
print(firstObj.object)
print(firstObj.sizeHeap)


print();
# print(instances[0]['TFile'])
# print(instances[0].keys())

print("Done");
