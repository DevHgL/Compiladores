import ply.yacc as yacc
from lexico import MyLexer

class MyParser:

    tokens = MyLexer.tokens

    start = 'program'

    def __init__(self):
        self.lexer = MyLexer()
        self.lexer.build()
        self.parser = yacc.yacc(module=self, debug=True)

    def p_empty(self, p):
        'empty :'
        p[0] = None

    def p_error(self, p):
        if p:
            print(f"Syntax error at token '{p.value}' on line {p.lineno}")
        else:
            print("Syntax error at the end of file")

    def p_program(self, p):
        'program : declarations block'
        p[0] = ('program', p[1], p[2])

    def p_block(self, p):
        'block : BEGIN command_list END'
        p[0] = ('block', p[2])

    def p_declarations(self, p):
        '''declarations : declaration declarations
                        | empty'''
        p[0] = [] if len(p) == 2 else [p[1]] + p[2]

    def p_declaration(self, p):
        '''declaration : const_def
                       | type_def
                       | var_def
                       | routine_def'''
        p[0] = p[1]

    def p_const_def(self, p):
        'const_def : CONST ID EQUAL const_value SEMICOLON'
        p[0] = ('constant', p[2], p[4])

    def p_const_value(self, p):
        '''const_value : NUMBER
                       | STRING'''
        p[0] = p[1]

    def p_type_def(self, p):
        'type_def : TYPE ID EQUAL data_type SEMICOLON'
        p[0] = ('type', p[2], p[4])

    def p_data_type(self, p):
        '''data_type : INTEGER
                     | REAL
                     | CHAR
                     | BOOLEAN'''
        p[0] = p[1]

    def p_var_def(self, p):
        'var_def : VAR ID COLON data_type SEMICOLON'
        p[0] = ('variable', p[2], p[4])

    def p_routine_def(self, p):
        '''routine_def : FUNCTION ID param_list COLON data_type block
                       | PROCEDURE ID param_list block'''
        p[0] = ('function', p[2], p[3], p[5], p[6]) if len(p) == 7 else ('procedure', p[2], p[3], p[4])

    def p_param_list(self, p):
        '''param_list : LEFT_PAREN param RIGHT_PAREN
                      | empty'''
        p[0] = [] if len(p) == 2 else p[2]

    def p_param(self, p):
        '''param : ID COLON data_type COMMA param
                 | ID COLON data_type'''
        p[0] = [(p[1], p[3])] if len(p) == 4 else [(p[1], p[3])] + p[5]

    def p_command_list(self, p):
        '''command_list : command SEMICOLON command_list
                        | command'''
        p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[3]

    def p_command(self, p):
        '''command : ID ASSIGN expression
                   | WRITE const_value
                   | READ ID'''
        if len(p) == 4:
            p[0] = ('assign', p[1], p[3])
        elif p[1] == 'write':
            p[0] = ('write', p[2])
        else:
            p[0] = ('read', p[2])

    def p_expression(self, p):
        '''expression : term PLUS term
                      | term MINUS term
                      | term'''
        p[0] = ('expression', p[2], p[1], p[3]) if len(p) == 4 else p[1]

    def p_term(self, p):
        '''term : factor TIMES factor
                | factor DIVIDE factor
                | factor'''
        p[0] = ('term', p[2], p[1], p[3]) if len(p) == 4 else p[1]

    def p_factor(self, p):
        '''factor : NUMBER
                  | ID
                  | LEFT_PAREN expression RIGHT_PAREN'''
        p[0] = p[2] if len(p) == 4 else p[1]

if __name__ == "__main__":
    import sys
    lexer = MyLexer()
    lexer.build()

    parser = MyParser()
    filename = sys.argv[1] if len(sys.argv) > 1 else None

    if filename:
        try:
            with open(filename, 'r') as file:
                data = file.read()
            result = parser.parser.parse(data, lexer=lexer.lexer)
            print("Abstract Syntax Tree (AST):")
            print(result)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error during parsing: {e}")
    else:
        print("Usage: python sint.py <source_file>")