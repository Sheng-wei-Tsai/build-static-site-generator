from textnode import TextNode, TextType
from markdown_extractors import extract_markdown_images, extract_markdown_links

def split_nodes_images(old_nodes):
  """
  Splits a list of TextNodes containing markdown image syntax into separate nodes.

  :parameter old_nodes: list of TextNode objects
  :return list of new TextNode objects, where image markdown is split into image and text nodes
  """
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.NORMAL:
      new_nodes.append(node)
      continue
    images = extract_markdown_images(node.text)

    if not images:
      new_nodes.append(node)
      continue
    remaining_text = node.text
    for alt, url in images:
      sections = remaining_text.split(f"![{alt}]({url})", 1)
      if sections[0]:
        new_nodes.append(TextNode(sections[0], TextType.NORMAL))
      new_nodes.append(TextNode(alt, TextType.IMAGE, url))
      remaining_text = sections[1]

    if remaining_text:
      new_nodes.append(TextNode(remaining_text, TextType.NORMAL))
  return new_nodes

def split_nodes_links(old_nodes):
  """
  Splits a list of TextNodes containing markdown link syntax into separate nodes.

  :parameter old_nodes: list of TextNode objects
  :return list of new TextNode objects, where link markdown is split into link and text nodes
  """

  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.NORMAL:
      new_nodes.append(node)
      continue
    links = extract_markdown_links(node.text)

    if not links:
      new_nodes.append(node)
      continue

    remaining_text = node.text
    for anchor_text, url in links:
      sections = remaining_text.split(f"[{anchor_text}]({url})", 1)
      if sections[0]:
        new_nodes.append(TextNode(sections[0], TextType.NORMAL))
      new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
      remaining_text = sections[1]

    if remaining_text:
      new_nodes.append(TextNode(remaining_text, TextType.NORMAL))
  return new_nodes