import ply.yacc as yacc
from lexic import tokens

class SyntacticAnalyzer:
    def __init__(self):
        self.tokens = tokens
        self.precedence = (
            ('right', 'UMINUS'),  # Precedência para operadores unários
            ('left', '+', '-'),
            ('left', '*', '/'),
        )
        self.parser = yacc.yacc(module=self)

    def p_program(self, p):
        """PROGRAM : DECLARATIONS BLOCK"""
        p[0] = ('program', p[1], p[2])

    def p_declarations(self, p):
        """DECLARATIONS : CONST_DECLARATIONS VAR_DECLARATIONS
                        | VAR_DECLARATIONS
                        | CONST_DECLARATIONS
                        | empty"""
        if len(p) == 3:
            p[0] = p[1] + p[2]
        elif len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = []

    def p_const_declarations(self, p):
        """CONST_DECLARATIONS : CONST_DEF ID '=' NUMBER ';' CONST_DECLARATIONS
                              | CONST_DEF ID '=' NUMBER ';'"""
        if len(p) == 7:
            p[0] = [(p[2], p[4])] + p[6]
        else:
            p[0] = [(p[2], p[4])]

    def p_var_declarations(self, p):
        """VAR_DECLARATIONS : VAR_DEF ID ':' ID ';' VAR_DECLARATIONS
                            | VAR_DEF ID ':' ID ';'"""
        if len(p) == 7:
            p[0] = [(p[2], p[4])] + p[6]
        else:
            p[0] = [(p[2], p[4])]

    def p_block(self, p):
        """BLOCK : BEGIN COMMAND_LIST END"""
        p[0] = ('block', p[2])

    def p_command_list(self, p):
        """COMMAND_LIST : COMMAND ';' COMMAND_LIST
                        | COMMAND
                        | empty"""
        if len(p) == 4:
            p[0] = [p[1]] + p[3]
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = []

    def p_command(self, p):
        """COMMAND : assignment"""
        p[0] = p[1]

    def p_assignment(self, p):
        """assignment : ID ASSIGNMENT EXP"""
        p[0] = ('assignment', p[1], p[3])

    def p_exp(self, p):
        """EXP : EXP '+' EXP
                | EXP '-' EXP
                | EXP '*' EXP
                | EXP '/' EXP
                | '-' EXP %prec UMINUS
                | '(' EXP ')'
                | ID
                | NUMBER"""
        if len(p) == 4:
            p[0] = ('bin_op', p[2], p[1], p[3])
        elif len(p) == 3:
            p[0] = ('unary_op', p[1], p[2])
        else:
            p[0] = p[1]

    def p_empty(self, p):
        """empty :"""
        p[0] = None

    def p_error(self, p):
        if p:
            print(f"Syntax error at {p.value}")
        else:
            print("Syntax error at EOF")
