from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
        match self.text_type:
            case "text":
                return LeafNode(self.text)
            case "bold":
                return LeafNode(self.text, "b")
            case "italic":
                return LeafNode(self.text, "i")
            case "code":
                return LeafNode(self.text, "code")
            case "link":
                return LeafNode(self.text, "a", {"href": self.url})
            case "image":
                return LeafNode("", "img", {"src": self.url, "alt": self.text})
            case _:
                raise Exception("Invalid text type")
    
def main():
    node = TextNode("Hello", "World", "https://www.google.com")
    print(node)
