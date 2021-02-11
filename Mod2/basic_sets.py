"""
To test the following lines of code,
run each cell individually to see each functionality.
You can also run the whole code.

Feel free to test and tweak code to better understand.
"""
#%% Preset sets for testing
"""
Run this cell before any other
Declare any other sets here if you'd like
"""
A = {1, 2, 3, 4, 5}
B = {5, 6, 7, 8, 9}
C = {9, 10, 11, 12}

#%%
"""Cardinality"""

cardinality = lambda x: len(x) # Takes a set as an argument and returns cardinality

print(f'Cardinality of {cardinality(A)}\n')

#%%
"""Intersections"""

intersect_m1 = A&B # Method 1 using logical operators, add more sets separated with &
intersect_m2 = A.intersection(B) # Method 2 using a method of set, add more sets separarated by a comma

print(f'Method one intersection is {intersect_m1} and method 2 is {intersect_m2}\n')

#%%
"""Unions"""

union_m1 = A|B # Using logical operators, add more sets separated with &
union_m2 = A.union(B) # Using union method for sets, add more sets separarated by a comma

print(f'Method one union is {union_m1} and method 2 is {union_m2}\n')

#%%
"""Differences"""

diff_m1 = A-B # Returns all differences
diff_m2 = A.difference(B) # Returns only the different values from the called object

print(f'Method one diff is {diff_m1} and method two is {diff_m2}\n')

sym_diff_m1 = A^B
sym_diff_m2 = A.symmetric_difference(B) # Returns all different values from both sets (symmetric diff)

print(f'Method one sym diff is {sym_diff_m1} and method two is {sym_diff_m2}\n')

#%%
"""Subsets"""

subset_m1 = A<=B # Checks if A is subset of B, boolean returned
subset_m2 = A.issubset(B) # Does the same as the above

print(f'Method one subset is {subset_m1} and method subset is {subset_m2}\n')

#%%
"""Own subsets"""

def isownsubset(A:set, B:set):
    return A.issubset(B) and A!=B
    












