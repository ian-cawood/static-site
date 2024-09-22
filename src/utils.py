import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)

def split_text_node(node, delimiter, text_type):
    new_nodes = []
    split_text = node.text.split(delimiter)

    if len(split_text)  % 2 == 0:
        raise Exception("Invalid markdown syntax, delimiter must be surrounded by text")
    
    for i in range(0, len(split_text)):
        if i % 2 == 0:
            new_nodes.append(TextNode(split_text[i], text_type_text))
        else:
            new_nodes.append(TextNode(split_text[i], text_type))

    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            new_nodes.extend(split_text_node(node, delimiter, text_type))
        else:
            new_nodes.append(node)

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            original_text = node.text
            images = extract_markdown_images(original_text)
            if len(images) > 0:
                for image in images:
                    sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
                    if len(sections) != 2:
                        raise ValueError("Invalid markdown, image section not closed")
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], text_type_text))
                    new_nodes.append(TextNode(image[0], text_type_image, image[1]))
                    original_text = sections[1]
                if original_text != "":
                    new_nodes.append(original_text, text_type_text)
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            original_text = node.text
            links = extract_markdown_links(original_text)
            if len(links) > 0:
                for link in links:
                    sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
                    if len(sections) != 2:
                        raise ValueError("Invalid markdown, link section not closed")
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], text_type_text))
                    new_nodes.append(TextNode(link[0], text_type_link, link[1]))
                    original_text = sections[1]
                if original_text != "":
                    new_nodes.append(original_text, text_type_text)
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes
