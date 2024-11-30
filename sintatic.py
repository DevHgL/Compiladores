###########################################################################################
#                                                                                         #      
#   Trabalho do Analisador Sintático                                                      #              
#                                                                                         #              
#   Author: Hugo Leonardo Melo                                                            #                 
#                                                                                         #              
###########################################################################################


import ply.yacc as yacc
import sys
from analisador_lexico import tokens, lexer

# Regras da gramática
def p_programa(p):
    "PROGRAMA : DECLARACOES BLOCO"
    p[0] = ('programa', p[1], p[2])

def p_bloco(p):
    "BLOCO : BEGIN COMANDO LISTA_COM END"
    p[0] = ('bloco', p[2], p[3])

def p_declaracoes(p):
    "DECLARACOES : DEF_CONST DEF_TIPOS DEF_VAR DEF_ROTINA"
    p[0] = ('declaracoes', p[1], p[2], p[3], p[4])

def p_def_const(p):
    """DEF_CONST : CONSTANTE DEF_CONST
                 | """
    if len(p) > 1:
        p[0] = ('def_const', p[1], p[2])
    else:
        p[0] = ('def_const', None)


def p_def_tipos(p):
    """DEF_TIPOS : TIPO DEF_TIPOS
                 | """
    if len(p) > 1:
        p[0] = ('def_tipos', p[1], p[2])
    else:
        p[0] = ('def_tipos', None)


def p_def_var(p):
    """DEF_VAR : VARIAVEL DEF_VAR
               | """
    if len(p) > 1:
        p[0] = ('def_var', p[1], p[2])
    else:  # Empty rule
        p[0] = ('def_var', None)


def p_def_rotina(p):
    """DEF_ROTINA : ROTINA DEF_ROTINA
                  | """
    if len(p) > 1:
        p[0] = ('def_rotina', p[1], p[2])
    else:  # Empty rule
        p[0] = ('def_rotina', None)


def p_constante(p):
    "CONSTANTE : CONST ID '=' CONST_VALOR ';'"
    p[0] = ('constante', p[2], p[4])

def p_const_valor(p):
    """CONST_VALOR : PALAVRA
                   | EXP_CONST"""
    p[0] = ('const_valor', p[1])

def p_tipo(p):
    "TIPO : TYPE ID '=' TIPO_DADO ';'"
    p[0] = ('tipo', p[2], p[4])

def p_variavel(p):
    "VARIAVEL : VAR CAMPO ';'"
    p[0] = ('variavel', p[2])

def p_lista_id(p):
    """LISTA_ID : ',' ID LISTA_ID
                | """
    if len(p) > 1:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []

def p_campos(p):
    "CAMPOS : CAMPO LISTA_CAMPOS"
    p[0] = ('campos', [p[1]] + p[2])


def p_campo(p):
    "CAMPO : ID LISTA_ID ':' TIPO_DADO"
    p[0] = ('campo', [p[1]] + p[2], p[4])

def p_lista_campos(p):
    """LISTA_CAMPOS : ';' CAMPO LISTA_CAMPOS
                    | """
    if len(p) > 1:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []


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
    if len(p) > 1:
        p[0] = ('parametros', p[2])
    else:
        p[0] = []

def p_bloco_rotina(p):
    "BLOCO_ROTINA : DEF_VAR BLOCO"
    p[0] = ('bloco_rotina', p[1], p[2])

def p_lista_com(p):
    """LISTA_COM : ';' COMANDO LISTA_COM
                 | """
    if len(p) > 1:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []

def p_bloco_com(p):
    """BLOCO_COM : BLOCO
               | COMANDO"""

def p_comando(p):
    """COMANDO : ID NOME ATRIBUICAO
               | WHILE EXP_COM DO BLOCO_COM
               | IF EXP_COM THEN BLOCO_COM ALTERNATIVA_ELSE
               | FOR FOR_COMANDO DO BLOCO_COM
               | WRITE CONST_VALOR
               | READ ID NOME"""
    print(p[1])
    if len(p) == 4 and p[2] == 'ATRIBUICAO_SIMBOLO':
        p[0] = ('ATRIBUICAO', p[1], p[3])
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

def p_for_comando(p):
    "FOR_COMANDO : ID ATRIBUICAO PARAMETRO TO PARAMETRO"
    p[0] = ('FOR_COMANDO', p[1], p[3], p[5])

def p_alternativa_else(p):
    """ALTERNATIVA_ELSE : ELSE BLOCO_COM
                        | """
    if len(p) > 1:
        p[0] = ('else', p[2])
    else:
        p[0] = None

def p_atribuicao(p):
    "ATRIBUICAO : ATRIBUICAO_SIMBOLO EXP"
    p[0] = ('ATRIBUICAO', p[2])

def p_lista_param(p):
    """LISTA_PARAM : PARAMETRO ',' LISTA_PARAM
                   | PARAMETRO
                   | """
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = []

def p_exp(p):
    """EXP : PARAMETRO EXP_L1
           | '(' PARAMETRO EXP_L2"""
    if len(p) == 3:  # PARAMETRO EXP_L1
        p[0] = ('exp', p[1], p[2])
    elif len(p) == 4:  # '(' PARAMETRO EXP_L2
        p[0] = ('exp_group', p[2], p[3])
    pass


def p_exp_l1(p):
    """EXP_L1 : OP_MAT EXP
              | PARAM_LOGICO EXP_LOGICA
              | """
    if len(p) == 1:
        p[0] = None
    elif len(p) == 3:
        if p[1] in ['+', '-', '*', '/']:
            p[0] = ('op_mat', p[1], p[2])
        else:
            p[0] = ('param_logico', p[1], p[2])
    pass

def p_exp_logica(p):
    """EXP_LOGICA : OP_LOGICO EXP
                  | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = ('op_logico', p[1], p[2])
    pass

def p_param_logico(p):
    """PARAM_LOGICO : OP_COMP PARAMETRO
                    | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = ('op_comp', p[1], p[2])
    pass

def p_exp_l2(p):
    """EXP_L2 : OP_MAT EXP ')'
              | PARAM_LOGICO OP_LOGICO EXP ')'"""
    if len(p) == 4:
        p[0] = ('exp_mat_group', p[1], p[2], p[3])
    elif len(p) == 5:
        p[0] = ('exp_logic_group', p[1], p[2], p[3])
    pass

def p_exp_const(p):
    """EXP_CONST : PARAMETRO EXP_CONST_L
                 | '(' PARAMETRO OP_MAT EXP_CONST ')'"""
    if len(p) == 3:
        p[0] = ('exp_const', p[1], p[2])
    elif len(p) == 6:
        p[0] = ('exp_const_group', p[2], p[3], p[4])

def p_exp_const_l(p):
    """EXP_CONST_L : OP_MAT EXP_CONST
                   | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = ('exp_const_l', p[1], p[2])

def p_exp_com(p):
    """EXP_COM : PARAMETRO PARAM_LOGICO EXP_COM_L
               | '(' PARAMETRO PARAM_LOGICO OP_LOGICO EXP_COM ')'"""
    if len(p) == 4:
        p[0] = ('exp_com', p[1], p[2], p[3])
    elif len(p) == 7:
        p[0] = ('exp_com_group', p[2], p[3], p[4], p[5])

def p_exp_com_l(p):
    """EXP_COM_L : OP_LOGICO EXP_COM
                 | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = ('exp_com_l', p[1], p[2])

def p_parametro(p):
    """PARAMETRO : ID NOME
                 | NUMERO
                 | FALSE
                 | TRUE"""
    if len(p) == 3:
        p[0] = ('parametro', 'id', p[1], p[2])
    else:
        p[0] = ('parametro', 'literal', p[1])


def p_op_logico(p):
    """OP_LOGICO : AND
                 | OR"""
    p[0] = p[1]

def p_op_comp(p):
    """OP_COMP : '>'
               | '<'
               | COMPARACAO"""
    p[0] = p[1]

def p_op_mat(p):
    """OP_MAT : '+'
              | '-'
              | '*'
              | '/'"""
    p[0] = p[1]

def p_nome(p):
    """NOME : '.' ID NOME
            | '[' PARAMETRO ']'
            | '(' LISTA_PARAM ')'
            | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = ('nome', p[1], p[2])

# Tratamento de erros
def p_error(p):
    if p:
        print(f"Erro de sintaxe próximo a '{p.value}' na linha {p.lineno}. Token inesperado: {p.type}")
        # Recovery: Skip to the next token
    else:
        print("Erro de sintaxe no final do arquivo.")


# Construção do parser
parser = yacc.yacc()

try:
    with open(sys.argv[1], 'r') as file:
        data = file.read()
    lexer.lineno = 1
    result = parser.parse(data)
    for i in result:
        print(i)
except FileNotFoundError:
    print(f"Erro: Arquivo '{sys.argv[1]}' não encontrado!")
except Exception as e:
    print(f"Erro ao analisar o arquivo: {e}")

