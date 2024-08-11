import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_repr_url(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://www.google.com)")

    def test_text_node_to_html_node_invalid(self):
        node = TextNode("This is a text node", "invalid")
        with self.assertRaises(Exception):
            node.text_node_to_html_node()

    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", "text")
        self.assertEqual(node.text_node_to_html_node().to_html(), "This is a text node")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.text_node_to_html_node().to_html(), "<b>This is a text node</b>")
      
    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is a text node", "italic")
        self.assertEqual(node.text_node_to_html_node().to_html(), "<i>This is a text node</i>")

    def test_text_node_to_html_node_code(self):
        node = TextNode("This is a text node", "code")
        self.assertEqual(node.text_node_to_html_node().to_html(), "<code>This is a text node</code>")

    def test_text_node_to_html_node_link(self):
        node = TextNode("This is a text node", "link", "https://www.google.com")
        self.assertEqual(node.text_node_to_html_node().to_html(), '<a href="https://www.google.com">This is a text node</a>')

    def test_text_node_to_html_node_image(self):
        node = TextNode("This is a text node", "image", "https://www.google.com")
        self.assertEqual(node.text_node_to_html_node().to_html(), '<img src="https://www.google.com" alt="This is a text node"></img>')


if __name__ == "__main__":
    unittest.main()
