def process_line(line) :
    """
    """
    # print(line,end='')
    newline = line.split()
    # print(newline)

    object = str(newline[0])
    countTot = int(newline[1])
    countHeap = int(newline[2])
    sizeSingle = int(newline[3])
    sizeTot = int(newline[4])
    sizeHeap = int(newline[5])

    return (object, countTot, countHeap, sizeSingle, sizeTot, sizeHeap)

def check_start(line,file) :
    if not line.startswith('Object statistics') :
        return False

    line = next(file)
    if not line.startswith('class') :
        return False

    line = next(file)
    if not line.startswith('======') :
        return False

    return True

def check_end(line,file) :
    if not line.startswith('-------') :
        return False

    line = next(file)
    if not line.startswith('Total:') :
        return False

    line = next(file)
    if not line.startswith('=======') :
        return False

    return True

def parse_file(filepath) :
    """
    """

    print("=====  Parsing file content  ======================================")
    print

    with open(filepath, 'r') as file :
        within = False
        listInstances = []

        line = next(file)
        while line :
            if not within :
                if check_start(line,file) :
                    print(' --- Start found!')
                    within = True
                    newInstance = list()
                    line = next(file)

            if within :
                if check_end(line,file) :
                    print(' --- End found!')
                    within = False
                    listInstances.append(newInstance)
                    line = next(file)

            if within :
                obj = process_line(line)
                print(obj)
                newInstance.append(obj)

            line = next(file,None)

        print("=====  Parsing finised  =======================================")
        print("Found %d instances" % len(listInstances))
        # print(listInstances)


        print("=====  Instances   ============================================")
        for i,ins in enumerate(listInstances) :
            print("\n----- Printing instance %d with %d entries ----------------" % (i,len(ins)))
            print(ins)

    return listInstances

print("=== Parser ===")
# filepath = "test/single.txt"
filepath = "test/out"
instances = parse_file(filepath)

print("Parsing finished!")
print(len(instances))

print(instances[0][0][1])

print("Done");
