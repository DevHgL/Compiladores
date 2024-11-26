from analisador_lexico import tokens, reserved_words  # Importa os tokens definidos no analisador léxico
import ply.yacc as yacc

# Gramática
def p_program(p):
    'program : PROGRAM lista_declaracoes BEGIN lista_com END'
    pass

def p_lista_declaracoes(p):
    '''lista_declaracoes : declaracoes lista_declaracoes
                         | empty'''
    pass

def p_declaracoes(p):
    '''declaracoes : CONST lista_const
                   | VAR lista_var
                   | TYPE lista_tipo
                   | empty'''
    pass

def p_lista_const(p):
    '''lista_const : ID ATRIB NUMBER SEMICOLON lista_const
                   | empty'''
    pass

def p_lista_var(p):
    '''lista_var : ID COLON tipo SEMICOLON lista_var
                 | empty'''
    pass

def p_tipo(p):
    '''tipo : INTEGER
            | REAL
            | CHAR
            | BOOLEAN'''
    pass

def p_lista_tipo(p):
    '''lista_tipo : ID ATRIB tipo SEMICOLON lista_tipo
                  | empty'''
    pass

def p_bloco(p):
    '''bloco : BEGIN lista_com END'''
    pass

def p_lista_com(p):
    '''lista_com : comando SEMICOLON lista_com
                 | empty'''
    pass

def p_comando(p):
    '''comando : atribuicao
               | leitura
               | escrita'''
    pass

def p_atribuicao(p):
    'atribuicao : ID ASSIGN NUMBER'
    pass

def p_leitura(p):
    'leitura : READ LPAREN ID RPAREN'
    pass

def p_escrita(p):
    'escrita : WRITE LPAREN STRING RPAREN'
    pass

# Regra para vazio (ignora produções opcionais)
def p_empty(p):
    'empty :'
    pass

# Regra para lidar com erros sintáticos
def p_error(p):
    if p:
        print(f"Erro de sintaxe no token '{p.value}' (tipo '{p.type}'), na linha {p.lineno}")
    else:
        print("Erro de sintaxe: entrada inesperada ou arquivo vazio.")

# Criar o parser
parser = yacc.yacc()
