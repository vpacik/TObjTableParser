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
filepath = "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/out_gridtest_wCor_all_full"
# filepath = "/Users/vpacik/Codes/ALICE/Flow/uniFlow/class/misc/testMem/gridTest/stdout"

# parsing raw input
# instances = parse_file(filepath,stats=False)
instances = parse_file(filepath,stats=False,hook="TObjectTable::")
list_instances_total = [ i.total for i in instances ]


# getting list of total 'sizeHeap' for plotting
list_sizeHeap = [ i.sizeHeap for i in list_instances_total]
if gDebug : print(list_sizeHeap)

list_notes = [ i.note for i in instances]

# translating list_sizeHeap into [x,y]
x = [ i for i in range(0,len(instances)) ]

# converting data to DataFrame
d = { 'index' : x, 'sizeHeap' : list_sizeHeap, 'notes' : list_notes }
if gDebug : print(d)

df = pd.DataFrame(d)
print(df.head())

sns.scatterplot(x='index', y='sizeHeap',data=df,hue='notes')

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
