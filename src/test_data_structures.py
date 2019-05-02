import unittest
from data_structures import BinarySearchTree


class Test(unittest.TestCase):

    def setUp(self):
        self.values_1 = [7, 11, 6, 8, 20, 1, 9, 14, 22]  # root value 10
        self.values_2 = [10, 65, -3.14, 12, 43, 256]  # root value 20
        self.bst_1 = BinarySearchTree(10)
        self.bst_2 = BinarySearchTree(20)
        for x in self.values_1:
            self.bst_1.insert(x)
        for y in self.values_2:
            self.bst_2.insert(y)

    def test_preorder_traversal(self):
        """Tests preorder traversal of Binary Search Tree."""
        expected_traversal_1 = [10, 7, 6, 1, 8, 9, 11, 20, 14, 22]
        expected_traversal_2 = [20, 10, -3.14, 12, 65, 43, 256]
        self.assertEqual(self.bst_1.preorder_traversal(), expected_traversal_1)
        self.assertEqual(self.bst_2.preorder_traversal(), expected_traversal_2)

    def test_inorder_traversal(self):
        """Tests inorder traversal for Binary Search Tree."""
        expected_traversal_1 = [1, 6, 7, 9, 8, 10, 14, 20, 22, 11]
        expected_traversal_2 = [-3.14, 10, 12, 20, 43, 65, 256]
        expected_traversal_3 = [4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90]
        values = [15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]
        bst_3 = BinarySearchTree(25)
        for x in values:
            bst_3.insert(x)
        self.assertEqual(self.bst_1.inorder_traversal(), expected_traversal_1)
        self.assertEqual(self.bst_2.inorder_traversal(), expected_traversal_2)
        self.assertEqual(bst_3.inorder_traversal(), expected_traversal_3)
