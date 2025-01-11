import re

def extract_markdown_images(text):
  """
  Extracts markdown image syntax from the given text and returns a list of tuples.
  Each tuple contains the alt text and URL.
  :parameter test: str = The raw markdown text
  :return: list of tuples [(alt_text, url), ...]
  """

  pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(pattern, text)
  return matches

def extract_markdown_links(text):
  """
  Extracts markdown link syntax from the given text and return a list of tuples.
  Each tuple contains the anchor text and URL.
  :param text: str = The raw markdown text
  :return: list of tuples [(anchor_text, url), ...]
  """

  pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(pattern, text)
  return matches