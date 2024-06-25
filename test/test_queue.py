import unittest
from _02_Queue.Queue import Queue


class MyTestCase(unittest.TestCase):
    queue = Queue()

    def test_1_init(self):
        self.assertEqual(self.queue.head, None)
        self.assertEqual(self.queue.tail, None)

    def test_2_enqueue(self):
        self.queue.enqueue("test_data1")
        self.assertEqual(self.queue.head.data, "test_data1")
        self.queue.enqueue("test_data2")
        self.assertEqual(self.queue.tail.data, "test_data2")

    def test_3_dequeue(self):
        self.queue.dequeue()
        self.assertEqual(self.queue.head.data, "test_data2")
        self.queue.dequeue()
        self.assertEqual(self.queue.dequeue(), None)
