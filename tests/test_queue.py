from data_structure.queue import Queue
import unittest

class TestQueue(unittest.TestCase):
    
    def setUp(self):
        self.queue = Queue()
    
    def enqueue_test_values(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
    
    def test_initializer(self):
        self.assertEqual(self.queue.node_count, 0)
        
    def test_enqueue(self):
        self.enqueue_test_values()
        self.assertEqual(self.queue.node_count, 3)
    
    def test_dequeue(self):
        self.enqueue_test_values()
        self.assertEqual(self.queue.dequeue().value, 1)
        self.assertEqual(self.queue.dequeue().value, 2)
        self.assertEqual(self.queue.dequeue().value, 3)
        
        with self.assertRaises(Exception) as context:
            self.queue.dequeue()
        self.assertTrue('There\'s nothing to dequeue!' in str(context.exception))
        
    def test_node_at_index(self):
        self.enqueue_test_values()
        self.assertEqual(self.queue.node_at_index(1).value, 2)
    
    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.enqueue_test_values()
        self.assertFalse(self.queue.is_empty())
    
    def test_description(self):
        self.enqueue_test_values()
        self.assertEqual("{}".format(self.queue), "[1 <-> 2 <-> 3]")
    
suite = unittest.TestLoader().loadTestsFromModule(TestQueue())
unittest.TextTestRunner().run(suite)