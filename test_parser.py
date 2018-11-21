from TObjectTable import TObjectTable, TObjectEntry
from parser import *

print("=== Parser ===")
# filepath = "test/single.txt"
filepath = "test/out"
# filepath = "test/out_perEvent_10"
# filepath = "test/out_perEvent_100"

instances = parse_file(filepath,stats=True)



# NB : printing first instance
# firstInst = instances[0];
# print("Printing first instance with %d entries" % len(firstInst))
# print(firstInst)
# print_inst(firstInst)

# NB: simple example of search-up
# print("Printing TFile TObject")
# firstObj = firstInst['TFile'];
# print(firstObj)
# print(firstObj.object)
# print(firstObj.sizeHeap)

print("Testing diff")
first = instances[1]
second = instances[2]
diff = first.diff(second)

key = 'TClonesArray'
print("=====")
print("first")
print(first[key])
print("second")
print(second[key])
print("diff")
print(diff[key])
print("=====")

# print(first)
# print(second)
# print(diff)
# diff.list()
print("Done");
