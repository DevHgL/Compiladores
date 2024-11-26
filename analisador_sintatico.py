import ply.yacc as yacc
from analisador_lexico import tokens, lexer

# Programa principal
def p_program(p):
    '''program : PROGRAM ID SEMICOLON declarations compound_statement DOT'''
    p[0] = ('program', p[2], p[4], p[5])

# Declarações
def p_declarations(p):
    '''declarations : const_declaration type_declaration var_declaration
                    | const_declaration
                    | type_declaration
                    | var_declaration
                    | empty'''
    p[0] = ('declarations', p[1:])

# Definição de constantes
def p_const_declaration(p):
    '''const_declaration : CONST const_list
                         | empty'''
    p[0] = ('const_declaration', p[2]) if len(p) > 2 else None

def p_const_list(p):
    '''const_list : ID ATRIB expression SEMICOLON
                  | const_list ID ATRIB expression SEMICOLON'''
    if len(p) == 5:
        p[0] = [('const', p[1], p[3])]
    else:
        p[0] = p[1] + [('const', p[2], p[4])]

# Expressões
def p_expression(p):
    '''expression : EXP
                  | EXP_CONST
                  | EXP_COM'''
    p[0] = p[1]

def p_EXP(p):
    '''EXP : PARAMETRO EXP_L1
           | LPAREN EXP RPAREN'''
    p[0] = ('expression', p[1], p[2]) if len(p) > 2 else p[2]

def p_EXP_L1(p):
    '''EXP_L1 : OP_MAT EXP
              | empty'''
    p[0] = ('op_expression', p[1], p[2]) if len(p) > 2 else None

def p_EXP_LOGICO(p):
    '''EXP_LOGICO : OP_LOGICO EXP
                  | empty'''
    p[0] = ('logic_expression', p[1], p[2]) if len(p) > 2 else None

# Constantes e valores
def p_CONST_VALOR(p):
    '''CONST_VALOR : STRING
                   | EXP_CONST'''
    p[0] = ('const_value', p[1])

def p_EXP_CONST(p):
    '''EXP_CONST : PARAMETRO EXP_CONST_LINHA
                 | LPAREN EXP_CONST RPAREN'''
    p[0] = ('const_expression', p[1], p[2]) if len(p) > 2 else p[2]

def p_EXP_CONST_LINHA(p):
    '''EXP_CONST_LINHA : OP_MAT EXP_CONST
                       | empty'''
    p[0] = ('op_const', p[1], p[2]) if len(p) > 2 else None

# Comando geral
def p_COMANDO(p):
    '''COMANDO : ID
               | NAME
               | ATRIBUICAO
               | WHILE LPAREN EXP_COM RPAREN DO compound_statement'''
    if len(p) > 2:
        p[0] = ('while', p[3], p[6])
    else:
        p[0] = ('command', p[1])

def p_EXP_COM(p):
    '''EXP_COM : PARAM_LOGICO EXP_COM_LINHA
               | LPAREN EXP_COM RPAREN'''
    p[0] = ('compound_expression', p[1], p[2]) if len(p) > 2 else p[2]

def p_EXP_COM_LINHA(p):
    '''EXP_COM_LINHA : OP_LOGICO EXP_COM
                     | empty'''
    p[0] = ('op_compound', p[1], p[2]) if len(p) > 2 else None

# Tipos e variáveis
def p_type_declaration(p):
    '''type_declaration : TYPE type_list
                       | empty'''
    if len(p) > 2:
        p[0] = ('type_declaration', p[2])
    else:
        p[0] = None

def p_type_list(p):
    '''type_list : ID ATRIB type SEMICOLON
                 | type_list ID ATRIB type SEMICOLON'''
    if len(p) == 5:
        p[0] = [('type_def', p[1], p[3])]
    else:
        p[0] = p[1] + [('type_def', p[2], p[4])]

def p_type(p):
    '''type : INTEGER
            | REAL
            | CHAR
            | BOOLEAN
            | array_type
            | record_type'''
    p[0] = ('type', p[1])

def p_array_type(p):
    '''array_type : ARRAY LBRACKET NUMBER RBRACKET OF type'''
    p[0] = ('array_type', p[3], p[6])

def p_record_type(p):
    '''record_type : RECORD field_list END'''
    p[0] = ('record_type', p[2])

def p_field_list(p):
    '''field_list : ID COLON type SEMICOLON
                  | field_list ID COLON type SEMICOLON'''
    if len(p) == 5:
        p[0] = [('field', p[1], p[3])]
    else:
        p[0] = p[1] + [('field', p[2], p[4])]

def p_var_declaration(p):
    '''var_declaration : VAR var_list
                      | empty'''
    if len(p) > 2:
        p[0] = ('var_declaration', p[2])
    else:
        p[0] = None

def p_var_list(p):
    '''var_list : ID COLON type SEMICOLON
                | var_list ID COLON type SEMICOLON'''
    if len(p) == 5:
        p[0] = [('var', p[1], p[3])]
    else:
        p[0] = p[1] + [('var', p[2], p[4])]

# Composto e comandos
def p_compound_statement(p):
    '''compound_statement : BEGIN statement_list END'''
    p[0] = ('compound_statement', p[2])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list SEMICOLON statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_statement(p):
    '''statement : assignment_statement
                 | if_statement
                 | while_statement
                 | for_statement
                 | compound_statement
                 | read_statement
                 | write_statement
                 | empty'''
    p[0] = ('statement', p[1])

# Definição de assignment_statement
def p_assignment_statement(p):
    '''assignment_statement : ID ATRIB expression'''
    p[0] = ('assignment_statement', p[1], p[3])

# Definição de if_statement
def p_if_statement(p):
    '''if_statement : IF expression THEN statement ELSE statement'''
    p[0] = ('if_statement', p[2], p[4], p[6])

# Definição de while_statement
def p_while_statement(p):
    '''while_statement : WHILE expression DO statement'''
    p[0] = ('while_statement', p[2], p[4])

# Definição de for_statement
def p_for_statement(p):
    '''for_statement : FOR ID ASSIGN expression TO expression DO statement'''
    p[0] = ('for_statement', p[2], p[4], p[6], p[8])

# Definição de read_statement
def p_read_statement(p):
    '''read_statement : READ LPAREN ID RPAREN'''
    p[0] = ('read_statement', p[3])

# Definição de write_statement
def p_write_statement(p):
    '''write_statement : WRITE LPAREN expression RPAREN'''
    p[0] = ('write_statement', p[3])

# Função para definir a regra 'empty'
def p_empty(p):
    'empty :'
    pass

# Função para salvar a saída sintática em arquivo
def save_sintatico_result(result):
    with open("saida_sintatico.txt", "w") as output_file:
        def write_node(node, level=0):
            if isinstance(node, tuple):
                output_file.write("  " * level + f"{node[0]}: \n")
                for child in node[1:]:
                    write_node(child, level + 1)
            else:
                output_file.write("  " * level + f"{node}\n")
        
        if result:
            write_node(result)
        else:
            output_file.write("Nenhuma análise sintática foi realizada.\n")
    
    print("Análise sintática concluída com sucesso! Resultados salvos em 'saida_sintatico.txt'.")

# Função de erro
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: Token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: Fim inesperado do arquivo")

# Criar o parser
parser = yacc.yacc()

# Função para fazer o parsing de um arquivo
def parse_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
        result = parser.parse(data)
        save_sintatico_result(result)
        return result
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado!")
        return None
    except Exception as e:
        print(f"Erro ao analisar o arquivo: {e}")
        return None
