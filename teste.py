import subprocess

# Caminhos ajustados
lexic_output = "/mnt/data/Lexical-Output.txt"
syntactic_output = "/mnt/data/Syntactic-Output.txt"
input_file_path = 

results = {}

# Análise léxica
try:
    subprocess.run(['python', '/mnt/data/lexic.py', input_file_path, lexic_output], check=True)
    with open(lexic_output, 'r') as f:
        results['lexical'] = f.read()
except Exception as e:
    results['lexical'] = f"Erro: {e}"

# Análise sintática
try:
    subprocess.run(['python', '/mnt/data/syntactic.py', input_file_path], check=True)
    with open(syntactic_output, 'r') as f:
        results['syntactic'] = f.read()
except Exception as e:
    results['syntactic'] = f"Erro: {e}"

# Análise semântica
try:
    semantic_output = subprocess.run(['python', '/mnt/data/semantic.py', input_file_path], check=True, capture_output=True, text=True)
    results['semantic'] = semantic_output.stdout
except Exception as e:
    results['semantic'] = f"Erro: {e}"

results
