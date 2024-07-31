import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("td", "content", [], {"class": "table-cell", "href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' class="table-cell" href="https://www.google.com"')

    def test_props_to_html_none(self):
        node = HTMLNode("td", "content", [])
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("td", "content", [], {"class": "table-cell", "href": "https://www.google.com"})
        self.assertEqual(repr(node), "HTMLNode(td, content, [], {'class': 'table-cell', 'href': 'https://www.google.com'})")

    def test_repr_none(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(None, None, None, None)")

if __name__ == "__main__":
    unittest.main()
