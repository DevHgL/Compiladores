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
        
        # Verificando o tipo do nó e agindo de acordo
        if isinstance(node, tuple):
            node_type = node[0]
            print(f"Tipo do nó: {node_type}")

            # Chama a função de acordo com o tipo do nó
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
        
        if len(node) < 2:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada na declaração de variável: {node}")
        
        _, var_info = node  # Pega as informações da variável

        # Caso a variável seja uma lista de campos (ex.: múltiplas variáveis em uma linha)
        if isinstance(var_info, tuple):
            print(f"Desempacotando o campo de variável: {var_info}")
            if len(var_info) > 1:
                field_info = var_info[1]  # A segunda parte contém os campos de variável

                for field in field_info:
                    if isinstance(field, tuple) and field[0] == 'field':  # Verifica se é realmente um campo
                        names, var_type = field[1], field[2]
                        print(f"Adicionando variáveis: {names} do tipo '{var_type[1]}'")

                        # Adiciona as variáveis à tabela de símbolos
                        for name in names:
                            self.symbol_table.add_symbol(name, var_type[1], "variable", line)
        else:
            print(f"Definição simples de variável encontrada: {var_info}")
            names = [var_info[0]]  # Caso haja apenas uma variável
            var_type = var_info[1]  # Tipo da variável
            
            # Adiciona a variável simples à tabela de símbolos
            for name in names:
                self.symbol_table.add_symbol(name, var_type[1], "variable", line)

    def handle_constant(self, node, line):
        print(f"Analisando constante na linha {line}: {node}")
        if len(node) < 3:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada na declaração de constante: {node}")
        _, name, value = node
        self.symbol_table.add_symbol(name, type(value).__name__, "constant", line)

    def handle_assignment(self, node, line):
        print(f"Analisando atribuição na linha {line}: {node}")
        if len(node) < 4:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada na atribuição: {node}")
        _, var, _, expr = node
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
        print(f"Analisando procedimento na linha {line}: {node}")
        if len(node) < 4:
            raise Exception(f"Erro na linha {line}: Estrutura inesperada no procedimento: {node}")
        _, name, params, block = node
        self.symbol_table.add_symbol(name, "procedure", "procedure", line)
        self.symbol_table.enter_scope(line)
        if params:
            self.analyze(params)
        if block:
            self.analyze(block)
        self.symbol_table.exit_scope(line)

    def handle_block(self, node, line):
        print(f"Analisando bloco na linha {line}: {node}")
        if len(node) < 2:
            raise Exception(f"Erro: Estrutura inesperada do nó do bloco: {node}")
        block_type, *commands = node
        self.symbol_table.enter_scope(line)
        for command in commands:
            if command:
                self.analyze(command, line)
        self.symbol_table.exit_scope(line)

    def get_expression_type(self, expr, line):
        print(f"Analisando tipo da expressão na linha {line}: {expr}")
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
