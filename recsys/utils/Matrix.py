'''
Created on Jul 7, 2012

@author: alex
'''

class Matrix(dict):
    '''
    Base Class of Matrix
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self = dict()
        
    def addToMat(self, row, col, value):
        if self.has_key(row):
            if self[row].has_key(col):
                #self[row][col] += float(value)
                self[row][col] += float(value)
            else:
                self[row][col] = float(value)
        else:
            self[row] = dict()
            self[row][col] = float(value)
            
    def getAll(self):
        return self.items()
            
    def getRowNames(self):
        return self.keys()
    
    def getColNames(self, row):
        if self.has_key(row):
            return self[row].keys()
        return list()
    
    def getRows(self, row):
        if self.has_key(row):
            return self[row].items()
        return None
    
    def setItem(self, row, col, value):
        
        if self.has_key(row):
            self[row][col] = float(value)
        else:
            self[row] = dict()
            self[row][col] = float(value)
    
    def getItem(self, row, col):
        
        if self.has_key(row):
            if self[row].has_key(col):
                return float(self[row][col])
        return None