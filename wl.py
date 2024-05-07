'''
Interface for importing `weighted-list` via `suptools`.
'''

import importlib
WeightedList = importlib.import_module(".weighted-list.python", "suptools").WeightedList
