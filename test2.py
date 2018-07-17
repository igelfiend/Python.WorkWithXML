import unittest

from main2 import *


class XmlDataTester(unittest.TestCase):
    def test_print_nodes_list(self):
        # Testing print all nodes in xml
        data = init()
        test_pref_res = ['data', 'name', 'age',
                         'sex', 'languages', 'language',
                         'language', 'language', 'pc',
                         'pc_item', 'pc_item', 'pc_item',
                         'pc_item']
        self.assertEqual(listNodes(data), test_pref_res)

    def test_delete_tags1(self):
        # Deleting tag languages,
        # Children must be deleted too
        data = init()
        test_pref_res = ['data', 'name', 'age',
                         'sex', 'pc', 'pc_item',
                         'pc_item', 'pc_item', 'pc_item']
        deleteTagNodes(data, "languages")
        self.assertEqual(listNodes(data), test_pref_res)

    def test_delete_tags2(self):
        # Deleting all pc_item tags
        data = init()
        test_pref_res = ['data', 'name', 'age',
                         'sex', 'languages', 'language',
                         'language', 'language', 'pc']
        deleteTagNodes(data, "pc_item")
        self.assertEqual(listNodes(data), test_pref_res)

    def test_delete_tags3(self):
        # Deleting non-present tag, must do nothing
        data = init()
        test_pref_res = ['data', 'name', 'age',
                         'sex', 'languages', 'language',
                         'language', 'language', 'pc',
                         'pc_item', 'pc_item', 'pc_item',
                         'pc_item']
        deleteTagNodes(data, "secondname")
        self.assertEqual(listNodes(data), test_pref_res)

    def test_getparent1(self):
        # Getting parent from "sex" tag in "data"
        data = init()
        res = getParent(data, data[2])
        self.assertEqual(res.tag, "data")

    def test_getparent2(self):
        # Getting parent from "language" C# in "languages"
        data = init()
        res = getParent(data, data[3][2])
        self.assertEqual(res.tag, "languages")

    def test_getparent3(self):
        # Getting parent of root, must return None
        data = init()
        res = getParent(data, data)
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
