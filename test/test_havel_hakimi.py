# Test algoritmo de Havel-Hakimi
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from grafos.havelhakimi import HavelHakimi

hk = HavelHakimi()
hk.algorithm([2,4,4,5,5,5,6,7])
print('{:*^25}'.format('*'))
hk.algorithm([2,2,2,2,2,3,4,5])