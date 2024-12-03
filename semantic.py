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

    def add_symbol(self, name, symbol_type, kind, line):
        current_scope = self.scopes[-1]
        if name in current_scope:
            raise Exception(f"Erro na linha {line}: Identificador '{name}' já foi declarado neste escopo.")
        current_scope[name] = {"type": symbol_type, "kind": kind, "line": line}
        print(f"Adicionado: {name} -> {current_scope[name]}")

    def lookup(self, name, line):
        for scope in reversed(self.scopes):
            if name in scope:
                print(f"Encontrado: {name} -> {scope[name]}")
                return scope[name]
        raise Exception(f"Erro na linha {line}: Identificador '{name}' não foi declarado.")

    def enter_scope(self, line):
        print(f"Entrando em um novo escopo na linha {line}.")
        self.scopes.append({})

    def exit_scope(self, line):
        if len(self.scopes) > 1:
            print(f"Saindo do escopo na linha {line}.")
            self.scopes.pop()
        else:
            raise Exception(f"Erro na linha {line}: Tentativa de sair do escopo global.")

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, node, line=0):
        if isinstance(node, tuple):
            print(f"Tipo do nó: {node[0]} - Conteúdo: {node}")
            node_type = node[0]
            if node_type == 'program':
                self.handle_program(node)
            elif node_type == 'declarations':
                self.handle_declarations(node)
            elif node_type == 'block':
                self.handle_block(node)
            elif node_type == 'variable':
                self.handle_variable(node, line)
            elif node_type == 'constant':
                self.handle_constant(node, line)
            elif node_type == 'command_assign':
                self.handle_assignment(node, line)
            elif node_type == 'procedure':
                self.handle_procedure(node, line)
        elif isinstance(node, list):
            for child in node:
                self.analyze(child, line)

    def handle_program(self, node):
        if len(node) < 3:
            raise Exception(f"Erro: Estrutura inesperada do nó do programa: {node}")
        _, declarations, block = node
        print("Analisando programa.")
        self.analyze(declarations)
        self.analyze(block)

    def handle_declarations(self, node):
        if len(node) < 5:
            raise Exception(f"Erro: Estrutura inesperada do nó de declarações: {node}")
        _, const_def, type_def, var_def, routine_def = node
        print("Analisando declarações.")
        if const_def and const_def[1] is not None:
            self.analyze(const_def)
        if type_def and type_def[1] is not None:
            self.analyze(type_def)
        if var_def:  # Processa as declarações de variáveis
            self.analyze(var_def)
        if routine_def and routine_def[1] is not None:
            self.analyze(routine_def)


    def handle_block(self, node):
        if len(node) < 2:
            raise Exception(f"Erro: Estrutura inesperada do nó do bloco: {node}")
        block_type, *commands = node
        print(f"Analisando bloco: {block_type}")
        for command in commands:
            if command:
                self.analyze(command)

    def handle_variable(self, node, line):
        if len(node) < 2:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada na declaração de variável: {node}")
        _, fields = node
        print(f"Analisando variáveis: {fields}")
        # Itera sobre os campos das variáveis
        for field in fields:
            if isinstance(field, tuple) and field[0] == 'field':
                names, var_type = field[1], field[2]
                for name in names:
                    self.symbol_table.add_symbol(name, var_type[1], "variable", line)
            else:
                raise Exception(f"Erro na linha {line}: Estrutura de campo inválida: {field}")

            print(f"Tabela de símbolos atual: {self.symbol_table.scopes}")


    def handle_constant(self, node, line):
        if len(node) < 3:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada na declaração de constante: {node}")
        _, name, value = node
        print(f"Analisando constante: {name} = {value}")
        self.symbol_table.add_symbol(name, type(value).__name__, "constant", line)

    def handle_assignment(self, node, line):
        if len(node) < 4:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada na atribuição: {node}")
        _, var, _, expr = node
        print(f"Analisando atribuição: {var} := {expr} na linha {line}")
        try:
            var_info = self.symbol_table.lookup(var, line)
        except Exception:
            raise Exception(f"Erro na linha {line}: Identificador '{var}' não foi declarado.")
        if var_info['kind'] != 'variable':
            raise Exception(f"Erro na linha {line}: '{var}' não é uma variável.")
        expr_type = self.get_expression_type(expr, line)
        if var_info['type'] != expr_type:
            raise Exception(f"Erro na linha {line}: Tipos incompatíveis. '{var}' é do tipo '{var_info['type']}' e não pode receber '{expr_type}'.")


    def handle_procedure(self, node, line):
        if len(node) < 4:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada no procedimento: {node}")
        _, name, params, block = node
        print(f"Analisando procedimento: {name}")
        self.symbol_table.add_symbol(name, "procedure", "procedure", line)
        self.symbol_table.enter_scope(line)
        self.analyze(params)
        self.analyze(block)
        self.symbol_table.exit_scope(line)

    def get_expression_type(self, expr, line):
        if isinstance(expr, tuple):
            if expr[0] == 'binary_op':
                left_type = self.get_expression_type(expr[2], line)
                right_type = self.get_expression_type(expr[3], line)
                if left_type != right_type:
                    raise Exception(f"Erro na linha {line}: Tipos incompatíveis na operação '{expr[1]}'.")
                return left_type
            elif expr[0] == 'parameter':
                param_info = self.symbol_table.lookup(expr[1], line)
                return param_info['type']
            elif expr[0] == 'value':
                return self.get_expression_type(expr[1], line)
        elif isinstance(expr, (int, float)):
            return "integer" if isinstance(expr, int) else "real"
        elif isinstance(expr, str):
            return "char" if len(expr) == 1 else "string"
        else:
            raise Exception(f"Erro na linha {line}: Estrutura de expressão desconhecida: {expr}")

def main():
    try:
        # Abre o arquivo e realiza a análise léxica e sintática
        with open(sys.argv[1], 'r') as file:
            data = file.read()

        lexer.lineno = 1
        syntax_tree = parser.parse(data)

        # Salva a árvore sintática
        save_syntax_tree_to_file(syntax_tree)

        # Realiza a análise semântica
        analyzer = SemanticAnalyzer()
        analyzer.analyze(syntax_tree)
        print("Análise semântica concluída com sucesso.")

    except Exception as e:
        print(f"Erro durante a análise semântica: {e}")

if __name__ == "__main__":
    main()
