import secrets
import argparse
import string

charsets = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "alnum": string.ascii_letters + string.digits,
    "all": string.digits + string.punctuation + string.ascii_letters
}

def header(msg):
    size = 60
    print('-' * size)
    print(msg.center(60))
    print('-' * size)

def password_generator(length: int, charset_name: str = "alnum") -> str:
    charset = charsets.get(charset_name, charset_name)
    return ''.join(secrets.choice(charset)for _ in range(length)) 

def main():
    p = argparse.ArgumentParser(description= "Gerador de senhas aleatórias")
    p.add_argument("-l", "--length", type=int, default=16, help="tamanho da senha")
    p.add_argument("-c", "--charset", choices = list(charsets.keys()) + ["custom"], default="alnum", help="conjunto de caracteres para a senha")
    p.add_argument("--custom", type=str, help="caracteres customizados (use junto com --charset custom)")
    args = p.parse_args()

    if args.charset == "custom":
        if not args.custom:
            p.error("se charset --custom, informe o --custom com a string de caracteres")
        charset = args.custom
    else:
        charset = charsets[args.charset]

    pw = password_generator(args.length, charset)
    header('Your new random password')
    print()
    print(f'{pw.center(60)}')
    print()
    

if __name__ == "__main__":
    main()