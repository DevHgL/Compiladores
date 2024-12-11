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
class Token:
    def __init__(self, tipo, valor, linha):
        self.tipo = tipo
        self.valor = valor
        self.linha = linha

    def __str__(self):
        return f"Token({self.tipo}, {self.valor}, Linha: {self.linha})"

lista_analisados = []

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
    'or': 'LOGIC_OP_OR',
    'and': 'LOGIC_OP_AND',

}

# Tokens literais, possuem como nome o mesmo simbolo que os define
literals = ['+', '-', '*', '/', '=', ',', ';', ':', '.', '[', ']', '(', ')']

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
t_COMP_OP = r'==|!=|>=|<=|>|<'

t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_NOT_EQUALS = r'!='
t_EQUAL = r'=='
# t_LOGIC_OP = r'\bAND\b|\bOR\b'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservados.get(t.value, 'ID')  # Verifica se é uma palavra reservada
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
t_ignore = ' \t'

# Tratamento de erro quando um caracter nao e identificado pelo analisador
def t_error(t):
    print(f"Caracter {t.value[0]} nao identificado.")
    # Pula o elemento para que identifique outros possiveis erros na mesma analise
    t.lexer.skip(1)

# Compila as regras definidas para o lexer
lexer = lex.lex()

# Função para realizar a análise léxica e salvar em arquivo
def analyze_and_save(file_name, output_file):
    try:
        with open(file_name, 'r') as file:
            data = file.read()

        lexer.input(data)

        with open(output_file, 'w') as output:
            while True:
                tok = lexer.token()
                if not tok:
                    break
                token_obj = Token(tok.type, tok.value, tok.lineno)
                lista_analisados.append(token_obj)
                output.write(str(token_obj) + '\n')
        
        print(f"Análise léxica concluída. Resultados salvos em {output_file}.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found!")
    except Exception as e:
        print(f"Erro durante a análise léxica: {e}")

# Execute a análise
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python lexic.py <arquivo_entrada> <arquivo_saida>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        analyze_and_save(input_file, output_file)
