class IntermediateCodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_count = 0

    def generate(self, tree):
        """Percorre a árvore sintática e gera código intermediário."""
        if isinstance(tree, tuple):
            if tree[0] == 'program':
                self.handle_program(tree)
            elif tree[0] == 'block':
                self.handle_block(tree)
            elif tree[0] == 'assignment':
                self.handle_assignment(tree)
            elif tree[0] == 'bin_op':
                return self.handle_bin_op(tree)
            elif tree[0] == 'unary_op':
                return self.handle_unary_op(tree)
            elif isinstance(tree[0], str):  # Declarações simples
                return None  # Ignorar declarações no código intermediário
            else:
                raise ValueError(f"Nó desconhecido na árvore: {tree}")
        elif isinstance(tree, str):  # Identificadores (variáveis)
            return tree
        elif isinstance(tree, (int, float)):  # Números
            return str(tree)
        elif isinstance(tree, list):  # Processa listas de comandos
            for item in tree:
                if item is not None:
                    self.generate(item)
        return self.code

    def handle_program(self, node):
        _, declarations, block = node
        if declarations:
            self.generate(declarations)  # Processa declarações
        self.generate(block)

    def handle_block(self, node):
        _, commands = node
        self.generate(commands)

    def handle_assignment(self, node):
        _, var, exp = node
        result = self.generate(exp)
        self.code.append(f"{var} := {result}")

    def handle_bin_op(self, node):
        """Gera código intermediário para operações binárias."""
        _, op, left, right = node
        left_result = self.generate(left)  # Gera o operando esquerdo
        right_result = self.generate(right)  # Gera o operando direito
        temp_var = self.new_temp()
        self.code.append(f"{temp_var} := {left_result} {op} {right_result}")
        return temp_var

    def handle_unary_op(self, node):
        """Gera código intermediário para operações unárias."""
        _, op, operand = node
        operand_result = self.generate(operand)
        temp_var = self.new_temp()
        self.code.append(f"{temp_var} := {op} {operand_result}")
        return temp_var

    def new_temp(self):
        """Gera uma nova variável temporária."""
        self.temp_count += 1
        return f"t{self.temp_count}"
