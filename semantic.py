from collections import defaultdict

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = defaultdict(dict)  # Tabela de símbolos
        self.errors = []  # Lista de erros semânticos

    def analyze(self, tree):
        """Percorre a árvore sintática e realiza análise semântica."""
        print("\nProcessando Programa...")
        self._analyze(tree)
        if self.errors:
            print("\nErros Semânticos Encontrados:")
            for error in self.errors:
                print(f"- {error}")
        else:
            print("\nAnálise Semântica Concluída Sem Erros!")  # Mensagem única

    def _analyze(self, tree):
        """Processa a árvore recursivamente."""
        if isinstance(tree, tuple):
            if tree[0] == 'program':
                self.handle_program(tree)
            elif tree[0] == 'assignment':
                self.handle_assignment(tree)
            elif tree[0] == 'bin_op':
                self.handle_bin_op(tree)
            elif tree[0] == 'unary_op':
                self.handle_unary_op(tree)
        elif isinstance(tree, list):
            for node in tree:
                self._analyze(node)

    def handle_program(self, node):
        """Processa o nó do programa."""
        _, declarations, block = node
        self._analyze(declarations)  # Processa declarações
        self._analyze(block)  # Processa o bloco principal

    def handle_assignment(self, node):
        """Valida atribuições."""
        _, var, exp = node
        if var not in self.symbol_table:
            self.errors.append(f"Erro: Variável '{var}' não foi declarada.")
        self._analyze(exp)  # Valida a expressão no lado direito

    def handle_bin_op(self, node):
        """Valida operações binárias."""
        _, op, left, right = node
        self._analyze(left)
        self._analyze(right)

    def handle_unary_op(self, node):
        """Valida operações unárias."""
        _, op, operand = node
        self._analyze(operand)

    def add_to_symbol_table(self, var, type_):
        """Adiciona uma variável ou constante à tabela de símbolos."""
        if var in self.symbol_table:
            self.errors.append(f"Erro: Variável ou constante '{var}' já foi declarada.")
        else:
            self.symbol_table[var] = {'type': type_}

    def _process_declarations(self, declarations):
        """Processa as declarações e atualiza a tabela de símbolos."""
        for decl in declarations:
            if isinstance(decl, tuple) and len(decl) == 2:
                var, type_or_value = decl
                self.add_to_symbol_table(var, type_or_value)

    def display_symbol_table(self):
        """Exibe a tabela de símbolos."""
        print("\nTabela de Símbolos:")
        for var, attributes in self.symbol_table.items():
            print(f"- {var}: {attributes}")
