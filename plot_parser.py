import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from TObjectTable import TObjectTable, TObjectEntry
from parser import *

gDebug = False

print("###### Parser ######")

filepaths = [
    "test/single.txt"
]

frames = []

for path in filepaths :
    # parsing raw input
    instances = parse_file(path,stats=False)

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

f, axes = plt.subplots(1, 1, sharey=True, sharex=True, figsize=(4, 4))
sns.scatterplot(x='index', y='sizeHeap',data=frames[0],hue='notes',ax=axes)

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
