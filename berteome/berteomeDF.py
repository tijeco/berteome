# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_dataframe.ipynb (unless otherwise specified).

__all__ = ['modelPredDF']

# Cell
import pandas as pd

# Cell
class modelPredDF():
    def __init__(self, predDict, seq, aas):
        self.predDf = pd.DataFrame.from_dict(predDict, orient = "index", columns = list(aas))
        self.predDf.insert(0, "wt",list(seq))
        self.predDf.insert(1, "wtIndex",list(range(1,len(seq)+1)))