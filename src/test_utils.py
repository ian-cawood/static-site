import unittest

from utils import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text"),
        ])

    def test_bold_block(self):
        node = TextNode("This is text with a **bold block** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", "text"),
            TextNode("bold block", "bold"),
            TextNode(" word", "text"),
        ])

    def test_italic_block(self):
        node = TextNode("This is text with a *italic block* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", "text"),
            TextNode("italic block", "italic"),
            TextNode(" word", "text"),
        ])

    def test_double_bold_block(self):
        node = TextNode("This is text with a **bold block** and another **bold block**", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", "text"),
            TextNode("bold block", "bold"),
            TextNode(" and another ", "text"),
            TextNode("bold block", "bold"),
            TextNode("", "text"),
        ])

    def test_no_closing_delimiter(self):
        node = TextNode("This is text with a *italic block word", "text")
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", "italic")

    def test_no_opening_delimiter(self):
        node = TextNode("This is text with a italic block* word", "text")
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", "italic")

    def test_extract_markdown_images(self):
        text = "![alt text](https://www.google.com)"
        self.assertEqual(extract_markdown_images(text), [("alt text", "https://www.google.com")])

    def test_extract_markdown_images_multiple(self):
        text = "some other text ![alt text](https://www.google.com) in the middle ![alt](https://www.google.ca)"
        self.assertEqual(extract_markdown_images(text), [("alt text", "https://www.google.com"), ("alt", "https://www.google.ca")])

    def test_extract_markdown_images_no_images(self):
        text = "some other text in the middle"
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_markdown_links(self):
        text = "some text [link text](https://www.google.com)"
        self.assertEqual(extract_markdown_links(text), [("link text", "https://www.google.com")])

    def test_extract_markdown_links_multiple(self):
        text = "some text [link text](https://www.google.com) in the middle [link](https://www.google.ca)"
        self.assertEqual(extract_markdown_links(text), [("link text", "https://www.google.com"), ("link", "https://www.google.ca")])

    def test_extract_markdown_links_no_links(self):
        text = "some other text in the middle"
        self.assertEqual(extract_markdown_links(text), [])
