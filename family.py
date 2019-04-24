# Family Selection
# Author: Yamila M. Omar
# Date: 23/4/2019

class Family:
    def __init__(self):
        '''Initializes Family object. All Family objects are initialized with three empty
        attributes: 
        - base: is the set of nodes (workstations) for this family. Default: empty set.
        - family_members: is a list of paths that belong to this family. Default: empty list.
        - family_count: is an integer accounting for the number of processed items that 
        belong to this family. Default: 0.
        Users are expected to call on the find_family method to populate these attributes.'''
        self.base = set([])
        self.family_members = []
        self.family_count = 0
    
    def _log_process(self, text):
        '''This internal function allows to create a text file to log data from the 
        find_family method. It was used during module development to understand how the 
        method functioned.'''
        filename = "family_search_log.txt"
        with open(filename, 'a') as f:
            f.write(text)
    
    def find_family(self, sets_list, threshold=0.7, log=False):
        '''This method finds the base, family_members and family_count of the Family object. 
        It requires the following input variables: 
        - sets_list: a list of path sets in which each element is a tuple (c, p) where c is 
        the path count and p is the path set.
        - threshold: float between 0 and 1. It is needed to calculate if a path set Jaccard 
        similarity is above or below threshold. Default: 0.7.
        - log: boolean indicating if a log text file should be written. Default: False.
        This function returns a list of unused sets from the input sets_list.'''
        sets_list.sort(reverse = True)
        for item in sets_list:
            text = "\nProcessing item: {}\n".format(item)
            path, count = item[1], item[0]
            if not self.base: 
                self.base = set(path)
                self.family_members.append(path)
                self.family_count += count
            else:
                jaccard_similarity = Similarity(self.base, path).jaccard
                text += "J = {} for base = {}\n".format(jaccard_similarity, self.base)
                if jaccard_similarity >= threshold:
                    new_base = self.base.union( set(path) )
                    family_jaccard = [Similarity(new_base, member).jaccard for member in self.family_members]
                    text += "min family jaccard = {}\n".format(min(family_jaccard))
                    if min(family_jaccard) >= threshold:
                        self.base = new_base
                        self.family_members.append(path)
                        self.family_count += count
                        text += "{} added to family\n".format(item)
            if log: self._log_process(text)
        sets_list = [(c,p) for (c,p) in sets_list if p not in self.family_members]
        return sets_list
        
        


        
class Similarity:
    def __init__(self, S, T):
        '''Initializes Similarity object. Input variables: S and T. They are iterables that can 
        be converted to sets.'''
        self.S = set(S)
        self.T = set(T) 
        
    @property
    def jaccard(self):
        '''Property that calculates the Jaccard Similarity of sets S and T.'''
        return len(self.S.intersection(self.T)) / len(self.S.union(self.T))