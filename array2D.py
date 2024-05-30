import array
class Array2D:
    def __init__(self,nRows, nCols):
        self.nRows=nRows
        self.nCols=nCols
        self.con = array(nRows)
        for i in range(nRows):
            self.con[i]= array(nCols)
    def numRows(self):
        return len(self.con)
    def print(self):
        for i in range(self.numRows()):
            print(self.con)
    # Reinitialise le tableau avec value a chaque position
    def clear(self, value):
        for i in range(self.numRows()):
            self.con[i].clear(value)
    