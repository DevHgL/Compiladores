from analisador_lexico import analyze_file
from analisador_sintatico import parse_file
from InquirerPy import prompt
import os

menu = [
    {
        "type": "list",
        "message": "Escolha uma opção:",
        "choices": ["1. Léxico", "2. Sintático", "3. Sair"],
        "name": "opcao"
    }
]

def main():
    while True:
        resposta = prompt(menu)['opcao']
        
        if resposta == "1. Léxico":
            filename = input("Digite o nome do arquivo para análise léxica: ")
            if os.path.isfile(filename):  # Verifica se o arquivo existe
                analyze_file(filename)
            else:
                print(f"Erro: O arquivo '{filename}' não foi encontrado!")
        
        elif resposta == "2. Sintático":
            filename = input("Digite o nome do arquivo para análise sintática: ")
            if os.path.isfile(filename):  # Verifica se o arquivo existe
                result = parse_file(filename)
                if result:
                    print("Análise sintática concluída com sucesso! Resultados salvos em 'saida_sintatico.txt'.")
                else:
                    print("Erro na análise sintática. Verifique o arquivo de entrada.")
            else:
                print(f"Erro: O arquivo '{filename}' não foi encontrado!")
        
        elif resposta == "3. Sair":
            print("Saindo...")
            break

if __name__ == "__main__":
    main()
