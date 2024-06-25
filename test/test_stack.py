import unittest
from _01_Stack.Stack import Stack


class MyTestCase(unittest.TestCase):
    stack = Stack(2)

    def test_1_init(self):
        self.assertEqual(self.stack.stack_size, 2)

    def test_2_push(self):
        self.assertEqual(self.stack.push("test_data1"), None)
        self.stack.push("test_data2")
        self.assertEqual(self.stack.push("test_data3"), "Стэк переполнен")

    def test_3_pop(self):
        self.assertEqual(self.stack.pop(), "test_data2")
        self.stack.clear_stack()
        self.assertEqual(self.stack.pop(), "Стэк пуст")

    def test_4_is_empty(self):
        self.stack.push("test_data1")
        self.assertEqual(self.stack.is_empty(), False)

    def test_5_is_full(self):
        self.assertEqual(self.stack.is_full(), False)
        self.stack.push("test_data")
        self.assertEqual(self.stack.is_full(), True)

    def test_6_clear_stack(self):
        self.stack.clear_stack()
        self.assertEqual(self.stack.is_empty(), True)

    def test_7_get_data(self):
        self.stack.push("test_data1")
        self.assertEqual(self.stack.get_data(0), "test_data1")
        self.assertEqual(self.stack.get_data(10), "Out of range")

    def test_8_size_stack(self):
        self.assertEqual(self.stack.size_stack(), 1)

    def test_9_counter_int(self):
        self.stack.push(1)
        self.assertEqual(self.stack.counter_int(), 1)
