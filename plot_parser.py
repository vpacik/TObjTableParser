import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from TObjectTable import TObjectTable, TObjectEntry
from parser import *

gDebug = False

print("###### Parser ######")
# filepath = "test/single.txt"
# filepath = "test/out"
# filepath = "test/out_perEvent_10"
# filepath = "test/out_perEvent_100"
# filepath = "test/out_hook_all_20"
# filepath = "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/out_gridtest_wCor_all_full"
# filepath = "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/gridTest/stdout"

filepaths = [
    "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/out_gridtest_wCor_all_0",
    "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/out_gridtest_wCor_all_100",
    "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/out_gridtest_wCor_all_full"
]

frames = []

for path in filepaths :
    # parsing raw input
    # instances = parse_file(filepath,stats=False)
    instances = parse_file(path,stats=False,hook="TObjectTable::")

    x = [ i for i in range(0,len(instances)) ]
    list_instances_total = [ i.total for i in instances ]
    list_notes = [ i.note for i in instances]

    # getting individual variables for plotting
    list_sizeHeap = [ i.sizeHeap for i in list_instances_total]
    if gDebug : print(list_sizeHeap)

    list_countHeap = [ i.countHeap for i in list_instances_total]
    if gDebug : print(list_countHeap)

    # converting data to DataFrame
    d = { 'index' : x, 'sizeHeap' : list_sizeHeap, 'countHeap' : list_countHeap, 'notes' : list_notes }
    if gDebug : print(d)

    df = pd.DataFrame(d)
    print(df.head())

    frames.append(df)

f, axes = plt.subplots(1, 3, sharey=True, figsize=(6, 4))
sns.scatterplot(x='index', y='sizeHeap',data=frames[0],hue='notes',ax=axes[0])
sns.scatterplot(x='index', y='sizeHeap',data=frames[1],hue='notes',ax=axes[1])
sns.scatterplot(x='index', y='sizeHeap',data=frames[2],hue='notes',ax=axes[2])

# # making diffs
# list_diffs = []
# for i in range(len(instances) - 1) :
#     this = instances[i]
#     next = instances[i+1]
#     diff = this.diff(next)
#     list_diffs.append(diff)
#     print("Diff %d :" % i,end=''); print(diff)
#
# list_diff_total = [i.total for i in list_diffs]
# print(list_diff_total)

# fig2, ax2 = plt.subplots(figsize=(12, 6))
# ax2.scatter(x,y)
plt.show()

print("########################")
