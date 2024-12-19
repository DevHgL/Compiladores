###########################################################################################
#                                                                                         #
#   Author: Hugo Leonardo Melo                                                            #
#                                                                                         #
#   Trabalho do Analisador Léxico e Sintático                                             #
#                                                                                         #
###########################################################################################

import ply.yacc as yacc
import sys
from lexic import tokens, lexer  # Certifique-se de que o arquivo lexic.py define 'tokens'

class SyntacticAnalyzer:
    def __init__(self):
        self.precedence = (
            ('nonassoc', 'ELSE'),  # Resolve ambiguidade entre IF-THEN-ELSE
            ('nonassoc', 'IF'),
            ('left', 'LOGIC_OP_OR'),
            ('left', 'LOGIC_OP_AND'),
            ('left', '+', '-'),
            ('left', '*', '/'),
            ('right', 'UMINUS'),
        )
        self.tokens = tokens  # Usa a lista de tokens importada do módulo léxico
        self.parser = yacc.yacc(module=self)

    # Regras de gramática
    def p_program(self, p):
        "PROGRAM : DECLARATIONS BLOCK"
        p[0] = ('program', p[1], p[2])

    def p_block(self, p):
        """BLOCK : BEGIN COMMAND_LIST END
                   | BEGIN END"""
        if len(p) == 4:
            p[0] = ('block', p[2])
        else:
            p[0] = ('empty_block',)

    def p_declarations(self, p):
        "DECLARATIONS : CONST_DEF TYPE_DEF VAR_DEF"
        p[0] = ('declarations', p[1], p[2], p[3])

    def p_const_def(self, p):
        """CONST_DEF : CONSTANT CONST_DEF
                       | """
        if len(p) > 1:
            p[0] = ('const_def', p[1], p[2])
        else:
            p[0] = ('const_def', None)

    def p_constant(self, p):
        "CONSTANT : CONST ID '=' CONST_VALUE ';'"
        p[0] = ('constant', p[2], p[4])

    def p_const_value(self, p):
        """CONST_VALUE : STRING
                         | CONST_EXP"""
        p[0] = ('const_value', p[1])

    def p_const_exp(self, p):
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

    def p_type_def(self, p):
        """TYPE_DEF : TYPE_DECLARATION TYPE_DEF
                      | """
        if len(p) > 1:
            p[0] = ('type_def', p[1], p[2])
        else:
            p[0] = ('type_def', None)

    def p_type_declaration(self, p):
        "TYPE_DECLARATION : TYPE ID '=' DATA_TYPE ';'"
        p[0] = ('type', p[2], p[4])

    def p_data_type(self, p):
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

    def p_var_def(self, p):
        """VAR_DEF : VARIABLE VAR_DEF
                     | """
        if len(p) > 1:
            p[0] = ('var_def', p[1], p[2])
        else:
            p[0] = ('var_def', None)

    def p_variable(self, p):
        "VARIABLE : VAR ID_LIST ':' DATA_TYPE ';'"
        p[0] = ('variable', p[2], p[4])

    def p_id_list(self, p):
        """ID_LIST : ID
                     | ID_LIST ',' ID"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_fields(self, p):
        "FIELDS : FIELD FIELD_LIST"
        p[0] = ('fields', [p[1]] + p[2])

    def p_field(self, p):
        "FIELD : ID ':' DATA_TYPE"
        p[0] = ('field', p[1], p[3])

    def p_field_list(self, p):
        """FIELD_LIST : ';' FIELD FIELD_LIST
                        | """
        if len(p) > 1:
            p[0] = [p[2]] + p[3]
        else:
            p[0] = []

    def p_command_list(self, p):
        """COMMAND_LIST : COMMAND
                          | COMMAND_LIST ';' COMMAND"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_command(self, p):
        """COMMAND : ASSIGN_STATEMENT
                     | FUNCTION_CALL
                     | CONDITIONAL
                     | LOOP
                     | BLOCK"""
        p[0] = p[1]

    def p_assign_statement(self, p):
        "ASSIGN_STATEMENT : ID ASSIGNMENT EXP"
        p[0] = ('assign', p[1], p[3])

    def p_function_call(self, p):
        "FUNCTION_CALL : ID '(' PARAM_LIST ')'"
        p[0] = ('function_call', p[1], p[3])

    def p_conditional(self, p):
        """CONDITIONAL : IF '(' COM_EXP ')' THEN COMMAND
                         | IF '(' COM_EXP ')' THEN COMMAND ELSE COMMAND"""
        if len(p) == 7:
            p[0] = ('if', p[3], p[6])
        else:
            p[0] = ('if', p[3], p[6], p[8])

    def p_loop(self, p):
        "LOOP : WHILE '(' COM_EXP ')' DO COMMAND"
        p[0] = ('while', p[3], p[6])

    def p_param_list(self, p):
        """PARAM_LIST : EXP
                        | PARAM_LIST ',' EXP
                        | """
        if len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 4:
            p[0] = p[1] + [p[3]]
        else:
            p[0] = []

    def p_com_exp(self, p):
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

    def p_exp(self, p):
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

    def p_exp_uminus(self, p):
        "EXP : '-' EXP %prec UMINUS"
        p[0] = ('uminus', p[2])

    def p_error(self, p):
        if p:
            print(f"Syntax error near '{p.value}' on line {p.lineno}. Unexpected token: {p.type}")
        else:
            print("Syntax error at end of file.")

    def parse(self, data):
        lexer.lineno = 1
        return self.parser.parse(data, lexer=lexer)

# Função para salvar a árvore sintática
def save_syntax_tree_to_file(tree, filename="Syntactic-Output.txt"):
    if tree is None:
        print("Erro: Árvore sintática é None. Não foi possível salvar.")
        return
    try:
        with open(filename, 'w') as file:
            file.write(str(tree))
        print(f"Árvore sintática salva com sucesso em {filename}.")
    except Exception as e:
        print(f"Erro ao salvar a árvore sintática: {e}")


# Execução principal
if __name__ == "__main__":
    try:
        with open(sys.argv[1], 'r') as file:
            data = file.read()

        analyzer = SyntacticAnalyzer()
        result = analyzer.parse(data)
        save_syntax_tree_to_file(result)
        print(result)

    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found!")
    except Exception as e:
        print(f"Error while parsing file: {e}")
