import ply.lex as lex

# Lista de palavras reservadas
reserved = {
    'begin': 'BEGIN',
    'end': 'END',
    'const': 'CONST',
    'type': 'TYPE',
    'var': 'VAR',
    'function': 'FUNCTION',
    'procedure': 'PROCEDURE',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'to': 'TO',
    'read': 'READ',
    'write': 'WRITE',
    'array': 'ARRAY',
    'of': 'OF',
    'record': 'RECORD',
    'true': 'TRUE',
    'false': 'FALSE',
    'integer': 'INTEGER',
    'real': 'REAL',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'and': 'AND',
    'or': 'OR'
}

# Lista de todos os tokens
tokens = [
    'ID',           # Identificadores
    'NUMERO',       # Números (inteiros ou reais)
    'PALAVRA',      # Strings
    'ATRIBUICAO',   # :=
    'COMPARACAO',   # ==, <=, >=, !=
    'MAIS',         # +
    'MENOS',        # -
    'VEZES',        # *
    'DIVIDE',       # /
    'MENOR',        # <
    'MAIOR',        # >
    'PONTO',        # .
    'VIRGULA',      # ,
    'DOISPONTOS',   # :
    'PONTOVIRGULA', # ;
    'ABREPAR',      # (
    'FECHAPAR',     # )
    'ABRECOL',      # [
    'FECHACOL',     # ]
    'IGUAL'         # =
] + list(reserved.values())

# Expressões regulares para tokens simples
t_MAIS = r'\+'
t_MENOS = r'-'
t_VEZES = r'\*'
t_DIVIDE = r'/'
t_IGUAL = r'='
t_MENOR = r'<'
t_MAIOR = r'>'
t_PONTO = r'\.'
t_VIRGULA = r','
t_DOISPONTOS = r':'
t_PONTOVIRGULA = r';'
t_ABREPAR = r'\('
t_FECHAPAR = r'\)'
t_ABRECOL = r'\['
t_FECHACOL = r'\]'

# Expressões regulares com ações
def t_ATRIBUICAO(t):
    r':='
    return t

def t_COMPARACAO(t):
    r'==|<=|>=|!='
    return t

def t_PALAVRA(t):
    r'\"[^\"]*\"'
    return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    # Verifica se é uma palavra reservada
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

# Caracteres ignorados
t_ignore = ' \t'  # Espaços e tabs
t_ignore_COMMENT = r'\{[^}]*\}'  # Comentários entre chaves

# Nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Constrói o lexer
lexer = lex.lex()

# Construir o analisador léxico
lexer = lex.lex()

# Função para analisar um arquivo e salvar a saída em um arquivo de texto
def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        lexer.input(data)
        
        with open("saida_lexico.txt", "w") as output_file:
            for tok in lexer:
                output_file.write(f"{tok.type}({tok.value}) na linha {tok.lineno}\n")
        print("Análise léxica concluída com sucesso! Resultados salvos em 'saida_lexico.txt'.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado!")
    except Exception as e:
        print(f"Erro ao analisar o arquivo: {e}")
