import unittest

from textnode import TextNode, TextType,text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_NotEqual(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node 8", TextType.LINK)
        self.assertNotEqual(node, node2)
        
    def test_url_blank(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, None) 
        self.assertIs(node.url, None)   
        self.assertIs(node2.url, None) 
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()