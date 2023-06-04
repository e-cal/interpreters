from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"
    IDENT = "IDENT"
    INT = "INT"
    ASSIGN = "="
    PLUS = "+"
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    FUNCTION = "FUNCTION"
    LET = "LET"


@dataclass
class Token:
    token_type: TokenType
    literal: str


class Lexer:
    def __init__(self, input: str) -> None:
        self.input = input
        self.position = 0
        self.read_position = 0
        self.ch = "\0"
        self.read_char()

    def read_char(self) -> None:
        # there's probably a way to do this with a generator
        if self.read_position >= len(self.input):
            self.ch = "\0"
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def next_token(self) -> Token:
        tok = {
            "=": Token(TokenType.ASSIGN, "="),
            ";": Token(TokenType.SEMICOLON, ";"),
            "(": Token(TokenType.LPAREN, "("),
            ")": Token(TokenType.RPAREN, ")"),
            ",": Token(TokenType.COMMA, ","),
            "+": Token(TokenType.PLUS, "+"),
            "{": Token(TokenType.LBRACE, "{"),
            "}": Token(TokenType.RBRACE, "}"),
            "\0": Token(TokenType.EOF, ""),
        }[self.ch]
        self.read_char()
        return tok
