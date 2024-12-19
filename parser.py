import ply.yacc as yacc
from lexic import MyLexer

class MyParser:

    tokens = MyLexer.tokens

    start = 'PROGRAMA'

    def __init__(self):

        self.lexer = MyLexer()
        self.lexer.build()
        
        # Inicializar o parser
        self.parser = yacc.yacc(module=self)

    def p_empty(self, p):
        '''
        empty :
        '''
        p[0] = None

    def p_error(self, p):
        if p:
            print(f"Erro sintático no token '{p.value}' na linha {p.lineno}")
        else:
            print("Erro sintático no final do arquivo")

    def p_PROGRAMA(self, p):
        '''
        PROGRAMA : DECLARACOES BLOCO
        '''
        p[0] = ('programa', p[1], p[2])

    def p_BLOCO(self, p):
        '''
        BLOCO : BEGIN COMANDO LISTA_COM END
        '''
        p[0] = ('bloco', p[2], p[3])

    def p_DECLARACOES(self, p):
        '''
        DECLARACOES : DEF_CONST DEF_TIPOS DEF_VAR DEF_ROTINA
        '''
        p[0] = ('declaracoes', p[1], p[2], p[3], p[4])

    def p_DEF_CONST(self, p):
        '''
        DEF_CONST : CONSTANTE DEF_CONST
                | empty
        '''
        if len(p) == 3:
            p[0] = ('def_const', p[1], p[2])
        else:
            p[0] = None

    def p_DEF_TIPOS(self, p):
        '''
        DEF_TIPOS : TIPO DEF_TIPOS
                | empty
        '''
        if len(p) == 3:
            p[0] = ('def_tipos', p[1], p[2])
        else:
            p[0] = None

    def p_DEF_VAR(self, p):
        '''
        DEF_VAR : VARIAVEL DEF_VAR
                | empty
        '''
        if len(p) == 3:
            p[0] = ('def_var', p[1], p[2])
        else:
            p[0] = None

    def p_DEF_ROTINA(self, p):
        '''
        DEF_ROTINA : ROTINA DEF_ROTINA
                | empty
        '''
        if len(p) == 3:
            p[0] = ('def_rotina', p[1], p[2])
        else:
            p[0] = None


    def p_LISTA_ID(self, p):
        '''
        LISTA_ID : VIRGULA ID LISTA_ID
                | empty
        '''
        if len(p) == 4:
            p[0] = ('lista_id', p[2], p[3])
        else:
            p[0] = None


    def p_CONSTANTE(self, p):
        '''
        CONSTANTE : CONST ID IGUAL CONST_VALORP PONTOVIRG
        '''
        p[0] = ('constante', p[2], p[4])

    def p_TIPO(self, p):
        '''
        TIPO : TYPE ID IGUAL TIPO_DADO PONTOVIRG
        '''
        p[0] = ('tipo', p[2], p[4])

    def p_VARIAVEL(self, p):
        '''
        VARIAVEL : VAR CAMPO PONTOVIRG
        '''
        p[0] = ('variavel', p[2])

    def p_CAMPOS(self, p):
        '''
        CAMPOS : CAMPO LISTA_CAMPOS
        '''
        p[0] = ('campos', p[1], p[2])

    def p_CAMPO(self, p):
        '''
        CAMPO : ID LISTA_ID DOISPONTOS TIPO_DADO
        '''
        p[0] = ('campo', p[1], p[2], p[4])

    def p_LISTA_CAMPOS(self, p):
        '''
        LISTA_CAMPOS : PONTOVIRG CAMPO LISTA_CAMPOS
                    | empty
        '''
        if len(p) == 4:
            p[0] = ('lista_campos', p[2], p[3])
        else:
            p[0] = None

    def p_TIPO_DADO(self, p):
        '''
        TIPO_DADO : INTEGER
                | REAL
                | CHAR
                | BOOLEAN
                | ARRAY COLCHESQ NUMERO COLCHDIR OF TIPO_DADO
                | RECORD CAMPOS END
                | ID
        '''
        if len(p) == 2:
            p[0] = ('tipo_dado', p[1])
        elif p[1] == 'array':
            p[0] = ('tipo_dado_array', p[3], p[6])
        elif p[1] == 'record':
            p[0] = ('tipo_dado_record', p[2])

    def p_ROTINA(self, p):
        '''
        ROTINA : FUNCTION ID PARAM_ROTINA DOISPONTOS TIPO_DADO BLOCO_ROTINA
            | PROCEDURE ID PARAM_ROTINA BLOCO_ROTINA
        '''
        if len(p) == 7:
            p[0] = ('function', p[2], p[3], p[5], p[6])
        else:
            p[0] = ('procedure', p[2], p[3], p[4])

    def p_PARAM_ROTINA(self, p):
        '''
        PARAM_ROTINA : PARENTESQ CAMPOS PARENTDIR
                    | empty
        '''
        if len(p) == 4:
            p[0] = ('param_rotina', p[2])
        else:
            p[0] = None

    def p_BLOCO_ROTINA(self, p):
        '''
        BLOCO_ROTINA : DEF_VAR BLOCO
        '''
        p[0] = ('bloco_rotina', p[1], p[2])

    def p_LISTA_COM(self, p):
        '''
        LISTA_COM : PONTOVIRG COMANDO LISTA_COM
                | empty
        '''
        if len(p) == 4:
            p[0] = ('lista_comandos', p[2], p[3])
        else:
            p[0] = None

    def p_BLOCO_COM(self, p):
        '''
        BLOCO_COM : BLOCO
                | COMANDO
        '''
        p[0] = ('bloco_comando', p[1])

    def p_COMANDO(self, p):
        '''
        COMANDO : ID NOME ATRIBUICAO
                | WHILE EXP_COM DO BLOCO_COM
                | IF EXP_COM THEN BLOCO_COM ELSEP
                | FOR FORP DO BLOCO_COM
                | WRITE CONST_VALORP
                | READ ID NOME
        '''
        if len(p) == 4:
            if p[1] == 'while':
                p[0] = ('comando_while', p[2], p[4])
            elif p[1] == 'if':
                p[0] = ('comando_if', p[2], p[4], p[5])
            elif p[1] == 'for':
                p[0] = ('comando_for', p[2], p[4])
            elif p[1] == 'write':
                p[0] = ('comando_write', p[2])
            elif p[1] == 'read':
                p[0] = ('comando_read', p[2], p[3])
            else:
                p[0] = ('comando_atribuicao', p[1], p[2], p[3])

    def p_FORP(self, p):
        '''
        FORP : ID ATRIB PARAMETRO TO PARAMETRO
        '''
        p[0] = ('for_parametros', p[1], p[3], p[5])

    def p_ELSEP(self, p):
        '''
        ELSEP : ELSE BLOCO_COM
            | empty
        '''
        if len(p) == 3:
            p[0] = ('else', p[2])
        else:
            p[0] = None

    def p_ATRIBUICAO(self, p):
        '''
        ATRIBUICAO : ATRIB EXP
                | empty
        '''
        if len(p) == 3:
            p[0] = ('atribuicao', p[2])
        else:
            p[0] = None

    def p_EXP(self, p):
        '''
        EXP : PARAMETRO EXP_L1
            | PARENTESQ PARAMETRO EXP_L2
        '''
        if len(p) == 3:
            p[0] = ('exp', p[1], p[2])
        else:
            p[0] = ('exp_parentesis', p[2], p[3])

    def p_EXP_L1(self, p):
        '''
        EXP_L1 : OP_MAT EXP
            | empty
        '''
        if len(p) == 3:
            p[0] = ('exp_l1', p[1], p[2])
        else:
            p[0] = None

    def p_EXP_LOGICO(self, p):
        '''
        EXP_LOGICO : OP_LOGICO EXP
                | empty
        '''
        if len(p) == 3:
            p[0] = ('exp_logico', p[1], p[2])
        else:
            p[0] = None

    def p_EXP_L2(self, p):
        '''
        EXP_L2 : OP_MAT EXP PARENTDIR
            | PARAM_LOGICO OP_LOGICO EXP PARENTDIR
        '''
        if len(p) == 4:
            p[0] = ('exp_l2_mat', p[1], p[2])
        else:
            p[0] = ('exp_l2_logico', p[1], p[2], p[3])

    def p_PARAM_LOGICO(self, p):
        '''
        PARAM_LOGICO : OP_COMP PARAMETRO
                    | EXP
        '''
        if len(p) == 3:
            p[0] = ('param_logico_comparacao', p[1], p[2])            
        else:
            p[0] = ('param_logico_exp', p[1])

    def p_PARAMETRO(self, p):
        '''
        PARAMETRO : ID NOME
                | NUMERO
                | FALSE
                | TRUE
        '''
        if len(p) == 3:
            p[0] = ('parametro_id', p[1], p[2])
        else:
            p[0] = ('parametro', p[1])

    def p_LISTA_PARAM(self, p):
        '''
        LISTA_PARAM : PARAMETRO VIRGULA LISTA_PARAM
                    | PARAMETRO
                    | empty
        '''
        if len(p) == 4:
            p[0] = ('lista_param', p[1], p[3])
        elif len(p) == 2:
            p[0] = ('lista_param', p[1])
        else:
            p[0] = None


    def p_CONST_VALORP(self, p):
        '''
        CONST_VALORP : CONST_VALOR
                    | EXP_CONST
        '''
        p[0] = ('const_valor', p[1])


    def p_EXP_CONST(self, p):
        '''
        EXP_CONST : PARAMETRO EXP_CONST_LINHA
                | PARENTESQ PARAMETRO OP_MAT EXP_CONST PARENTDIR
        '''
        if len(p) == 3:
            p[0] = ('exp_const', p[1], p[2])
        elif len(p) == 6:
            p[0] = ('exp_const_parentesis', p[2], p[3], p[4])
        else:
            print(f"Erro inesperado em EXP_CONST: {p}")
            p[0] = None


    def p_EXP_CONST_LINHA(self, p):
        '''
        EXP_CONST_LINHA : OP_MAT EXP_CONST
                        | empty
        '''
        if len(p) == 3:
            p[0] = ('exp_const_linha', p[1], p[2])
        else:
            p[0] = None

    def p_EXP_COM(self, p):
        '''
        EXP_COM : PARAMETRO PARAM_LOGICO EXP_COM_LINHA
                | PARENTESQ PARAMETRO PARAM_LOGICO OP_LOGICO EXP_COM PARENTDIR
        '''
        if len(p) == 4:
            p[0] = ('exp_com', p[1], p[2], p[3])
        elif len(p) == 7:
            p[0] = ('exp_com_parentesis', p[2], p[3], p[4], p[5])
        else:
            print(f"Erro inesperado em EXP_CONST: {p}")
            p[0] = None

    def p_EXP_COM_LINHA(self, p):
        '''
        EXP_COM_LINHA : OP_LOGICO EXP_COM
                    | empty
        '''
        if len(p) == 3:
            p[0] = ('exp_com_linha', p[1], p[2])
        else:
            p[0] = None

    def p_OP_LOGICO(self, p):
        '''
        OP_LOGICO : AND
                | OR
        '''
        p[0] = ('op_logico', p[1])

    def p_OP_COMP(self, p):
        '''
        OP_COMP : MAIOR
                | MENOR
                | IGUAL
                | DIFERENTE
                | MAIORIGUAL
                | MENORIGUAL
        '''
        p[0] = ('op_comparacao', p[1])

    def p_OP_MAT(self, p):
        '''
        OP_MAT : MAIS
            | MENOS
            | VEZES
            | DIVIDE
        '''
        p[0] = ('op_matematico', p[1])

    def p_NOME(self, p):
        '''
        NOME : PONTO ID NOME
            | COLCHESQ PARAMETRO COLCHDIR
            | PARENTESQ LISTA_PARAM PARENTDIR
            | empty
        '''
        if len(p) == 4:
            if p[1] == '.':
                p[0] = ('nome_ponto', p[2], p[3])
            elif p[1] == '[':
                p[0] = ('nome_colchetes', p[2])
            else:
                p[0] = ('nome_parenteses', p[2])
        else:
            p[0] = None