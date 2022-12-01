# Scanner-for-Tiny-Language
A terminal Program that implements the first phase of a complier which is scanning

## User guide
* make sure you have Python on your computer and run the file in your terminal using the following command
```
>py scanner.py
```
or use the executable file (.exe)

* The program starts by asking for the text file name that contains the code to be scanned, if the file is in the same directory as the code file or (.exe) just write the file name otherwise enter the full directory to your file
* The program will print on the terminal a table showing each Token value and the Token type and this table will also be generated in an output text file
* The program will then ask if you want to scan another code or it should terminate

## List of supported Tokens
|    Token Type |    Token Value |
|     :---:      |     :---:     |
| SEMICOLON     | ;    |
| IF       | if      |
| THEN       | then      |
| END       | end      |
| REPEAT       | repeat      |
| UNTIL       | until     |
| Identifier       | * x
                     * abc |
| ASSIGN       | :=      |
| READ       | read     |
| WRITE       | write     |
| LESS THAN       | <      |
| EQUAL       | =      |
| PLUS       | +      |
| MINUS       | -      |
| MULT      | *      |
| DIV       | /      |
| OPENBRACKET       | (      |
| CLOSEDBRACKET       | )      |
| NUMBER       | * 127
                 * 289 |




