import ply.yacc as yacc
import sys
from analisador_lexico import tokens  # Importe os tokens definidos no lexer

# Precedência e associatividade para resolver conflitos
precedence = (
    ('right', 'ELSE'),  # Garante que o ELSE associa ao IF mais próximo
)

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
    "LISTA_COM : COMANDO LISTA_COM_RESTO"
    p[0] = [p[1]] + p[2]

def p_lista_com_resto(p):
    """LISTA_COM_RESTO : ';' COMANDO LISTA_COM_RESTO
                       | ';'"""
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[2]] + p[3]

def p_lista_campos(p):
    """LISTA_CAMPOS : ';' CAMPO LISTA_CAMPOS
                    | ';'"""
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[2]] + p[3]

# Blocos ajustados
def p_bloco(p):
    "BLOCO : BEGIN COMANDO LISTA_COM END"
    p[0] = ('bloco', p[2], p[3])

# Adicionar precedência
precedence = (
    ('left', ';'),
)


def p_declaracoes(p):
    "DECLARACOES : DEF_CONST DEF_TIPOS DEF_VAR DEF_ROTINA"
    p[0] = ('declaracoes', p[1], p[2], p[3], p[4])

def p_def_const_vazio(p):
    "DEF_CONST : "
    p[0] = []

def p_def_const(p):
    "DEF_CONST : CONSTANTE DEF_CONST"
    p[0] = [p[1]] + p[2]

def p_constante(p):
    "CONSTANTE : CONST ID '=' CONST_VALOR ';'"
    p[0] = ('constante', p[2], p[4])

def p_const_valor(p):
    """CONST_VALOR : PALAVRA
                   | EXP_MAT"""
    p[0] = ('const_valor', p[1])

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

def p_comando(p):
    """COMANDO : ID ATRIBUICAO EXP
               | WHILE EXP_LOGICA DO BLOCO
               | IF EXP_LOGICA THEN BLOCO alternativa_else
               | FOR FOR_PARAMS DO BLOCO
               | WRITE CONST_VALOR
               | READ ID"""
    if len(p) == 4 and p[2] == 'ATRIBUICAO':
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

def p_alternativa_else(p):
    """alternativa_else : ELSE BLOCO
                        | """
    if len(p) > 1:
        p[0] = ('else', p[2])
    else:
        p[0] = None

def p_for_params(p):
    "FOR_PARAMS : ID ATRIBUICAO PARAMETRO TO PARAMETRO"
    p[0] = ('for_params', p[1], p[3], p[5])

def p_exp(p):
    """EXP : EXP_MAT
           | EXP_LOGICA"""
    p[0] = p[1]

def p_exp_logica(p):
    """EXP_LOGICA : PARAM_LOGICO OP_LOGICO EXP_LOGICA
                  | PARAM_LOGICO"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('logica', p[1], p[2], p[3])

def p_param_logico(p):
    """PARAM_LOGICO : PARAMETRO OP_COMP PARAMETRO"""
    p[0] = ('comparacao', p[1], p[2], p[3])

def p_exp_mat(p):
    """EXP_MAT : PARAMETRO OP_MAT EXP_MAT
               | PARAMETRO"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('matematica', p[1], p[2], p[3])

def p_op_logico(p):
    """OP_LOGICO : AND
                 | OR"""
    p[0] = p[1]

def p_op_comp(p):
    """OP_COMP : '>'
               | '<'
               | '='"""
    p[0] = p[1]

def p_op_mat(p):
    """OP_MAT : '+'
              | '-'
              | '*'
              | '/'"""
    p[0] = p[1]

def p_parametro(p):
    """PARAMETRO : ID
                 | NUMERO
                 | FALSE
                 | TRUE"""
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Erro de sintaxe próximo a '{p.value}' na linha {p.lineno}.")
    else:
        print("Erro de sintaxe no final do arquivo.")


# Adicionar precedência
precedence = (
    ('left', ';'),
)

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

