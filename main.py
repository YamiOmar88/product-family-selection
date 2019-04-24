# 
# Author: Yamila M. Omar
# Date: 23/4/2019

import fileread
import pathsets
import family

filename = "data/paths_with_count.txt"
all_paths = fileread.FileRead(filename).read_paths_with_counts()
paths_sets = pathsets.PathSets(all_paths)
paths_list = paths_sets.order_sets(reversed=True)


f1 = family.Family()
unused1 = f1.find_family(paths_list, threshold=0.63)

f2 = family.Family()
unused2 = f2.find_family(unused1, threshold=0.63)

f3 = family.Family()
unused3 = f3.find_family(unused2, threshold=0.63)

unaccounted = 0
for item in unused3:
    unaccounted += item[0]