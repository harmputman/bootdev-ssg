import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    return list(filter(lambda x: x != "", map(lambda x: x.strip(), markdown.split("\n\n"))))

def block_to_block_type(block):
    if re.match(r"^#{1,6}", block):
        return BlockType.HEADING

    if re.match(r"^```[^`]*```$", block):
        return BlockType.CODE

    if all(map(lambda x: re.match(r"^> ", x), block.split("\n"))):
        return BlockType.QUOTE

    if all(map(lambda x: re.match(r"^- ", x), block.split("\n"))):
        return BlockType.ULIST

    if all(map(lambda x: re.match(r"^\d\. ", x), block.split("\n"))):
        return BlockType.OLIST

    return BlockType.PARAGRAPH