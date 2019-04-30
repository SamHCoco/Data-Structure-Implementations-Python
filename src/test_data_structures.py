import unittest
from data_structures import BinarySearchTree


class Test(unittest.TestCase):

    def test_preorder_traversal(self):
        """Tests preorder traversal of Binary Search Tree."""
        values_1 = [7, 11, 6, 8, 20, 1, 9, 14, 22]  # root value 10
        values_2 = [10, 65, -3.14, 12, 43, 256]  # root value 20
        expected_traversal_1 = [10, 7, 6, 1, 8, 9, 11, 20, 14, 22]
        expected_traversal_2 = [20, 10, -3.14, 12, 65, 43, 256]
        bst_1 = BinarySearchTree(10)
        bst_2 = BinarySearchTree(20)
        for x in values_1:
            bst_1.insert(x)
        for y in values_2:
            bst_2.insert(y)
        self.assertEqual(bst_1.preorder_traversal(), expected_traversal_1)
        self.assertEqual(bst_2.preorder_traversal(), expected_traversal_2)
