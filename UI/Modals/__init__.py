# Modals/__init__.py

import os
import importlib

package_dir = os.path.dirname(__file__)

for filename in os.listdir(package_dir):
    if filename.endswith(".py") and filename !="__init__.py": 
        module_name = filename[:-3]
        module = importlib.import_module(f".{module_name}", package=__name__)
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute,type):
                globals()[attribute_name] = attribute

