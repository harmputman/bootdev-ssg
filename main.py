from src.textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.high-five.dev")
    print(node)

main()
