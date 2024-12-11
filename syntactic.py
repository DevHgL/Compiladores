###########################################################################################
#                                                                                         #
#   Author: Hugo Leonardo Melo                                                            #
#                                                                                         #
#   Trabalho do Analisador Sintático                                                      #
#                                                                                         #
###########################################################################################

import ply.yacc as yacc
import sys
from lexic import tokens, lexer

# Grammar rules
def p_program(p):
    "PROGRAM : DECLARATIONS BLOCK"
    p[0] = ('program', p[1], p[2])

def p_block(p):
    """BLOCK : BEGIN COMMAND_LIST END
             | BEGIN END"""
    if len(p) == 4:
        p[0] = ('block', p[2])
    else:
        p[0] = ('empty_block',)

def p_declarations(p):
    "DECLARATIONS : CONST_DEF TYPE_DEF VAR_DEF"
    p[0] = ('declarations', p[1], p[2], p[3])

def p_const_def(p):
    """CONST_DEF : CONSTANT CONST_DEF
                 | """
    if len(p) > 1:
        p[0] = ('const_def', p[1], p[2])
    else:
        p[0] = ('const_def', None)

def p_constant(p):
    "CONSTANT : CONST ID '=' CONST_VALUE ';'"
    p[0] = ('constant', p[2], p[4])

def p_const_value(p):
    """CONST_VALUE : STRING
                   | CONST_EXP"""
    p[0] = ('const_value', p[1])

def p_const_exp(p):
    """CONST_EXP : NUMBER
                 | '(' CONST_EXP ')'
                 | CONST_EXP '+' CONST_EXP
                 | CONST_EXP '-' CONST_EXP
                 | CONST_EXP '*' CONST_EXP
                 | CONST_EXP '/' CONST_EXP"""
    if len(p) == 2:
        p[0] = p[1]  # Número simples
    elif len(p) == 4 and p[2] in ['+', '-', '*', '/']:
        p[0] = ('bin_op', p[2], p[1], p[3])  # Operação binária
    elif len(p) == 4:  # Parênteses
        p[0] = p[2]

def p_type_def(p):
    """TYPE_DEF : TYPE_DECLARATION TYPE_DEF
                | """
    if len(p) > 1:
        p[0] = ('type_def', p[1], p[2])
    else:
        p[0] = ('type_def', None)

def p_type_declaration(p):
    "TYPE_DECLARATION : TYPE ID '=' DATA_TYPE ';'"
    p[0] = ('type', p[2], p[4])

def p_data_type(p):
    """DATA_TYPE : INTEGER
                 | REAL
                 | CHAR
                 | BOOLEAN
                 | ARRAY '[' NUMBER ']' OF DATA_TYPE
                 | RECORD FIELDS END
                 | ID"""
    if len(p) == 2:
        p[0] = ('data_type', p[1])
    elif p[1] == 'array':
        p[0] = ('array', p[3], p[6])
    elif p[1] == 'record':
        p[0] = ('record', p[2])
    else:
        p[0] = ('simple_type', p[1])

def p_var_def(p):
    """VAR_DEF : VARIABLE VAR_DEF
               | """
    if len(p) > 1:
        p[0] = ('var_def', p[1], p[2])
    else:
        p[0] = ('var_def', None)

def p_variable(p):
    "VARIABLE : VAR ID_LIST ':' DATA_TYPE ';'"
    p[0] = ('variable', p[2], p[4])

def p_id_list(p):
    """ID_LIST : ID
               | ID_LIST ',' ID"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_fields(p):
    "FIELDS : FIELD FIELD_LIST"
    p[0] = ('fields', [p[1]] + p[2])

def p_field(p):
    "FIELD : ID ':' DATA_TYPE"
    p[0] = ('field', p[1], p[3])

def p_field_list(p):
    """FIELD_LIST : ';' FIELD FIELD_LIST
                  | """
    if len(p) > 1:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []

def p_command_list(p):
    """COMMAND_LIST : COMMAND
                    | COMMAND_LIST ';' COMMAND"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_command(p):
    """COMMAND : ID ASSIGNMENT EXP
               | ID ASSIGNMENT FUNCTION_CALL
               | IF '(' COM_EXP ')' THEN COMMAND
               | IF '(' COM_EXP ')' THEN COMMAND ELSE COMMAND
               | WHILE '(' COM_EXP ')' DO COMMAND
               | BEGIN COMMAND_LIST END"""
    if len(p) >= 4 and p[2] == ':=':
        p[0] = ('assign', p[1], p[3])
    elif p[1] == 'if':
        if len(p) == 7:
            p[0] = ('if', p[3], p[6])
        else:
            p[0] = ('if', p[3], p[6], p[8])
    elif p[1] == 'while':
        p[0] = ('while', p[3], p[6])
    elif p[1] == 'begin':
        p[0] = ('block', p[2])

def p_function_call(p):
    "FUNCTION_CALL : ID '(' PARAM_LIST ')'"
    p[0] = ('function_call', p[1], p[3])

def p_param_list(p):
    """PARAM_LIST : EXP
                  | PARAM_LIST ',' EXP
                  | """
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = []

def p_com_exp(p):
    """COM_EXP : EXP COMP_OP EXP
               | COM_EXP LOGIC_OP_OR COM_EXP
               | COM_EXP LOGIC_OP_AND COM_EXP"""
    if len(p) == 4:
        if p[2] in ('AND', 'OR'):
            p[0] = ('logic_op', p[2], p[1], p[3])
        else:
            p[0] = ('comparison', p[2], p[1], p[3])
    else:
        p[0] = p[1]



def p_exp(p):
    """EXP : EXP '+' EXP
           | EXP '-' EXP
           | EXP '*' EXP
           | EXP '/' EXP
           | '(' EXP ')'
           | ID
           | NUMBER
           | TRUE
           | FALSE"""
    if len(p) == 4 and p[1] == '(':
        p[0] = p[2]  # Expressão entre parênteses
    elif len(p) == 4:
        p[0] = ('bin_op', p[2], p[1], p[3])  # Operação binária
    else:
        p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error near '{p.value}' on line {p.lineno}. Unexpected token: {p.type}")
    else:
        print("Syntax error at end of file.")

# Build the parser
parser = yacc.yacc()

def save_syntax_tree_to_file(tree, filename="Syntactic-Output.txt"):
    try:
        with open(filename, 'w') as file:
            file.write(str(tree))
        print(f"Árvore sintática salva com sucesso em {filename}.")
    except Exception as e:
        print(f"Erro ao salvar a árvore sintática: {e}")

# Main logic
try:
    with open(sys.argv[1], 'r') as file:
        data = file.read()
    lexer.lineno = 1
    result = parser.parse(data)
    save_syntax_tree_to_file(result)
    print(result)
except FileNotFoundError:
    print(f"Error: File '{sys.argv[1]}' not found!")
except Exception as e:
    print(f"Error while parsing file: {e}")
