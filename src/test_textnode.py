import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_empty_url(self):
        node = TextNode("Lorem ipsum", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_non_empty_url(self):
        node = TextNode("Lorem ipsum", TextType.BOLD, "https://www.high-five.dev")
        self.assertNotEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()
