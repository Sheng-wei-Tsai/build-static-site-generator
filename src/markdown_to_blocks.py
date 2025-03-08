from blocktype import BlockType

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
      if block == "":
        continue
      block = block.strip()
      filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
  lines = block.split("\n")

  # HEADING
  if block.startswith(("# ", "## ", "### ", "#### ", "#### ", "##### ", "###### ")):
    return BlockType.HEADING

  # CODE
  if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
    return BlockType.CODE

  # QUOTE
  if block.startswith(">"):
    for line in lines:
      if not line.startswith(">"):
        return BlockType.PARAGRAPH
    return BlockType.QUOTE

  # UNORDERED LIST
  if block.startswith("- "):
    for line in lines:
      if not line.startswith("- "):
        return BlockType.PARAGRAPH
    return BlockType.UNORDERED_LIST
  # ORDERED LIST
  if block.startswith("1. "):
    index = 1
    for line in lines:
      if not line.startswith(f"{index}. "):
        return BlockType.PARAGRAPH
      index += 1
    return BlockType.ORDERED_LIST

  # all exception cases return PARAGRAPH
  return BlockType.PARAGRAPH

