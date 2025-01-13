from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  """
  Splits text nodes based on delimiter and converts the delimited portions into a specific text type: bold, italic...

  (Input)
  Args:
    old_nodes(list): A list of TextNode objects
    delimiter(str): The delimiter to split the text by.
    text_type(TextType): The type to assign to the delimited text

  Output
  Return:
    list: A new list of TextNode objects, where delimited sections are converted
  """
  new_nodes = []

  for node in old_nodes:
    if node.text_type != TextType.NORMAL:
      new_nodes.append(node)
      continue

    # split the node's text by the delimiter
    parts = node.text.split(delimiter)
    if len(parts) % 2 == 0:
      raise ValueError(f"Unmatched delimiter '{delimiter} in text: {node.text}'")
    for i, part in enumerate(parts):
      if i % 2 == 0:
        # Even indices are plain text
        if part:
          new_nodes.append(TextNode(part, TextType.NORMAL))
      else:
        # odd are delimited text
        new_nodes.append(TextNode(part, text_type))

  return new_nodes


