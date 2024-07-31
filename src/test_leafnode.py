import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_value_to_html(self):
        node = LeafNode("content")
        self.assertEqual(node.to_html(), "content")

    def test_none_value_to_html(self):
        node = LeafNode(None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_tag_value_to_html(self):
        node = LeafNode("content", "td")
        self.assertEqual(node.to_html(), "<td>content</td>")

    def test_full_to_html(self):
        node = LeafNode("content", "td", {"class": "table-cell", "href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<td class="table-cell" href="https://www.google.com">content</td>')

if __name__ == "__main__":
    unittest.main()
