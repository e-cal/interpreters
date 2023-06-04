import unittest

from lexer import Lexer, Token, TokenType


class Test(unittest.TestCase):
    def test_next_token(self):
        input = "=+(){},;"

        tests = [
            Token(TokenType.ASSIGN, "="),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.LPAREN, "("),
            Token(TokenType.RPAREN, ")"),
            Token(TokenType.LBRACE, "{"),
            Token(TokenType.RBRACE, "}"),
            Token(TokenType.COMMA, ","),
            Token(TokenType.SEMICOLON, ";"),
            Token(TokenType.EOF, ""),
        ]

        l = Lexer(input)
        for i, tt in enumerate(tests):
            tok = l.next_token()
            self.assertEqual(
                tok.token_type,
                tt.token_type,
                f"tests[{i}] - tokentype wrong. expected={tt.token_type}, got={tok.token_type}",
            )
            self.assertEqual(
                tok.literal,
                tt.literal,
                f"tests[{i}] - literal wrong. expected={tt.literal}, got={tok.literal}",
            )


if __name__ == "__main__":
    unittest.main()
