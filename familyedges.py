# Family Edges
# Author: Yamila M. Omar
# Date: 2/5/2019

class FamilyEdges:
    def __init__(self, all_paths, family_members):
        '''Initializes and calculates family edges dictionary. It takes two
        input variables that are passed to other functions:
        - all_paths: a dictionary with all the paths in the data. Keys are
        tuples of paths and values are the count of such path.
        - family_members: a list of path sets that belong to the family
        under study.'''
        self.family_paths = self.find_family_paths(all_paths, family_members)
        self.family_edges = self.make_family_edges(all_paths, family_members)


    def find_family_paths(self, all_paths, family_members):
        '''Since the family members are path sets and not paths, this
        function searches for the paths that belong to the family. Input
        variables:
        - all_paths: a dictionary with all the paths in the data. Keys are
        tuples of paths and values are the count of such path.
        - family_members: a list of path sets that belong to the family
        under study.
        The function returns a dictionary (family_paths) with paths as
        keys and counts as values.'''
        family_paths = dict()
        for path, count in all_paths.items():
            path_set = list(path)
            path_set.sort()
            path_set  = tuple(path_set)
            if path_set in family_members:
                family_paths[path] = count
        return family_paths


    def make_family_edges(self, all_paths, family_members):
        '''This function returns a dictionary of family edges where each
        key represents an edge and its value is the count of that edge.'''
        # family_paths = self.find_family_paths(all_paths, family_members)
        family_edges = dict()
        for path, count in self.family_paths.items():
            family_edges[('i', path[0])] = family_edges.get(('i', path[0]), 0) + count
            family_edges[(path[-1], 'f')] = family_edges.get((path[-1], 'f'), 0) + count
            for index in range(len(path) - 1):
                edge = (path[index], path[index + 1])
                family_edges[edge] = family_edges.get(edge, 0) + count
        return family_edges


    def save_to_file(self, filename):
        '''This function allows to save the family edges to a text file.
        Input variable: filename path (string).'''
        with open(filename, 'w') as f:
            for edge, count in self.family_edges.items():
                line = str(edge[0]) + ' ' + str(edge[1]) + ' ' + str(count) + '\n'
                f.write(line)
        return True
