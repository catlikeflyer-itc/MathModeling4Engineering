import matplotlib.pyplot as plt
import matplotlib_venn as venn

# Preset sets for testing
'''
Testing with lists, to change to type->set use key brackets instead 
'''
A = {1, 2, 3, 4, 5}
B = {5, 6, 7, 8, 9}
C = {9, 10, 11, 12}

"""Plotting venn diagram"""
def show_venn(A: set, B: set, C: set) -> None:
    """
    Show venn diagram given 3 sets
    Set de venn function number venn{number} depending on the sets
    This function takes three sets.
    """

    venn.venn3([A, B, C], ('Group1', 'Group2', 'Group3'))

    plt.show()
