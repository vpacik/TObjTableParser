from collections import namedtuple


TObjectEntry = namedtuple("TObjectEntry", ['object','countTot','countHeap','sizeSingle','sizeTot','sizeHeap'] ,verbose=False)
"""
single TObject entry from TObjectTable
"""
#class TObjectEntry :
#    pass

class TObjectTable :
    """
    Implementation of single instance of TObjectTable
    """

    def __init__(self) :
        self.inst = dict()
        self.total = TObjectEntry('Total',0,0,0,0,0)

    def __del__(self) :
        self.inst.clear()

    def __repr__(self) :
        return "TObjectTable()"

    def __str__(self) :
        return str(self.total)

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

    def list(self) :
        """
        List all the TObjectEntries in a Table
        """
        for key,obj in self.inst.items() :
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

    def diff(self, table) :
        """
        Compares this Table to another one and return new Table containing 'diff' between them.
        """
        if not isinstance(table, TObjectTable) :
            raise TypeError("Not a TObjTable!")

        orig = self.inst
        latter = table.inst

        # TODO : implement

        return latter
