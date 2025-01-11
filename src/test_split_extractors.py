import unittest
from split_nodes_extractors import split_nodes_images, split_nodes_links
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
  def test_split_nodes_link(self):
    node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
    )
    expected = [
      TextNode("This is text with a link ", TextType.NORMAL),
      TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
      TextNode(" and ", TextType.NORMAL),
      TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
    ]
    self.assertEqual(split_nodes_links([node]), expected)

  def test_split_nodes_image(self):
    node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.NORMAL
    )
    expected = [
      TextNode("This is text with a ", TextType.NORMAL),
      TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
      TextNode(" and ", TextType.NORMAL),
      TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    ]
    self.assertEqual(split_nodes_images([node]), expected)

  def test_no_links(self):
    node = TextNode("This is plain text with no links.", TextType.NORMAL)
    self.assertEqual(split_nodes_links([node]), [node])

  def test_no_images(self):
    node = TextNode("This is plain text with no images.", TextType.NORMAL)
    self.assertEqual(split_nodes_images([node]), [node])

if __name__ == "__main__":
  unittest.main()
