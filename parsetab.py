
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left;ABRECOL ABREPAR AND ARRAY ATRIBUICAO BEGIN BOOLEAN CHAR COMPARACAO CONST DIVIDE DO DOISPONTOS ELSE END FALSE FECHACOL FECHAPAR FOR FUNCTION ID IF IGUAL INTEGER MAIOR MAIS MENOR MENOS NUMERO OF OR PALAVRA PONTO PONTOVIRGULA PROCEDURE READ REAL RECORD THEN TO TRUE TYPE VAR VEZES VIRGULA WHILE WRITEPROGRAMA : DECLARACOES BLOCOLISTA_COM : LISTA_COM : COMANDO LISTA_COM_RESTOLISTA_COM_RESTO : ';' COMANDO LISTA_COM_RESTO\n                       | ';'BLOCO : BEGIN COMANDO LISTA_COM ENDDECLARACOES : DEF_CONST DEF_TIPOS DEF_VAR DEF_ROTINADEF_CONST : DEF_CONST : CONSTANTE DEF_CONSTCONSTANTE : CONST ID '=' CONST_VALOR ';'CONST_VALOR : PALAVRA\n                   | EXP_MATDEF_TIPOS : DEF_TIPOS : TIPO DEF_TIPOSTIPO : TYPE ID '=' TIPO_DADO ';'TIPO_DADO : INTEGER\n                 | REAL\n                 | CHAR\n                 | BOOLEAN\n                 | ARRAY '[' NUMERO ']' OF TIPO_DADO\n                 | RECORD CAMPOS END\n                 | IDDEF_VAR : DEF_VAR : VARIAVEL DEF_VARVARIAVEL : VAR CAMPOS ';'CAMPOS : CAMPO LISTA_CAMPOSLISTA_CAMPOS : LISTA_CAMPOS : ';' CAMPO LISTA_CAMPOSCAMPO : ID LISTA_ID ':' TIPO_DADOLISTA_ID : LISTA_ID : ',' ID LISTA_IDDEF_ROTINA : DEF_ROTINA : ROTINA DEF_ROTINAROTINA : FUNCTION ID PARAM_ROTINA ':' TIPO_DADO BLOCO_ROTINA\n              | PROCEDURE ID PARAM_ROTINA BLOCO_ROTINAPARAM_ROTINA : PARAM_ROTINA : '(' CAMPOS ')'BLOCO_ROTINA : DEF_VAR BLOCOCOMANDO : ID ATRIBUICAO EXP\n               | WHILE EXP_LOGICA DO BLOCO\n               | IF EXP_LOGICA THEN BLOCO alternativa_else\n               | FOR FOR_PARAMS DO BLOCO\n               | WRITE CONST_VALOR\n               | READ IDalternativa_else : ELSE BLOCO\n                        | FOR_PARAMS : ID ATRIBUICAO PARAMETRO TO PARAMETROEXP : EXP_MAT\n           | EXP_LOGICAEXP_LOGICA : PARAM_LOGICO OP_LOGICO EXP_LOGICA\n                  | PARAM_LOGICOPARAM_LOGICO : PARAMETRO OP_COMP PARAMETROEXP_MAT : PARAMETRO OP_MAT EXP_MAT\n               | PARAMETROOP_LOGICO : AND\n                 | OROP_COMP : '>'\n               | '<'\n               | '='OP_MAT : '+'\n              | '-'\n              | '*'\n              | '/'PARAMETRO : ID\n                 | NUMERO\n                 | FALSE\n                 | TRUE"
    
_lr_action_items = {'TYPE':([0,3,4,9,11,93,108,],[-8,10,-8,10,-9,-10,-15,]),'VAR':([0,3,4,8,9,11,21,23,79,80,85,87,88,89,90,93,104,108,123,126,127,132,],[-8,-13,-8,22,-13,-9,22,-14,-36,-25,-22,-16,-17,-18,-19,-10,22,-15,-21,22,-37,-20,]),'FUNCTION':([0,3,4,8,9,11,20,21,23,45,48,56,80,93,108,117,128,130,],[-8,-13,-8,-23,-13,-9,46,-23,-14,46,-24,-6,-25,-10,-15,-35,-38,-34,]),'PROCEDURE':([0,3,4,8,9,11,20,21,23,45,48,56,80,93,108,117,128,130,],[-8,-13,-8,-23,-13,-9,47,-23,-14,47,-24,-6,-25,-10,-15,-35,-38,-34,]),'BEGIN':([0,2,3,4,8,9,11,20,21,23,44,45,48,56,61,69,70,77,79,80,85,87,88,89,90,93,104,108,113,117,118,123,126,127,128,130,132,],[-8,7,-13,-8,-23,-13,-9,-32,-23,-14,-7,-32,-24,-6,7,7,7,-33,-36,-25,-22,-16,-17,-18,-19,-10,-23,-15,7,-35,7,-21,-23,-37,-38,-34,-20,]),'CONST':([0,4,93,],[5,5,-10,]),'$end':([1,6,56,],[0,-1,-6,]),'ID':([5,7,10,13,15,16,17,18,19,22,25,28,30,32,33,34,35,39,40,41,42,43,46,47,52,55,56,57,58,59,60,62,63,64,65,66,67,68,71,72,73,74,75,76,82,84,92,95,96,97,98,99,101,103,106,112,114,115,124,131,],[12,14,24,14,32,32,38,32,43,51,32,32,-51,-64,-65,-66,-67,-43,-11,-12,-54,-44,78,79,85,14,-6,-39,-48,-49,-54,32,-55,-56,32,-57,-58,-59,32,32,-60,-61,-62,-63,51,107,51,-40,-50,-52,-46,-42,-53,51,85,-41,32,85,-45,85,]),'WHILE':([7,13,30,32,33,34,35,39,40,41,42,43,55,56,57,58,59,60,95,96,97,98,99,101,112,124,],[15,15,-51,-64,-65,-66,-67,-43,-11,-12,-54,-44,15,-6,-39,-48,-49,-54,-40,-50,-52,-46,-42,-53,-41,-45,]),'IF':([7,13,30,32,33,34,35,39,40,41,42,43,55,56,57,58,59,60,95,96,97,98,99,101,112,124,],[16,16,-51,-64,-65,-66,-67,-43,-11,-12,-54,-44,16,-6,-39,-48,-49,-54,-40,-50,-52,-46,-42,-53,-41,-45,]),'FOR':([7,13,30,32,33,34,35,39,40,41,42,43,55,56,57,58,59,60,95,96,97,98,99,101,112,124,],[17,17,-51,-64,-65,-66,-67,-43,-11,-12,-54,-44,17,-6,-39,-48,-49,-54,-40,-50,-52,-46,-42,-53,-41,-45,]),'WRITE':([7,13,30,32,33,34,35,39,40,41,42,43,55,56,57,58,59,60,95,96,97,98,99,101,112,124,],[18,18,-51,-64,-65,-66,-67,-43,-11,-12,-54,-44,18,-6,-39,-48,-49,-54,-40,-50,-52,-46,-42,-53,-41,-45,]),'READ':([7,13,30,32,33,34,35,39,40,41,42,43,55,56,57,58,59,60,95,96,97,98,99,101,112,124,],[19,19,-51,-64,-65,-66,-67,-43,-11,-12,-54,-44,19,-6,-39,-48,-49,-54,-40,-50,-52,-46,-42,-53,-41,-45,]),'=':([12,24,31,32,33,34,35,60,],[25,52,68,-64,-65,-66,-67,68,]),'END':([13,27,30,32,33,34,35,39,40,41,42,43,50,54,55,56,57,58,59,60,81,85,87,88,89,90,95,96,97,98,99,101,105,110,111,112,119,120,123,124,132,],[-2,56,-51,-64,-65,-66,-67,-43,-11,-12,-54,-44,-27,-3,-5,-6,-39,-48,-49,-54,-26,-22,-16,-17,-18,-19,-40,-50,-52,-46,-42,-53,-27,123,-4,-41,-28,-29,-21,-45,-20,]),'ATRIBUICAO':([14,38,],[28,71,]),'NUMERO':([15,16,18,25,28,62,63,64,65,66,67,68,71,72,73,74,75,76,109,114,],[33,33,33,33,33,33,-55,-56,33,-57,-58,-59,33,33,-60,-61,-62,-63,122,33,]),'FALSE':([15,16,18,25,28,62,63,64,65,66,67,68,71,72,73,74,75,76,114,],[34,34,34,34,34,34,-55,-56,34,-57,-58,-59,34,34,-60,-61,-62,-63,34,]),'TRUE':([15,16,18,25,28,62,63,64,65,66,67,68,71,72,73,74,75,76,114,],[35,35,35,35,35,35,-55,-56,35,-57,-58,-59,35,35,-60,-61,-62,-63,35,]),'PALAVRA':([18,25,],[40,40,]),';':([26,30,32,33,34,35,39,40,41,42,43,49,50,53,56,57,58,59,60,81,85,86,87,88,89,90,94,95,96,97,98,99,101,105,112,119,120,123,124,132,],[55,-51,-64,-65,-66,-67,-43,-11,-12,-54,-44,80,82,93,-6,-39,-48,-49,-54,-26,-22,108,-16,-17,-18,-19,55,-40,-50,-52,-46,-42,-53,82,-41,-28,-29,-21,-45,-20,]),'DO':([29,30,32,33,34,35,37,96,97,125,],[61,-51,-64,-65,-66,-67,70,-50,-52,-47,]),'THEN':([30,32,33,34,35,36,96,97,],[-51,-64,-65,-66,-67,69,-50,-52,]),'AND':([30,32,33,34,35,97,],[63,-64,-65,-66,-67,-52,]),'OR':([30,32,33,34,35,97,],[64,-64,-65,-66,-67,-52,]),'>':([31,32,33,34,35,60,],[66,-64,-65,-66,-67,66,]),'<':([31,32,33,34,35,60,],[67,-64,-65,-66,-67,67,]),'+':([32,33,34,35,42,60,],[-64,-65,-66,-67,73,73,]),'-':([32,33,34,35,42,60,],[-64,-65,-66,-67,74,74,]),'*':([32,33,34,35,42,60,],[-64,-65,-66,-67,75,75,]),'/':([32,33,34,35,42,60,],[-64,-65,-66,-67,76,76,]),'TO':([32,33,34,35,100,],[-64,-65,-66,-67,114,]),')':([50,81,85,87,88,89,90,105,116,119,120,123,132,],[-27,-26,-22,-16,-17,-18,-19,-27,127,-28,-29,-21,-20,]),':':([51,78,83,102,107,121,127,],[-30,-36,106,115,-30,-31,-37,]),',':([51,107,],[84,84,]),'INTEGER':([52,106,115,131,],[87,87,87,87,]),'REAL':([52,106,115,131,],[88,88,88,88,]),'CHAR':([52,106,115,131,],[89,89,89,89,]),'BOOLEAN':([52,106,115,131,],[90,90,90,90,]),'ARRAY':([52,106,115,131,],[91,91,91,91,]),'RECORD':([52,106,115,131,],[92,92,92,92,]),'ELSE':([56,98,],[-6,113,]),'(':([78,79,],[103,103,]),'[':([91,],[109,]),']':([122,],[129,]),'OF':([129,],[131,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'DECLARACOES':([0,],[2,]),'DEF_CONST':([0,4,],[3,11,]),'CONSTANTE':([0,4,],[4,4,]),'BLOCO':([2,61,69,70,113,118,],[6,95,98,99,124,128,]),'DEF_TIPOS':([3,9,],[8,23,]),'TIPO':([3,9,],[9,9,]),'COMANDO':([7,13,55,],[13,26,94,]),'DEF_VAR':([8,21,104,126,],[20,48,118,118,]),'VARIAVEL':([8,21,104,126,],[21,21,21,21,]),'LISTA_COM':([13,],[27,]),'EXP_LOGICA':([15,16,28,62,],[29,36,59,96,]),'PARAM_LOGICO':([15,16,28,62,],[30,30,30,30,]),'PARAMETRO':([15,16,18,25,28,62,65,71,72,114,],[31,31,42,42,60,31,97,100,42,125,]),'FOR_PARAMS':([17,],[37,]),'CONST_VALOR':([18,25,],[39,53,]),'EXP_MAT':([18,25,28,72,],[41,41,58,101,]),'DEF_ROTINA':([20,45,],[44,77,]),'ROTINA':([20,45,],[45,45,]),'CAMPOS':([22,92,103,],[49,110,116,]),'CAMPO':([22,82,92,103,],[50,105,50,50,]),'LISTA_COM_RESTO':([26,94,],[54,111,]),'EXP':([28,],[57,]),'OP_LOGICO':([30,],[62,]),'OP_COMP':([31,60,],[65,65,]),'OP_MAT':([42,60,],[72,72,]),'LISTA_CAMPOS':([50,105,],[81,119,]),'LISTA_ID':([51,107,],[83,121,]),'TIPO_DADO':([52,106,115,131,],[86,120,126,132,]),'PARAM_ROTINA':([78,79,],[102,104,]),'alternativa_else':([98,],[112,]),'BLOCO_ROTINA':([104,126,],[117,130,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> DECLARACOES BLOCO','PROGRAMA',2,'p_programa','analisador_sintatico.py',12),
  ('LISTA_COM -> <empty>','LISTA_COM',0,'p_lista_com_vazia','analisador_sintatico.py',20),
  ('LISTA_COM -> COMANDO LISTA_COM_RESTO','LISTA_COM',2,'p_lista_com','analisador_sintatico.py',24),
  ('LISTA_COM_RESTO -> ; COMANDO LISTA_COM_RESTO','LISTA_COM_RESTO',3,'p_lista_com_resto','analisador_sintatico.py',28),
  ('LISTA_COM_RESTO -> ;','LISTA_COM_RESTO',1,'p_lista_com_resto','analisador_sintatico.py',29),
  ('BLOCO -> BEGIN COMANDO LISTA_COM END','BLOCO',4,'p_bloco','analisador_sintatico.py',45),
  ('DECLARACOES -> DEF_CONST DEF_TIPOS DEF_VAR DEF_ROTINA','DECLARACOES',4,'p_declaracoes','analisador_sintatico.py',55),
  ('DEF_CONST -> <empty>','DEF_CONST',0,'p_def_const_vazio','analisador_sintatico.py',59),
  ('DEF_CONST -> CONSTANTE DEF_CONST','DEF_CONST',2,'p_def_const','analisador_sintatico.py',63),
  ('CONSTANTE -> CONST ID = CONST_VALOR ;','CONSTANTE',5,'p_constante','analisador_sintatico.py',67),
  ('CONST_VALOR -> PALAVRA','CONST_VALOR',1,'p_const_valor','analisador_sintatico.py',71),
  ('CONST_VALOR -> EXP_MAT','CONST_VALOR',1,'p_const_valor','analisador_sintatico.py',72),
  ('DEF_TIPOS -> <empty>','DEF_TIPOS',0,'p_def_tipos_vazio','analisador_sintatico.py',76),
  ('DEF_TIPOS -> TIPO DEF_TIPOS','DEF_TIPOS',2,'p_def_tipos','analisador_sintatico.py',80),
  ('TIPO -> TYPE ID = TIPO_DADO ;','TIPO',5,'p_tipo','analisador_sintatico.py',84),
  ('TIPO_DADO -> INTEGER','TIPO_DADO',1,'p_tipo_dado','analisador_sintatico.py',88),
  ('TIPO_DADO -> REAL','TIPO_DADO',1,'p_tipo_dado','analisador_sintatico.py',89),
  ('TIPO_DADO -> CHAR','TIPO_DADO',1,'p_tipo_dado','analisador_sintatico.py',90),
  ('TIPO_DADO -> BOOLEAN','TIPO_DADO',1,'p_tipo_dado','analisador_sintatico.py',91),
  ('TIPO_DADO -> ARRAY [ NUMERO ] OF TIPO_DADO','TIPO_DADO',6,'p_tipo_dado','analisador_sintatico.py',92),
  ('TIPO_DADO -> RECORD CAMPOS END','TIPO_DADO',3,'p_tipo_dado','analisador_sintatico.py',93),
  ('TIPO_DADO -> ID','TIPO_DADO',1,'p_tipo_dado','analisador_sintatico.py',94),
  ('DEF_VAR -> <empty>','DEF_VAR',0,'p_def_var_vazio','analisador_sintatico.py',105),
  ('DEF_VAR -> VARIAVEL DEF_VAR','DEF_VAR',2,'p_def_var','analisador_sintatico.py',109),
  ('VARIAVEL -> VAR CAMPOS ;','VARIAVEL',3,'p_variavel','analisador_sintatico.py',113),
  ('CAMPOS -> CAMPO LISTA_CAMPOS','CAMPOS',2,'p_campos','analisador_sintatico.py',117),
  ('LISTA_CAMPOS -> <empty>','LISTA_CAMPOS',0,'p_lista_campos_vazio','analisador_sintatico.py',121),
  ('LISTA_CAMPOS -> ; CAMPO LISTA_CAMPOS','LISTA_CAMPOS',3,'p_lista_campos','analisador_sintatico.py',125),
  ('CAMPO -> ID LISTA_ID : TIPO_DADO','CAMPO',4,'p_campo','analisador_sintatico.py',129),
  ('LISTA_ID -> <empty>','LISTA_ID',0,'p_lista_id_vazio','analisador_sintatico.py',133),
  ('LISTA_ID -> , ID LISTA_ID','LISTA_ID',3,'p_lista_id','analisador_sintatico.py',137),
  ('DEF_ROTINA -> <empty>','DEF_ROTINA',0,'p_def_rotina_vazio','analisador_sintatico.py',141),
  ('DEF_ROTINA -> ROTINA DEF_ROTINA','DEF_ROTINA',2,'p_def_rotina','analisador_sintatico.py',145),
  ('ROTINA -> FUNCTION ID PARAM_ROTINA : TIPO_DADO BLOCO_ROTINA','ROTINA',6,'p_rotina','analisador_sintatico.py',149),
  ('ROTINA -> PROCEDURE ID PARAM_ROTINA BLOCO_ROTINA','ROTINA',4,'p_rotina','analisador_sintatico.py',150),
  ('PARAM_ROTINA -> <empty>','PARAM_ROTINA',0,'p_param_rotina_vazio','analisador_sintatico.py',157),
  ('PARAM_ROTINA -> ( CAMPOS )','PARAM_ROTINA',3,'p_param_rotina','analisador_sintatico.py',161),
  ('BLOCO_ROTINA -> DEF_VAR BLOCO','BLOCO_ROTINA',2,'p_bloco_rotina','analisador_sintatico.py',165),
  ('COMANDO -> ID ATRIBUICAO EXP','COMANDO',3,'p_comando','analisador_sintatico.py',169),
  ('COMANDO -> WHILE EXP_LOGICA DO BLOCO','COMANDO',4,'p_comando','analisador_sintatico.py',170),
  ('COMANDO -> IF EXP_LOGICA THEN BLOCO alternativa_else','COMANDO',5,'p_comando','analisador_sintatico.py',171),
  ('COMANDO -> FOR FOR_PARAMS DO BLOCO','COMANDO',4,'p_comando','analisador_sintatico.py',172),
  ('COMANDO -> WRITE CONST_VALOR','COMANDO',2,'p_comando','analisador_sintatico.py',173),
  ('COMANDO -> READ ID','COMANDO',2,'p_comando','analisador_sintatico.py',174),
  ('alternativa_else -> ELSE BLOCO','alternativa_else',2,'p_alternativa_else','analisador_sintatico.py',189),
  ('alternativa_else -> <empty>','alternativa_else',0,'p_alternativa_else','analisador_sintatico.py',190),
  ('FOR_PARAMS -> ID ATRIBUICAO PARAMETRO TO PARAMETRO','FOR_PARAMS',5,'p_for_params','analisador_sintatico.py',197),
  ('EXP -> EXP_MAT','EXP',1,'p_exp','analisador_sintatico.py',201),
  ('EXP -> EXP_LOGICA','EXP',1,'p_exp','analisador_sintatico.py',202),
  ('EXP_LOGICA -> PARAM_LOGICO OP_LOGICO EXP_LOGICA','EXP_LOGICA',3,'p_exp_logica','analisador_sintatico.py',206),
  ('EXP_LOGICA -> PARAM_LOGICO','EXP_LOGICA',1,'p_exp_logica','analisador_sintatico.py',207),
  ('PARAM_LOGICO -> PARAMETRO OP_COMP PARAMETRO','PARAM_LOGICO',3,'p_param_logico','analisador_sintatico.py',214),
  ('EXP_MAT -> PARAMETRO OP_MAT EXP_MAT','EXP_MAT',3,'p_exp_mat','analisador_sintatico.py',218),
  ('EXP_MAT -> PARAMETRO','EXP_MAT',1,'p_exp_mat','analisador_sintatico.py',219),
  ('OP_LOGICO -> AND','OP_LOGICO',1,'p_op_logico','analisador_sintatico.py',226),
  ('OP_LOGICO -> OR','OP_LOGICO',1,'p_op_logico','analisador_sintatico.py',227),
  ('OP_COMP -> >','OP_COMP',1,'p_op_comp','analisador_sintatico.py',231),
  ('OP_COMP -> <','OP_COMP',1,'p_op_comp','analisador_sintatico.py',232),
  ('OP_COMP -> =','OP_COMP',1,'p_op_comp','analisador_sintatico.py',233),
  ('OP_MAT -> +','OP_MAT',1,'p_op_mat','analisador_sintatico.py',237),
  ('OP_MAT -> -','OP_MAT',1,'p_op_mat','analisador_sintatico.py',238),
  ('OP_MAT -> *','OP_MAT',1,'p_op_mat','analisador_sintatico.py',239),
  ('OP_MAT -> /','OP_MAT',1,'p_op_mat','analisador_sintatico.py',240),
  ('PARAMETRO -> ID','PARAMETRO',1,'p_parametro','analisador_sintatico.py',244),
  ('PARAMETRO -> NUMERO','PARAMETRO',1,'p_parametro','analisador_sintatico.py',245),
  ('PARAMETRO -> FALSE','PARAMETRO',1,'p_parametro','analisador_sintatico.py',246),
  ('PARAMETRO -> TRUE','PARAMETRO',1,'p_parametro','analisador_sintatico.py',247),
]
