#!/usr/bin/env python
# Created by "Thieu" at 22:25, 19/03/2023 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import numpy as np


def calculate_perimeter_and_area_circle(radius: float):
    p = 2 * np.pi * radius
    a = np.pi * radius**2
    return p, a


def calculate_perimeter_and_area_rectangle(length: float, width: float):
    p = 2 * (length + width)
    a = length * width
    return p, a


def calculate_perimeter_and_area_square(length: float):
    p = 4 * length
    a = length**2
    return p, a
