import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
  def test_simple_text(self):
    text = "This is plain text."
    expected = [TextNode("This is plain text.", TextType.NORMAL)]
    self.assertEqual(text_to_textnodes(text), expected)

  def test_bold_and_italic(self):
    text = "This is **bold** and *italic*."
    expected = [
      TextNode("This is ", TextType.NORMAL),
      TextNode("bold", TextType.BOLD),
      TextNode(" and ", TextType.NORMAL),
      TextNode("italic", TextType.ITALIC),
      TextNode(".", TextType.NORMAL),
    ]
    self.assertEqual(text_to_textnodes(text), expected)

  def test_code_and_link(self):
    text = "This is `code` and a [link](https://boot.dev)."
    expected = [
      TextNode("This is ", TextType.NORMAL),
      TextNode("code", TextType.CODE),
      TextNode(" and a ", TextType.NORMAL),
      TextNode("link", TextType.LINK, 'https://boot.dev'),
      TextNode(".", TextType.NORMAL),
    ]
    self.assertEqual(text_to_textnodes(text), expected)

  def test_image_and_text(self):
    text = "An ![image](https://example.com/image.png) and text."
    expected = [
      TextNode("An ", TextType.NORMAL),
      TextNode("image", TextType.IMAGE, 'https://example.com/image.png'),
      TextNode(" and text.", TextType.NORMAL),
    ]
    self.assertEqual(text_to_textnodes(text), expected)


if __name__ == "__main__":
  unittest.main()