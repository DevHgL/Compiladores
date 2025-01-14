import ply.lex as lex

# Palavras reservadas
reservados = {
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'const': 'CONST_DEF',
    'type': 'TYPE_DEF',
    'var': 'VAR_DEF',
    'true': 'TRUE',
    'false': 'FALSE',
    'or': 'LOGIC_OP_OR',
    'and': 'LOGIC_OP_AND',
    'record': 'RECORD',
    'array': 'ARRAY',
    'of': 'OF'
}

# Lista de tokens
tokens = tuple(reservados.values()) + (
    'ID', 'NUMBER', 'ASSIGNMENT', 'COMP_OP',
)

# Literais
literals = ['+', '-', '*', '/', '=', ',', ';', ':', '.', '[', ']', '(', ')', '<', '>']

# Regras de expressão regular
t_ASSIGNMENT = r':='
t_COMP_OP = r'(<=|>=|!=|==|<|>)'
t_ignore = ' \t'

# Token para números
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Token para identificadores e palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservados.get(t.value.lower(), 'ID')  # Verifica palavras reservadas
    return t

# Nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres inválidos
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Constrói o analisador léxico
lexer = lex.lex()

def analyze_lexical(source_code):
    """Processa o código fonte e gera os tokens."""
    lexer.input(source_code)
    tokens = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    return tokens
