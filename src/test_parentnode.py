import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
  def test_render_simple_parent_node(self):
    node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )
    self.assertEqual(
      node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    )

    def test_render_nested_parent_node(self):
      child = ParentNode(
        "div",
        [
          LeafNode("b", "Bold text"),
          LeafNode(None, "Normal text"),
        ],
      )

      parent = ParentNode(
        "section",
        [
          child,
          LeafNode("p", "A paragraph inside the section."),
        ],
      )
      self.assertEqual(
        parent.to_html(),
        "<section><div><b>Bold text</b>Normal text</div><p>A paragraph inside the section.</p></section>"
      )

    def test_no_tag_raises_error(self):
      with self.assertRaises(ValueError) as context:
        ParentNode(None, [LeafNode("b", "Bold text")])
      self.assertEqual(str(context.exception), "ParentNode must have a tag.")

    def test_no_children_raises_error(self):
      with self.assertRaises(ValueError) as context:
        ParentNode("div", [])
      self.assertEqual(str(context.exception), "ParentNode must have children.")

    def test_render_with_props(self):
      node = ParentNode(
        "div",
        [
          LeafNode("b", "Bold text"),
        ],
        props={"class": "container"},
      )
      self.assertEqual(
        node.to_html(),
        '<div class="container"<b>Bold text</b></div>',
      )

    if __name__ == "__main__":
      unittest.main()