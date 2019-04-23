# Read file data
# Author: Yamila M. Omar
# Date: 19/4/2019

class FileRead:
    def __init__(self, filename):
        '''Initializes FileRead object with filename.'''
        self.filename = filename
        
    
    def read_paths_with_counts(self):
        '''Reads paths from file.'''
        all_paths = {}
        with open(self.filename) as f:
            for line in f:
                line = line.strip().split()
                line = [int(x) for x in line]
                path = tuple(line[:-1])
                count = line[-1]
                all_paths[path] = all_paths.get(path, 0) + count 
        return all_paths 