from analisador_lexico import analyze_file as lex_analyze, lexer
from analisador_sintatico import parser
from InquirerPy import prompt

# Perguntas do Menu com InquirerPy
menu_opcoes = [
    {
        "type": "list",
        "message": "Selecione a opção desejada:",
        "choices": [
            "1. Executar analisador léxico",
            "2. Executar analisador sintático",
            "3. Executar casos de teste",
            "4. Sair"
        ],
        "name": "opcao",
    }
]

def rodar_testes():
    testes = {
        "teste1.sp": "begin a := 5; end.",
        "teste2.sp": "begin if a < 5 then b := 10; else c := 15; end.",
        "teste3.sp": """
        const x = 10;
        var arr : array [5] of integer;
        begin 
            for i := 0 to 4 do arr[i] := i * x; 
        end.
        """
    }
    for nome, codigo in testes.items():
        print(f"\nExecutando teste: {nome}")
        try:
            lexer.input(codigo)  # Inicializa o lexer com o código
            parser.parse(codigo)  # Faz a análise sintática
            print(f"Teste {nome} concluído com sucesso!")
        except Exception as e:
            print(f"Erro no teste {nome}: {e}")

def main():
    while True:
        resposta = prompt(menu_opcoes)  # Exibe o menu
        opcao = resposta['opcao']

        if opcao.startswith("1"):
            filename = input("Digite o nome do arquivo a ser analisado (ex: exemplo.sp): ")
            output_filename = input("Digite o nome do arquivo de saída (ou pressione Enter para exibir no console): ")
            if not output_filename.strip():
                output_filename = None
            try:
                lex_analyze(filename, output_filename)
            except FileNotFoundError:
                print(f"Erro: O arquivo '{filename}' não foi encontrado!")

        elif opcao.startswith("2"):
            filename = input("Digite o nome do arquivo a ser analisado sintaticamente (ex: exemplo.sp): ")
            try:
                with open(filename, 'r') as file:
                    data = file.read()
                print("Analisando sintaticamente o arquivo...")
                parser.parse(data)
                print("Análise sintática concluída com sucesso!")
            except FileNotFoundError:
                print(f"Erro: O arquivo '{filename}' não foi encontrado!")
            except Exception as e:
                print(f"Erro durante a análise sintática: {e}")

        elif opcao.startswith("3"):
            rodar_testes()

        elif opcao.startswith("4"):
            print("Encerrando o programa.")
            break

if __name__ == "__main__":
    main()
