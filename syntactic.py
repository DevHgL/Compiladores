import ply.yacc as yacc
from lexic import tokens

class SyntacticAnalyzer:
    def __init__(self):
        self.tokens = tokens
        self.precedence = (
            ('right', 'UMINUS'),  # Precedência para operadores unários
            ('left', 'LOGIC_OP_OR'),
            ('left', 'LOGIC_OP_AND'),
            ('left', 'COMP_OP'),  # Para operadores como <, >, <=, >=
            ('left', '+', '-'),
            ('left', '*', '/'),
            ('left', '.')  # Precedência para o operador ponto
        )
        self.parser = yacc.yacc(module=self)

    def p_program(self, p):
        """PROGRAM : DECLARATIONS BLOCK"""
        p[0] = ('program', p[1], p[2])

    def p_block(self, p):
        """BLOCK : BEGIN COMMAND_LIST END"""
        p[0] = ('block', p[2])

    def p_declarations(self, p):
        """DECLARATIONS : CONST_DECLARATIONS TYPE_DECLARATIONS VAR_DECLARATIONS
                        | TYPE_DECLARATIONS VAR_DECLARATIONS
                        | CONST_DECLARATIONS VAR_DECLARATIONS
                        | CONST_DECLARATIONS TYPE_DECLARATIONS
                        | CONST_DECLARATIONS
                        | TYPE_DECLARATIONS
                        | VAR_DECLARATIONS
                        | empty"""
        p[0] = p[1:] if len(p) > 1 else []

    def p_const_declarations(self, p):
        """CONST_DECLARATIONS : CONST_DEF ID '=' NUMBER ';' CONST_DECLARATIONS
                              | CONST_DEF ID '=' NUMBER ';'"""
        if len(p) == 7:
            p[0] = [(p[2], p[4])] + p[6]
        else:
            p[0] = [(p[2], p[4])]

    def p_type_declarations(self, p):
        """TYPE_DECLARATIONS : TYPE_DEF ID '=' TYPE ';' TYPE_DECLARATIONS
                             | TYPE_DEF ID '=' TYPE ';'"""
        if len(p) == 7:
            p[0] = [(p[2], p[4])] + p[6]
        else:
            p[0] = [(p[2], p[4])]

    def p_type(self, p):
        """TYPE : ID
                | ARRAY '[' NUMBER ']' OF ID
                | RECORD FIELD_LIST END"""
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 7:
            p[0] = ('array', p[3], p[6])
        elif len(p) == 4:
            p[0] = ('record', p[2])

    def p_field_list(self, p):
        """FIELD_LIST : ID ':' ID ';' FIELD_LIST
                      | ID ':' ID"""
        if len(p) == 6:
            p[0] = [(p[1], p[3])] + p[5]
        else:
            p[0] = [(p[1], p[3])]

    def p_var_declarations(self, p):
        """VAR_DECLARATIONS : VAR_DEF ID_LIST ':' ID ';' VAR_DECLARATIONS
                            | VAR_DEF ID_LIST ':' ID ';'"""
        if len(p) == 7:
            p[0] = [(p[2], p[4])] + p[6]
        else:
            p[0] = [(p[2], p[4])]

    def p_id_list(self, p):
        """ID_LIST : ID ',' ID_LIST
                   | ID"""
        if len(p) == 4:
            p[0] = [p[1]] + p[3]
        else:
            p[0] = [p[1]]

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
        """COMMAND : assignment
                   | conditional
                   | loop
                   | function_call"""
        p[0] = p[1]

    def p_assignment(self, p):
        """assignment : ID ASSIGNMENT EXP"""
        p[0] = ('assignment', p[1], p[3])

    def p_conditional(self, p):
        """conditional : IF '(' EXP ')' THEN BLOCK ELSE BLOCK
                       | IF '(' EXP ')' THEN BLOCK"""
        if len(p) == 9:
            p[0] = ('if', p[3], p[6], p[8])
        else:
            p[0] = ('if', p[3], p[6])

    def p_loop(self, p):
        """loop : WHILE EXP DO BLOCK"""
        p[0] = ('while', p[2], p[4])

    def p_function_call(self, p):
        """function_call : ID '(' ARG_LIST ')'"""
        p[0] = ('call', p[1], p[3])

    def p_arg_list(self, p):
        """ARG_LIST : EXP ',' ARG_LIST
                    | EXP
                    | empty"""
        if len(p) == 4:
            p[0] = [p[1]] + p[3]
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = []

    def p_exp(self, p):
        """
        EXP : EXP '+' EXP
            | EXP '-' EXP
            | EXP '*' EXP
            | EXP '/' EXP
            | EXP COMP_OP EXP
            | EXP LOGIC_OP_OR EXP
            | EXP LOGIC_OP_AND EXP
            | '-' EXP %prec UMINUS
            | '(' EXP ')'
            | ID '(' ARG_LIST ')'
            | ID '.' ID            
            | ID
            | NUMBER
            | TRUE
            | FALSE
        """
        if len(p) == 4 and p[2] in ['+', '-', '*', '/', 'COMP_OP', 'LOGIC_OP_OR', 'LOGIC_OP_AND']:
            p[0] = ('bin_op', p[2], p[1], p[3])
        elif len(p) == 3:
            p[0] = ('unary_op', p[1], p[2])
        elif len(p) == 5 and p[2] == '(':
            p[0] = ('call', p[1], p[3])  # Chamadas de função
        elif len(p) == 4 and p[2] == '.':
            p[0] = ('field_access', p[1], p[3])  # Acesso a campos
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
