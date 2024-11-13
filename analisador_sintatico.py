# ====================================================================
#                                                                    =
#          Trabalho de Compiladores - Analisador Sintático           =
#                   @author: Hugo Leonardo Melo                      =
#                                                                    =
# ====================================================================

from analisador_lexico import tokens, lexer  # Importando os tokens e o lexer definidos no analisador léxico
import ply.yacc as yacc

# Definindo a gramática com base na estrutura fornecida

# Programa principal
def p_program(p):
    'program : PROGRAM ID SEMICOLON declaracoes bloco'
    pass

# Declarações
def p_declaracoes(p):
    '''declaracoes : def_const def_tipos def_var def_rotina
                   | empty'''
    pass

# Definição de constantes
def p_def_const(p):
    '''def_const : CONST lista_const
                 | empty'''
    pass

def p_lista_const(p):
    '''lista_const : ID EQUALS const_valor SEMICOLON lista_const
                   | ID EQUALS const_valor SEMICOLON'''
    pass

def p_const_valor(p):
    '''const_valor : NUMERO
                   | STRING'''
    pass

# Definição de tipos
def p_def_tipos(p):
    '''def_tipos : TYPE lista_tipos
                 | empty'''
    pass

def p_lista_tipos(p):
    '''lista_tipos : ID EQUALS tipo SEMICOLON lista_tipos
                   | ID EQUALS tipo SEMICOLON'''
    pass

# Definição de variáveis
def p_def_var(p):
    '''def_var : VAR lista_var
               | empty'''
    pass

def p_lista_var(p):
    '''lista_var : var SEMICOLON lista_var
                 | var SEMICOLON'''
    pass

def p_var(p):
    'var : lista_id COLON tipo'
    pass

def p_lista_id(p):
    '''lista_id : ID COMMA lista_id
                | ID'''
    pass

# Tipos de dados
def p_tipo(p):
    '''tipo : INTEGER
            | REAL
            | CHAR
            | BOOLEAN
            | ARRAY LBRACKET NUMERO RBRACKET OF tipo
            | RECORD lista_campos END'''
    pass

def p_lista_campos(p):
    '''lista_campos : campo SEMICOLON lista_campos
                    | campo SEMICOLON'''
    pass

def p_campo(p):
    'campo : lista_id COLON tipo'
    pass

# Definição de rotinas (funções e procedimentos)
def p_def_rotina(p):
    '''def_rotina : rotina def_rotina
                  | empty'''
    pass

def p_rotina(p):
    '''rotina : function
              | procedure'''
    pass

def p_function(p):
    'function : FUNCTION ID LPAREN parametros RPAREN COLON tipo bloco_rotina'
    pass

def p_procedure(p):
    'procedure : PROCEDURE ID LPAREN parametros RPAREN bloco_rotina'
    pass

def p_parametros(p):
    '''parametros : param
                  | empty'''
    pass

def p_param(p):
    '''param : lista_id COLON tipo
             | lista_id COLON tipo SEMICOLON param'''
    pass

# Bloco de rotina
def p_bloco_rotina(p):
    '''bloco_rotina : declaracoes bloco'''
    pass

# Bloco principal
def p_bloco(p):
    'bloco : BEGIN lista_com END'
    pass

# Lista de comandos
def p_lista_com(p):
    '''lista_com : comando SEMICOLON lista_com
                 | comando SEMICOLON
                 | empty'''
    pass

# Comandos
def p_comando(p):
    '''comando : atribuicao
               | leitura
               | escrita
               | repeticao
               | condicional
               | chamada_rotina'''
    pass

def p_atribuicao(p):
    'atribuicao : ID ASSIGN exp'
    pass

def p_leitura(p):
    'leitura : READ LPAREN ID RPAREN'
    pass

def p_escrita(p):
    'escrita : WRITE LPAREN const_valor RPAREN'
    pass

def p_repeticao(p):
    '''repeticao : WHILE exp_logica DO bloco
                 | FOR atribuicao TO exp DO bloco'''
    pass

def p_condicional(p):
    '''condicional : IF exp_logica THEN bloco ELSE bloco
                   | IF exp_logica THEN bloco'''
    pass

def p_chamada_rotina(p):
    'chamada_rotina : ID LPAREN lista_param RPAREN'
    pass

# Lista de parâmetros
def p_lista_param(p):
    '''lista_param : parametro COMMA lista_param
                   | parametro
                   | empty'''
    pass

def p_parametro(p):
    '''parametro : exp
                 | ID'''
    pass

# Expressão lógica
def p_exp_logica(p):
    '''exp_logica : exp_mat op_logico exp_logica
                  | exp_mat'''
    pass

def p_op_logico(p):
    '''op_logico : AND
                 | OR'''
    pass

# Expressão matemática
def p_exp_mat(p):
    '''exp_mat : exp_mat op_mat exp_mat
               | parametro'''
    pass

def p_op_mat(p):
    '''op_mat : PLUS
              | MINUS
              | TIMES
              | DIVIDE'''
    pass

# Expressão
def p_exp(p):
    'exp : exp_mat'
    pass

# Valor vazio
def p_empty(p):
    'empty :'
    pass

# Tratamento de erros sintáticos
def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final da entrada")

# Função de erro do lexer para tokens não reconhecidos
def t_error(t):
    print(f"Token não reconhecido '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Construir o parser com debug=True
parser = yacc.yacc(debug=True)

# Função principal para ler o arquivo e analisar
def main(filename):
    try:
        # Ler o conteúdo do arquivo
        with open(filename, 'r') as file:
            input_data = file.read()
        
        # Fazer análise sintática diretamente com o parser
        print("\nAnalisando a sintaxe...")
        parser.parse(input_data, lexer=lexer)
        print("Análise sintática concluída.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
