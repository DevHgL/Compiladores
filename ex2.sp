PROGRAM TestProgram;

CONST
  MAX = 100;
  PI = 3.14;

TYPE
  Numbers = ARRAY[10] OF INTEGER;
  Person = RECORD
    age: INTEGER;
    name: CHAR;
  END;

VAR
  count: INTEGER;
  values: Numbers;
  user: Person;

BEGIN
  count := 0;
  IF count < MAX THEN
    BEGIN
      READ(count);
      WRITE(count)
    END
  ELSE
    count := MAX;
  
  WHILE count > 0 DO
    BEGIN
      count := count - 1;
      FOR i := 1 TO 10 DO
        WRITE(i)
    END
END.