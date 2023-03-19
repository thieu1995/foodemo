#!/usr/bin/env python
# Created by "Thieu" at 19:11, 19/03/2023 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import os

files = os.listdir(__path__[0])
modules = (
    x.replace(".py", "") for x in files if x.endswith(".py") and not x.startswith("__")
)
for module in modules:
    __import__("foo." + module)
