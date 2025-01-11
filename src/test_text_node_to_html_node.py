import unittest
from textnode import TextNode, TextType
from htmlnode import text_node_to_html_node, LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):
  def test_normal_text(self):
    text_node = TextNode("Normal text", TextType.NORMAL)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.to_html(), "Normal text")

  def test_bold_text(self):
    text_node = TextNode("Bold text", TextType.BOLD)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

  def test_italic_text(self):
    text_node = TextNode("Italic text", TextType.ITALIC)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

  def test_link_text(self):
    text_node = TextNode("Click me", TextType.LINK, url="https://example.com")
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.to_html(), '<a href="https://example.com">Click me</a>')

  def test_code_text(self):
    text_node = TextNode("Code text", TextType.CODE)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.to_html(), "<code>Code text</code>")

  def test_image_text(self):
    text_node = TextNode("Image alt Text", TextType.IMAGE, url="https://example.com/image.png")
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.to_html(), '<img src="https://example.com/image.png" alt="Image alt Text">')

  def test_invalid_type(self):
    class FakeType:
      pass
    text_node = TextNode("Invalid text", FakeType())
    with self.assertRaises(ValueError):
      text_node_to_html_node(text_node)

  def test_link_missing_url(self):
    text_node = TextNode("Click me", TextType.LINK)
    with self.assertRaises(ValueError):
      text_node_to_html_node(text_node)

  def test_image_missing_url(self):
    text_node = TextNode("Image alt text", TextType.IMAGE)
    with self.assertRaises(ValueError):
      text_node_to_html_node(text_node)

if __name__ == "__main__":
  unittest.main()