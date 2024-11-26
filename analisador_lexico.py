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

# Lista de tokens
tokens = [
    'STRING',       # Strings entre aspas
    'COLON',        # :
    'LBRACKET',     # [
    'RBRACKET',     # ]
    'ASSIGN',       # :=
    'ATRIB',       # =
    'NUMBER',       # Números inteiros
    'PLUS',         # +
    'MINUS',        # -
    'TIMES',        # *
    'DIVIDE',       # /
    'LPAREN',       # (
    'RPAREN',       # )
    'LBRACE',       # {
    'RBRACE',       # }
    'SEMICOLON',    # ;
    'COMMA',        # ,
    'ID',           # Identificadores
    'EQUALS',       # ==
    'NOT_EQUALS',   # !=
    'LESS_THAN',    # <
    'GREATER_THAN', # >
    'LESS_EQUAL',   # <=
    'GREATER_EQUAL',# >=
    'DOT',          # .
] + list(reserved_words.values())

# Expressões regulares para tokens simples
t_STRING = r'\".*?\"'
t_COLON = r':'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_ASSIGN = r':='
t_ATRIB= r'='
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
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_DOT = r'\.'


# Definição de identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value, 'ID')  # Verifica palavras reservadas
    return t

# Definição de números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Converte o valor para inteiro
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Contar novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Lidar com caracteres ilegais
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)
    
    


# Construir o analisador léxico
lexer = lex.lex()

# Função para analisar um arquivo
def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        lexer.input(data)
        for tok in lexer:
            print(f"{tok.type}({tok.value}) na linha {tok.lineno}")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado!")
    except Exception as e:
        print(f"Erro ao analisar o arquivo: {e}")
