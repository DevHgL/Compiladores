###########################################################################################
#                                                                                         #      
#   Author: Hugo Leonardo Melo                                                            #                 
#                                                                                         #              
#   Trabalho do Analisador Léxico                                                         #              
#                                                                                         #              
###########################################################################################
import ply.lex as lex
import sys

# Classe para armazenar os tokens
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

# Tokens literais
literals = ['+', '-', '*', '/', '=', ',', ';', ':', '.', '[', ']', '(', ')']

# Lista de tokens deve estar definida no escopo global
tokens = [
    'ID',
    'NUMBER',
    'STRING',
    'ASSIGNMENT',
    'COMP_OP',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'EQUAL',
    'NOT_EQUALS'
] + list(reservados.values())


# Regras regulares para tokens simples
t_ASSIGNMENT = r':='
t_COMP_OP = r'==|!=|>=|<=|>|<'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservados.get(t.value.lower(), 'ID')  # Prioridade para palavras reservadas
    return t

def t_STRING(t):
    r'"[A-Za-z0-9\s]*"'
    t.value = str(t.value)
    return t

# Regras especiais
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'  # Ignorar espaços e tabulações

def t_error(t):
    print(f"Caracter {t.value[0]} não identificado na linha {t.lineno}.")
    t.lexer.skip(1)  # Avança para evitar erros contínuos

# Compila o lexer
lexer = lex.lex()

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
        print(f"Erro: Arquivo '{file_name}' não encontrado!")
    except Exception as e:
        print(f"Erro durante a análise léxica: {e}")

# Execução principal
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python lexic.py <arquivo_entrada> <arquivo_saida>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        analyze_and_save(input_file, output_file)
