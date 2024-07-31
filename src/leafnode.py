from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value,tag=None, props=None):
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be None")
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
