###########################################################################################
#                                                                                         #      
#   Author: Hugo Leonardo Melo                                                            #                 
#                                                                                         #              
#   Trabalho do Analisador Léxico                                                         #              
#                                                                                         #              
###########################################################################################
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
    'print': 'PRINT',
    'const': 'CONSTANT',
    'var': 'VARIABLE',
    'true': 'TRUE',
    'false': 'FALSE',
    'or': 'LOGIC_OP_OR',
    'and': 'LOGIC_OP_AND',
    'type': 'TYPE',
    'array': 'ARRAY',
    'of': 'OF',
    'record': 'RECORD'
}

# Tokens literais
literals = ['+', '-', '*', '/', '=', ',', ';', ':', '.', '[', ']', '(', ')']

tokens = (
    'ID', 'NUMBER', 'TRUE', 'FALSE', 'BEGIN', 'END', 'IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'PRINT',
    'CONSTANT', 'VARIABLE', 'COMP_OP', 'LOGIC_OP_OR', 'LOGIC_OP_AND', 'ASSIGNMENT', 'TYPE', 'ARRAY', 'OF', 'RECORD'
    # Adicione outros tokens conforme necessário
)

# Definições de tokens
t_TRUE = r'true'
t_FALSE = r'false'
t_BEGIN = r'begin'
t_END = r'end'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_WHILE = r'while'
t_DO = r'do'
t_PRINT = r'print'
t_CONSTANT = r'const'
t_VARIABLE = r'var'
t_ASSIGNMENT = r':='
t_COMP_OP = r'==|!=|>=|<=|>|<'
t_TYPE = r'type'
t_ARRAY = r'array'
t_OF = r'of'
t_RECORD = r'record'

# Regras regulares para tokens simples
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservados.get(t.value.lower(), 'ID')  # Prioridade para palavras reservadas
    return t

# Regra para contar linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados (espaços e tabulações)
t_ignore = ' \t'

# Regra para tratar erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Definição de um lexer
lexer = lex.lex()