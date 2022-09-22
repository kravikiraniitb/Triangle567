# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:44:00 2022
Updated on Sep 21, 2022

The primary goal of this file is to demonstrate a simple python program to classify triangles


@ravikiran
"""
import math
import cmath

def classifyTriangle(a,b,c):
    
    try:


       
        if a > 200 or b > 200 or c > 200:
            return 'InvalidInput'
            
        elif a <= 0 or b <= 0 or c <= 0:
            return 'InvalidInput'
        
        
        elif not ((isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float)) and (isinstance(c,int) or isinstance(c,float))):
            return 'InvalidInput';
        
        
        elif (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
            return 'NotATriangle'
            
        
        elif a == b == c :
            return 'Equilateral'
        elif (a**2 + b**2 == c**2) or (c**2 + b**2 == a**2) or (a**2 + c**2 == b**2):
            return 'Right'
        elif (a != b) and  (b != c) and (a != b):
            return 'Scalene'
        else:
            return 'Isoceles'

    except ValueError:
        return "InvalidInput"

    except TypeError:
        return "InvalidInput"
