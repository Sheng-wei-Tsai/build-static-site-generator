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