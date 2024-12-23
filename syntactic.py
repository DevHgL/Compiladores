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
        """CONST_DEF : CONSTANT ID '=' EXP ';' CONST_DEF
                       | """
        if len(p) > 1:
            p[0] = ('const_def', p[2], p[4], p[6])
        else:
            p[0] = ('empty_const_def',)

    def p_type_def(self, p):
        """TYPE_DEF : TYPE ID '=' TYPE_DECL ';' TYPE_DEF
                      | """
        if len(p) > 1:
            p[0] = ('type_def', p[2], p[4], p[6])
        else:
            p[0] = ('empty_type_def',)

    def p_type_decl(self, p):
        """TYPE_DECL : ARRAY '[' NUMBER ']' OF TYPE_DECL
                     | RECORD FIELD_LIST END
                     | ID"""
        if p[1].lower() == 'array':
            p[0] = ('array', p[3], p[6])
        elif p[1].lower() == 'record':
            p[0] = ('record', p[3])
        else:
            p[0] = p[1]

    def p_field_list(self, p):
        """FIELD_LIST : FIELD_LIST FIELD
                      | FIELD"""
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    def p_field(self, p):
        "FIELD : ID ':' TYPE_DECL ';'"
        p[0] = (p[1], p[3])

    def p_var_def(self, p):
        """VAR_DEF : VARIABLE ID_LIST ':' TYPE_DECL ';' VAR_DEF
                     | """
        if len(p) > 1:
            p[0] = ('var_def', p[2], p[4], p[6])
        else:
            p[0] = ('empty_var_def',)

    def p_id_list(self, p):
        """ID_LIST : ID
                   | ID_LIST ',' ID"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_command_list(self, p):
        """COMMAND_LIST : COMMAND
                          | COMMAND_LIST COMMAND"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_command(self, p):
        """COMMAND : assignment
                     | if_statement
                     | while_statement
                     | print_statement
                     | FUNCTION_CALL
                     | BLOCK"""
        p[0] = p[1]

    def p_assignment(self, p):
        "assignment : ID ASSIGNMENT EXP"
        p[0] = ('assignment', p[1], p[3])

    def p_if_statement(self, p):
        """if_statement : IF COM_EXP THEN BLOCK ELSE BLOCK
                        | IF COM_EXP THEN BLOCK"""
        if len(p) == 7:
            p[0] = ('if_else', p[2], p[4], p[6])
        else:
            p[0] = ('if', p[2], p[4])

    def p_while_statement(self, p):
        "while_statement : WHILE COM_EXP DO BLOCK"
        p[0] = ('while', p[2], p[4])

    def p_print_statement(self, p):
        "print_statement : PRINT EXP"
        p[0] = ('print', p[2])

    def p_exp(self, p):
        """EXP : EXP '+' EXP
                 | EXP '-' EXP
                 | EXP '*' EXP
                 | EXP '/' EXP
                 | '(' EXP ')'
                 | ID
                 | NUMBER
                 | TRUE
                 | FALSE
                 | FUNCTION_CALL"""
        if len(p) == 4 and p[1] == '(':
            p[0] = p[2]  # Expressão entre parênteses
        elif len(p) == 4:
            p[0] = ('bin_op', p[2], p[1], p[3])  # Operação binária
        else:
            p[0] = p[1]

    def p_exp_uminus(self, p):
        "EXP : '-' EXP %prec UMINUS"
        p[0] = ('uminus', p[2])

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

    def p_param_list(self, p):
        """PARAM_LIST : EXP
                        | PARAM_LIST ',' EXP"""
        if len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 4:
            p[0] = p[1] + [p[3]]

    def p_function_call(self, p):
        """FUNCTION_CALL : ID '(' PARAM_LIST ')'"""
        p[0] = ('function_call', p[1], p[3])

    def p_error(self, p):
        if p:
            print(f"Syntax error near '{p.value}' on line {p.lineno}. Unexpected token: {p.type}")
            print(f"Context: {p.lexer.lexdata[max(0, p.lexpos-20):p.lexpos+20]}")
        else:
            print("Syntax error at EOF")

    def parse(self, data):
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
    from lexic import lexer  # Certifique-se de que o lexer está corretamente importado
    syntactic_analyzer = SyntacticAnalyzer()
    
    # Lendo o conteúdo do arquivo exemplo1.sp
    with open("exemplo1.sp", "r") as file:
        data = file.read()
    
    syntax_tree = syntactic_analyzer.parse(data)
    save_syntax_tree_to_file(syntax_tree)