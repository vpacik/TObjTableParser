from TObjectTable import TObjectTable, TObjectEntry
from parser import *

print("=== Parser ===")
# filepath = "test/single.txt"
# filepath = "test/out"
# filepath = "test/out_perEvent_10"
# filepath = "test/out_perEvent_100"
filepath = "test/out_hook_all_1"

instances = parse_file(filepath,stats=True,hook="TObjectTable::")

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


# print("===== Making diffs ===============================")
# diff_instances = []
#
# for i in range(len(instances)-1) :
#     diff_table = instances[i].diff(instances[i+1])
#     diff_instances.append(diff_table)
#     print(diff_table)
#
# print("==================================================")


# print("Testing diff")
# first = instances[1]
# second = instances[2]
# diff = first.diff(second)
#
# key = 'TClonesArray'
# print("=====")
# print("first")
# print(first[key])
# print("second")
# print(second[key])
# print("diff")
# print(diff[key])
# print("=====")

# print(first)
# print(second)
# print(diff)
# diff.list()
print("Done");
