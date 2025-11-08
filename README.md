# 🔐 Secure Password Generator  
*[Português - BR](README.pt-BR.md)*  

A simple generator for random and secure passwords, built with Python.  
It uses cryptographically secure sources (`secrets`) and allows you to choose the password length and character set.

## Requirements

- Python 3.10 or higher  
- No external dependencies (uses only the standard library)

## Usage

Run the script from the terminal:

```
python generator.py [options]
```
Examples:

Generate a 16-character password:
```
python generator.py --length 16
```

Generate a password with letters, numbers, and symbols:
```
python generator.py --charset all
```

Generate a password with a custom character set:
```
python generator.py --charset custom --custom "ABC123!@#"
```
---
### Available charset options

- lower: lowercase letters
- upper: uppercase letters
- alnum (default): letters and numbers
- all: letters + numbers + special characters
