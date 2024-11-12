# ====================================================================
#                                                                    =
# Trabalho de Compiladores para a gramática oferecida no classroom   =
# @author: Hugo Leonardo Melo                                        =
#                                                                    =
# ====================================================================
import ply.lex as lex

# Palavras reservadas
reserved_words = {
    
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
    'ID',           # Identificadores (nomes de variáveis)
    'ATRIBUITION',  # Atribuição =
    'EQUALS',       # ==
    'NOT_EQUALS',   # !=
    'LESS_THAN',    # <
    'GREATER_THAN', # >
    'LESS_EQUAL',   # <=
    'GREATER_EQUAL',# >=
    'DOTS',         # :
    'ASSING',       # :=
    'DOT',          # .
    'BREAKLINE',    # \n
    'BREAKLINE_2',  # \r
    'OBRACKET',     # [
    'CBRACKET',     # ]

] + list(reserved_words.values())

# Expressões regulares para tokens simples
t_PLUS           = r'\+'
t_MINUS          = r'-'
t_TIMES          = r'\*'
t_DIVIDE         = r'/'
t_LPAREN         = r'\('
t_RPAREN         = r'\)'
t_LBRACE         = r'\{'
t_RBRACE         = r'\}'
t_SEMICOLON      = r';'
t_COMMA          = r','
t_ATRIBUITION    = r'='
t_ASSING         = r':='
t_EQUALS         = r'=='
t_NOT_EQUALS     = r'!='
t_LESS_THAN      = r'<'
t_GREATER_THAN   = r'>'
t_LESS_EQUAL     = r'<='
t_GREATER_EQUAL  = r'>='
t_DOTS           = r':'
t_DOT            = r'\.'
t_OBRACKET       = r'\['
t_CBRACKET       = r'\]'

# Função para capturar quebra de linha \n
def t_BREAKLINE(t):
    r'\n'
    t.lexer.lineno += 1  # Atualiza a contagem de linhas
    return t

# Função para capturar quebra de linha \r (carriage return)
def t_BREAKLINE_2(t):
    r'\r'
    return t

# Expressão regular para um identificador (ID)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t

# Expressão regular para um número (NUMBER)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Converte o número para inteiro
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Definição de regras para lidar com erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na posição {t.lexpos}")
    t.lexer.skip(1)

# Criação do analisador léxico
lexer = lex.lex()

# Função para ler o arquivo e analisar o código
def analyze_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

# Analisando o arquivo de entrada
analyze_file('./exemplo2.sp')

# Função para ler o arquivo e analisar o código
def analyze_file(filename, output_filename):
    with open(filename, 'r') as file:
        data = file.read()
    lexer.input(data)
    
    with open(output_filename, 'w') as output_file:
        while True:
            tok = lexer.token()
            if not tok:
                break
            output_file.write(str(tok) + '\n')  # Escreve a saída no arquivo
        print(f"Análise léxica concluída e armazenada em {output_filename}")

# Analisando o arquivo de entrada e salvando a saída
analyze_file('./exemplo3.sp', './saida_lexica.txt')
