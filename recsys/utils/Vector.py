'''
Created on Jul 7, 2012

@author: alex
'''

class Vector(dict):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self = dict()
        
        
    def getItem(self, key):
        if self.has_key(key):
            return float(self[key])
        return None
    
    def addToVec(self, key, value):
        if self.has_key(key):
            self[key] += float(value)
        else:
            self[key] = float(value)
        pass
    
    def setItem(self, key, value):
        self[key] = float(value)
        
    def getAll(self):
        return self.items()
            