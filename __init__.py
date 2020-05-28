"""
Created on Sat May 23 13:47:32 2020.

@author: Tocivlasok

@directory: _git_repo_mechanic_ba/
"""

"""
Python defines two types of packages:
| Namespace packages
| Regular packages - traditional packages as existed in Python 3.2 and earlier.
A regular package is typically implemented as a directory containing an __init__.py file.
When a regular package is imported, this __init__.py file is implicitly executed,
and the objects it defines are bound to names in the package’s namespace.
The __init__.py file can contain the same Python code that any other module can contain,
and Python will add some additional attributes to the module when it is imported.
"""

"""
Files __init__.py are used to mark directories on disk as Python package directories.
If you have the files
mydir/spam/__init__.py
mydir/spam/module.py
and mydir is on your path, you can import the code in module.py as
import spam.module
or
from spam import module
- the contents of the init module can be accessed as import spam
If you remove the __init__.py file, Python will no longer look for submodules inside that directory,
so attempts to import the module will fail.
__init__.py is usually empty, but can be used to:
- export selected portions of the package under more convenient name,
- hold convenience functions
"""


from play_with_string import play_with_string
