from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag cannot be None")
        
        if self.children is None:
            raise ValueError("children cannot be None")
        
        children_html = "".join([child.to_html() for child in self.children])
        
        return f"<{self.tag}>{children_html}</{self.tag}>"