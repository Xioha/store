"""
    unittest
    1.子类继承TestCase
    2.写用例，test开头
"""
from unittest import TestCase
from Calc import Calc

class TestCalc(TestCase):

    def testAdd1(self):
        a = 6
        b = 5
        c = 11

        calc = Calc()
        s = calc.add(a,b)

        self.assertEqual(s,c)

    def testAdd2(self):
        a = -6
        b = -5
        c = -11

        calc = Calc()
        s = calc.add(a, b)

        self.assertEqual(s, c)

    def testAdd3(self):
        a = -6
        b = 5
        c = -1

        calc = Calc()
        s = calc.add(a, b)

        self.assertEqual(s, c)

    def testAdd4(self):
        a = 6
        b = -5
        c = 1

        calc = Calc()
        s = calc.add(a, b)

        self.assertEqual(s, c)

    def testAdd5(self):
        a = 6000000000000000000000000000000000000000000000000000000000000000
        b = 5
        c = 6000000000000000000000000000000000000000000000000000000000000005

        calc = Calc()
        s = calc.add(a, b)

        self.assertEqual(s, c)

    def testMinus1(self):
        a = 6
        b = 5
        c = 1

        calc = Calc()
        s = calc.minus(a,b)

        self.assertEqual(s,c)
    def testMinus2(self):
        a = 6
        b = 5
        c = 3

        calc = Calc()
        s = calc.minus(a,b)

        self.assertEqual(s,c)

    def testMulti1(self):
        a = 6
        b = 5
        c = 30

        calc = Calc()
        s = calc.multi(a,b)

        self.assertEqual(s,c)
    def testMulti2(self):
        a = 6
        b = 5
        c = 3

        calc = Calc()
        s = calc.multi(a,b)

        self.assertEqual(s,c)

    def testDevision1(self):
        a = 27
        b = 9
        c = 3

        calc = Calc()
        s = calc.devision(a,b)

        self.assertEqual(s,c)
    def testDevision2(self):
        a = 27
        b = 9
        c = 10

        calc = Calc()
        s = calc.devision(a,b)

        self.assertEqual(s,c)
