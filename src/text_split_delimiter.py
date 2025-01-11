import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_split_code(self):
    node = TextNode("This is text with a `code block` word", TextType.NORMAL)
    result = split_nodes_delimiter([node], "`", TextType.CODE)
    expected = [
      TextNode("This is text with a ", TextType.NORMAL),
      TextNode("code block", TextType.CODE),
      TextNode(" word", TextType.NORMAL)
    ]
    self.assertEqual(result, expected)

  def test_split_bold(self):
    node = TextNode("Some **bold** text", TextType.NORMAL)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)
    expected = [
      TextNode("Some ", TextType.NORMAL),
      TextNode("bold", TextType.BOLD),
      TextNode(" text", TextType.NORMAL)
    ]
    self.assertEqual(result, expected)

  def test_unmatched_delimiter(self):
    node = TextNode("This is `unmatched delimiter", TextType.NORMAL)
    with self.assertRaises(ValueError):
      split_nodes_delimiter([node], "`", TextType.CODE)

  def test_no_delimiter(self):
    node = TextNode("Plain text with no special formatting", TextType.NORMAL)
    result = split_nodes_delimiter([node], "`", TextType.CODE)
    # return the original node unchanged
    self.assertEqual(result, [node])

  def test_mixed_nodes(self):
    nodes = [
      TextNode("This is ", TextType.NORMAL),
      TextNode("**bold** text", TextType.NORMAL),
      TextNode(" and this is normal", TextType.NORMAL)
    ]
    result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    expected = [
      TextNode("This is ", TextType.NORMAL),
      TextNode("bold", TextType.BOLD),
      TextNode(" text and this is normal", TextType.NORMAL),
    ]
    self.assertEqual(result, expected)

if __name__ == "__main__":
  unittest.main()