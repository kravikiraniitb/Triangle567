# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:44:00 2022
Updated on Sep 21, 2022

The primary goal of this file is to demonstrate a simple python program to classify triangles

@ravikiran
"""

def classifytriangle(a_a,b_b,c_c):
    """A dummy docstring."""
    try:
        if a_a > 200 or b_b > 200 or c_c > 200:
            return 'InvalidInput'
        if a_a <= 0 or b_b <= 0 or c_c <= 0:
            return 'InvalidInput'
        if not((isinstance(a_a,(float,int)))and(isinstance(b_b,(float,int)))and(isinstance(c_c,(float,int)))):
            return 'InvalidInput'
        if (a_a >= (b_b + c_c)) or (b_b >= (a_a + c_c)) or (c_c >= (a_a + b_b)):
            return 'NotATriangle'
        if a_a == b_b == c_c :
            return 'Equilateral'
        if (a_a**2+b_b**2 == c_c**2) or (c_c**2+b_b**2 == a_a**2) or (a_a**2 + c_c**2 == b_b**2):
            return 'Right'
        if ((b_b not in [a_a, c_c]) and (a_a not in [b_b, c_c]) and (c_c not in [a_a, b_b])):
            return 'Scalene'
        return 'Isoceles'
    except ValueError:
        return "InvalidInput"
    except TypeError:
        return "InvalidInput"
