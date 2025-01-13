import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html_empty(self):
    node = HTMLNode(tag="a")
    self.assertEqual(node.props_to_html(), "")

  def test_props_to_html_with_attributes(self):
    node = HTMLNode(
      tag="a", props={"href": "https://www.google.com", "target": "_blank"}
    )
    self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

  def test_repr(self):
    node = HTMLNode(
      tag="div", value="Hello, world!", props={"class": "container"}
    )
    self.assertEqual(
      repr(node),
      "HTMLNode(tag=div, value=Hello, world!, children=[], props={'class': 'container'})",
    )



class TestLeafNode(unittest.TestCase):
  def test_render_leaf_node_with_tag(self):
    node = LeafNode("p", "This is a paragraph of text.")
    self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

  def test_render_leaf_node_with_props(self):
    node = LeafNode(
      "a", "Click me!", {"href": "https://www.google.com", "target":"_blank"}
    )
    self.assertEqual(node.to_html(),
                     '<a href="https://www.google.com" target="_blank">Click me!</a>'
                     )
  def test_render_leaf_node_as_raw_text(self):
    node = LeafNode(
      None, "This is raw text."
    )
    self.assertEqual(node.to_html(), "This is raw text.")

  def test_leaf_node_no_value_raises_error(self):
    with self.assertRaises(ValueError):
      LeafNode("p", None)

  def test_repr(self):
    node = LeafNode("b", "Bold text", {"class": "bold"})
    self.assertEqual(
      repr(node),
      "LeafNode(tag=b, value=Bold text, props={'class': 'bold'})",
    )

  if __name__ == "__main__":
    unittest.main()