# ====================================================================
#                                                                    =
# Trabalho de Compiladores para a gramática oferecida no classroom   =
# @author: Hugo Leonardo Melo                                        =
#                                                                    =
# ====================================================================

import ply.lex as lex
import ply.yacc as yacc

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
    'NUMERO',         # Números inteiros
    'STRING',         # Strings
    'PLUS',           # +
    'MINUS',          # -
    'TIMES',          # *
    'DIVIDE',         # /
    'LPAREN',         # (
    'RPAREN',         # )
    'SEMICOLON',      # ;
    'COMMA',          # ,
    'ID',             # Identificadores (nomes de variáveis)
    'EQUALS',         # =
    'COLON',          # :
    'ASSIGN',         # :=
    'DOT',            # .
    'LBRACKET',       # [
    'RBRACKET',       # ]
    'NOT_EQUALS',     # !=
    'LESS_THAN',      # <
    'GREATER_THAN',   # >
    'LESS_EQUAL',     # <=
    'GREATER_EQUAL',  # >=
] + list(reserved_words.values())

# Expressões regulares para tokens simples
t_PLUS           = r'\+'
t_MINUS          = r'-'
t_TIMES          = r'\*'
t_DIVIDE         = r'/'
t_LPAREN         = r'\('
t_RPAREN         = r'\)'
t_SEMICOLON      = r';'
t_COMMA          = r','
t_EQUALS         = r'='
t_COLON          = r':'
t_ASSIGN         = r':='
t_DOT            = r'\.'
t_LBRACKET       = r'\['
t_RBRACKET       = r'\]'
t_NOT_EQUALS     = r'!='
t_LESS_THAN      = r'<'
t_GREATER_THAN   = r'>'
t_LESS_EQUAL     = r'<='
t_GREATER_EQUAL  = r'>='

# Expressão regular para um identificador (ID)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value.lower(), 'ID')  # Verifica se é uma palavra reservada (ignora maiúsculas/minúsculas)
    return t

# Expressão regular para um número (NUMERO)
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)  # Converte o número para inteiro
    return t

# Expressão regular para uma string (STRING)
def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Remove as aspas
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
def analyze_file(filename, output_filename=None):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        lexer.input(data)
        
        if output_filename:
            with open(output_filename, 'w') as output_file:
                while True:
                    tok = lexer.token()
                    if not tok:
                        break
                    output_file.write(str(tok) + '\n')
                print(f"Análise léxica concluída e armazenada em {output_filename}")
        else:
            while True:
                tok = lexer.token()
                if not tok:
                    break
                print(tok)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado!")

# Função principal que executa a análise automaticamente
def main():
    filename = input("Digite o nome do arquivo a ser analisado (ex: exemplo.sp): ")
    analyze_file(filename)

if __name__ == "__main__":
    main()
