# Gerador de Senhas Seguras

Um gerador simples de senhas aleatórias e seguras, feito em Python.
Utiliza fontes criptograficamente seguras (`secrets`) e permite escolher o tamanho e conjunto de caracteres.
 
## Requisitos

- Python 3.10 ou superior
- Nenhuma dependência externa (usa apenas biblioteca padrão)

## Como usar
Execute o script pelo terminal:

```
python generator.py [opções]
```

Exemplos:

Gerar uma senha com 16 caracteres:
```
python generator.py --length 16
```

Gerar uma senha com letras, números e símbolos:
```
python generator.py --charset all
```

Gerar senha com conjunto personalizado:
```
python generator.py --charset custom --custom "ABC123!@#"
```
---
