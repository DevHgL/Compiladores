###########################################################################################
#                                                                                         #      
#   Author: Hugo Leonardo Melo                                                            #                 
#                                                                                         #              
#   Trabalho do Analisador Semântico                                                      #              
#                                                                                         #              
###########################################################################################

import sys
from lexic import lexer
from syntactic import parser, save_syntax_tree_to_file

class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # Pilha de escopos
        print("Inicializando a tabela de símbolos com o escopo global.")

    def add_symbol(self, name, symbol_type, kind, line):
        current_scope = self.scopes[-1]  # Pega o escopo atual
        print(f"Adicionando o símbolo: {name}, tipo: {symbol_type}, tipo de variável: {kind}, linha: {line}")
        if name in current_scope:
            raise Exception(f"Erro na linha {line}: Identificador '{name}' já foi declarado neste escopo.")
        
        current_scope[name] = {"type": symbol_type, "kind": kind, "line": line}
        print(f"Símbolo '{name}' adicionado ao escopo atual: {current_scope[name]}")

    def lookup(self, name, line):
        print(f"Buscando o símbolo '{name}' na tabela de símbolos na linha {line}.")
        for scope in reversed(self.scopes):  # Busca nos escopos de dentro para fora
            if name in scope:
                print(f"Símbolo '{name}' encontrado no escopo: {scope[name]}")
                return scope[name]
        raise Exception(f"Erro na linha {line}: Identificador '{name}' não foi declarado.")

    def enter_scope(self, line):
        print(f"Entrando em um novo escopo na linha {line}.")
        self.scopes.append({})
        print(f"Escopos após entrada: {self.scopes}")

    def exit_scope(self, line):
        print(f"Saindo do escopo na linha {line}.")
        if len(self.scopes) > 1:
            self.scopes.pop()  # Remove o escopo atual
            print(f"Escopos após saída: {self.scopes}")
        else:
            raise Exception(f"Erro na linha {line}: Tentativa de sair do escopo global.")

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, node, line=None):
        current_line = line if line is not None else lexer.lineno
        print(f"\nAnalisando nó: {node} na linha {current_line}")
        
        if isinstance(node, tuple):
            node_type = node[0]
            print(f"Tipo do nó: {node_type}")

            if node_type == 'program':
                self.handle_program(node, current_line)
            elif node_type == 'declarations':
                self.handle_declarations(node, current_line)
            elif node_type == 'block':
                self.handle_block(node, current_line)
            elif node_type == 'var_def':
                self.handle_variable(node, current_line)
            elif node_type == 'constant':
                self.handle_constant(node, current_line)
            elif node_type == 'command_assign':
                self.handle_assignment(node, current_line)
            elif node_type == 'procedure':
                self.handle_procedure(node, current_line)
        elif isinstance(node, list):
            for child in node:
                self.analyze(child, current_line)

    def handle_program(self, node, line):
        print(f"Analisando o programa na linha {line}.")
        _, declarations, block = node
        self.symbol_table.enter_scope(line)  # Entra no escopo global
        self.analyze(declarations, line)    # Analisa as declarações no escopo global
        self.analyze(block, line)           # Analisa o bloco principal
        self.symbol_table.exit_scope(line)  # Sai do escopo global

    def handle_declarations(self, node, line):
        print(f"Analisando declarações na linha {line}.")
        if len(node) < 5:
            raise Exception(f"Erro: Estrutura inesperada do nó de declarações: {node}")
        _, const_def, type_def, var_def, routine_def = node

        if const_def:
            self.analyze(const_def, line)
        if type_def:
            self.analyze(type_def, line)
        if var_def:
            self.analyze(var_def, line)
        if routine_def:
            self.analyze(routine_def, line)

    def handle_variable(self, node, line):
        print(f"\nAnalisando variáveis na linha {line}: {node}")
        
        if isinstance(node, tuple) and node[0] == 'var_def':
            _, variable_node, next_var_def = node

            if variable_node:
                self.handle_variable(variable_node, line)

            if next_var_def is not None and not (isinstance(next_var_def, tuple) and next_var_def[1] is None):
                self.handle_variable(next_var_def, line)
            else:
                print("Nenhuma próxima definição válida de variável encontrada. Ignorando.")

        elif isinstance(node, tuple) and node[0] == 'variable':
            _, field = node
            if isinstance(field, tuple) and field[0] == 'field':
                field_names = field[1]
                field_type = field[2]

                for name in field_names:
                    print(f"Adicionando variável: {name} do tipo '{field_type[1]}' na linha {line}.")
                    self.symbol_table.add_symbol(name, field_type[1], "variable", line)
        else:
            print(f"Nó inesperado em handle_variable: {node}")

    def handle_constant(self, node, line):
        print(f"\nAnalisando constantes na linha {line}: {node}")

        if isinstance(node, tuple) and node[0] == 'const_def':
            _, const_node, next_const_def = node

            if const_node:
                self.handle_constant(const_node, line)

            if next_const_def is not None and not (isinstance(next_const_def, tuple) and next_const_def[1] is None):
                self.handle_constant(next_const_def, line)
            else:
                print("Nenhuma próxima definição válida de constante encontrada. Ignorando.")

        elif isinstance(node, tuple) and node[0] == 'constant':
            _, name, value = node
            print(f"Adicionando constante: {name} = {value} na linha {line}.")
            self.symbol_table.add_symbol(name, type(value).__name__, "constant", line)
        else:
            print(f"Nó inesperado em handle_constant: {node}")

    def handle_assignment(self, node, line):
        print(f"Analisando atribuição na linha {line}: {node}")

        if len(node) < 4:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada na atribuição: {node}")

        _, var, _, expr = node
        print(f"Buscando o símbolo '{var}' na tabela de símbolos na linha {line}.")
        var_info = self.symbol_table.lookup(var, line)

        if var_info['kind'] != 'variable':
            raise Exception(f"Erro na linha {line}: '{var}' não é uma variável.")

        # Obtenha o tipo da expressão
        expr_type = self.get_expression_type(expr, line)

        if var_info['type'] != expr_type:
            raise Exception(f"Erro na linha {line}: Tipos incompatíveis. '{var}' é do tipo '{var_info['type']}' e não pode receber '{expr_type}'.")


    def handle_procedure(self, node, line):
        print(f"\nAnalisando procedimentos na linha {line}: {node}")

        if isinstance(node, tuple) and node[0] == 'routine_def':
            _, routine_node, next_routine_def = node

            if routine_node:
                self.handle_procedure(routine_node, line)

            if next_routine_def is not None and not (isinstance(next_routine_def, tuple) and next_routine_def[1] is None):
                self.handle_procedure(next_routine_def, line)
            else:
                print("Nenhuma próxima definição válida de procedimento encontrada. Ignorando.")

        elif isinstance(node, tuple) and node[0] in ('procedure', 'function'):
            _, name, params, block = node
            print(f"Adicionando procedimento: {name} na linha {line}.")
            self.symbol_table.add_symbol(name, "procedure", "procedure", line)

            self.symbol_table.enter_scope(line)
            if params:
                self.analyze(params)
            if block:
                self.analyze(block)
            self.symbol_table.exit_scope(line)
        else:
            print(f"Nó inesperado em handle_procedure: {node}")

    def handle_block(self, node, line):
        print(f"Analisando bloco na linha {line}: {node}")
        
        if len(node) < 2:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada do nó do bloco: {node}")
        
        _, main_command, additional_commands = node  # Divide o nó em comando principal e comandos adicionais
        
        self.symbol_table.enter_scope(line)  # Entra no escopo do bloco
        
        # Analisa o comando principal, se houver
        if main_command:
            print(f"Analisando comando principal do bloco: {main_command}")
            self.analyze(main_command, line)
        
        # Analisa os outros comandos, se houver
        if isinstance(additional_commands, list):
            for command in additional_commands:
                if command:
                    print(f"Analisando comando adicional no bloco: {command}")
                    self.analyze(command, line)
        else:
            print("Nenhum comando adicional encontrado no bloco.")
        
        self.symbol_table.exit_scope(line)  # Sai do escopo do bloco
        
    def get_expression_type(self, expr, line):
        print(f"Analisando tipo da expressão na linha {line}: {expr}")
        
        if isinstance(expr, tuple):
            if expr[0] == 'assign':
                _, inner_expr = expr
                return self.get_expression_type(inner_expr, line)
            
            elif expr[0] == 'exp':
                left_expr = self.get_expression_type(expr[1], line)
                if expr[2]:  # Verifica se existe uma operação adicional
                    right_expr = self.get_expression_type(expr[2], line)
                    if left_expr != right_expr:
                        raise Exception(f"Erro na linha {line}: Tipos incompatíveis na expressão.")
                return left_expr
    
            elif expr[0] == 'parameter':
                if expr[1] == 'literal':
                    return "integer" if isinstance(expr[2], int) else "real"
                elif expr[1] == 'id':
                    param_info = self.symbol_table.lookup(expr[2], line)
                    return param_info['type']
    
            elif expr[0] == 'math_op':
                if len(expr) < 4 or expr[2] is None:
                    raise Exception(f"Erro na linha {line}: Operação matemática incompleta ou lado direito ausente: {expr}")
                operator = expr[1]
                left = expr[2]
                right = expr[3] if len(expr) > 3 else None  # Trata ausência do lado direito
                left_type = self.get_expression_type(left, line)
                if right is not None:
                    right_type = self.get_expression_type(right, line)
                    if left_type != right_type:
                        raise Exception(f"Erro na linha {line}: Tipos incompatíveis para operação '{operator}'.")
                return left_type
    
        elif isinstance(expr, (int, float)):
            return "integer" if isinstance(expr, int) else "real"
    
        raise Exception(f"Erro na linha {line}: Estrutura de expressão desconhecida: {expr}")
    
def main():
    try:
        with open(sys.argv[1], 'r') as file:
            data = file.read()

        lexer.lineno = 1
        syntax_tree = parser.parse(data)

        save_syntax_tree_to_file(syntax_tree)

        analyzer = SemanticAnalyzer()
        analyzer.analyze(syntax_tree)
        print("Análise semântica concluída com sucesso.")

    except Exception as e:
        print(f"Erro durante a análise semântica: {e}")

if __name__ == "__main__":
    main()
