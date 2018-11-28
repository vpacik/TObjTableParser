import numpy as np
import pandas as pd

from TObjectTable import TObjectTable, TObjectEntry, diff
from parser import *

gDebug = False

print("###### Parser ######")
# filepath = "test/single.txt"
# filepath = "test/out"
# filepath = "test/out_perEvent_10"
# filepath = "test/out_perEvent_100"
# filepath = "test/out_hook_all_20"
# filepath = "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/out/out_old/out_gridtest_wCor_all_full"
filepath = "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/out/out_3/out_gridtest_wCorQAweight_all_100"
# filepath = "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/out_gridtest_wCor_all_100"
# filepath = "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/out_gridtest_wCor_all_full"
# filepath = "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/gridTest/stdout"

instances = parse_file(filepath,stats=False,hook="TObjectTable::")

list_instances_total = [ i.total for i in instances ]
list_notes = [ i.note for i in instances]

if gDebug : print(list_notes)

# testing diffs between end of event and start of event

inst_start = {}
inst_end = {}
inst_diff = {}

index_start = 0
index_end = 0

for idx,inst in enumerate(instances) :
    # print("%d: " % idx, end='')
    # print(inst)

    note = inst.note

    if note.startswith('UserExec: start') :
        index_start = idx
        if gDebug : print("%d : start found" % index_start )
        continue

    if note.startswith('UserExec: end') :
        index_end = idx
        if gDebug : print("%d : end found" % index_end)
        inst_end[str(index_end)] = inst

        start = instances[index_start]
        inst_start[str(index_start)] = start

        table_diff = diff(start,inst)
        inst_diff[str(index_end)] = table_diff

# print(inst_start)
# print(inst_end)

for i,key in inst_diff.items() :
    if key.total.countTot != 0 :
        print("%s : " % i,end='')
        print(key)
        key.list()

# testing diffs between UserExec: start

print("### Testing diffs between starts")
inst_diff_start = []

for i in range(len(inst_start)-1) :
    inst = list(inst_start.values())
    # print(inst)
    table_diff = diff(inst[i],inst[i+1])
    inst_diff_start.append(table_diff)
    if table_diff.total.countTot != 0 :
        print(i,end=": ")
        print(table_diff)
        table_diff.list()

# print("double_diff")
# double_diff = diff(inst_diff['8'],inst_diff['13'])
# print(double_diff)
# double_diff.list()
#
#
# print("Positive entries")
# list_pos = [ obj for i,obj in double_diff.inst.items() if obj.countTot > 0]
# for i in list_pos : print(i)
#
# print("Negative entries")
# list_neg = [ obj for i,obj in double_diff.inst.items() if obj.countTot < 0]
# for i in list_neg : print(i)


# # getting individual variables for plotting
# list_sizeHeap = [ i.sizeHeap for i in list_instances_total]
# if gDebug : print(list_sizeHeap)
#
# list_countHeap = [ i.countHeap for i in list_instances_total]
# if gDebug : print(list_countHeap)
#
# # converting data to DataFrame
# d = { 'index' : x, 'sizeHeap' : list_sizeHeap, 'countHeap' : list_countHeap, 'notes' : list_notes }
# if gDebug : print(d)
#
# df = pd.DataFrame(d)
# print(df.head())


print("########################")
