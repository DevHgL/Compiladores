# Trabalho de Compiladores

## Analisador Sintático
Como Funciona?
Estrutura: 
graph TD
    PROGRAM[Program] --> DECLARATIONS
    PROGRAM --> BLOCK

    DECLARATIONS --> CONST_DEF[Constant Definitions]
    DECLARATIONS --> TYPE_DEF[Type Definitions]
    DECLARATIONS --> VAR_DEF[Variable Definitions]
    DECLARATIONS --> ROUTINE_DEF[Routine Definitions]

    BLOCK --> BEGIN
    BLOCK --> COMMANDS[Commands]
    BLOCK --> END

    COMMANDS --> COMMAND
    COMMAND --> ASSIGN[Assignment]
    COMMAND --> WHILE[While Loop]
    COMMAND --> IF[If Statement]
    COMMAND --> FOR[For Loop]
    COMMAND --> IO[Input/Output]

    ROUTINE_DEF --> FUNCTION
    ROUTINE_DEF --> PROCEDURE

    TYPE_DEF --> SIMPLE[Simple Types]
    TYPE_DEF --> COMPLEX[Complex Types]

    SIMPLE --> INTEGER
    SIMPLE --> REAL
    SIMPLE --> CHAR
    SIMPLE --> BOOLEAN

    COMPLEX --> ARRAY
    COMPLEX --> RECORD

    subgraph "Expressions"
        EXP[Expression] --> MATH[Math Expression]
        EXP --> LOGIC[Logic Expression]
        EXP --> COMP[Comparison Expression]
    end

