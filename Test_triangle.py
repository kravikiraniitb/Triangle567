# -*- coding: utf-8 -*-
"""
Updated on Sep 21, 2022
The primary goal of this file is to demonstrate a simple unittest implementation

@ravikiran
"""
import math
import cmath


import unittest

from triangle import classifytriangle

def fun():
    pass


class TestTriangles(unittest.TestCase):
    
#1
    def testRightTriangleA(self): 
        self.assertEqual(classifytriangle(3,4,5),'Right','3,4,5 is a Right triangle')
#2
    def testRightTriangleB(self): 
        self.assertEqual(classifytriangle(5,3,4),'Right','5,3,4 is a Right triangle')
  #3      
    def testEquilateralTriangles(self): 
        self.assertEqual(classifytriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
#4
    def testTriangle1(self): 
        self.assertEqual(classifytriangle(201,400,500),'InvalidInput','Outside limit' )
#5
    def testTriangle2(self): 
        self.assertEqual(classifytriangle(5,0,4),'InvalidInput', "Triangle can't have zero length" )
  #6      
    def testTriangle3(self): 
        self.assertEqual(classifytriangle(0,5,1),'InvalidInput', "Triangle can't have zero length")
#7
    def testTriangle4(self): 
        self.assertEqual(classifytriangle(3,4,0),'InvalidInput', "Triangle can't have zero length")

#8
    def testTriangle5(self): 
        self.assertEqual(classifytriangle("5","3","4"),'InvalidInput', "String data type not allowed")

  #9      
    def testTriangle6(self): 
        self.assertEqual(classifytriangle("1",1,1),'InvalidInput', "String data type not allowed")
#10
    def testTriangle7(self): 
        self.assertEqual(classifytriangle(3,"4",5),'InvalidInput', "String data type not allowed")
#11
    def testTriangle8(self): 
        self.assertEqual(classifytriangle(5,3,"4"),'InvalidInput', "String data type not allowed")

  #12      
    def testTriangle9(self): 
        self.assertEqual(classifytriangle(0.1,0.1,0.1),'Equilateral', "All non zero and non negative inputs should be allowed")
#13
    def testTriangle10(self): 
        self.assertEqual(classifytriangle(3,4,8),'NotATriangle', "Traingle with given inputs not possible")
#14
    def testTriangle11(self): 
        self.assertEqual(classifytriangle(8,3,4),'NotATriangle', "Traingle with given inputs not possible")
 #15       
    def testTriangle12(self): 
        self.assertEqual(classifytriangle(4,8,3),'NotATriangle', "Traingle with given inputs not possible")
#16
    def testTriangle13(self): 
        self.assertEqual(classifytriangle(8,4,3),'NotATriangle', "Traingle with given inputs not possible")


#17
    def testTriangle14(self): 
        self.assertEqual(classifytriangle(6,4,3),'Scalene', "6,4,3 is a Scalene triangle")
#18        
    def testTriangle15(self): 
        self.assertEqual(classifytriangle(5,5,3),'Isoceles', "5,5,3 is a Isoceles triangle")

#19    
    def testTriangle16(self): 
        self.assertEqual(classifytriangle(3,3,4),'Isoceles', "3,3,4 is a Isoceles triangle")
        
#20
    def testTriangle17(self): 
        self.assertEqual(classifytriangle(-3,4,5),'InvalidInput', "Only non zero and non negative inputs should be allowed")
#21
    def testTriangle18(self): 
        self.assertEqual(classifytriangle(complex(0,5),3,4),'InvalidInput', "Only real numbers allowed")
  #22      
    def testTriangle19(self): 
        self.assertEqual(classifytriangle(math.pi,1,1),'NotATriangle', "Should be a Isoceles taingle")
       
#23
    #def testTriangle20(self): 
       # self.assertEqual(classifyTriangle(math.sqrt(2),math.sqrt(3),math.sqrt(5)),'Right', "Should be a Right taingle")
#24
    def testTriangle21(self): 
        self.assertEqual(classifytriangle(-5,0,-4),'InvalidInput', "Only non zero and non negative inputs should be allowed")

   

    def testTriangle22(self): 
        self.assertEqual(classifytriangle(fun(),3,4),'InvalidInput', "Only non zero and non negative inputs should be allowed")
        
  

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

