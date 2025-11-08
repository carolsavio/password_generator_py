# 🔐 Gerador de Senhas Seguras  
*[English](README.md)*  

Um gerador simples de senhas aleatórias e seguras, feito em Python.  
Utiliza fontes criptograficamente seguras (`secrets`) e permite escolher o tamanho e conjunto de caracteres.

## Requisitos

- Python 3.10 ou superior  
- Nenhuma dependência externa (usa apenas a biblioteca padrão)

## Como usar

Execute o script pelo terminal:

```
python generator.py [opções]
```
Exemplos

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
### Opções disponíveis de caracteres para o charset

- lower: letras minúsculas
- upper: letras maiúsculas
- alnum (padrão): letras e números
- all: letras + números + caracteres especiais