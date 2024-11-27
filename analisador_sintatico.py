import ply.yacc as yacc
import sys
from analisador_lexico import tokens  # Importe os tokens definidos no lexer

# Regras da gramática

def p_programa(p):
    "PROGRAMA : DECLARACOES BLOCO"
    p[0] = ('programa', p[1], p[2])

def p_bloco(p):
    "BLOCO : BEGIN COMANDO LISTA_COM END"
    p[0] = ('bloco', p[2], p[3])

def p_lista_com_vazia(p):
    "LISTA_COM : "
    p[0] = []

def p_lista_com(p):
    "LISTA_COM : ';' COMANDO LISTA_COM"
    p[0] = [p[2]] + p[3]

def p_declaracoes(p):
    "DECLARACOES : DEF_CONST DEF_TIPOS DEF_VAR DEF_ROTINA"
    p[0] = ('declaracoes', p[1], p[2], p[3], p[4])

def p_def_const_vazio(p):
    "DEF_CONST : "
    p[0] = []

def p_def_const(p):
    "DEF_CONST : CONSTANTE DEF_CONST"
    p[0] = [p[1]] + p[2]

# Exemplo para constantes
def p_constante(p):
    "CONSTANTE : CONST ID '=' CONST_VALOR ';'"
    p[0] = ('constante', p[2], p[4])

def p_const_valor(p):
    """CONST_VALOR : PALAVRA
                   | EXP_MAT"""
    p[0] = ('const_valor', p[1])

# Regras adicionais

# Definição de tipos
def p_def_tipos_vazio(p):
    "DEF_TIPOS : "
    p[0] = []

def p_def_tipos(p):
    "DEF_TIPOS : TIPO DEF_TIPOS"
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
        p[0] = ('tipo_dado', p[1])
    elif p[1] == 'array':
        p[0] = ('array', p[3], p[6])
    elif p[1] == 'record':
        p[0] = ('record', p[2])
    else:
        p[0] = ('tipo_simples', p[1])

# Declaração de variáveis
def p_def_var_vazio(p):
    "DEF_VAR : "
    p[0] = []

def p_def_var(p):
    "DEF_VAR : VARIAVEL DEF_VAR"
    p[0] = [p[1]] + p[2]

def p_variavel(p):
    "VARIAVEL : VAR CAMPOS ';'"
    p[0] = ('variavel', p[2])

def p_campos(p):
    "CAMPOS : CAMPO LISTA_CAMPOS"
    p[0] = [p[1]] + p[2]

def p_lista_campos_vazio(p):
    "LISTA_CAMPOS : "
    p[0] = []

def p_lista_campos(p):
    "LISTA_CAMPOS : ';' CAMPO LISTA_CAMPOS"
    p[0] = [p[2]] + p[3]

def p_campo(p):
    "CAMPO : ID LISTA_ID ':' TIPO_DADO"
    p[0] = ('campo', [p[1]] + p[2], p[4])

def p_lista_id_vazio(p):
    "LISTA_ID : "
    p[0] = []

def p_lista_id(p):
    "LISTA_ID : ',' ID LISTA_ID"
    p[0] = [p[2]] + p[3]

# Rotinas (funções e procedimentos)
def p_def_rotina_vazio(p):
    "DEF_ROTINA : "
    p[0] = []

def p_def_rotina(p):
    "DEF_ROTINA : ROTINA DEF_ROTINA"
    p[0] = [p[1]] + p[2]

def p_rotina(p):
    """ROTINA : FUNCTION ID PARAM_ROTINA ':' TIPO_DADO BLOCO_ROTINA
              | PROCEDURE ID PARAM_ROTINA BLOCO_ROTINA"""
    if p[1] == 'function':
        p[0] = ('function', p[2], p[3], p[5], p[6])
    else:
        p[0] = ('procedure', p[2], p[3], p[4])

def p_param_rotina_vazio(p):
    "PARAM_ROTINA : "
    p[0] = []

def p_param_rotina(p):
    "PARAM_ROTINA : '(' CAMPOS ')'"
    p[0] = ('parametros', p[2])

def p_bloco_rotina(p):
    "BLOCO_ROTINA : DEF_VAR BLOCO"
    p[0] = ('bloco_rotina', p[1], p[2])

# Comandos
def p_comando(p):
    """COMANDO : ID NOME atribuicao
               | WHILE EXP_LOGICA DO bloco_com
               | IF EXP_LOGICA THEN bloco_com alternativa_else
               | FOR FOR_PARAMS DO bloco_com
               | WRITE CONST_VALOR
               | READ ID NOME"""
    if len(p) == 4 and p[2] == 'atribuicao':
        p[0] = ('atribuicao', p[1], p[3])
    elif p[1] == 'while':
        p[0] = ('while', p[2], p[4])
    elif p[1] == 'if':
        p[0] = ('if', p[2], p[4], p[5])
    elif p[1] == 'for':
        p[0] = ('for', p[2], p[4])
    elif p[1] == 'write':
        p[0] = ('write', p[2])
    elif p[1] == 'read':
        p[0] = ('read', p[2])

def p_bloco_com(p):
    """bloco_com : BLOCO
               | COMANDO"""

# Ajuste para atribuição
def p_atribuicao(p):
    "atribuicao : ATRIBUICAO EXP"
    p[0] = ('atribuicao', p[2])

# Ajuste para alternativa do ELSE
def p_alternativa_else(p):
    """alternativa_else : ELSE bloco_com
                        | """
    if len(p) > 1:
        p[0] = ('else', p[2])
    else:
        p[0] = None

def p_for_params(p):
    "FOR_PARAMS : ID ATRIBUICAO PARAMETRO_GRAMATICA TO PARAMETRO_GRAMATICA"
    p[0] = ('for_params', p[1], p[3], p[5])

# Expressões
def p_exp(p):
    """EXP : EXP_MAT
           | EXP_LOGICA"""
    p[0] = p[1]

def p_exp_logica(p):
    """EXP_LOGICA : LOGICAL_PARAM LOGICAL_OP EXP_LOGICA
                  | '(' LOGICAL_PARAM LOGICAL_OP EXP_LOGICA ')'
                  | LOGICAL_PARAM"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('logica', p[1], p[2], p[3])

def p_logical_param(p):
    """LOGICAL_PARAM : PARAMETRO_GRAMATICA OP_COMP PARAMETRO_GRAMATICA
                    | PARAMETRO_GRAMATICA"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('comparacao', p[1], p[2], p[3])

def p_exp_mat(p):
    """EXP_MAT : PARAMETRO_GRAMATICA MATHEMATICAL_OP EXP_MAT
               | '(' PARAMETRO_GRAMATICA MATHEMATICAL_OP EXP_MAT ')'
               | PARAMETRO_GRAMATICA"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('matematica', p[1], p[2], p[3])

# Operadores e parâmetros
def p_logical_op(p):
    """LOGICAL_OP : AND
                 | OR"""
    p[0] = p[1]

def p_op_comp(p):
    """OP_COMP : '>'
               | '<'
               | COMPARACAO"""
    p[0] = p[1]

def p_mathematical_op(p):
    """MATHEMATICAL_OP : '+'
                      | '-'
                      | '*'
                      | '/'"""
    p[0] = p[1]

def p_param(p):
    """PARAM : ID
             | NOME
             | NUMERO
             | FALSE
             | TRUE"""
    p[0] = p[1]

def p_parametro_gramatica(p):
    """PARAMETRO_GRAMATICA : NUMERO"""
    p[0] = p[1]

# Erros
def p_error(p):
    print("Erro de sintaxe:", p)

# Construção do parser
parser = yacc.yacc()

try:
    with open(sys.argv[1], 'r') as file:
        data = file.read()
    result = parser.parse(data)
except FileNotFoundError:
    print(f"Erro: Arquivo '{sys.argv[1]}' não encontrado!")
except Exception as e:
    print(f"Erro ao analisar o arquivo: {e}")
