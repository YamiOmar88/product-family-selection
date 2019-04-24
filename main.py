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
    

# Threshold study
# ===============
threshold_values = [0.5, 0.55, 0.6, 0.63, 0.65, 0.68, 0.7, 0.75, 0.8, 0.9]
F1_count, F1_bases, F2_count, F2_bases, F3_count, F3_bases = [],[],[],[],[],[]
bases = [(58379, (24, 26, 29, 30, 33, 34, 36, 37)), (10613, (0, 1, 2, 5, 6, 8, 11, 29, 30, 33, 34, 36, 37)), (4011, (12, 13, 15, 17, 18, 20, 23, 29, 30, 33, 34, 36, 37))]
Paths_List = [x for x in paths_list if x not in bases]


for t in threshold_values:
    F1 = family.Family()
    F1.base = {24, 26, 29, 30, 33, 34, 36, 37}
    F1.family_members.append((24, 26, 29, 30, 33, 34, 36, 37))
    F1.family_count += 58379
    Unused1 = F1.find_family(Paths_List, threshold=t)
    F1_count.append(F1.family_count)
    F1_bases.append(F1.base)
    
    F2 = family.Family()
    F2.base = {0, 1, 2, 5, 6, 8, 11, 29, 30, 33, 34, 36, 37}
    F2.family_members.append((0, 1, 2, 5, 6, 8, 11, 29, 30, 33, 34, 36, 37))
    F2.family_count += 10613
    Unused2 = F2.find_family(Unused1, threshold=t)
    F2_count.append(F2.family_count)
    F2_bases.append(F2.base)
    
    F3 = family.Family()
    F3.base = {12, 13, 15, 17, 18, 20, 23, 29, 30, 33, 34, 36, 37}
    F3.family_members.append((12, 13, 15, 17, 18, 20, 23, 29, 30, 33, 34, 36, 37))
    F3.family_count += 4011
    Unused3 = F3.find_family(Unused2, threshold=t)
    F3_count.append(F3.family_count)
    F3_bases.append(F3.base)
    

F1_count = [i/total_number_items for i in F1_count]
F2_count = [i/total_number_items for i in F2_count]
F3_count = [i/total_number_items for i in F3_count]
total_count = [a+b+c for a,b,c in zip(F1_count, F2_count, F3_count)] 
 
import matplotlib.pyplot as plt
plt.xlim(0.4,1)
plt.ylim(0,1)
plt.axvline(x=0.63, linewidth=2, linestyle='--', color='#808080')
plt.plot(threshold_values, F2_count, marker='o', color='#FF0000', markersize=3, linewidth=2)
plt.plot(threshold_values, F1_count, marker='o', color='#008000', markersize=3, linewidth=2)
plt.plot(threshold_values, F3_count, marker='o', color='#0000FF', markersize=3, linewidth=2)
plt.plot(threshold_values, total_count, marker='o', color='#000000', markersize=3, linewidth=2)
plt.xlabel('threshold values')
plt.ylabel('fraction of items')
plt.legend(['threshold = 0.63', 'F1', 'F2', 'F3', 'F1 + F2 + F3'], loc=1)
plt.savefig('results/threshold_study.pdf')