
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY ASSIGN BEGIN BOOLEAN CHAR COLON COMMA CONST DIVIDE DO DOT ELSE END EQUALS FALSE FOR FUNCTION GREATER_EQUAL GREATER_THAN ID IF INTEGER LBRACE LBRACKET LESS_EQUAL LESS_THAN LPAREN MINUS NOT_EQUALS NUMBER OF OR PLUS PROCEDURE PROGRAM RBRACE RBRACKET READ REAL RECORD RPAREN SEMICOLON STRING THEN TIMES TO TRUE TYPE VAR WHILE WRITEprogram : PROGRAM ID SEMICOLON declaracoes blocodeclaracoes : def_const def_tipos def_var def_rotina\n                   | emptydef_const : CONST lista_const\n                 | emptylista_const : ID EQUALS const_valor SEMICOLON lista_const\n                   | ID EQUALS const_valor SEMICOLONconst_valor : NUMBER\n                   | STRINGdef_tipos : TYPE lista_tipos\n                 | emptylista_tipos : ID EQUALS tipo SEMICOLON lista_tipos\n                   | ID EQUALS tipo SEMICOLONdef_var : VAR lista_var\n               | emptylista_var : var SEMICOLON lista_var\n                 | var SEMICOLONvar : lista_id COLON tipolista_id : ID COMMA lista_id\n                | IDtipo : INTEGER\n            | REAL\n            | CHAR\n            | BOOLEAN\n            | ARRAY LBRACKET NUMBER RBRACKET OF tipo\n            | RECORD lista_campos ENDlista_campos : campo SEMICOLON lista_campos\n                    | campo SEMICOLONcampo : lista_id COLON tipodef_rotina : rotina def_rotina\n                  | emptyrotina : function\n              | procedurefunction : FUNCTION ID LPAREN parametros RPAREN COLON tipo bloco_rotinaprocedure : PROCEDURE ID LPAREN parametros RPAREN bloco_rotinaparametros : param\n                  | emptyparam : lista_id COLON tipo\n             | lista_id COLON tipo SEMICOLON parambloco_rotina : declaracoes blocobloco : BEGIN lista_com ENDlista_com : comando SEMICOLON lista_com\n                 | comando SEMICOLON\n                 | emptycomando : atribuicao\n               | leitura\n               | escrita\n               | repeticao\n               | condicional\n               | chamada_rotinaatribuicao : ID ASSIGN expleitura : READ LPAREN ID RPARENescrita : WRITE LPAREN const_valor RPARENrepeticao : WHILE exp_logica DO bloco\n                 | FOR atribuicao TO exp DO blococondicional : IF exp_logica THEN bloco\n                   | IF exp_logica THEN bloco ELSE blocoexp : NUMBER\n           | ID\n           | LPAREN exp RPAREN\n           | exp PLUS exp\n           | exp MINUS exp\n           | exp TIMES exp\n           | exp DIVIDE expexp_logica : exp operador_logico expoperador_logico : EQUALS\n                       | NOT_EQUALS\n                       | LESS_THAN\n                       | GREATER_THAN\n                       | LESS_EQUAL\n                       | GREATER_EQUAL\n                       | AND\n                       | ORempty :chamada_rotina : ID LPAREN argumentos RPAREN SEMICOLONargumentos : lista_param\n                  | emptylista_param : parametro COMMA lista_param\n                   | parametroparametro : exp\n                 | ID'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,9,37,],[0,-1,-41,]),'ID':([2,8,10,12,28,29,30,32,38,39,40,41,47,56,57,77,78,79,80,81,82,83,84,85,86,87,88,89,91,96,98,105,106,108,120,121,125,143,159,],[3,15,25,35,46,49,46,61,25,46,68,74,46,94,95,46,46,46,46,46,-66,-67,-68,-69,-70,-71,-72,-73,46,61,61,61,15,68,61,61,35,61,61,]),'SEMICOLON':([3,17,19,20,21,22,23,24,37,45,46,59,63,64,65,67,99,100,101,102,103,107,109,110,111,113,114,115,116,117,119,123,128,131,142,145,146,152,154,161,],[4,38,-45,-46,-47,-48,-49,-50,-41,-58,-59,96,106,-8,-9,-51,125,-21,-22,-23,-24,131,-52,-53,-54,-61,-62,-63,-64,-60,-56,-18,143,-75,-26,-55,-57,-29,159,-25,]),'CONST':([4,100,101,102,103,142,149,158,161,],[8,-21,-22,-23,-24,-26,8,8,-25,]),'BEGIN':([4,5,6,7,11,13,14,31,33,34,37,51,52,53,54,55,58,76,92,93,96,100,101,102,103,106,122,125,130,133,134,140,142,149,155,156,158,160,161,162,],[-74,10,-74,-3,-74,-11,-4,-74,-15,-10,-41,-2,-74,-31,-32,-33,-14,10,10,-30,-17,-21,-22,-23,-24,-7,-16,-13,-6,10,10,-12,-26,-74,-35,10,-74,-40,-25,-34,]),'TYPE':([4,6,7,14,100,101,102,103,106,130,142,149,158,161,],[-74,12,-5,-4,-21,-22,-23,-24,-7,-6,-26,-74,-74,-25,]),'VAR':([4,6,7,11,13,14,34,100,101,102,103,106,125,130,140,142,149,158,161,],[-74,-74,-5,32,-11,-4,-10,-21,-22,-23,-24,-7,-13,-6,-12,-26,-74,-74,-25,]),'FUNCTION':([4,6,7,11,13,14,31,33,34,37,52,54,55,58,96,100,101,102,103,106,122,125,130,140,142,149,155,158,160,161,162,],[-74,-74,-5,-74,-11,-4,56,-15,-10,-41,56,-32,-33,-14,-17,-21,-22,-23,-24,-7,-16,-13,-6,-12,-26,-74,-35,-74,-40,-25,-34,]),'PROCEDURE':([4,6,7,11,13,14,31,33,34,37,52,54,55,58,96,100,101,102,103,106,122,125,130,140,142,149,155,158,160,161,162,],[-74,-74,-5,-74,-11,-4,57,-15,-10,-41,57,-32,-33,-14,-17,-21,-22,-23,-24,-7,-16,-13,-6,-12,-26,-74,-35,-74,-40,-25,-34,]),'END':([10,16,18,38,66,127,143,151,],[-74,37,-44,-43,-42,142,-28,-27,]),'READ':([10,38,],[26,26,]),'WRITE':([10,38,],[27,27,]),'WHILE':([10,38,],[28,28,]),'FOR':([10,38,],[29,29,]),'IF':([10,38,],[30,30,]),'EQUALS':([15,35,44,45,46,113,114,115,116,117,],[36,62,82,-58,-59,-61,-62,-63,-64,-60,]),'ASSIGN':([25,49,],[39,39,]),'LPAREN':([25,26,27,28,30,39,40,47,77,78,79,80,81,82,83,84,85,86,87,88,89,91,94,95,108,],[40,41,42,47,47,47,47,47,47,47,47,47,47,-66,-67,-68,-69,-70,-71,-72,-73,47,120,121,47,]),'NUMBER':([28,30,36,39,40,42,47,77,78,79,80,81,82,83,84,85,86,87,88,89,91,108,126,],[45,45,64,45,45,64,45,45,45,45,45,45,-66,-67,-68,-69,-70,-71,-72,-73,45,45,141,]),'STRING':([36,42,],[65,65,]),'ELSE':([37,119,],[-41,134,]),'RPAREN':([40,45,46,64,65,68,69,70,71,72,73,74,75,90,100,101,102,103,113,114,115,116,117,120,121,132,135,136,137,139,142,154,161,163,],[-74,-58,-59,-8,-9,-59,107,-76,-77,-79,-80,109,110,117,-21,-22,-23,-24,-61,-62,-63,-64,-60,-74,-74,-78,147,-36,-37,149,-26,-38,-25,-39,]),'DO':([43,45,46,112,113,114,115,116,117,118,],[76,-58,-59,-65,-61,-62,-63,-64,-60,133,]),'PLUS':([44,45,46,67,68,73,90,112,113,114,115,116,117,118,],[78,-58,-59,78,-59,78,78,78,78,78,78,78,-60,78,]),'MINUS':([44,45,46,67,68,73,90,112,113,114,115,116,117,118,],[79,-58,-59,79,-59,79,79,79,79,79,79,79,-60,79,]),'TIMES':([44,45,46,67,68,73,90,112,113,114,115,116,117,118,],[80,-58,-59,80,-59,80,80,80,80,80,80,80,-60,80,]),'DIVIDE':([44,45,46,67,68,73,90,112,113,114,115,116,117,118,],[81,-58,-59,81,-59,81,81,81,81,81,81,81,-60,81,]),'NOT_EQUALS':([44,45,46,113,114,115,116,117,],[83,-58,-59,-61,-62,-63,-64,-60,]),'LESS_THAN':([44,45,46,113,114,115,116,117,],[84,-58,-59,-61,-62,-63,-64,-60,]),'GREATER_THAN':([44,45,46,113,114,115,116,117,],[85,-58,-59,-61,-62,-63,-64,-60,]),'LESS_EQUAL':([44,45,46,113,114,115,116,117,],[86,-58,-59,-61,-62,-63,-64,-60,]),'GREATER_EQUAL':([44,45,46,113,114,115,116,117,],[87,-58,-59,-61,-62,-63,-64,-60,]),'AND':([44,45,46,113,114,115,116,117,],[88,-58,-59,-61,-62,-63,-64,-60,]),'OR':([44,45,46,113,114,115,116,117,],[89,-58,-59,-61,-62,-63,-64,-60,]),'TO':([45,46,48,67,113,114,115,116,117,],[-58,-59,91,-51,-61,-62,-63,-64,-60,]),'COMMA':([45,46,61,68,72,73,113,114,115,116,117,],[-58,-59,98,-59,108,-80,-61,-62,-63,-64,-60,]),'THEN':([45,46,50,112,113,114,115,116,117,],[-58,-59,92,-65,-61,-62,-63,-64,-60,]),'COLON':([60,61,124,129,138,147,],[97,-20,-19,144,148,153,]),'INTEGER':([62,97,144,148,153,157,],[100,100,100,100,100,100,]),'REAL':([62,97,144,148,153,157,],[101,101,101,101,101,101,]),'CHAR':([62,97,144,148,153,157,],[102,102,102,102,102,102,]),'BOOLEAN':([62,97,144,148,153,157,],[103,103,103,103,103,103,]),'ARRAY':([62,97,144,148,153,157,],[104,104,104,104,104,104,]),'RECORD':([62,97,144,148,153,157,],[105,105,105,105,105,105,]),'LBRACKET':([104,],[126,]),'RBRACKET':([141,],[150,]),'OF':([150,],[157,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaracoes':([4,149,158,],[5,156,156,]),'def_const':([4,149,158,],[6,6,6,]),'empty':([4,6,10,11,31,38,40,52,120,121,149,158,],[7,13,18,33,53,18,71,53,137,137,7,7,]),'bloco':([5,76,92,133,134,156,],[9,111,119,145,146,160,]),'def_tipos':([6,],[11,]),'lista_const':([8,106,],[14,130,]),'lista_com':([10,38,],[16,66,]),'comando':([10,38,],[17,17,]),'atribuicao':([10,29,38,],[19,48,19,]),'leitura':([10,38,],[20,20,]),'escrita':([10,38,],[21,21,]),'repeticao':([10,38,],[22,22,]),'condicional':([10,38,],[23,23,]),'chamada_rotina':([10,38,],[24,24,]),'def_var':([11,],[31,]),'lista_tipos':([12,125,],[34,140,]),'exp_logica':([28,30,],[43,50,]),'exp':([28,30,39,40,47,77,78,79,80,81,91,108,],[44,44,67,73,90,112,113,114,115,116,118,73,]),'def_rotina':([31,52,],[51,93,]),'rotina':([31,52,],[52,52,]),'function':([31,52,],[54,54,]),'procedure':([31,52,],[55,55,]),'lista_var':([32,96,],[58,122,]),'var':([32,96,],[59,59,]),'lista_id':([32,96,98,105,120,121,143,159,],[60,60,124,129,138,138,129,138,]),'const_valor':([36,42,],[63,75,]),'argumentos':([40,],[69,]),'lista_param':([40,108,],[70,132,]),'parametro':([40,108,],[72,72,]),'operador_logico':([44,],[77,]),'tipo':([62,97,144,148,153,157,],[99,123,152,154,158,161,]),'lista_campos':([105,143,],[127,151,]),'campo':([105,143,],[128,128,]),'parametros':([120,121,],[135,139,]),'param':([120,121,159,],[136,136,163,]),'bloco_rotina':([149,158,],[155,162,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON declaracoes bloco','program',5,'p_program','analisador_sintatico.py',16),
  ('declaracoes -> def_const def_tipos def_var def_rotina','declaracoes',4,'p_declaracoes','analisador_sintatico.py',21),
  ('declaracoes -> empty','declaracoes',1,'p_declaracoes','analisador_sintatico.py',22),
  ('def_const -> CONST lista_const','def_const',2,'p_def_const','analisador_sintatico.py',27),
  ('def_const -> empty','def_const',1,'p_def_const','analisador_sintatico.py',28),
  ('lista_const -> ID EQUALS const_valor SEMICOLON lista_const','lista_const',5,'p_lista_const','analisador_sintatico.py',32),
  ('lista_const -> ID EQUALS const_valor SEMICOLON','lista_const',4,'p_lista_const','analisador_sintatico.py',33),
  ('const_valor -> NUMBER','const_valor',1,'p_const_valor','analisador_sintatico.py',37),
  ('const_valor -> STRING','const_valor',1,'p_const_valor','analisador_sintatico.py',38),
  ('def_tipos -> TYPE lista_tipos','def_tipos',2,'p_def_tipos','analisador_sintatico.py',43),
  ('def_tipos -> empty','def_tipos',1,'p_def_tipos','analisador_sintatico.py',44),
  ('lista_tipos -> ID EQUALS tipo SEMICOLON lista_tipos','lista_tipos',5,'p_lista_tipos','analisador_sintatico.py',48),
  ('lista_tipos -> ID EQUALS tipo SEMICOLON','lista_tipos',4,'p_lista_tipos','analisador_sintatico.py',49),
  ('def_var -> VAR lista_var','def_var',2,'p_def_var','analisador_sintatico.py',54),
  ('def_var -> empty','def_var',1,'p_def_var','analisador_sintatico.py',55),
  ('lista_var -> var SEMICOLON lista_var','lista_var',3,'p_lista_var','analisador_sintatico.py',59),
  ('lista_var -> var SEMICOLON','lista_var',2,'p_lista_var','analisador_sintatico.py',60),
  ('var -> lista_id COLON tipo','var',3,'p_var','analisador_sintatico.py',64),
  ('lista_id -> ID COMMA lista_id','lista_id',3,'p_lista_id','analisador_sintatico.py',68),
  ('lista_id -> ID','lista_id',1,'p_lista_id','analisador_sintatico.py',69),
  ('tipo -> INTEGER','tipo',1,'p_tipo','analisador_sintatico.py',74),
  ('tipo -> REAL','tipo',1,'p_tipo','analisador_sintatico.py',75),
  ('tipo -> CHAR','tipo',1,'p_tipo','analisador_sintatico.py',76),
  ('tipo -> BOOLEAN','tipo',1,'p_tipo','analisador_sintatico.py',77),
  ('tipo -> ARRAY LBRACKET NUMBER RBRACKET OF tipo','tipo',6,'p_tipo','analisador_sintatico.py',78),
  ('tipo -> RECORD lista_campos END','tipo',3,'p_tipo','analisador_sintatico.py',79),
  ('lista_campos -> campo SEMICOLON lista_campos','lista_campos',3,'p_lista_campos','analisador_sintatico.py',83),
  ('lista_campos -> campo SEMICOLON','lista_campos',2,'p_lista_campos','analisador_sintatico.py',84),
  ('campo -> lista_id COLON tipo','campo',3,'p_campo','analisador_sintatico.py',88),
  ('def_rotina -> rotina def_rotina','def_rotina',2,'p_def_rotina','analisador_sintatico.py',93),
  ('def_rotina -> empty','def_rotina',1,'p_def_rotina','analisador_sintatico.py',94),
  ('rotina -> function','rotina',1,'p_rotina','analisador_sintatico.py',98),
  ('rotina -> procedure','rotina',1,'p_rotina','analisador_sintatico.py',99),
  ('function -> FUNCTION ID LPAREN parametros RPAREN COLON tipo bloco_rotina','function',8,'p_function','analisador_sintatico.py',103),
  ('procedure -> PROCEDURE ID LPAREN parametros RPAREN bloco_rotina','procedure',6,'p_procedure','analisador_sintatico.py',107),
  ('parametros -> param','parametros',1,'p_parametros','analisador_sintatico.py',111),
  ('parametros -> empty','parametros',1,'p_parametros','analisador_sintatico.py',112),
  ('param -> lista_id COLON tipo','param',3,'p_param','analisador_sintatico.py',116),
  ('param -> lista_id COLON tipo SEMICOLON param','param',5,'p_param','analisador_sintatico.py',117),
  ('bloco_rotina -> declaracoes bloco','bloco_rotina',2,'p_bloco_rotina','analisador_sintatico.py',122),
  ('bloco -> BEGIN lista_com END','bloco',3,'p_bloco','analisador_sintatico.py',127),
  ('lista_com -> comando SEMICOLON lista_com','lista_com',3,'p_lista_com','analisador_sintatico.py',132),
  ('lista_com -> comando SEMICOLON','lista_com',2,'p_lista_com','analisador_sintatico.py',133),
  ('lista_com -> empty','lista_com',1,'p_lista_com','analisador_sintatico.py',134),
  ('comando -> atribuicao','comando',1,'p_comando','analisador_sintatico.py',139),
  ('comando -> leitura','comando',1,'p_comando','analisador_sintatico.py',140),
  ('comando -> escrita','comando',1,'p_comando','analisador_sintatico.py',141),
  ('comando -> repeticao','comando',1,'p_comando','analisador_sintatico.py',142),
  ('comando -> condicional','comando',1,'p_comando','analisador_sintatico.py',143),
  ('comando -> chamada_rotina','comando',1,'p_comando','analisador_sintatico.py',144),
  ('atribuicao -> ID ASSIGN exp','atribuicao',3,'p_atribuicao','analisador_sintatico.py',148),
  ('leitura -> READ LPAREN ID RPAREN','leitura',4,'p_leitura','analisador_sintatico.py',152),
  ('escrita -> WRITE LPAREN const_valor RPAREN','escrita',4,'p_escrita','analisador_sintatico.py',156),
  ('repeticao -> WHILE exp_logica DO bloco','repeticao',4,'p_repeticao','analisador_sintatico.py',160),
  ('repeticao -> FOR atribuicao TO exp DO bloco','repeticao',6,'p_repeticao','analisador_sintatico.py',161),
  ('condicional -> IF exp_logica THEN bloco','condicional',4,'p_condicional','analisador_sintatico.py',165),
  ('condicional -> IF exp_logica THEN bloco ELSE bloco','condicional',6,'p_condicional','analisador_sintatico.py',166),
  ('exp -> NUMBER','exp',1,'p_exp','analisador_sintatico.py',171),
  ('exp -> ID','exp',1,'p_exp','analisador_sintatico.py',172),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_exp','analisador_sintatico.py',173),
  ('exp -> exp PLUS exp','exp',3,'p_exp','analisador_sintatico.py',174),
  ('exp -> exp MINUS exp','exp',3,'p_exp','analisador_sintatico.py',175),
  ('exp -> exp TIMES exp','exp',3,'p_exp','analisador_sintatico.py',176),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp','analisador_sintatico.py',177),
  ('exp_logica -> exp operador_logico exp','exp_logica',3,'p_exp_logica','analisador_sintatico.py',181),
  ('operador_logico -> EQUALS','operador_logico',1,'p_operador_logico','analisador_sintatico.py',185),
  ('operador_logico -> NOT_EQUALS','operador_logico',1,'p_operador_logico','analisador_sintatico.py',186),
  ('operador_logico -> LESS_THAN','operador_logico',1,'p_operador_logico','analisador_sintatico.py',187),
  ('operador_logico -> GREATER_THAN','operador_logico',1,'p_operador_logico','analisador_sintatico.py',188),
  ('operador_logico -> LESS_EQUAL','operador_logico',1,'p_operador_logico','analisador_sintatico.py',189),
  ('operador_logico -> GREATER_EQUAL','operador_logico',1,'p_operador_logico','analisador_sintatico.py',190),
  ('operador_logico -> AND','operador_logico',1,'p_operador_logico','analisador_sintatico.py',191),
  ('operador_logico -> OR','operador_logico',1,'p_operador_logico','analisador_sintatico.py',192),
  ('empty -> <empty>','empty',0,'p_empty','analisador_sintatico.py',197),
  ('chamada_rotina -> ID LPAREN argumentos RPAREN SEMICOLON','chamada_rotina',5,'p_chamada_rotina','analisador_sintatico.py',210),
  ('argumentos -> lista_param','argumentos',1,'p_argumentos','analisador_sintatico.py',215),
  ('argumentos -> empty','argumentos',1,'p_argumentos','analisador_sintatico.py',216),
  ('lista_param -> parametro COMMA lista_param','lista_param',3,'p_lista_param','analisador_sintatico.py',221),
  ('lista_param -> parametro','lista_param',1,'p_lista_param','analisador_sintatico.py',222),
  ('parametro -> exp','parametro',1,'p_parametro','analisador_sintatico.py',226),
  ('parametro -> ID','parametro',1,'p_parametro','analisador_sintatico.py',227),
]
