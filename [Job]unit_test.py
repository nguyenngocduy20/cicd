#!/usr/bin/python
import unittest
import sys
sys.path.append('./firstApp')

from views import *

class TestUnitMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(tong(3, 7), 10)

    def test_isupper(self):
        self.assertTrue(login(200))
        self.assertFalse(login(201))

    def test_split(self):
        s = 'this is a test demo'
        self.assertEqual(s.split(), ['this', 'is', 'a', 'test', 'demo'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(5)

if __name__ == '__main__':
#       unittest.main()
#       suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
#       unittest.TextTestRunner(verbosity=2).run(suite)
        import xmlrunner
#       unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports/report.xml'))
        with open('results.xml', 'w') as output: unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)