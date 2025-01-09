class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children if children else []
    self.props = props if props else {}

  def props_to_html(self):
    """Convert props dictionary to HTML attributes string."""
    return "".join(f' {key}="{value}"' for key, value in self.props.items())

  def to_html(self):
    """Render the node as HTML. To be overridden by subclasses."""
    raise NotImplementedError("Subclasses should implement this method.")

  def __repr__(self):
    return (
      f"HTMLNode(tag={self.tag}, value={self.value}, "
      f"children={self.children}, props={self.props})"
    )
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    if value is None:
      raise ValueError("LeafNode must have a value.")
    super().__init__(tag=tag, value=value, props=props)

  def to_html(self):
    """Render the leaf node as an HTML string."""
    if self.tag is None:
      return self.value
    props_str = self.props_to_html()
    return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

  def __repr__(self):
    return (
      f"LeafNode(tag={self.tag}, value={self.value}, "
      f"props={self.props})"
    )

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    if not tag:
      raise ValueError("ParentNode must have a tag.")
    if not children:
      raise ValueError("ParentNode must have children.")
    super().__init__(tag=tag, children=children, props=props)

  def to_html(self):
    """Render the parent node and its children as an HTML string."""
    props_str = self.props_to_html()
    children_html = "".join(child.to_html() for child in self.children)
    return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"

  def __repr__(self):
    return (
      f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
    )
