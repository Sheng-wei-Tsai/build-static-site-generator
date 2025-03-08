from blocktype import BlockType
from markdown_to_blocks import block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from textnode import TextNode

def markdown_to_html_node(markdown):
  # pareent div node
  parent_node = HTMLNode("div", None, [])

  blocks = markdown_to_blocks(markdown)

  for block in blocks:
    block_type = block_to_block_type(block)
    block_node = create_block_node(block, block_type)
    parent_node.children.append(block_node)

  return parent_node

def create_block_node(block, block_type):

  if block_type == BlockType.PARAGRAPH:
    return create_paragraph_node(block)
  elif block_type == BlockType.HEADING:
    return create_heading_node(block)
  elif block_type == BlockType.CODE:
    return create_code_node(block)
  elif block_type == BlockType.QUOTE:
    return create_quote_node(block)
  elif block_type == BlockType.UNORDERED_LIST:
    return create_unordered_list_node(block)
  elif block_type == BlockType.ORDERED_LIST:
    return create_ordered_list_node(block)
  else:
    return create_paragraph_node(block)

def create_paragraph_node(block):
  children = text_to_children(block)
  return HTMLNode("p", None, children)

def create_heading_node(block):
  # count the number of # at the beginning of the block
  level = 0
  for char in block:
    if char == "#":
      level += 1
    else:
      break
  # remove the # and the space afterit
  content = block[level+1:]
  children = text_to_children(content)
  return HTMLNode(f"h{level}", None, children)

def create_code_node(block):
  # remove the ``` at the beginning and the ``` at the end
  content = block[3:-3].strip()
  # for code block, we do not parse inline markdown
  text_node = TextNode(content, "text")
  code_node = text_node_to_html_node(text_node)

  # wrap in a pre tag
  return HTMLNode("pre", None, [code_node])

def create_quote_node(block):
  # remove the > from each line
  lines = block.split("\n")
  content = "\n".join(line[1:].strip() for line in lines)

  children = text_to_children(content)
  return HTMLNode("blockquote", None, children)

def create_unordered_list_node(block):
  lines = block.split("\n")
  list_items = []
  for line in lines:
  # remove the - from each line
   content = line.lstrip()[2:]
   children = text_to_children(content)
   list_item = HTMLNode("li", None, children)
   list_items.append(list_item)
  return HTMLNode("ul", None, list_items)

def create_ordered_list_node(block):
  lines = block.split("\n")
  list_items = []

  for line in lines:
    # find the position of the first period
    period_position = line.find(".")
    if period_position == -1:
      # extract the content after the period and space
      content = line[period_position+1:].strip()
      children = text_to_children(content)
      list_item = HTMLNode("li", None, children)
      list_items.append(list_item)
    return HTMLNode("ol", None, list_items)

def text_to_children(text):
  text_nodes = text_to_textnodes(text)
  html_nodes = []
  for text_node in text_nodes:
    html_node = text_node_to_html_node(text_node)
    html_nodes.append(html_node)
  return html_nodes



