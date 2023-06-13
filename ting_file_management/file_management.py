import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('.txt'):
            sys.stderr.write("Formato inválido")

        with open(path_file, 'r') as file:
            lines = file.read().splitlines()
            return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
