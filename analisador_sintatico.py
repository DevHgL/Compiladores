# ====================================================================
#                                                                    =
# Trabalho de Compiladores - Annalisador Sintático                   =
# @author: Hugo Leonardo Melo                                        =
#                                                                    =
# ====================================================================

from analisador_lexico import tokens
import ply.yacc as yacc
    
    # Esta função deve retornar uma lista de tokens, onde cada token é um objeto com:
    # 'type' (tipo do token), 'value' (valor do token), e 'lineno' (número da linha)

def tokenize(input_data):

    return
    [
        {
         'type': 'PROGRAM', 
         'value': 'program',
         'lineno': 1
        },
        {
         'type': 'ID',
         'value': 'teste', 
         'lineno': 1
        },
        {
        'type': 'SEMICOLON', 
        'value': ';', 
        'lineno': 1
        },
        
        #TODO adicionar mais tokens, pra deixar mais completo.
    ]

# Definindo a gramática com base na estrutura fornecida

def p_program(p):
    'program : PROGRAM ID SEMICOLON decl corpo'
    pass

def p_decl(p):
    '''decl : dvar
            | func
            | dvar func
            | empty'''
    pass

def p_dvar(p):
    'dvar : VAR vars'
    pass

def p_vars(p):
    'vars : var SEMICOLON vars'
    pass

def p_vars_end(p):
    'vars : var SEMICOLON'
    pass

def p_var(p):
    'var : lista_id COLON tipo'
    pass

def p_lista_id(p):
    '''lista_id : ID COMMA lista_id
                | ID'''
    pass

def p_tipo(p):
    'tipo : REAL'
    pass

def p_func(p):
    'func : FUNCTION ID LPAREN parametros RPAREN COLON tipo bloco'
    pass

def p_parametros(p):
    '''parametros : var
                  | empty'''
    pass

def p_corpo(p):
    'corpo : BEGIN comandos END'
    pass

def p_comandos(p):
    '''comandos : empty'''
    pass

def p_bloco(p):
    '''bloco : BEGIN comandos END'''
    pass

# Regra para epsilon (vazio)
def p_empty(p):
    'empty :'
    pass

# Tratamento de erros sintáticos
def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final da entrada")

# Construir o parser
parser = yacc.yacc()

# Função principal para ler o arquivo e analisar
def main(filename):
    try:
        # Ler o conteúdo do arquivo
        with open(filename, 'r') as file:
            input_data = file.read()
        
        # Usar o analisador léxico externo para obter os tokens
        tokens = tokenize(input_data)
        
        # Fazer análise sintática usando os tokens gerados
        print("\nAnalisando a sintaxe...")
        parser.parse(input_data, lexer=LexerWrapper(tokens))
        print("Análise sintática concluída.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")

class LexerWrapper:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def token(self):
        if self.index < len(self.tokens):
            tok = self. tokens[self.index]
            self.index += 1
            return type('Token', (object,), tok)
        return None
    

    

# Exemplo de uso: analisando o conteúdo de 'entrada.txt'
if __name__ == "__main__":
    main("entrada.txt")
