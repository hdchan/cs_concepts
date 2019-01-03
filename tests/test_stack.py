from data_structure.stack import Stack
import unittest

class TestStack(unittest.TestCase):
    
    def setUp(self):
        self.stack = Stack()
    
    def tearDown(self):
        self.stack = None
    
    def push_test_values(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
    
    def test_pop(self):
        self.push_test_values()
        self.assertEqual(self.stack.pop().value, 3)
        self.assertEqual(self.stack.pop().value, 2)
        self.assertEqual(self.stack.pop().value, 1)
        
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.push_test_values()
        self.assertFalse(self.stack.is_empty())
    
suite = unittest.TestLoader().loadTestsFromModule(TestStack())
unittest.TextTestRunner().run(suite)