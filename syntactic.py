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
    "BLOCK : BEGIN COMMAND COMMAND_LIST END"
    p[0] = ('block', p[2], p[3])

def p_declarations(p):
    "DECLARATIONS : CONST_DEF TYPE_DEF VAR_DEF ROUTINE_DEF"
    p[0] = ('declarations', p[1], p[2], p[3], p[4])

def p_const_def(p):
    """CONST_DEF : CONSTANT CONST_DEF
                 | """
    if len(p) > 1:
        p[0] = ('const_def', p[1], p[2])
    else:
        p[0] = ('const_def', None)

def p_type_def(p):
    """TYPE_DEF : TYPE_DECLARATION TYPE_DEF
                | """
    if len(p) > 1:
        p[0] = ('type_def', p[1], p[2])
    else:
        p[0] = ('type_def', None)
def p_var_def(p):
    """VAR_DEF : VARIABLE VAR_DEF
               | """
    if len(p) > 1:
        p[0] = ('var_def', p[1], p[2])
    else:
        p[0] = ('var_def', None)

def p_routine_def(p):
    """ROUTINE_DEF : ROUTINE ROUTINE_DEF
                   | """
    if len(p) > 1:
        p[0] = ('routine_def', p[1], p[2])
    else:
        p[0] = ('routine_def', None)

def p_constant(p):
    "CONSTANT : CONST ID '=' CONST_VALUE ';'"
    p[0] = ('constant', p[2], p[4])

def p_const_value(p):
    """CONST_VALUE : STRING
                   | CONST_EXP"""
    p[0] = ('const_value', p[1])

def p_type_declaration(p):
    "TYPE_DECLARATION : TYPE ID '=' DATA_TYPE ';'"
    p[0] = ('type', p[2], p[4])

def p_variable(p):
    "VARIABLE : VAR FIELD ';'"
    p[0] = ('variable', p[2])

def p_id_list(p):
    """ID_LIST : ',' ID ID_LIST
               | """
    if len(p) > 1:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []

def p_fields(p):
    "FIELDS : FIELD FIELD_LIST"
    p[0] = ('fields', [p[1]] + p[2])

def p_field(p):
    "FIELD : ID ID_LIST ':' DATA_TYPE"
    p[0] = ('field', [p[1]] + p[2], p[4])

def p_field_list(p):
    """FIELD_LIST : ';' FIELD FIELD_LIST
                  | """
    if len(p) > 1:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []

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

def p_routine(p):
    """ROUTINE : FUNCTION ID ROUTINE_PARAM ':' DATA_TYPE ROUTINE_BLOCK
               | PROCEDURE ID ROUTINE_PARAM ROUTINE_BLOCK"""
    if p[1] == 'function':
        p[0] = ('function', p[2], p[3], p[5], p[6])
    else:
        p[0] = ('procedure', p[2], p[3], p[4])

def p_routine_param(p):
    """ROUTINE_PARAM : '(' FIELDS ')'
                     | """
    if len(p) > 1:
        p[0] = ('parameters', p[2])
    else:
        p[0] = []

def p_routine_block(p):
    "ROUTINE_BLOCK : VAR_DEF BLOCK"
    p[0] = ('routine_block', p[1], p[2])

def p_command_list(p):
    """COMMAND_LIST : ';' COMMAND COMMAND_LIST
                    | """
    if len(p) > 1:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []

def p_command_block(p):
    """COMMAND_BLOCK : BLOCK
                    | COMMAND"""

def p_command(p):
    """COMMAND : ID NAME ASSIGN_EXPRESSION
               | WHILE COM_EXP DO COMMAND_BLOCK
               | IF COM_EXP THEN COMMAND_BLOCK ELSE_ALTERNATIVE
               | FOR FOR_COMMAND DO COMMAND_BLOCK
               | WRITE CONST_VALUE
               | READ ID NAME"""
    if len(p) == 4 and p[3][0] == 'assign':  # Changed to match new node type
        p[0] = ('command_assign', p[1], p[2], p[3])
    elif p[1] == 'while':
        p[0] = ('while', p[2], p[4])
    elif p[1] == 'if':
        p[0] = ('if', p[2], p[4], p[5])
    elif p[1] == 'for':
        p[0] = ('for', p[2], p[4])
    elif p[1] == 'write':
        p[0] = ('write', p[2])
    elif p[1] == 'read':
        p[0] = ('read', p[2], p[3])

def p_assign_expression(p):
    "ASSIGN_EXPRESSION : ASSIGNMENT EXP"
    p[0] = ('assign', p[2])

def p_for_command(p):
    "FOR_COMMAND : ID ASSIGNMENT_STMT TO PARAMETER"  # Updated reference
    p[0] = ('FOR_COMMAND', p[1], p[3], p[5])

def p_else_alternative(p):
    """ELSE_ALTERNATIVE : ELSE COMMAND_BLOCK
                       | """
    if len(p) > 1:
        p[0] = ('else', p[2])
    else:
        p[0] = None

def p_assignment_statement(p): 
    "ASSIGNMENT_STMT : ASSIGNMENT EXP"    
    p[0] = ('assignment', p[2])          
def p_param_list(p):
    """PARAM_LIST : PARAMETER ',' PARAM_LIST
                  | PARAMETER
                  | """
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = []

def p_exp(p):
    """EXP : PARAMETER EXP_L1
           | '(' PARAMETER EXP_L2"""
    if len(p) == 3:
        p[0] = ('exp', p[1], p[2])
    elif len(p) == 4:
        p[0] = ('exp_group', p[2], p[3])

def p_exp_l1(p):
    """EXP_L1 : MATH_OP EXP
              | LOGIC_PARAM LOGIC_EXP
              | """
    if len(p) == 1:
        p[0] = None
    elif len(p) == 3:
        if p[1] in ['+', '-', '*', '/']:
            p[0] = ('math_op', p[1], p[2])
        else:
            p[0] = ('logic_param', p[1], p[2])

def p_logic_exp(p):
    """LOGIC_EXP : LOGIC_OP EXP
                 | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = ('logic_op', p[1], p[2])

def p_logic_param(p):
    """LOGIC_PARAM : COMP_OP PARAMETER
                   | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = ('comp_op', p[1], p[2])

def p_exp_l2(p):
    """EXP_L2 : MATH_OP EXP ')'
              | LOGIC_PARAM LOGIC_OP EXP ')'"""
    if len(p) == 4:
        p[0] = ('exp_math_group', p[1], p[2], p[3])
    elif len(p) == 5:
        p[0] = ('exp_logic_group', p[1], p[2], p[3])

def p_const_exp(p):
    """CONST_EXP : PARAMETER CONST_EXP_L
                 | '(' PARAMETER MATH_OP CONST_EXP ')'"""
    if len(p) == 3:
        p[0] = ('const_exp', p[1], p[2])
    elif len(p) == 6:
        p[0] = ('const_exp_group', p[2], p[3], p[4])

def p_const_exp_l(p):
    """CONST_EXP_L : MATH_OP CONST_EXP
                   | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = ('const_exp_l', p[1], p[2])

def p_com_exp(p):
    """COM_EXP : PARAMETER LOGIC_PARAM COM_EXP_L
               | '(' PARAMETER LOGIC_PARAM LOGIC_OP COM_EXP ')'"""
    if len(p) == 4:
        p[0] = ('com_exp', p[1], p[2], p[3])
    elif len(p) == 7:
        p[0] = ('com_exp_group', p[2], p[3], p[4], p[5])

def p_com_exp_l(p):
    """COM_EXP_L : LOGIC_OP COM_EXP
                 | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = ('com_exp_l', p[1], p[2])

def p_parameter(p):
    """PARAMETER : ID NAME
                | NUMBER
                | FALSE
                | TRUE"""
    if len(p) == 3:
        p[0] = ('parameter', 'id', p[1], p[2])
    else:
        p[0] = ('parameter', 'literal', p[1])

def p_logic_op(p):
    """LOGIC_OP : AND
                | OR"""
    p[0] = p[1]

def p_comp_op(p):
    """COMP_OP : '>'
               | '<'
               | COMPARATOR"""
    p[0] = p[1]

def p_math_op(p):
    """MATH_OP : '+'
               | '-'
               | '*'
               | '/'"""
    p[0] = p[1]

def p_name(p):
    """NAME : '.' ID NAME
           | '[' PARAMETER ']'
           | '(' PARAM_LIST ')'
           | """
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = ('name', p[1], p[2])

# Error handling
def p_error(p):
    if p:
        print(f"Syntax error near '{p.value}' on line {p.lineno}. Unexpected token: {p.type}")
    else:
        print("Syntax error at end of file.")

# Parser construction
parser = yacc.yacc()

def print_tree(tree, file, indent=0):
    """Função recursiva que imprime a árvore sintática em um arquivo .txt."""
    if tree is None:
        return

    # Criar a indentação de acordo com a profundidade
    indent_str = '  ' * indent

    # Se a árvore for uma tupla, imprimimos o tipo de nó (primeiro elemento) e recursivamente
    if isinstance(tree, tuple):
        file.write(f"{indent_str}{tree[0]}\n")
        for subtree in tree[1:]:
            print_tree(subtree, file, indent + 1)
    # Se a árvore for uma lista, assumimos que seja uma lista de IDs, então imprimimos cada elemento
    elif isinstance(tree, list):
        for item in tree:
            print_tree(item, file, indent)
    # Se for um valor simples, apenas imprimimos o valor
    else:
        file.write(f"{indent_str}{tree}\n")


def save_syntax_tree_to_file(tree, filename="Syntactic-Output.txt"):
    """Função principal que salva a árvore sintática em um arquivo .txt."""
    try:
        with open(filename, 'w') as file:
            print_tree(tree, file)
        print(f"Árvore sintática salva com sucesso em {filename}.")
    except Exception as e:
        print(f"Erro ao salvar a árvore sintática: {e}")


try:
    with open(sys.argv[1], 'r') as file:
        data = file.read()
    lexer.lineno = 1
    result = parser.parse(data)
    save_syntax_tree_to_file(result)
    for i in result:
        print(i)
except FileNotFoundError:
    print(f"Error: File '{sys.argv[1]}' not found!")
except Exception as e:
    print(f"Error while parsing file: {e}")
    
    
