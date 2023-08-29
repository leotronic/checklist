import unittest
from model.checklist import Checklist


class TestChecklist(unittest.TestCase):

    def setUp(self):
        self.checklist = Checklist()

    def test_init(self):
        self.assertEqual(self.checklist.items, [])

    def test_add_item(self):
        self.checklist.add_item("Milk")
        self.assertEqual(self.checklist.items, ["Milk"])

    def test_remove_item(self):
        self.checklist.add_item("Milk")
        self.checklist.remove_item("Milk")
        self.assertEqual(self.checklist.items, [])

    def test_update_item(self):
        self.checklist.add_item("Milk")
        self.checklist.update_item(0, "Water")
        self.assertEqual(self.checklist.items, ["Water"])

    def test_set_items(self):
        self.checklist.items = ["Milk", "Water"]
        self.assertEqual(self.checklist.items, ["Milk", "Water"])

    def test_invalid_set_items(self):
        with self.assertRaises(ValueError):
            self.checklist.items = "Not a list"

    def test_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.checklist.update_item(999, "Doesn't matter")


if __name__ == '__main__':
    unittest.main()
