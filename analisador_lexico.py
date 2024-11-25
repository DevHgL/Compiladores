
import ply.lex as lex

# Palavras reservadas
reserved_words = {
    'program': 'PROGRAM',
    'const': 'CONST',
    'begin': 'BEGIN',
    'end': 'END',
    'type': 'TYPE',
    'var': 'VAR',
    'integer': 'INTEGER',
    'real': 'REAL',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'array': 'ARRAY',
    'of': 'OF',
    'record': 'RECORD',
    'function': 'FUNCTION',
    'procedure': 'PROCEDURE',
    'while': 'WHILE',
    'do': 'DO',
    'if': 'IF',
    'then': 'THEN',
    'for': 'FOR',
    'write': 'WRITE',
    'read': 'READ',
    'to': 'TO',
    'else': 'ELSE',
    'false': 'FALSE',
    'true': 'TRUE',
    'and': 'AND',
    'or': 'OR',
}

# Lista de tokens, incluindo as palavras reservadas
tokens = [
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COMMA', 'ID', 'ASSIGN',
    'EQUALS', 'NOT_EQUALS', 'LESS_THAN', 'GREATER_THAN',
    'LESS_EQUAL', 'GREATER_EQUAL', 'COLON', 'DOT',
    'STRING', 'LBRACKET', 'RBRACKET'
] + list(reserved_words.values())

# Expressões regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_ASSIGN = r':='
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_COLON = r':'
t_DOT = r'\.'
t_STRING = r'\".*?\"'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Função para identificar identificadores e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value, 'ID')
    return t

# Função para identificar números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Função para rastrear quebras de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Função para tratar erros léxicos
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Criar o analisador léxico
lexer = lex.lex()

# Função para ler um arquivo e analisar o código
def analyze_file(filename, output_filename=None):
    with open(filename, 'r') as file:
        data = file.read()
    lexer.input(data)
    if output_filename:
        with open(output_filename, 'w') as output_file:
            for tok in lexer:
                output_file.write(str(tok) + '\n')
        print(f"Análise léxica concluída. Resultados salvos em {output_filename}")
    else:
        for tok in lexer:
            print(tok)
