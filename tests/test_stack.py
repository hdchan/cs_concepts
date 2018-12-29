from cs_concept.data_structure.stack import Stack
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
    
    def test_initializer(self):
        self.assertEqual(self.stack.node_count, 0)
        
    def test_push(self):
        self.push_test_values()
        self.assertEqual(self.stack.node_count, 3)
        self.assertEqual(self.stack.head_node.value, 3)
        self.stack.push(4)
        self.assertEqual(self.stack.head_node.value, 4)
    
    def test_pop(self):
        self.push_test_values()
        self.stack.pop()
        self.assertEqual(self.stack.node_count, 2)
        self.assertEqual(self.stack.head_node.value, 2)
        self.stack.pop()
        self.assertEqual(self.stack.head_node.value, 1)
        self.stack.pop()
        self.assertEqual(self.stack.node_count, 0)
        
        with self.assertRaises(Exception) as context:
            self.stack.pop()
        self.assertTrue('There\'s nothing to pop!' in str(context.exception))
    
    def test_node_at_index(self):
        self.push_test_values()
        self.assertEqual(self.stack.node_at_index(1).value, 2)
        
        with self.assertRaises(Exception) as context:
            self.stack.node_at_index(4)
        self.assertTrue('Index 4 out of bounds' in str(context.exception))
        
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        
        with self.assertRaises(Exception) as context: 
            self.stack.node_at_index(4)
        self.assertTrue('List is empty.' in str(context.exception))
        
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.push_test_values()
        self.assertFalse(self.stack.is_empty())
        
    def test_description(self):
        self.push_test_values()
        self.assertEqual("{}".format(self.stack), "[3, 2, 1]")
    
suite = unittest.TestLoader().loadTestsFromModule(TestStack())
unittest.TextTestRunner().run(suite)