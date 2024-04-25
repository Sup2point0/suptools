'''
suptools
v2.0.0

Uility functions and classes.
'''

from .source import *

# importing weighted-list takes a little fiddling,
# since it has a hyphen in the name...
import importlib
WeightedList = importlib.import_module(".weighted-list.Python.weightedlist", "suptools").WeightedList
