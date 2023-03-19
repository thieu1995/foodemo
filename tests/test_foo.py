#!/usr/bin/env python
# Created by "Thieu" at 19:14, 19/03/2023 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from foo import foo


def test_foo():
    assert foo() == "foo"


def test_foo_uppercase():
    assert foo(True) == "FOO"
