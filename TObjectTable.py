from collections import namedtuple


# ==============================================================================
# Single TObject entry from TObjectTable
TObjectEntry = namedtuple("TObjectEntry", ['object','countTot','countHeap','sizeSingle','sizeTot','sizeHeap'] ,verbose=False)
TObjectEntry.__new__.__defaults__ = (0,) * len(TObjectEntry._fields) # defaults setting

# ==============================================================================
def subtract_entries(first, second) :
    """
    Take two TObjectEntries of the same 'object' and return new one with difference 'second' - 'first'
    NB: 'object' & 'sizeSingle' are constant and thus taken from 'second' instance
    """

    if not isinstance(first, TObjectEntry) :
        raise TypeError("First is not an TObjectEntry but %s" % type(first))

    if not isinstance(first, TObjectEntry) :
        raise TypeError("Second is not an TObjectEntry but %s" % type(second))

    if first.object != second.object :
        raise TypeError("Entries with different 'object' data")

    if first.sizeSingle > 0 :
        object = first.object
        sizeSingle = first.sizeSingle
    elif second.sizeSingle > 0 :
        object = second.object
        sizeSingle = second.sizeSingle
    else :
        raise TypeError("Both TObjectEntries are empty")

    countTot = second.countTot - first.countTot
    countHeap = second.countHeap - first.countHeap
    sizeTot = second.sizeTot - first.sizeTot
    sizeHeap = second.sizeHeap - first.sizeHeap

    return TObjectEntry(object=object,countTot=countTot,countHeap=countHeap,sizeTot=sizeTot,sizeHeap=sizeHeap,sizeSingle=sizeSingle)

# ==============================================================================
class TObjectTable :
    """
    Implementation of single instance of TObjectTable
    """

    def __init__(self) :
        self.inst = dict()
        self.total = TObjectEntry('Total')
        self.note = None

    def __del__(self) :
        self.inst.clear()

    def __repr__(self) :
        return "TObjectTable()"

    def __str__(self) :
        return str(self.total) + " " + str(self.note)

    # NB: namedtuples are immutable
    # def __setitem__(self,key,value) :
        # self.inst.__setitem__(key,value)

    def __missing__(self,key) :
        return TObjectEntry(object=key,countTot=None,countHeap=None,sizeTot=None,sizeHeap=None,sizeSingle=None)

    def __getitem__(self,key) :
        if key not in self.inst :
            return self.__missing__(key)
        return self.inst.__getitem__(key)

    def __delitem__(self,key) :
        self.inst.__delitem__(key)

    def __iter__(self) :
        return self.inst.__iter__()

    def __reversed__(self) :
        return self.inst.__reversed__()

    def __contains__(self,key) :
        return self.inst.__contains__(key)

    def __len__(self) :
        """
        Return number of entries / elements in TObjectTable dict
        """
        return len(self.inst)

    def list(self,nozeros=True) :
        """
        List all the TObjectEntries in a Table
        """
        for key,obj in self.inst.items() :
            if nozeros and obj.countTot == 0 :
                continue

            print(obj)

    def append(self,key,value) :
        """
        Insert a new key-value pair into a dictionary
        """
        if key in self.inst :
            raise KeyError("Key '%s' already exists!" % key)

        self.inst.__setitem__(key,value)

    def set_summary(self,obj) :
        """
        Add a single TObjectEntry outside of dictionary for summary
        """
        self.total = obj

    def calc_summary(self) :
        """
        Sums individual TObjectEntries to calculate summary object
        """

        object = 'Total'
        countTot = 0
        countHeap = 0
        sizeTot = 0
        sizeHeap = 0
        sizeSingle = 0

        for key,obj in self.inst.items() :
            countTot += obj.countTot
            countHeap += obj.countHeap
            sizeHeap += obj.sizeHeap
            sizeTot += obj.sizeTot
            sizeSingle += obj.sizeSingle

        return TObjectEntry(object=object,countTot=countTot,countHeap=countHeap,sizeTot=sizeTot,sizeHeap=sizeHeap,sizeSingle=sizeSingle)


    def diff(self, table) :
        """
        Compares this Table to another one and return new Table containing (only non-zero-count) 'diff' TObjectEntries between them.
        Notation for counting: 'table' - 'self', i.e.
            - zero : when same
            - negative : when self.count > table.count
            - positive : when self.count < table.count
        """
        if not isinstance(table, TObjectTable) :
            raise TypeError("Not a TObjTable!")

        orig = self.inst
        latter = table.inst

        keys_orig = set(orig.keys())
        keys_latter = set(latter.keys())
        # keys_union = keys_orig.union(keys_latter)
        keys_inter = keys_orig.intersection(keys_latter)
        keys_diff = keys_latter.symmetric_difference(keys_orig)

        new_table = TObjectTable()
        new_table.note = str(table.note) + " / " + str(self.note)

        # looping over intersection of the keys of the two Tables to subtract its entries
        for key in keys_inter :
            diff_entry = subtract_entries(self[key],latter[key])
            new_table.append(diff_entry.object, diff_entry)

        # looping over symmetric difference of the keys of the two Tables to put corresponding entry
        for key in keys_diff :
            if key in keys_orig :
                diff_entry = subtract_entries(orig[key],TObjectEntry(object=str(key)))

            if key in keys_latter :
                diff_entry = subtract_entries(TObjectEntry(object=str(key)),latter[key])

            new_table.append(diff_entry.object, diff_entry)

        # print(len(new_table))
        new_table.set_summary(new_table.calc_summary())
        return new_table
