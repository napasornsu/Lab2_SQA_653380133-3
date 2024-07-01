# Lab#2 - Test design - designing practical test scenarios and test cases
# Student name: Miss Napasorn Subongkotch
# Student ID: 653380133-3 

import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))

from print_promotion import print_promotion

# TS001
def test_under500_case1():
    result = print_promotion(155)
    assert result == "Thank you and see you next time"

def test_under500_case2():
    result = print_promotion(499)
    assert result == "Thank you and see you next time"

# TS002
def test_500to700_case1():
    result = print_promotion(500)
    assert result == "Free ice cream cone = 1"

def test_500to700_case2():
    result = print_promotion(699)
    assert result == "Free ice cream cone = 1"
    
# TS003
def test_700to1200_case1():
    result = print_promotion(700)
    assert result == "Free chocolate cake = 1"

def test_700to1200_case2():
    result = print_promotion(1199)
    assert result == "Free chocolate cake = 1"
    
# TS004
def test_equal_and_morethan_1200_case1():
    result = print_promotion(1200)
    assert result == "Free ice cream cone = 1 and Free chocolate cake = 1"    

def test_equal_and_morethan_1200_case2():
    result = print_promotion(1700)
    assert result == "Free ice cream cone = 2 and Free chocolate cake = 1"

def test_equal_and_morethan_1200_case3():
    result = print_promotion(1900)
    assert result == "Free ice cream cone = 1 and Free chocolate cake = 2"

def test_equal_and_morethan_1200_case4():
    result = print_promotion(2400)
    assert result == "Free ice cream cone = 2 and Free chocolate cake = 2"

