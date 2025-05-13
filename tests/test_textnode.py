import unittest

from src.textnode import TextNode, TextType


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

    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image_to_html(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold_to_html(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()
