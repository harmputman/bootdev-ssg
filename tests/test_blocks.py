import unittest

from src.markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)

class TestBlocksMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading_block_to_block_type(self):
        md = "# Heading"
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.HEADING)

    def test_code_block_to_block_type(self):
        md = """```
console.log('test');
```"""
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.CODE)

    def test_quote_block_to_block_type(self):
        md = """> some
> multiline
> quote"""
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.QUOTE)

    def test_ul_block_to_block_type(self):
        md = """- some
- unordered
- list"""
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.ULIST)

    def test_ol_block_to_block_type(self):
        md = """1. some
2. ordered
3. list"""
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.OLIST)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()