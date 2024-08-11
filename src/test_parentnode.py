import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_leaf_children_to_html(self):
        node = ParentNode("p", [
            LeafNode("content"),
            LeafNode("content", "td", {"class": "table-cell", "href": "https://www.google.com"})
        ])
        self.assertEqual(node.to_html(), '<p>content<td class="table-cell" href="https://www.google.com">content</td></p>')

    def test_no_children_to_html(self):
        node = ParentNode("p", [])
        self.assertEqual(node.to_html(), '<p></p>')

    def test_parent_children_to_html(self):
        node = ParentNode("p", [
            ParentNode("div", [
                LeafNode("content"),
                LeafNode("content", "td", {"class": "table-cell", "href": "https://www.google.com"})
            ]),
            LeafNode("different content")
        ])
        self.assertEqual(node.to_html(), '<p><div>content<td class="table-cell" href="https://www.google.com">content</td></div>different content</p>')

    def test_double_nested_parents_to_html(self):
        node = ParentNode("p", [
            ParentNode("div", [
                ParentNode("span", [
                    LeafNode("content"),
                    LeafNode("content", "td", {"class": "table-cell", "href": "https://www.google.com"})
                ]),
                LeafNode("different content")
            ]),
            LeafNode("different content")
        ])
        self.assertEqual(node.to_html(), '<p><div><span>content<td class="table-cell" href="https://www.google.com">content</td></span>different content</div>different content</p>')

    def test_none_tag_to_html(self):
        node = ParentNode(None, [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_none_children_to_html(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
