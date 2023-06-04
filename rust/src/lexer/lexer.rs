// use anyhow::Result;

#[allow(dead_code)]
pub enum Token {
    Illegal,
    EOF,

    Ident(String),
    Int(String),

    Assign,
    Plus,

    Comma,
    Semicolon,

    Lparen,
    Rparen,
    Lbrace,
    Rbrace,

    Function,
    Let,
}
