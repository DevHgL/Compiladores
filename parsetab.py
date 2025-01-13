
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "rightUMINUSleft+-left*/ASSIGNMENT BEGIN COMP_OP CONST_DEF DO ELSE END FALSE ID IF LOGIC_OP_AND LOGIC_OP_OR NUMBER RECORD THEN TRUE TYPE_DEF VAR_DEF WHILEPROGRAM : DECLARATIONS BLOCKDECLARATIONS : CONST_DECLARATIONS VAR_DECLARATIONS\n                        | VAR_DECLARATIONS\n                        | CONST_DECLARATIONS\n                        | emptyCONST_DECLARATIONS : CONST_DEF ID '=' NUMBER ';' CONST_DECLARATIONS\n                              | CONST_DEF ID '=' NUMBER ';'VAR_DECLARATIONS : VAR_DEF ID ':' ID ';' VAR_DECLARATIONS\n                            | VAR_DEF ID ':' ID ';'BLOCK : BEGIN COMMAND_LIST ENDCOMMAND_LIST : COMMAND ';' COMMAND_LIST\n                        | COMMAND\n                        | emptyCOMMAND : assignmentassignment : ID ASSIGNMENT EXPEXP : EXP '+' EXP\n                | EXP '-' EXP\n                | EXP '*' EXP\n                | EXP '/' EXP\n                | '-' EXP %prec UMINUS\n                | '(' EXP ')'\n                | ID\n                | NUMBERempty :"
    
_lr_action_items = {'CONST_DEF':([0,31,],[6,6,]),'VAR_DEF':([0,3,31,32,39,],[7,7,-7,7,-6,]),'BEGIN':([0,2,3,4,5,10,31,32,39,40,],[-24,9,-4,-3,-5,-2,-7,-9,-6,-8,]),'$end':([1,8,20,],[0,-1,-10,]),'ID':([6,7,9,19,21,22,28,29,33,34,35,36,],[11,12,17,24,17,26,26,26,26,26,26,26,]),'END':([9,13,14,15,16,21,25,26,27,30,37,41,42,43,44,45,],[-24,20,-12,-13,-14,-24,-11,-22,-15,-23,-20,-16,-17,-18,-19,-21,]),'=':([11,],[18,]),':':([12,],[19,]),';':([14,16,23,24,26,27,30,37,41,42,43,44,45,],[21,-14,31,32,-22,-15,-23,-20,-16,-17,-18,-19,-21,]),'ASSIGNMENT':([17,],[22,]),'NUMBER':([18,22,28,29,33,34,35,36,],[23,30,30,30,30,30,30,30,]),'-':([22,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,45,],[28,-22,34,28,28,-23,28,28,28,28,34,34,-16,-17,-18,-19,-21,]),'(':([22,28,29,33,34,35,36,],[29,29,29,29,29,29,29,]),'+':([26,27,30,37,38,41,42,43,44,45,],[-22,33,-23,33,33,-16,-17,-18,-19,-21,]),'*':([26,27,30,37,38,41,42,43,44,45,],[-22,35,-23,35,35,35,35,-18,-19,-21,]),'/':([26,27,30,37,38,41,42,43,44,45,],[-22,36,-23,36,36,36,36,-18,-19,-21,]),')':([26,30,37,38,41,42,43,44,45,],[-22,-23,-20,45,-16,-17,-18,-19,-21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'DECLARATIONS':([0,],[2,]),'CONST_DECLARATIONS':([0,31,],[3,39,]),'VAR_DECLARATIONS':([0,3,32,],[4,10,40,]),'empty':([0,9,21,],[5,15,15,]),'BLOCK':([2,],[8,]),'COMMAND_LIST':([9,21,],[13,25,]),'COMMAND':([9,21,],[14,14,]),'assignment':([9,21,],[16,16,]),'EXP':([22,28,29,33,34,35,36,],[27,37,38,41,42,43,44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> DECLARATIONS BLOCK','PROGRAM',2,'p_program','syntactic.py',15),
  ('DECLARATIONS -> CONST_DECLARATIONS VAR_DECLARATIONS','DECLARATIONS',2,'p_declarations','syntactic.py',19),
  ('DECLARATIONS -> VAR_DECLARATIONS','DECLARATIONS',1,'p_declarations','syntactic.py',20),
  ('DECLARATIONS -> CONST_DECLARATIONS','DECLARATIONS',1,'p_declarations','syntactic.py',21),
  ('DECLARATIONS -> empty','DECLARATIONS',1,'p_declarations','syntactic.py',22),
  ('CONST_DECLARATIONS -> CONST_DEF ID = NUMBER ; CONST_DECLARATIONS','CONST_DECLARATIONS',6,'p_const_declarations','syntactic.py',31),
  ('CONST_DECLARATIONS -> CONST_DEF ID = NUMBER ;','CONST_DECLARATIONS',5,'p_const_declarations','syntactic.py',32),
  ('VAR_DECLARATIONS -> VAR_DEF ID : ID ; VAR_DECLARATIONS','VAR_DECLARATIONS',6,'p_var_declarations','syntactic.py',39),
  ('VAR_DECLARATIONS -> VAR_DEF ID : ID ;','VAR_DECLARATIONS',5,'p_var_declarations','syntactic.py',40),
  ('BLOCK -> BEGIN COMMAND_LIST END','BLOCK',3,'p_block','syntactic.py',47),
  ('COMMAND_LIST -> COMMAND ; COMMAND_LIST','COMMAND_LIST',3,'p_command_list','syntactic.py',51),
  ('COMMAND_LIST -> COMMAND','COMMAND_LIST',1,'p_command_list','syntactic.py',52),
  ('COMMAND_LIST -> empty','COMMAND_LIST',1,'p_command_list','syntactic.py',53),
  ('COMMAND -> assignment','COMMAND',1,'p_command','syntactic.py',62),
  ('assignment -> ID ASSIGNMENT EXP','assignment',3,'p_assignment','syntactic.py',66),
  ('EXP -> EXP + EXP','EXP',3,'p_exp','syntactic.py',70),
  ('EXP -> EXP - EXP','EXP',3,'p_exp','syntactic.py',71),
  ('EXP -> EXP * EXP','EXP',3,'p_exp','syntactic.py',72),
  ('EXP -> EXP / EXP','EXP',3,'p_exp','syntactic.py',73),
  ('EXP -> - EXP','EXP',2,'p_exp','syntactic.py',74),
  ('EXP -> ( EXP )','EXP',3,'p_exp','syntactic.py',75),
  ('EXP -> ID','EXP',1,'p_exp','syntactic.py',76),
  ('EXP -> NUMBER','EXP',1,'p_exp','syntactic.py',77),
  ('empty -> <empty>','empty',0,'p_empty','syntactic.py',86),
]
