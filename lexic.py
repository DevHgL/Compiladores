###########################################################################################
#                                                                                         #      
#   Author: Hugo Leonardo Melo                                                            #                 
#                                                                                         #              
#   Trabalho do Analisador Léxico                                                         #              
#                                                                                         #              
###########################################################################################
import ply.lex as lex
import sys

# Definindo uma classe para armazenar os tokens
class Token():
    def __init__(self, token):
        self.tipo = tok.type
        self.valor = tok.value
        self.linha = tok.lineno
lista_analisados = list()

# Palavras reservadas
reservados = {
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

# Tokens literais, possuem como nome o mesmo simbolo que os define
literals = ['+','-','*','/','=',',',';',':','.','[',']','(',')']

# Definicao dos tokens + uniao das palavras reservadas
tokens = [
    'ID',
    'NUMBER',
    'STRING',
    'ASSIGNMENT',    
    'LESS_THAN', 
    'GREATER_THAN', 
    'LESS_EQUAL', 
    'GREATER_EQUAL',
    'EQUAL', 
    'NOT_EQUALS', 
    'COMP_OP'
] + list(reservados.values())

# Expressoes regulares dos tokens simples

t_ASSIGNMENT = r':='
t_COMP_OP = r'>|>=|<|<='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_NOT_EQUALS = r'!='
t_EQUAL = r'=='


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservados.get(t.value,'ID')
    t.value = str(t.value)
    return t

def t_STRING(t):
    r'"[A-Za-z0-9\s]*"'
    t.value = str(t.value)
    return t

# Regra para determinar posição da linha do codigo
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados pelo analisador lexico, espacos e tabulacoes
t_ignore  = ' \t'

# Tratamento de erro quando um caracter nao e identificado pelo analisador
def t_error(t):
    print(f"Caracter {t.value[0]} nao identificado.")
    # Pula o elemento para que identifique outros possiveis erros na mesma analise
    t.lexer.skip(1)

# Compila as regras definidas para o lexer
lexer = lex.lex()


def run_lexical_analysis(data):
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


# Abre e entrega o arquivo a ser analisado
file_name = sys.argv[1]
data = open(file_name, 'r').read()
lexer.input(data)

# Analisa os tokens do arquivo
while True:
    tok = lexer.token()
    if not tok: 
        break
    lista_analisados.append(tok)
    # print(tok)