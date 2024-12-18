###########################################################################################
#                             Arquivo Principal - Analyzer.py                             #
#                                                                                         #
#         Executa Análise Léxica, Sintática e Semântica e imprime os passos.               #
###########################################################################################

import sys
from lexic import lexer, analyze_and_save
from syntactic import parser, save_syntax_tree_to_file
from semantic import SemanticAnalyzer

def main(input_file):
    try:
        print("\n### Etapa 1: Análise Léxica ###")
        lex_output_file = "Lexical-Output.txt"
        analyze_and_save(input_file, lex_output_file)
        
        print("\n### Etapa 2: Análise Sintática ###")
        with open(input_file, 'r') as file:
            data = file.read()
        
        lexer.lineno = 1  # Reiniciar o contador de linhas
        syntax_tree = parser.parse(data)
        save_syntax_tree_to_file(syntax_tree)
        print(f"\nÁrvore sintática: {syntax_tree}")
        
        print("\n### Etapa 3: Análise Semântica ###")
        analyzer = SemanticAnalyzer()
        analyzer.analyze(syntax_tree)
        print("Análise semântica concluída com sucesso.")

    except Exception as e:
        print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python Analyzer.py <arquivo_entrada>")
    else:
        main(sys.argv[1])
