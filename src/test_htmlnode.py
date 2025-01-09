import unittest

from htmlnode import HTMLNode

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

  if __name__ == "__main__":
    unittest.main()