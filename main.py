from analisador_lexico import analyze_file
from analisador_sintatico import parse_file
from InquirerPy import prompt

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
            filename = input("Arquivo: ")
            analyze_file(filename)
        elif resposta == "2. Sintático":
            filename = input("Arquivo: ")
            result = parse_file(filename)
            if result:
                print("Análise sintática concluída com sucesso! Resultados salvos em 'saida_sintatico.txt'.")
        elif resposta == "3. Sair":
            break

if __name__ == "__main__":
    main()

