'''
Interface for importing `weighted-list` via `suptools`.
'''

# importing weighted-list takes a little fiddling, since it has a hyphen in the name...
import importlib
wl = importlib.import_module(".weighted-list.python", "suptools")

__all__ = ["WeightedItem", "WeightedList"]

WeightedItem = wl.WeightedItem
WeightedList = wl.WeightedList
