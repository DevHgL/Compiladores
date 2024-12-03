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
            print(f"Analisando nó: {node_type} na linha {line}")
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
        # Processa o nó de programa dinamicamente
        program_type = node[0]
        content = node[1:]  # Todo o resto do nó
        print(f"Analisando programa: {program_type}")
        for element in content:
            self.analyze(element)

    def handle_declarations(self, node):
        declarations_type = node[0]
        content = node[1:]  # Captura o restante dinamicamente
        print(f"Analisando declarações: {declarations_type}")
        for element in content:
            self.analyze(element)

    def handle_block(self, node):
        block_type = node[0]
        content = node[1:]  # Captura os elementos do bloco dinamicamente
        print(f"Analisando bloco: {block_type}")
        for element in content:
            self.analyze(element)

    def handle_variable(self, node, line):
        if len(node) < 2:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada na declaração de variável: {node}")
        variable_type = node[0]
        content = node[1:]
        print(f"Analisando variável: {variable_type}")
        for field in content:
            self.symbol_table.add_symbol(field[0], field[1], "variable", line)

    def handle_constant(self, node, line):
        if len(node) < 3:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada na declaração de constante: {node}")
        constant_type = node[0]
        name = node[1]
        value = node[2]
        print(f"Analisando constante: {name} = {value}")
        self.symbol_table.add_symbol(name, type(value).__name__, "constant", line)

    def handle_assignment(self, node, line):
        if len(node) < 3:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada na atribuição: {node}")
        assignment_type = node[0]
        var = node[1]
        expr = node[2]
        print(f"Analisando atribuição: {var} := {expr} na linha {line}")
        var_info = self.symbol_table.lookup(var, line)
        if var_info['kind'] != 'variable':
            raise Exception(f"Erro na linha {line}: '{var}' não é uma variável.")
        expr_type = self.get_expression_type(expr, line)
        if var_info['type'] != expr_type:
            raise Exception(f"Erro na linha {line}: Tipos incompatíveis. '{var}' é do tipo '{var_info['type']}' e não pode receber '{expr_type}'.")

    def handle_procedure(self, node, line):
        if len(node) < 4:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada no procedimento: {node}")
        procedure_type = node[0]
        name = node[1]
        params = node[2]
        block = node[3]
        print(f"Analisando procedimento: {name}")
        self.symbol_table.add_symbol(name, "procedure", "procedure", line)
        self.symbol_table.enter_scope(line)
        self.analyze(params)
        self.analyze(block)
        self.symbol_table.exit_scope(line)

    def get_expression_type(self, expr, line):
        if isinstance(expr, tuple):
            if expr[0] in ('math_op', 'logic_op'):
                left_type = self.get_expression_type(expr[1], line)
                right_type = self.get_expression_type(expr[2], line)
                if left_type != right_type:
                    raise Exception(f"Erro na linha {line}: Tipos incompatíveis na operação. '{left_type}' e '{right_type}' não podem ser combinados.")
                return left_type
        elif isinstance(expr, (int, float)):
            return "integer" if isinstance(expr, int) else "real"
        elif isinstance(expr, str):
            return "char" if len(expr) == 1 else "string"
        else:
            var_info = self.symbol_table.lookup(expr, line)
            return var_info['type']

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
