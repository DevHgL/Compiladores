import sys
from lexic import analyze_lexical
from syntactic import SyntacticAnalyzer
from semantic import SemanticAnalyzer
from intermediate import IntermediateCodeGenerator

def main(file_path):
    try:
        with open(file_path, 'r') as source_file:
            source_code = source_file.read()

        print("Iniciando análise léxica...")
        tokens = analyze_lexical(source_code)
        print("Tokens:", tokens)

        print("\nIniciando análise sintática...")
        parser = SyntacticAnalyzer()
        syntax_tree = parser.parser.parse(source_code)  # Passe o código fonte diretamente
        print("Árvore Sintática:", syntax_tree)

        print("\nIniciando análise semântica...")
        semantic_analyzer = SemanticAnalyzer()
        semantic_analyzer.analyze(syntax_tree)
        print("Análise semântica concluída!")

        print("\nIniciando geração de código intermediário...")
        intermediate_generator = IntermediateCodeGenerator()
        intermediate_code = intermediate_generator.generate(syntax_tree)
        print("Código Intermediário:", intermediate_code)

    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_path}' não encontrado.")
    except Exception as e:
        print(f"Erro durante o processamento: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <caminho_do_arquivo>")
    else:
        main(sys.argv[1])
