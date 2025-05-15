from src.htmlnode import HTMLNode, ParentNode, LeafNode
from src.markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)
from src.markdown_inline import text_to_textnodes
from src.textnode import TextNode, TextType


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))

    return ParentNode("div", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.HEADING:
            return handle_heading_block(block)
        case BlockType.CODE:
            return handle_code_block(block)
        case BlockType.QUOTE:
            return handle_quote_block(block)
        case BlockType.ULIST:
            return handle_ulist_block(block)
        case BlockType.OLIST:
            return handle_olist_block(block)
        case BlockType.PARAGRAPH:
            return handle_generic_block("p", block)
        case _:
            raise ValueError(f"invalid block type: {block_type}")

def handle_heading_block(block):
    level = block.count("#")
    text = block[level:].strip()
    html_node = LeafNode(f"h{level}", text)
    return html_node

def handle_code_block(block):
    code = block[4:-3].strip() + "\n"
    text_node = TextNode(code, TextType.CODE)
    return ParentNode("pre", [text_node.to_html_node()])

def handle_quote_block(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def handle_ulist_block(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        children.append(handle_generic_block("li", line[2:]))
    return ParentNode("ul", children)

def handle_olist_block(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        children.append(handle_generic_block("li", line[3:].strip()))
    return ParentNode("ol", children)

def handle_generic_block(tag, block):
    lines = block.split("\n")
    text = " ".join(lines)
    return ParentNode(tag, text_to_children(text))

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node.to_html_node())
    return children

