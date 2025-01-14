class IntermediateCodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0

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
            elif tree[0] == 'call':
                return self.handle_function_call(tree)
            elif tree[0] == 'field_access':
                return self.handle_field_access(tree)
            elif tree[0] == 'if':
                self.handle_if(tree)
            elif tree[0] == 'while':
                self.handle_while(tree)
            elif len(tree) == 2 and isinstance(tree[1], (int, str, tuple)):  # Ignorar declarações
                return None
            else:
                raise ValueError(f"Nó desconhecido na árvore: {tree}")
        elif isinstance(tree, str):  # Identificadores (variáveis)
            return tree
        elif isinstance(tree, (int, float)):  # Números
            return str(tree)
        elif isinstance(tree, list):  # Processa listas de comandos ou declarações
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
        left_result = self.generate(left)
        right_result = self.generate(right)
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

    def handle_function_call(self, node):
        """Gera código intermediário para chamadas de função."""
        _, func_name, args = node
        arg_results = [self.generate(arg) for arg in args if arg is not None]
        temp_var = self.new_temp()
        self.code.append(f"{temp_var} := call {func_name}({', '.join(arg_results)})")
        return temp_var

    def handle_field_access(self, node):
        """Gera código intermediário para acesso a campos de registros."""
        _, var, field = node
        return f"{var}.{field}"

    def handle_if(self, node):
        """Gera código intermediário para estruturas condicionais."""
        _, condition, block = node
        condition_result = self.generate(condition)
        label_else = self.new_label()
        label_end = self.new_label()
        self.code.append(f"if not {condition_result} goto {label_else}")
        self.generate(block)  # Código dentro do bloco `if`
        self.code.append(f"goto {label_end}")
        self.code.append(f"{label_else}:")  # Marca o início do bloco else
        self.code.append(f"{label_end}:")  # Marca o fim do bloco

    def handle_while(self, node):
        """Gera código intermediário para laços."""
        _, condition, block = node
        label_start = self.new_label()
        label_end = self.new_label()
        self.code.append(f"{label_start}:")  # Marca o início do laço
        condition_result = self.generate(condition)
        self.code.append(f"if not {condition_result} goto {label_end}")
        self.generate(block)  # Código dentro do laço
        self.code.append(f"goto {label_start}")
        self.code.append(f"{label_end}:")  # Marca o fim do laço

    def new_temp(self):
        """Gera uma nova variável temporária."""
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        """Gera um novo rótulo para controle de fluxo."""
        self.label_count += 1
        return f"L{self.label_count}"
