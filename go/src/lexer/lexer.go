package lexer

type TokenType string

type Token struct {
	Type    TokenType
	Literal string
}

const (
	// Special tokens
	Illegal = "ILLEGAL"
	EOF     = "EOF"

	// Identifiers + literals
	Ident = "IDENT"
	Int   = "INT"

	// Operators
	Assign = "="
	Plus   = "+"

	// Delimiters
	Comma     = ","
	Semicolon = ";"
	Lparen    = "("
	Rparen    = ")"
	Lbrace    = "{"
	Rbrace    = "}"

	// Keywords
	FunctiON = "FUNCTION"
	Let      = "LET"
)

type Lexer struct {
	input        string
	position     int  // current position in input (points to current char)
	readPosition int  // current reading position in input (after current char)
	ch           byte // current char under examination
}

func New(input string) *Lexer {
	l := &Lexer{input: input}
	l.readChar()
	return l
}

func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) { // read to end of input
		l.ch = 0
	} else {
		l.ch = l.input[l.readPosition]
	}
	l.position = l.readPosition
	l.readPosition += 1
}

func newToken(tokenType TokenType, ch byte) Token {
	return Token{Type: tokenType, Literal: string(ch)}
}

func (l *Lexer) NextToken() Token {
	var tok Token

	switch l.ch {
	case '=':
		tok = newToken(Assign, l.ch)
	case ';':
		tok = newToken(Semicolon, l.ch)
	case '(':
		tok = newToken(Lparen, l.ch)
	case ')':
		tok = newToken(Rparen, l.ch)
	case ',':
		tok = newToken(Comma, l.ch)
	case '+':
		tok = newToken(Plus, l.ch)
	case '{':
		tok = newToken(Lbrace, l.ch)
	case '}':
		tok = newToken(Rbrace, l.ch)
	case 0:
		tok.Literal = ""
		tok.Type = EOF
	}
	l.readChar()
	return tok
}
