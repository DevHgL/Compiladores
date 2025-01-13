import ply.lex as lex

reservados = {
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'print': 'PRINT',
    'const': 'CONST_DEF',
    'type': 'TYPE_DEF',
    'var': 'VAR_DEF',
    'true': 'TRUE',
    'false': 'FALSE',
    'or': 'LOGIC_OP_OR',
    'and': 'LOGIC_OP_AND',
    'record': 'RECORD'
}

tokens = (
    'ID', 'NUMBER', 'ASSIGNMENT', 'COMP_OP', 'LOGIC_OP_OR', 'LOGIC_OP_AND', 
    'CONST_DEF', 'TYPE_DEF', 'VAR_DEF', 'BEGIN', 'END', 'IF', 'THEN', 'ELSE', 
    'WHILE', 'DO', 'TRUE', 'FALSE', 'RECORD'
)

literals = ['+', '-', '*', '/', '=', ',', ';', ':', '.', '[', ']', '(', ')']

t_ASSIGNMENT = r':='
t_COMP_OP = r'(<=|>=|!=|==|<|>)'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservados.get(t.value.lower(), 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def analyze_lexical(source_code):
    lexer.input(source_code)
    tokens_list = []
    while tok := lexer.token():
        tokens_list.append(tok)
    return tokens_list
