import os
import sys

from . import _ensure_installed

# This is terrifying to many people. However, it seems SciML takes pragmatic approach.
_ensure_installed()

# PyJulia have to be loaded after `_ensure_installed()`
from juliacall import Main

# TODO: find a better way to do this or upstream this function into juliacall
def load_julia_package(name):
    return Main.seval(f"using {name}: {name}; {name}")

DifferentialEquations = load_julia_package("DifferentialEquations")
sys.modules[__name__] = DifferentialEquations   # mutate myself
