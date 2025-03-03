from textnode import TextNode, TextType

def main():
    dumyTextnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dumyTextnode)

main()