#!/usr/bin/env python
# Created by "Thieu" at 19:14, 19/03/2023 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from foo import speak


def test_english():
    assert speak.english("Natali") == "Natali"


def test_vietnamese():
    assert speak.vietnamese("Linh Nhi") == "Linh Nhi"
