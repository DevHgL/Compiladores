import ply.yacc as yacc
from analisador_lexico import tokens  # Certifique-se de que os tokens estão definidos corretamente

# Precedência e associatividade
precedence = (
    ('left', 'PONTOVIRGULA'),
    ('right', 'ELSE'),
    ('left', 'AND', 'OR'),
    ('left', 'MENOR', 'MAIOR', 'IGUAL', 'DIFERENTE', 'MAIOR_IGUAL', 'MENOR_IGUAL'),
    ('left', 'MAIS', 'MENOS'),
    ('left', 'VEZES', 'DIVIDE'),
)


# Regras da gramática

def p_programa(p):
    "PROGRAMA : DECLARACOES BLOCO"
    p[0] = ('programa', p[1], p[2])
    
def p_declaracoes(p):
    "DECLARACOES : DEF_CONST DEF_TIPOS DEF_VAR DEF_ROTINA"
    p[0] = ('declaracoes', p[1], p[2], p[3], p[4])

# Definições de constantes
def p_def_const(p):
    """DEF_CONST : CONSTANTE DEF_CONST
                 | """
    if len(p) == 1:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]

def p_constante(p):
    "CONSTANTE : CONST ID '=' CONST_VALOR ';'"
    p[0] = ('constante', p[2], p[4])

def p_const_valor(p):
    """CONST_VALOR : EXP_CONST"""
    p[0] = p[1]

def p_parametro(p):
    """PARAMETRO : ID
                 | PALAVRA"""
    p[0] = p[1]

def p_exp_const(p):
    """EXP_CONST : PARAMETRO EXP_CONST_L
                 | '(' PARAMETRO OP_MAT EXP_CONST ')'"""
    if len(p) == 3:
        p[0] = ('exp_const', p[1], p[2])
    else:
        p[0] = ('exp_const_par', p[2], p[3], p[4])

def p_exp_const_l(p):
    """EXP_CONST_L : OP_MAT EXP_CONST
                   | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = (p[1], p[2])

# Definições de tipos
def p_def_tipos(p):
    """DEF_TIPOS : TIPO DEF_TIPOS
                 | """
    if len(p) == 1:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]

def p_tipo(p):
    "TIPO : TYPE ID '=' TIPO_DADO ';'"
    p[0] = ('tipo', p[2], p[4])

def p_tipo_dado(p):
    """TIPO_DADO : INTEGER
                 | REAL
                 | CHAR
                 | BOOLEAN
                 | ARRAY '[' NUMERO ']' OF TIPO_DADO
                 | RECORD CAMPOS END
                 | ID"""
    if len(p) == 2:
        p[0] = ('tipo_simples', p[1])
    elif p[1] == 'array':
        p[0] = ('array', p[3], p[6])
    elif p[1] == 'record':
        p[0] = ('record', p[2])
    else:
        p[0] = ('tipo_ref', p[1])

# Definições de variáveis
def p_def_var(p):
    """DEF_VAR : VARIAVEL DEF_VAR
               | """
    if len(p) == 1:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]

def p_variavel(p):
    "VARIAVEL : VAR CAMPOS ';'"
    p[0] = ('variavel', p[2])

def p_campos(p):
    "CAMPOS : CAMPO LISTA_CAMPOS"
    p[0] = [p[1]] + p[2]

def p_campo(p):
    "CAMPO : ID LISTA_ID ':' TIPO_DADO"
    p[0] = ('campo', [p[1]] + p[2], p[4])

def p_lista_id(p):
    """LISTA_ID : ',' ID LISTA_ID
                | """
    if len(p) == 1:
        p[0] = []
    else:
        p[0] = [p[2]] + p[3]

def p_lista_com(p):
    """LISTA_COM : COMANDO PONTOVIRGULA LISTA_COM
                 | COMANDO"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_lista_campos(p):
    """LISTA_CAMPOS : CAMPO PONTOVIRGULA LISTA_CAMPOS 
                   | CAMPO"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
# Definições de rotinas
def p_def_rotina(p):
    """DEF_ROTINA : ROTINA DEF_ROTINA
                  | """
    if len(p) == 1:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]

def p_rotina(p):
    """ROTINA : FUNCTION ID PARAM_ROTINA ':' TIPO_DADO BLOCO_ROTINA
              | PROCEDURE ID PARAM_ROTINA BLOCO_ROTINA"""
    if p[1] == 'function':
        p[0] = ('function', p[2], p[3], p[5], p[6])
    else:
        p[0] = ('procedure', p[2], p[3], p[4])

def p_param_rotina(p):
    """PARAM_ROTINA : '(' CAMPOS ')'
                    | """
    p[0] = p[2] if len(p) > 1 else []

def p_bloco_rotina(p):
    "BLOCO_ROTINA : DEF_VAR BLOCO"
    p[0] = ('bloco_rotina', p[1], p[2])

# Blocos e comandos
def p_bloco(p):
    "BLOCO : BEGIN COMANDO LISTA_COM END"
    p[0] = ('bloco', p[2], p[3])

def p_comando(p):
    """COMANDO : ID atribuicao_regra
               | WHILE EXP_COM DO BLOCO
               | IF EXP_COM THEN BLOCO else_regra
               | FOR FOR_PARAMS DO BLOCO
               | WRITE CONST_VALOR
               | READ ID"""
    if p[1] == 'while':
        p[0] = ('while', p[2], p[4])
    elif p[1] == 'if':
        p[0] = ('if', p[2], p[4], p[5])
    elif p[1] == 'for':
        p[0] = ('for', p[2], p[4])
    elif p[1] == 'write':
        p[0] = ('write', p[2])
    elif p[1] == 'read':
        p[0] = ('read', p[2])
    else:
        p[0] = ('atribuicao', p[1], p[2])

def p_atribuicao_regra(p):
    "atribuicao_regra : ATRIBUICAO EXP"
    p[0] = p[2]


def p_else_regra(p):
    """else_regra : ELSE BLOCO
                  | """
    p[0] = p[2] if len(p) > 1 else None


def p_for_params(p):
    "FOR_PARAMS : ID ATRIBUICAO PARAMETRO TO PARAMETRO"
    p[0] = ('for_params', p[1], p[3], p[5])


# Expressões
def p_exp(p):
    """EXP : PARAMETRO OP_MAT EXP
           | PARAMETRO"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('exp', p[1], p[2], p[3])

def p_exp_com(p):
    """EXP_COM : PARAMETRO OP_COMP PARAMETRO
               | PARAMETRO"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('exp_com', p[1], p[2], p[3])

# Operadores e parâmetros
def p_op_mat(p):
    """OP_MAT : '+'
              | '-'
              | '*'
              | '/'"""
    p[0] = p[1]

def p_op_comp(p):
    """OP_COMP : '>'
               | '<'
               | IGUAL
               | DIFERENTE
               | MAIOR_IGUAL
               | MENOR_IGUAL"""
    p[0] = p[1]


# Tratamento de erros
def p_error(p):
    if p:
        print(f"Erro de sintaxe próximo a '{p.value}' na linha {p.lineno}.")
    else:
        print("Erro de sintaxe no final do arquivo.")

# Construção do parser
parser = yacc.yacc()

def parse_file(filename):

    try:
        with open(filename, 'r') as file:
            data = file.read()
        
        # Realiza a análise sintática
        result = parser.parse(data)
        
        # Salva o resultado em um arquivo
        save_sintatico_result(result)
        
        return result
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado!")
        return None
    except SyntaxError as e:
        print(f"Erro de sintaxe: {e}")
        return None
    except Exception as e:
        print(f"Erro ao analisar o arquivo: {e}")
        return None

def save_sintatico_result(result):

    try:
        with open("saida_sintatico.txt", "w") as output_file:
            def write_node(node, level=0):

                if isinstance(node, tuple):
                    output_file.write("  " * level + f"{node[0]}:\n")
                    for child in node[1:]:
                        write_node(child, level + 1)
                elif isinstance(node, list):
                    for item in node:
                        write_node(item, level)
                else:
                    output_file.write("  " * level + f"{node}\n")
            
            if result:
                write_node(result)
            else:
                output_file.write("Nenhuma análise sintática foi realizada.\n")
        
        print("Análise sintática concluída com sucesso! Resultados salvos em 'saida_sintatico.txt'.")
    except IOError as e:
        print(f"Erro ao salvar o arquivo de saída: {e}")

