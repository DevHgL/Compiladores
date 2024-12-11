
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ARRAY ASSIGNMENT BEGIN BOOLEAN CHAR COMP_OP CONST DO ELSE END EQUAL FALSE FOR FUNCTION GREATER_EQUAL GREATER_THAN ID IF INTEGER LESS_EQUAL LESS_THAN LOGIC_OP_AND LOGIC_OP_OR NOT_EQUALS NUMBER OF PROCEDURE READ REAL RECORD STRING THEN TO TRUE TYPE VAR WHILE WRITEPROGRAM : DECLARATIONS BLOCKBLOCK : BEGIN COMMAND_LIST END\n             | BEGIN ENDDECLARATIONS : CONST_DEF TYPE_DEF VAR_DEFCONST_DEF : CONSTANT CONST_DEF\n                 | CONSTANT : CONST ID '=' CONST_VALUE ';'CONST_VALUE : STRING\n                   | CONST_EXPCONST_EXP : NUMBER\n                 | '(' CONST_EXP ')'\n                 | CONST_EXP '+' CONST_EXP\n                 | CONST_EXP '-' CONST_EXP\n                 | CONST_EXP '*' CONST_EXP\n                 | CONST_EXP '/' CONST_EXPTYPE_DEF : TYPE_DECLARATION TYPE_DEF\n                | TYPE_DECLARATION : TYPE ID '=' DATA_TYPE ';'DATA_TYPE : INTEGER\n                 | REAL\n                 | CHAR\n                 | BOOLEAN\n                 | ARRAY '[' NUMBER ']' OF DATA_TYPE\n                 | RECORD FIELDS END\n                 | IDVAR_DEF : VARIABLE VAR_DEF\n               | VARIABLE : VAR ID_LIST ':' DATA_TYPE ';'ID_LIST : ID\n               | ID_LIST ',' IDFIELDS : FIELD FIELD_LISTFIELD : ID ':' DATA_TYPEFIELD_LIST : ';' FIELD FIELD_LIST\n                  | COMMAND_LIST : COMMAND\n                    | COMMAND_LIST ';' COMMANDCOMMAND : ID ASSIGNMENT EXP\n               | ID ASSIGNMENT FUNCTION_CALL\n               | IF '(' COM_EXP ')' THEN COMMAND\n               | IF '(' COM_EXP ')' THEN COMMAND ELSE COMMAND\n               | WHILE '(' COM_EXP ')' DO COMMAND\n               | BEGIN COMMAND_LIST ENDFUNCTION_CALL : ID '(' PARAM_LIST ')'PARAM_LIST : EXP\n                  | PARAM_LIST ',' EXP\n                  | COM_EXP : EXP COMP_OP EXP\n               | COM_EXP LOGIC_OP_OR COM_EXP\n               | COM_EXP LOGIC_OP_AND COM_EXPEXP : EXP '+' EXP\n           | EXP '-' EXP\n           | EXP '*' EXP\n           | EXP '/' EXP\n           | '(' EXP ')'\n           | ID\n           | NUMBER\n           | TRUE\n           | FALSE"
    
_lr_action_items = {'TYPE':([0,3,4,9,11,64,83,],[-6,10,-6,10,-5,-7,-18,]),'VAR':([0,3,4,8,9,11,21,23,64,83,105,],[-6,-17,-6,22,-17,-5,22,-16,-7,-18,-28,]),'BEGIN':([0,2,3,4,7,8,9,11,13,20,21,23,28,32,64,83,100,104,105,119,],[-6,7,-17,-6,13,-27,-17,-5,13,-4,-27,-16,13,-26,-7,-18,13,13,-28,13,]),'CONST':([0,4,64,],[5,5,-7,]),'$end':([1,6,15,27,],[0,-1,-3,-2,]),'ID':([5,7,10,13,22,28,29,30,31,35,46,54,55,63,70,71,72,73,74,77,78,79,100,104,109,110,112,119,120,],[12,17,24,17,34,17,43,52,52,56,52,56,82,87,52,52,52,52,52,52,52,52,17,17,87,56,52,17,56,]),'END':([7,14,16,26,41,42,43,44,45,47,48,49,52,56,58,59,60,61,85,86,95,96,97,98,99,107,108,111,113,114,116,117,121,122,123,],[15,27,-35,41,-42,-36,-55,-37,-38,-56,-57,-58,-55,-25,-19,-20,-21,-22,107,-34,-50,-51,-52,-53,-54,-24,-31,-43,-39,-41,-34,-32,-33,-40,-23,]),'IF':([7,13,28,100,104,119,],[18,18,18,18,18,18,]),'WHILE':([7,13,28,100,104,119,],[19,19,19,19,19,19,]),'=':([12,24,],[25,35,]),';':([14,16,26,36,37,38,39,41,42,43,44,45,47,48,49,52,56,57,58,59,60,61,81,86,88,89,90,91,92,95,96,97,98,99,107,111,113,114,116,117,122,123,],[28,-35,28,64,-8,-9,-10,-42,-36,-55,-37,-38,-56,-57,-58,-55,-25,83,-19,-20,-21,-22,105,109,-12,-13,-14,-15,-11,-50,-51,-52,-53,-54,-24,-43,-39,-41,109,-32,-40,-23,]),'ASSIGNMENT':([17,],[29,]),'(':([18,19,25,29,30,31,40,43,46,65,66,67,68,70,71,72,73,74,77,78,79,112,],[30,31,40,46,46,46,40,70,46,40,40,40,40,46,46,46,46,46,46,46,46,46,]),'STRING':([25,],[37,]),'NUMBER':([25,29,30,31,40,46,65,66,67,68,70,71,72,73,74,77,78,79,84,112,],[39,47,47,47,39,47,39,39,39,39,47,47,47,47,47,47,47,47,106,47,]),'TRUE':([29,30,31,46,70,71,72,73,74,77,78,79,112,],[48,48,48,48,48,48,48,48,48,48,48,48,48,]),'FALSE':([29,30,31,46,70,71,72,73,74,77,78,79,112,],[49,49,49,49,49,49,49,49,49,49,49,49,49,]),':':([33,34,82,87,],[54,-29,-30,110,]),',':([33,34,47,48,49,52,70,82,93,94,95,96,97,98,99,118,],[55,-29,-56,-57,-58,-55,-46,-30,112,-44,-50,-51,-52,-53,-54,-45,]),'INTEGER':([35,54,110,120,],[58,58,58,58,]),'REAL':([35,54,110,120,],[59,59,59,59,]),'CHAR':([35,54,110,120,],[60,60,60,60,]),'BOOLEAN':([35,54,110,120,],[61,61,61,61,]),'ARRAY':([35,54,110,120,],[62,62,62,62,]),'RECORD':([35,54,110,120,],[63,63,63,63,]),'+':([38,39,43,44,47,48,49,51,52,69,75,88,89,90,91,92,94,95,96,97,98,99,103,118,],[65,-10,-55,71,-56,-57,-58,71,-55,65,71,65,65,65,65,-11,71,71,71,71,71,-54,71,71,]),'-':([38,39,43,44,47,48,49,51,52,69,75,88,89,90,91,92,94,95,96,97,98,99,103,118,],[66,-10,-55,72,-56,-57,-58,72,-55,66,72,66,66,66,66,-11,72,72,72,72,72,-54,72,72,]),'*':([38,39,43,44,47,48,49,51,52,69,75,88,89,90,91,92,94,95,96,97,98,99,103,118,],[67,-10,-55,73,-56,-57,-58,73,-55,67,73,67,67,67,67,-11,73,73,73,73,73,-54,73,73,]),'/':([38,39,43,44,47,48,49,51,52,69,75,88,89,90,91,92,94,95,96,97,98,99,103,118,],[68,-10,-55,74,-56,-57,-58,74,-55,68,74,68,68,68,68,-11,74,74,74,74,74,-54,74,74,]),')':([39,47,48,49,50,52,53,69,70,75,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,118,],[-10,-56,-57,-58,76,-55,80,92,-46,99,-12,-13,-14,-15,-11,111,-44,-50,-51,-52,-53,-54,-48,-49,-47,-45,]),'ELSE':([41,43,44,45,47,48,49,52,95,96,97,98,99,111,113,114,122,],[-42,-55,-37,-38,-56,-57,-58,-55,-50,-51,-52,-53,-54,-43,119,-41,-40,]),'COMP_OP':([47,48,49,51,52,95,96,97,98,99,],[-56,-57,-58,79,-55,-50,-51,-52,-53,-54,]),'LOGIC_OP_OR':([47,48,49,50,52,53,95,96,97,98,99,101,102,103,],[-56,-57,-58,77,-55,77,-50,-51,-52,-53,-54,77,77,-47,]),'LOGIC_OP_AND':([47,48,49,50,52,53,95,96,97,98,99,101,102,103,],[-56,-57,-58,78,-55,78,-50,-51,-52,-53,-54,78,78,-47,]),'[':([62,],[84,]),'THEN':([76,],[100,]),'DO':([80,],[104,]),']':([106,],[115,]),'OF':([115,],[120,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'DECLARATIONS':([0,],[2,]),'CONST_DEF':([0,4,],[3,11,]),'CONSTANT':([0,4,],[4,4,]),'BLOCK':([2,],[6,]),'TYPE_DEF':([3,9,],[8,23,]),'TYPE_DECLARATION':([3,9,],[9,9,]),'COMMAND_LIST':([7,13,],[14,26,]),'COMMAND':([7,13,28,100,104,119,],[16,16,42,113,114,122,]),'VAR_DEF':([8,21,],[20,32,]),'VARIABLE':([8,21,],[21,21,]),'ID_LIST':([22,],[33,]),'CONST_VALUE':([25,],[36,]),'CONST_EXP':([25,40,65,66,67,68,],[38,69,88,89,90,91,]),'EXP':([29,30,31,46,70,71,72,73,74,77,78,79,112,],[44,51,51,75,94,95,96,97,98,51,51,103,118,]),'FUNCTION_CALL':([29,],[45,]),'COM_EXP':([30,31,77,78,],[50,53,101,102,]),'DATA_TYPE':([35,54,110,120,],[57,81,117,123,]),'FIELDS':([63,],[85,]),'FIELD':([63,109,],[86,116,]),'PARAM_LIST':([70,],[93,]),'FIELD_LIST':([86,116,],[108,121,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> DECLARATIONS BLOCK','PROGRAM',2,'p_program','syntactic.py',15),
  ('BLOCK -> BEGIN COMMAND_LIST END','BLOCK',3,'p_block','syntactic.py',19),
  ('BLOCK -> BEGIN END','BLOCK',2,'p_block','syntactic.py',20),
  ('DECLARATIONS -> CONST_DEF TYPE_DEF VAR_DEF','DECLARATIONS',3,'p_declarations','syntactic.py',27),
  ('CONST_DEF -> CONSTANT CONST_DEF','CONST_DEF',2,'p_const_def','syntactic.py',31),
  ('CONST_DEF -> <empty>','CONST_DEF',0,'p_const_def','syntactic.py',32),
  ('CONSTANT -> CONST ID = CONST_VALUE ;','CONSTANT',5,'p_constant','syntactic.py',39),
  ('CONST_VALUE -> STRING','CONST_VALUE',1,'p_const_value','syntactic.py',43),
  ('CONST_VALUE -> CONST_EXP','CONST_VALUE',1,'p_const_value','syntactic.py',44),
  ('CONST_EXP -> NUMBER','CONST_EXP',1,'p_const_exp','syntactic.py',48),
  ('CONST_EXP -> ( CONST_EXP )','CONST_EXP',3,'p_const_exp','syntactic.py',49),
  ('CONST_EXP -> CONST_EXP + CONST_EXP','CONST_EXP',3,'p_const_exp','syntactic.py',50),
  ('CONST_EXP -> CONST_EXP - CONST_EXP','CONST_EXP',3,'p_const_exp','syntactic.py',51),
  ('CONST_EXP -> CONST_EXP * CONST_EXP','CONST_EXP',3,'p_const_exp','syntactic.py',52),
  ('CONST_EXP -> CONST_EXP / CONST_EXP','CONST_EXP',3,'p_const_exp','syntactic.py',53),
  ('TYPE_DEF -> TYPE_DECLARATION TYPE_DEF','TYPE_DEF',2,'p_type_def','syntactic.py',62),
  ('TYPE_DEF -> <empty>','TYPE_DEF',0,'p_type_def','syntactic.py',63),
  ('TYPE_DECLARATION -> TYPE ID = DATA_TYPE ;','TYPE_DECLARATION',5,'p_type_declaration','syntactic.py',70),
  ('DATA_TYPE -> INTEGER','DATA_TYPE',1,'p_data_type','syntactic.py',74),
  ('DATA_TYPE -> REAL','DATA_TYPE',1,'p_data_type','syntactic.py',75),
  ('DATA_TYPE -> CHAR','DATA_TYPE',1,'p_data_type','syntactic.py',76),
  ('DATA_TYPE -> BOOLEAN','DATA_TYPE',1,'p_data_type','syntactic.py',77),
  ('DATA_TYPE -> ARRAY [ NUMBER ] OF DATA_TYPE','DATA_TYPE',6,'p_data_type','syntactic.py',78),
  ('DATA_TYPE -> RECORD FIELDS END','DATA_TYPE',3,'p_data_type','syntactic.py',79),
  ('DATA_TYPE -> ID','DATA_TYPE',1,'p_data_type','syntactic.py',80),
  ('VAR_DEF -> VARIABLE VAR_DEF','VAR_DEF',2,'p_var_def','syntactic.py',91),
  ('VAR_DEF -> <empty>','VAR_DEF',0,'p_var_def','syntactic.py',92),
  ('VARIABLE -> VAR ID_LIST : DATA_TYPE ;','VARIABLE',5,'p_variable','syntactic.py',99),
  ('ID_LIST -> ID','ID_LIST',1,'p_id_list','syntactic.py',103),
  ('ID_LIST -> ID_LIST , ID','ID_LIST',3,'p_id_list','syntactic.py',104),
  ('FIELDS -> FIELD FIELD_LIST','FIELDS',2,'p_fields','syntactic.py',111),
  ('FIELD -> ID : DATA_TYPE','FIELD',3,'p_field','syntactic.py',115),
  ('FIELD_LIST -> ; FIELD FIELD_LIST','FIELD_LIST',3,'p_field_list','syntactic.py',119),
  ('FIELD_LIST -> <empty>','FIELD_LIST',0,'p_field_list','syntactic.py',120),
  ('COMMAND_LIST -> COMMAND','COMMAND_LIST',1,'p_command_list','syntactic.py',127),
  ('COMMAND_LIST -> COMMAND_LIST ; COMMAND','COMMAND_LIST',3,'p_command_list','syntactic.py',128),
  ('COMMAND -> ID ASSIGNMENT EXP','COMMAND',3,'p_command','syntactic.py',135),
  ('COMMAND -> ID ASSIGNMENT FUNCTION_CALL','COMMAND',3,'p_command','syntactic.py',136),
  ('COMMAND -> IF ( COM_EXP ) THEN COMMAND','COMMAND',6,'p_command','syntactic.py',137),
  ('COMMAND -> IF ( COM_EXP ) THEN COMMAND ELSE COMMAND','COMMAND',8,'p_command','syntactic.py',138),
  ('COMMAND -> WHILE ( COM_EXP ) DO COMMAND','COMMAND',6,'p_command','syntactic.py',139),
  ('COMMAND -> BEGIN COMMAND_LIST END','COMMAND',3,'p_command','syntactic.py',140),
  ('FUNCTION_CALL -> ID ( PARAM_LIST )','FUNCTION_CALL',4,'p_function_call','syntactic.py',154),
  ('PARAM_LIST -> EXP','PARAM_LIST',1,'p_param_list','syntactic.py',158),
  ('PARAM_LIST -> PARAM_LIST , EXP','PARAM_LIST',3,'p_param_list','syntactic.py',159),
  ('PARAM_LIST -> <empty>','PARAM_LIST',0,'p_param_list','syntactic.py',160),
  ('COM_EXP -> EXP COMP_OP EXP','COM_EXP',3,'p_com_exp','syntactic.py',169),
  ('COM_EXP -> COM_EXP LOGIC_OP_OR COM_EXP','COM_EXP',3,'p_com_exp','syntactic.py',170),
  ('COM_EXP -> COM_EXP LOGIC_OP_AND COM_EXP','COM_EXP',3,'p_com_exp','syntactic.py',171),
  ('EXP -> EXP + EXP','EXP',3,'p_exp','syntactic.py',179),
  ('EXP -> EXP - EXP','EXP',3,'p_exp','syntactic.py',180),
  ('EXP -> EXP * EXP','EXP',3,'p_exp','syntactic.py',181),
  ('EXP -> EXP / EXP','EXP',3,'p_exp','syntactic.py',182),
  ('EXP -> ( EXP )','EXP',3,'p_exp','syntactic.py',183),
  ('EXP -> ID','EXP',1,'p_exp','syntactic.py',184),
  ('EXP -> NUMBER','EXP',1,'p_exp','syntactic.py',185),
  ('EXP -> TRUE','EXP',1,'p_exp','syntactic.py',186),
  ('EXP -> FALSE','EXP',1,'p_exp','syntactic.py',187),
]
