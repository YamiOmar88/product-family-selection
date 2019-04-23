# Path Sets
# Author: Yamila M. Omar
# Date: 19/4/2019

class PathSets:
    def __init__(self, paths):
        '''Initializes PathSets object. Input variables: 
        - paths: dictionary with path tuples as keys and counts as values.'''
        self.path_sets = self.find_sets(paths)
        
    def find_sets(self, paths):
        '''Since two paths may contain the same workstations in different order, 
        this function ignores ordering to find products that visit the same 
        workstations.'''
        path_sets = {}
        for k,v in paths.items():
            k = set(k)
            k = tuple(k)
            path_sets[k] = path_sets.get(k, 0) + v
        return path_sets
        
    def order_sets(self, reversed=True):
        '''This function takes the path_sets and makes a list of tuples (v,k) 
        and sorts it. It takes a boolean as input for list sorting.'''
        sets_list = []
        for k,v in self.path_sets.items():
            sets_list.append( (v,k) )
        sets_list.sort(reverse=reversed)
        return sets_list