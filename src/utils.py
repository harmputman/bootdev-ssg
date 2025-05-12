from textnode import TextType, TextNode
import re

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], old_node.text_type))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    return split_nodes_regex(old_nodes, extract_markdown_images, "![TEXT](URL)", TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes_regex(old_nodes, extract_markdown_links, "[TEXT](URL)", TextType.LINK)

def split_nodes_regex(old_nodes, method, pattern, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        items = method(original_text)
        if (len(items) == 0):
            new_nodes.append(old_node)
            continue
        for (text, url) in items:
            new_pattern = pattern.replace('TEXT', text)
            new_pattern = new_pattern.replace('URL', url)
            sections = original_text.split(new_pattern, 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(text, text_type, url))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]+)\]\(([^\(\)]+)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]+)\)", text)

