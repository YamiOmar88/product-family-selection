# Family Selection
# Author: Yamila M. Omar
# Date: 23/4/2019

class Family:
    def __init__(self):
        ''''''
        self.base = set([])
        self.family_members = []
        self.family_count = 0
    
    def _log_process(self, text):
        ''' '''
        filename = "family_search_log.txt"
        with open(filename, 'a') as f:
            f.write(text)
    
    def find_family(self, sets_list, threshold=0.7, log=False):
        ''''''
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
        ''' '''
        self.S = set(S)
        self.T = set(T) 
        
    @property
    def jaccard(self):
        ''' '''
        return len(self.S.intersection(self.T)) / len(self.S.union(self.T))