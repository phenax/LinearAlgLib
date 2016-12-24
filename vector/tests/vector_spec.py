
import unittest

from ..vector import Vector


class TestVectorMethods(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector([-1,2,3])
        self.v2 = Vector([1,2,3])

    def tearDown(self):
        del self.v1
        del self.v2


    def test_exception(self):
        print 'should raise exceptions for invalid inputs'

        with self.assertRaises(ValueError):
            Vector([])

        with self.assertRaises(TypeError):
            Vector(5)


    def test_vector_addition(self):
        print 'should add vector 1 and vector 2'

        vector_sum= self.v1.plus(self.v2);

        self.assertEqual(vector_sum[0], 0)
        self.assertEqual(vector_sum[1], 4)
        self.assertEqual(vector_sum[2], 6)


    def test_vector_subtraction(self):
        print 'should subtract vector 1 and vector 2'

        vector_subtraction= self.v1.minus(self.v2);

        self.assertEqual(vector_subtraction[0], -2)
        self.assertEqual(vector_subtraction[1], 0)
        self.assertEqual(vector_subtraction[2], 0)


    def test_scalar_multiplication(self):
        print 'should multiply a scala vector 1 and vector 2'

        vector= self.v1.sc_mult(5);

        self.assertEqual(vector[0], -5)
        self.assertEqual(vector[1], 10)
        self.assertEqual(vector[2], 15)



if __name__ == '__main__':
    unittest.main()
