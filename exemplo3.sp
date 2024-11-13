PROGRAM Exemplo;

CONST
    MAX = 100;
    MENSAGEM = 'Hello, World';

TYPE
    indice = INTEGER;
    matriz = ARRAY [1..MAX] OF INTEGER;
    registro = RECORD
        nome: CHAR;
        idade: INTEGER;
    END;

VAR
    x, y: INTEGER;
    nome: CHAR;
    valores: matriz;

PROCEDURE Saudacao(mensagem: CHAR);
BEGIN
    WRITE(mensagem);
END;

FUNCTION Soma(a, b: INTEGER): INTEGER;
BEGIN
    Soma := a + b;
END;

BEGIN
    x := 10;
    y := Soma(x, MAX);
    
    IF y > 50 THEN
    BEGIN
        Saudacao(MENSAGEM);
    END
    ELSE
    BEGIN
        WRITE('Soma é menor ou igual a 50');
    END;

    FOR x := 1 TO MAX DO
    BEGIN
        valores[x] := x * 2;
    END;
END.
