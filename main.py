# Finding Families
# Author: Yamila M. Omar
# Date: 23/4/2019

import fileread
import pathsets
import family

filename = "data/paths_with_count.txt"
all_paths = fileread.FileRead(filename).read_paths_with_counts()
paths_sets = pathsets.PathSets(all_paths)
paths_list = paths_sets.order_sets(reversed=True)

# Find families
# =============
f1 = family.Family()
unused1 = f1.find_family(paths_list, threshold=0.63)

f2 = family.Family()
unused2 = f2.find_family(unused1, threshold=0.63)

f3 = family.Family()
unused3 = f3.find_family(unused2, threshold=0.63)

unaccounted = 0
for item in unused3:
    unaccounted += item[0]
    
total_number_items = f1.family_count + f2.family_count + f3.family_count + unaccounted
    

# Save family edges
# =================
import familyedges

F1 = familyedges.FamilyEdges(all_paths, f1.family_members)
F1.save_to_file('results/F2.txt')

F2 = familyedges.FamilyEdges(all_paths, f2.family_members)
F2.save_to_file('results/F1.txt')

F3 = familyedges.FamilyEdges(all_paths, f3.family_members)
F3.save_to_file('results/F3.txt')