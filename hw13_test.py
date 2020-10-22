'''
    split_test.py
    
    This file tests string.split(). In the real world, there's no need to test
    Python's library functions, but we're just doing this as an intro to unit
    tests.
'''

import unittest
from hw13 import my_func

KEY_INPUT_NUM_ITERS = "input num iters"
KEY_INPUT_INITIAL = "input initial"
KEY_INPUT_SECOND = "input second"
KEY_EXPECTED = "expected"
KEY_RETURN = "return"

class Run_my_fun(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT_NUM_ITERS: 0,
                KEY_INPUT_INITIAL:5,
                KEY_INPUT_SECOND: 5,
                KEY_EXPECTED: {
                    KEY_RETURN: "Don't iterate",
                }
            },
             {
                KEY_INPUT_NUM_ITERS: 2,
                KEY_INPUT_INITIAL:5,
                KEY_INPUT_SECOND: 5,
                KEY_EXPECTED: {
                    KEY_RETURN: "counter is 10",
                }
            },
            {
                KEY_INPUT_NUM_ITERS: 2,
                KEY_INPUT_INITIAL:-5,
                KEY_INPUT_SECOND: 5,
                KEY_EXPECTED: {
                    KEY_RETURN: "initial is -5",
                }
            },
            ]
        self.failure_test_params = [
              {
                KEY_INPUT_NUM_ITERS: 0,
                KEY_INPUT_INITIAL:5,
                KEY_INPUT_SECOND: 5,
                KEY_EXPECTED: {
                    KEY_RETURN: "counter is 10",
                }
            },
            {
                KEY_INPUT_NUM_ITERS: 2,
                KEY_INPUT_INITIAL:5,
                KEY_INPUT_SECOND: 5,
                KEY_EXPECTED: {
                    KEY_RETURN: "initial is 5"
                }
            },
            {
                KEY_INPUT_NUM_ITERS: 2,
                KEY_INPUT_INITIAL:-5,
                KEY_INPUT_SECOND: 5,
                KEY_EXPECTED: {
                    KEY_RETURN: "counter is 10",
                }
            },
            ]
    
    def test_my_func_success(self):
        for test in self.success_test_params:
            num_iter = test[KEY_INPUT_NUM_ITERS]
            initial = test[KEY_INPUT_INITIAL]
            second = test[KEY_INPUT_SECOND]
            output = my_func(num_iter, initial, second)
            
            expected = test[KEY_EXPECTED]
            print(output)
            self.assertEqual(output, expected[KEY_RETURN])
            
    def test_my_func_failure(self):
        for test in self.failure_test_params:
            num_iter = test[KEY_INPUT_NUM_ITERS]
            initial = test[KEY_INPUT_INITIAL]
            second = test[KEY_INPUT_SECOND]
            output = my_func(num_iter, initial, second)
            expected = test[KEY_EXPECTED]
            self.assertNotEqual(output, expected[KEY_RETURN])


if __name__ == '__main__':
    unittest.main()