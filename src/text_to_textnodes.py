from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_extractors import split_nodes_images, split_nodes_links
from textnode import TextNode, TextType
def text_to_textnodes(text):
  """
  Convert a raw markdown-flavoured string into a list of TextNode objects.
  """
  # initial list with a single TextNode containing the entire text
  nodes = [TextNode(text, TextType.NORMAL)]

  # apply each splitting function in order of priority
  nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
  nodes = split_nodes_images(nodes)
  nodes = split_nodes_links(nodes)

  return nodes