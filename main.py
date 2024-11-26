from analisador_lexico import analyze_file, lexer
from analisador_sintatico import parser
from InquirerPy import prompt

menu = [
    {"type": "list", "message": "Escolha uma opção:", "choices": ["1. Léxico", "2. Sintático", "3. Sair"], "name": "opcao"}
]

def main():
    while True:
        resposta = prompt(menu)['opcao']
        if resposta == "1. Léxico":
            filename = input("Arquivo: ")
            analyze_file(filename)
        elif resposta == "2. Sintático":
            filename = input("Arquivo: ")
            with open(filename, 'r') as file:
                data = file.read()
                parser.parse(data)
        elif resposta == "3. Sair":
            break

if __name__ == "__main__":
    main()
