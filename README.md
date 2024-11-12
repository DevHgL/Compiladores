# Explicação pro Código

- p_program: Regra inicial, correspondente ao nó PGR na árvore. Define a estrutura básica do programa, começando com program ID ;.
 
- p_decl: Representa o bloco de declarações DECL, que pode conter declarações de variáveis (dvar), funções (func), ambos, ou estar vazio (empty).
 
- p_dvar e p_vars: Declarações de variáveis (dvar). p_vars representa múltiplas variáveis separadas por ponto e vírgula.
 
- p_var e p_lista_id: Definem uma variável e uma lista de identificadores (ID) separados por vírgulas. O tipo é fixo como real.
 
- p_func: Define a declaração de função (function), com um nome (ID), parâmetros, tipo de retorno (real), e bloco de comandos (bloco).
 
- p_parametros: Define os parâmetros da função, que podem ser uma lista de variáveis ou vazio.
 
- p_corpo e p_bloco: Define o corpo principal (corpo) e o bloco de uma função (bloco), ambos delimitados por BEGIN ... END.
 
- p_empty: Define o símbolo empty, usado para representar produções vazias.

- Tratamento de Erros: A função p_error lida com erros sintáticos, mostrando uma mensagem de erro e a linha onde ocorreu.