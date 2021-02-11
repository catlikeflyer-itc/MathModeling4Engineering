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
from sympy import FiniteSet, ProductSet
from sympy.sets.powerset import PowerSet

"""Finite Sets: represents a finite set of discrete numbers"""

A = FiniteSet(1, 2, 3, 4, 5)
B = FiniteSet(5, 6, 7, 8, 9)
C = FiniteSet(9, 10, 11, 12)

#%%
"""Powersets: all possible sets in a set"""

E = A.powerset() # Returns a new finite set with a finite set
F = PowerSet(A).rewrite(FiniteSet) # Returns a setwith many finite sets

print(F)

#%%
"""Cartesian product: """

cp_m1 = ProductSet(A, B) # Uses sympy function 
cp_m2 = A*B # Sympy syntax for finite sets

print()



