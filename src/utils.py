import re

from textnode import TextNode

def split_text_node(node, delimiter, text_type):
    new_nodes = []
    split_text = node.text.split(delimiter)

    if len(split_text)  % 2 == 0:
        raise Exception("Invalid markdown syntax, delimiter must be surrounded by text")
    
    for i in range(0, len(split_text)):
        if i % 2 == 0:
            new_nodes.append(TextNode(split_text[i], "text"))
        else:
            new_nodes.append(TextNode(split_text[i], text_type))

    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == "text":
            new_nodes.extend(split_text_node(node, delimiter, text_type))
        else:
            new_nodes.append(node)

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
