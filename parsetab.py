
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND ARRAY ASSIGNMENT BEGIN BOOLEAN CHAR COMPARATOR CONST DO ELSE END FALSE FOR FUNCTION ID IF INTEGER NUMBER OF OR PROCEDURE READ REAL RECORD STRING THEN TO TRUE TYPE VAR WHILE WRITEPROGRAM : DECLARATIONS BLOCKBLOCK : BEGIN COMMAND COMMAND_LIST ENDDECLARATIONS : CONST_DEF TYPE_DEF VAR_DEF ROUTINE_DEFCONST_DEF : CONSTANT CONST_DEF\n                 | TYPE_DEF : TYPE_DECLARATION TYPE_DEF\n                | VAR_DEF : VARIABLE VAR_DEF\n               | ROUTINE_DEF : ROUTINE ROUTINE_DEF\n                   | CONSTANT : CONST ID '=' CONST_VALUE ';'CONST_VALUE : STRING\n                   | CONST_EXPTYPE_DECLARATION : TYPE ID '=' DATA_TYPE ';'VARIABLE : VAR FIELD ';'ID_LIST : ',' ID ID_LIST\n               | FIELDS : FIELD FIELD_LISTFIELD : ID ID_LIST ':' DATA_TYPEFIELD_LIST : ';' FIELD FIELD_LIST\n                  | DATA_TYPE : INTEGER\n                | REAL\n                | CHAR\n                | BOOLEAN\n                | ARRAY '[' NUMBER ']' OF DATA_TYPE\n                | RECORD FIELDS END\n                | IDROUTINE : FUNCTION ID ROUTINE_PARAM ':' DATA_TYPE ROUTINE_BLOCK\n               | PROCEDURE ID ROUTINE_PARAM ROUTINE_BLOCKROUTINE_PARAM : '(' FIELDS ')'\n                     | ROUTINE_BLOCK : VAR_DEF BLOCKCOMMAND_LIST : ';' COMMAND COMMAND_LIST\n                    | COMMAND_BLOCK : BLOCK\n                    | COMMANDCOMMAND : ID NAME ASSIGN_EXPRESSION\n               | WHILE COM_EXP DO COMMAND_BLOCK\n               | IF COM_EXP THEN COMMAND_BLOCK ELSE_ALTERNATIVE\n               | FOR FOR_COMMAND DO COMMAND_BLOCK\n               | WRITE CONST_VALUE\n               | READ ID NAMEASSIGN_EXPRESSION : ASSIGNMENT EXPFOR_COMMAND : ID ASSIGNMENT_STMT TO PARAMETERELSE_ALTERNATIVE : ELSE COMMAND_BLOCK\n                       | ASSIGNMENT_STMT : ASSIGNMENT EXPPARAM_LIST : PARAMETER ',' PARAM_LIST\n                  | PARAMETER\n                  | EXP : PARAMETER\n           | EXP '+' EXP\n           | EXP '-' EXP\n           | '(' EXP ')'\n           | EXP '*' EXP\n           | EXP '/' EXPEXP_L1 : MATH_OP EXP\n              | LOGIC_PARAM LOGIC_EXP\n              | LOGIC_EXP : LOGIC_OP EXP\n                 | LOGIC_PARAM : COMP_OP PARAMETER\n                   | EXP_L2 : MATH_OP EXP ')'\n              | LOGIC_PARAM LOGIC_OP EXP ')'CONST_EXP : PARAMETER CONST_EXP_L\n                 | '(' PARAMETER MATH_OP CONST_EXP ')'CONST_EXP_L : MATH_OP CONST_EXP\n                   | COM_EXP : PARAMETER LOGIC_PARAM COM_EXP_L\n               | '(' PARAMETER LOGIC_PARAM LOGIC_OP COM_EXP ')'COM_EXP_L : LOGIC_OP COM_EXP\n                 | PARAMETER : ID NAME\n                | NUMBER\n                | FALSE\n                | TRUELOGIC_OP : AND\n                | ORCOMP_OP : '>'\n               | '<'\n               | COMPARATORMATH_OP : '+'\n               | '-'\n               | '*'\n               | '/'NAME : '.' ID NAME\n           | '[' PARAMETER ']'\n           | '(' PARAM_LIST ')'\n           | "
    
_lr_action_items = {'TYPE':([0,3,4,9,11,99,128,],[-5,10,-5,10,-4,-12,-15,]),'VAR':([0,3,4,8,9,11,21,23,87,88,91,93,94,95,96,99,125,128,151,162,163,171,],[-5,-7,-5,22,-7,-4,22,-6,-33,-16,-29,-23,-24,-25,-26,-12,22,-15,-28,22,-32,-27,]),'FUNCTION':([0,3,4,8,9,11,20,21,23,49,52,57,88,99,128,146,164,168,],[-5,-7,-5,-9,-7,-4,50,-9,-6,50,-8,-2,-16,-12,-15,-31,-34,-30,]),'PROCEDURE':([0,3,4,8,9,11,20,21,23,49,52,57,88,99,128,146,164,168,],[-5,-7,-5,-9,-7,-4,51,-9,-6,51,-8,-2,-16,-12,-15,-31,-34,-30,]),'BEGIN':([0,2,3,4,8,9,11,20,21,23,48,49,52,57,65,73,74,85,87,88,91,93,94,95,96,99,125,128,141,146,147,151,162,163,164,168,171,],[-5,7,-7,-5,-9,-7,-4,-11,-9,-6,-3,-11,-8,-2,7,7,7,-10,-33,-16,-29,-23,-24,-25,-26,-12,-9,-15,7,-31,7,-28,-9,-32,-34,-30,-27,]),'CONST':([0,4,99,],[5,5,-12,]),'$end':([1,6,57,],[0,-1,-2,]),'ID':([5,7,10,15,16,17,18,19,22,25,27,29,30,31,34,46,50,51,55,60,65,67,68,69,70,73,74,76,78,79,80,81,82,90,98,103,107,112,113,114,119,122,124,126,132,133,134,135,139,141,144,153,169,],[12,14,24,35,35,41,35,47,54,35,14,61,35,35,35,35,86,87,91,35,14,35,-82,-83,-84,14,14,35,35,-85,-86,-87,-88,127,54,35,35,35,-80,-81,35,35,54,91,35,35,35,35,35,14,91,54,91,]),'WHILE':([7,27,65,73,74,141,],[15,15,15,15,15,15,]),'IF':([7,27,65,73,74,141,],[16,16,16,16,16,16,]),'FOR':([7,27,65,73,74,141,],[17,17,17,17,17,17,]),'WRITE':([7,27,65,73,74,141,],[18,18,18,18,18,18,]),'READ':([7,27,65,73,74,141,],[19,19,19,19,19,19,]),'=':([12,24,],[25,55,]),';':([13,35,36,37,38,42,43,44,45,47,53,56,57,58,59,61,72,77,84,91,92,93,94,95,96,101,102,104,105,106,108,109,110,117,118,121,131,140,148,151,154,155,156,157,158,160,161,166,171,],[27,-92,-77,-78,-79,-43,-13,-14,-71,-92,88,99,-2,27,-39,-92,-76,-68,-44,-29,128,-23,-24,-25,-26,-45,-53,-89,-90,-91,-40,-37,-38,-48,-42,-70,153,-41,-20,-28,-54,-55,-57,-58,-56,-47,-69,153,-27,]),'END':([13,26,35,36,37,38,42,43,44,45,47,57,58,59,61,72,77,84,91,93,94,95,96,100,101,102,104,105,106,108,109,110,117,118,121,130,131,140,148,151,152,154,155,156,157,158,160,161,166,170,171,],[-36,57,-92,-77,-78,-79,-43,-13,-14,-71,-92,-2,-36,-39,-92,-76,-68,-44,-29,-23,-24,-25,-26,-35,-45,-53,-89,-90,-91,-40,-37,-38,-48,-42,-70,151,-22,-41,-20,-28,-19,-54,-55,-57,-58,-56,-47,-69,-22,-21,-27,]),'.':([14,35,47,61,],[29,29,29,29,]),'[':([14,35,47,61,97,],[30,30,30,30,129,]),'(':([14,15,16,18,25,35,47,60,61,76,78,79,80,81,82,86,87,103,112,113,114,122,132,133,134,135,139,],[31,34,34,46,46,31,31,103,31,103,46,-85,-86,-87,-88,124,124,103,34,-80,-81,46,103,103,103,103,34,]),'ASSIGNMENT':([14,28,41,61,104,105,106,],[-92,60,76,-92,-89,-90,-91,]),'NUMBER':([15,16,18,25,30,31,34,46,60,67,68,69,70,76,78,79,80,81,82,103,107,112,113,114,119,122,129,132,133,134,135,139,],[36,36,36,36,36,36,36,36,36,36,-82,-83,-84,36,36,-85,-86,-87,-88,36,36,36,-80,-81,36,36,150,36,36,36,36,36,]),'FALSE':([15,16,18,25,30,31,34,46,60,67,68,69,70,76,78,79,80,81,82,103,107,112,113,114,119,122,132,133,134,135,139,],[37,37,37,37,37,37,37,37,37,37,-82,-83,-84,37,37,-85,-86,-87,-88,37,37,37,-80,-81,37,37,37,37,37,37,37,]),'TRUE':([15,16,18,25,30,31,34,46,60,67,68,69,70,76,78,79,80,81,82,103,107,112,113,114,119,122,132,133,134,135,139,],[38,38,38,38,38,38,38,38,38,38,-82,-83,-84,38,38,-85,-86,-87,-88,38,38,38,-80,-81,38,38,38,38,38,38,38,]),'STRING':([18,25,],[43,43,]),')':([31,33,35,36,37,38,45,61,63,64,66,72,77,91,93,94,95,96,102,104,105,106,107,111,115,121,131,136,137,138,143,145,148,151,152,154,155,156,157,158,159,161,166,167,170,171,],[-52,-65,-92,-77,-78,-79,-71,-92,106,-51,-75,-76,-68,-29,-23,-24,-25,-26,-53,-89,-90,-91,-52,-72,-64,-70,-22,158,-50,-74,161,163,-20,-28,-19,-54,-55,-57,-58,-56,167,-69,-22,-73,-21,-27,]),'DO':([32,33,35,36,37,38,40,61,66,72,104,105,106,111,115,138,142,167,],[65,-65,-92,-77,-78,-79,74,-92,-75,-76,-89,-90,-91,-72,-64,-74,-46,-73,]),'AND':([33,35,36,37,38,61,66,71,72,104,105,106,115,116,],[-65,-92,-77,-78,-79,-92,113,-65,-76,-89,-90,-91,-64,113,]),'OR':([33,35,36,37,38,61,66,71,72,104,105,106,115,116,],[-65,-92,-77,-78,-79,-92,114,-65,-76,-89,-90,-91,-64,114,]),'THEN':([33,35,36,37,38,39,61,66,72,104,105,106,111,115,138,167,],[-65,-92,-77,-78,-79,73,-92,-75,-76,-89,-90,-91,-72,-64,-74,-73,]),'>':([33,35,36,37,38,61,71,72,104,105,106,],[68,-92,-77,-78,-79,-92,68,-76,-89,-90,-91,]),'<':([33,35,36,37,38,61,71,72,104,105,106,],[69,-92,-77,-78,-79,-92,69,-76,-89,-90,-91,]),'COMPARATOR':([33,35,36,37,38,61,71,72,104,105,106,],[70,-92,-77,-78,-79,-92,70,-76,-89,-90,-91,]),'+':([35,36,37,38,45,61,72,83,101,102,104,105,106,120,136,154,155,156,157,158,],[-92,-77,-78,-79,79,-92,-76,79,132,-53,-89,-90,-91,132,132,132,132,132,132,-56,]),'-':([35,36,37,38,45,61,72,83,101,102,104,105,106,120,136,154,155,156,157,158,],[-92,-77,-78,-79,80,-92,-76,80,133,-53,-89,-90,-91,133,133,133,133,133,133,-56,]),'*':([35,36,37,38,45,61,72,83,101,102,104,105,106,120,136,154,155,156,157,158,],[-92,-77,-78,-79,81,-92,-76,81,134,-53,-89,-90,-91,134,134,134,134,134,134,-56,]),'/':([35,36,37,38,45,61,72,83,101,102,104,105,106,120,136,154,155,156,157,158,],[-92,-77,-78,-79,82,-92,-76,82,135,-53,-89,-90,-91,135,135,135,135,135,135,-56,]),'ELSE':([35,36,37,38,42,43,44,45,47,57,59,61,72,77,84,101,102,104,105,106,108,109,110,117,118,121,140,154,155,156,157,158,160,161,],[-92,-77,-78,-79,-43,-13,-14,-71,-92,-2,-39,-92,-76,-68,-44,-45,-53,-89,-90,-91,-40,-37,-38,141,-42,-70,-41,-54,-55,-57,-58,-56,-47,-69,]),']':([35,36,37,38,61,62,72,104,105,106,150,],[-92,-77,-78,-79,-92,105,-76,-89,-90,-91,165,]),',':([35,36,37,38,54,61,64,72,104,105,106,127,],[-92,-77,-78,-79,90,-92,107,-76,-89,-90,-91,90,]),'TO':([35,36,37,38,61,72,75,102,104,105,106,120,154,155,156,157,158,],[-92,-77,-78,-79,-92,-76,119,-53,-89,-90,-91,-49,-54,-55,-57,-58,-56,]),':':([54,86,89,123,127,149,163,],[-18,-33,126,144,-18,-17,-32,]),'INTEGER':([55,126,144,169,],[93,93,93,93,]),'REAL':([55,126,144,169,],[94,94,94,94,]),'CHAR':([55,126,144,169,],[95,95,95,95,]),'BOOLEAN':([55,126,144,169,],[96,96,96,96,]),'ARRAY':([55,126,144,169,],[97,97,97,97,]),'RECORD':([55,126,144,169,],[98,98,98,98,]),'OF':([165,],[169,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'DECLARATIONS':([0,],[2,]),'CONST_DEF':([0,4,],[3,11,]),'CONSTANT':([0,4,],[4,4,]),'BLOCK':([2,65,73,74,141,147,],[6,109,109,109,109,164,]),'TYPE_DEF':([3,9,],[8,23,]),'TYPE_DECLARATION':([3,9,],[9,9,]),'COMMAND':([7,27,65,73,74,141,],[13,58,110,110,110,110,]),'VAR_DEF':([8,21,125,162,],[20,52,147,147,]),'VARIABLE':([8,21,125,162,],[21,21,21,21,]),'COMMAND_LIST':([13,58,],[26,100,]),'NAME':([14,35,47,61,],[28,72,84,104,]),'COM_EXP':([15,16,112,139,],[32,39,138,159,]),'PARAMETER':([15,16,18,25,30,31,34,46,60,67,76,78,103,107,112,119,122,132,133,134,135,139,],[33,33,45,45,62,64,71,83,102,115,102,45,102,64,33,142,45,102,102,102,102,33,]),'FOR_COMMAND':([17,],[40,]),'CONST_VALUE':([18,25,],[42,56,]),'CONST_EXP':([18,25,78,122,],[44,44,121,143,]),'ROUTINE_DEF':([20,49,],[48,85,]),'ROUTINE':([20,49,],[49,49,]),'FIELD':([22,98,124,153,],[53,131,131,166,]),'ASSIGN_EXPRESSION':([28,],[59,]),'PARAM_LIST':([31,107,],[63,137,]),'LOGIC_PARAM':([33,71,],[66,116,]),'COMP_OP':([33,71,],[67,67,]),'ASSIGNMENT_STMT':([41,],[75,]),'CONST_EXP_L':([45,],[77,]),'MATH_OP':([45,83,],[78,122,]),'ID_LIST':([54,127,],[89,149,]),'DATA_TYPE':([55,126,144,169,],[92,148,162,171,]),'EXP':([60,76,103,132,133,134,135,],[101,120,136,154,155,156,157,]),'COMMAND_BLOCK':([65,73,74,141,],[108,117,118,160,]),'COM_EXP_L':([66,],[111,]),'LOGIC_OP':([66,116,],[112,139,]),'ROUTINE_PARAM':([86,87,],[123,125,]),'FIELDS':([98,124,],[130,145,]),'ELSE_ALTERNATIVE':([117,],[140,]),'ROUTINE_BLOCK':([125,162,],[146,168,]),'FIELD_LIST':([131,166,],[152,170,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> DECLARATIONS BLOCK','PROGRAM',2,'p_program','syntactic.py',16),
  ('BLOCK -> BEGIN COMMAND COMMAND_LIST END','BLOCK',4,'p_block','syntactic.py',20),
  ('DECLARATIONS -> CONST_DEF TYPE_DEF VAR_DEF ROUTINE_DEF','DECLARATIONS',4,'p_declarations','syntactic.py',24),
  ('CONST_DEF -> CONSTANT CONST_DEF','CONST_DEF',2,'p_const_def','syntactic.py',28),
  ('CONST_DEF -> <empty>','CONST_DEF',0,'p_const_def','syntactic.py',29),
  ('TYPE_DEF -> TYPE_DECLARATION TYPE_DEF','TYPE_DEF',2,'p_type_def','syntactic.py',36),
  ('TYPE_DEF -> <empty>','TYPE_DEF',0,'p_type_def','syntactic.py',37),
  ('VAR_DEF -> VARIABLE VAR_DEF','VAR_DEF',2,'p_var_def','syntactic.py',43),
  ('VAR_DEF -> <empty>','VAR_DEF',0,'p_var_def','syntactic.py',44),
  ('ROUTINE_DEF -> ROUTINE ROUTINE_DEF','ROUTINE_DEF',2,'p_routine_def','syntactic.py',51),
  ('ROUTINE_DEF -> <empty>','ROUTINE_DEF',0,'p_routine_def','syntactic.py',52),
  ('CONSTANT -> CONST ID = CONST_VALUE ;','CONSTANT',5,'p_constant','syntactic.py',59),
  ('CONST_VALUE -> STRING','CONST_VALUE',1,'p_const_value','syntactic.py',63),
  ('CONST_VALUE -> CONST_EXP','CONST_VALUE',1,'p_const_value','syntactic.py',64),
  ('TYPE_DECLARATION -> TYPE ID = DATA_TYPE ;','TYPE_DECLARATION',5,'p_type_declaration','syntactic.py',68),
  ('VARIABLE -> VAR FIELD ;','VARIABLE',3,'p_variable','syntactic.py',72),
  ('ID_LIST -> , ID ID_LIST','ID_LIST',3,'p_id_list','syntactic.py',76),
  ('ID_LIST -> <empty>','ID_LIST',0,'p_id_list','syntactic.py',77),
  ('FIELDS -> FIELD FIELD_LIST','FIELDS',2,'p_fields','syntactic.py',84),
  ('FIELD -> ID ID_LIST : DATA_TYPE','FIELD',4,'p_field','syntactic.py',88),
  ('FIELD_LIST -> ; FIELD FIELD_LIST','FIELD_LIST',3,'p_field_list','syntactic.py',92),
  ('FIELD_LIST -> <empty>','FIELD_LIST',0,'p_field_list','syntactic.py',93),
  ('DATA_TYPE -> INTEGER','DATA_TYPE',1,'p_data_type','syntactic.py',100),
  ('DATA_TYPE -> REAL','DATA_TYPE',1,'p_data_type','syntactic.py',101),
  ('DATA_TYPE -> CHAR','DATA_TYPE',1,'p_data_type','syntactic.py',102),
  ('DATA_TYPE -> BOOLEAN','DATA_TYPE',1,'p_data_type','syntactic.py',103),
  ('DATA_TYPE -> ARRAY [ NUMBER ] OF DATA_TYPE','DATA_TYPE',6,'p_data_type','syntactic.py',104),
  ('DATA_TYPE -> RECORD FIELDS END','DATA_TYPE',3,'p_data_type','syntactic.py',105),
  ('DATA_TYPE -> ID','DATA_TYPE',1,'p_data_type','syntactic.py',106),
  ('ROUTINE -> FUNCTION ID ROUTINE_PARAM : DATA_TYPE ROUTINE_BLOCK','ROUTINE',6,'p_routine','syntactic.py',117),
  ('ROUTINE -> PROCEDURE ID ROUTINE_PARAM ROUTINE_BLOCK','ROUTINE',4,'p_routine','syntactic.py',118),
  ('ROUTINE_PARAM -> ( FIELDS )','ROUTINE_PARAM',3,'p_routine_param','syntactic.py',125),
  ('ROUTINE_PARAM -> <empty>','ROUTINE_PARAM',0,'p_routine_param','syntactic.py',126),
  ('ROUTINE_BLOCK -> VAR_DEF BLOCK','ROUTINE_BLOCK',2,'p_routine_block','syntactic.py',133),
  ('COMMAND_LIST -> ; COMMAND COMMAND_LIST','COMMAND_LIST',3,'p_command_list','syntactic.py',137),
  ('COMMAND_LIST -> <empty>','COMMAND_LIST',0,'p_command_list','syntactic.py',138),
  ('COMMAND_BLOCK -> BLOCK','COMMAND_BLOCK',1,'p_command_block','syntactic.py',145),
  ('COMMAND_BLOCK -> COMMAND','COMMAND_BLOCK',1,'p_command_block','syntactic.py',146),
  ('COMMAND -> ID NAME ASSIGN_EXPRESSION','COMMAND',3,'p_command','syntactic.py',149),
  ('COMMAND -> WHILE COM_EXP DO COMMAND_BLOCK','COMMAND',4,'p_command','syntactic.py',150),
  ('COMMAND -> IF COM_EXP THEN COMMAND_BLOCK ELSE_ALTERNATIVE','COMMAND',5,'p_command','syntactic.py',151),
  ('COMMAND -> FOR FOR_COMMAND DO COMMAND_BLOCK','COMMAND',4,'p_command','syntactic.py',152),
  ('COMMAND -> WRITE CONST_VALUE','COMMAND',2,'p_command','syntactic.py',153),
  ('COMMAND -> READ ID NAME','COMMAND',3,'p_command','syntactic.py',154),
  ('ASSIGN_EXPRESSION -> ASSIGNMENT EXP','ASSIGN_EXPRESSION',2,'p_assign_expression','syntactic.py',169),
  ('FOR_COMMAND -> ID ASSIGNMENT_STMT TO PARAMETER','FOR_COMMAND',4,'p_for_command','syntactic.py',173),
  ('ELSE_ALTERNATIVE -> ELSE COMMAND_BLOCK','ELSE_ALTERNATIVE',2,'p_else_alternative','syntactic.py',177),
  ('ELSE_ALTERNATIVE -> <empty>','ELSE_ALTERNATIVE',0,'p_else_alternative','syntactic.py',178),
  ('ASSIGNMENT_STMT -> ASSIGNMENT EXP','ASSIGNMENT_STMT',2,'p_assignment_statement','syntactic.py',185),
  ('PARAM_LIST -> PARAMETER , PARAM_LIST','PARAM_LIST',3,'p_param_list','syntactic.py',188),
  ('PARAM_LIST -> PARAMETER','PARAM_LIST',1,'p_param_list','syntactic.py',189),
  ('PARAM_LIST -> <empty>','PARAM_LIST',0,'p_param_list','syntactic.py',190),
  ('EXP -> PARAMETER','EXP',1,'p_exp','syntactic.py',199),
  ('EXP -> EXP + EXP','EXP',3,'p_exp','syntactic.py',200),
  ('EXP -> EXP - EXP','EXP',3,'p_exp','syntactic.py',201),
  ('EXP -> ( EXP )','EXP',3,'p_exp','syntactic.py',202),
  ('EXP -> EXP * EXP','EXP',3,'p_exp','syntactic.py',203),
  ('EXP -> EXP / EXP','EXP',3,'p_exp','syntactic.py',204),
  ('EXP_L1 -> MATH_OP EXP','EXP_L1',2,'p_exp_l1','syntactic.py',214),
  ('EXP_L1 -> LOGIC_PARAM LOGIC_EXP','EXP_L1',2,'p_exp_l1','syntactic.py',215),
  ('EXP_L1 -> <empty>','EXP_L1',0,'p_exp_l1','syntactic.py',216),
  ('LOGIC_EXP -> LOGIC_OP EXP','LOGIC_EXP',2,'p_logic_exp','syntactic.py',226),
  ('LOGIC_EXP -> <empty>','LOGIC_EXP',0,'p_logic_exp','syntactic.py',227),
  ('LOGIC_PARAM -> COMP_OP PARAMETER','LOGIC_PARAM',2,'p_logic_param','syntactic.py',234),
  ('LOGIC_PARAM -> <empty>','LOGIC_PARAM',0,'p_logic_param','syntactic.py',235),
  ('EXP_L2 -> MATH_OP EXP )','EXP_L2',3,'p_exp_l2','syntactic.py',242),
  ('EXP_L2 -> LOGIC_PARAM LOGIC_OP EXP )','EXP_L2',4,'p_exp_l2','syntactic.py',243),
  ('CONST_EXP -> PARAMETER CONST_EXP_L','CONST_EXP',2,'p_const_exp','syntactic.py',250),
  ('CONST_EXP -> ( PARAMETER MATH_OP CONST_EXP )','CONST_EXP',5,'p_const_exp','syntactic.py',251),
  ('CONST_EXP_L -> MATH_OP CONST_EXP','CONST_EXP_L',2,'p_const_exp_l','syntactic.py',258),
  ('CONST_EXP_L -> <empty>','CONST_EXP_L',0,'p_const_exp_l','syntactic.py',259),
  ('COM_EXP -> PARAMETER LOGIC_PARAM COM_EXP_L','COM_EXP',3,'p_com_exp','syntactic.py',266),
  ('COM_EXP -> ( PARAMETER LOGIC_PARAM LOGIC_OP COM_EXP )','COM_EXP',6,'p_com_exp','syntactic.py',267),
  ('COM_EXP_L -> LOGIC_OP COM_EXP','COM_EXP_L',2,'p_com_exp_l','syntactic.py',274),
  ('COM_EXP_L -> <empty>','COM_EXP_L',0,'p_com_exp_l','syntactic.py',275),
  ('PARAMETER -> ID NAME','PARAMETER',2,'p_parameter','syntactic.py',282),
  ('PARAMETER -> NUMBER','PARAMETER',1,'p_parameter','syntactic.py',283),
  ('PARAMETER -> FALSE','PARAMETER',1,'p_parameter','syntactic.py',284),
  ('PARAMETER -> TRUE','PARAMETER',1,'p_parameter','syntactic.py',285),
  ('LOGIC_OP -> AND','LOGIC_OP',1,'p_logic_op','syntactic.py',292),
  ('LOGIC_OP -> OR','LOGIC_OP',1,'p_logic_op','syntactic.py',293),
  ('COMP_OP -> >','COMP_OP',1,'p_comp_op','syntactic.py',297),
  ('COMP_OP -> <','COMP_OP',1,'p_comp_op','syntactic.py',298),
  ('COMP_OP -> COMPARATOR','COMP_OP',1,'p_comp_op','syntactic.py',299),
  ('MATH_OP -> +','MATH_OP',1,'p_math_op','syntactic.py',303),
  ('MATH_OP -> -','MATH_OP',1,'p_math_op','syntactic.py',304),
  ('MATH_OP -> *','MATH_OP',1,'p_math_op','syntactic.py',305),
  ('MATH_OP -> /','MATH_OP',1,'p_math_op','syntactic.py',306),
  ('NAME -> . ID NAME','NAME',3,'p_name','syntactic.py',310),
  ('NAME -> [ PARAMETER ]','NAME',3,'p_name','syntactic.py',311),
  ('NAME -> ( PARAM_LIST )','NAME',3,'p_name','syntactic.py',312),
  ('NAME -> <empty>','NAME',0,'p_name','syntactic.py',313),
]
