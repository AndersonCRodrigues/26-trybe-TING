from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    for index in range(len(instance)):
        data = instance.search(index)
        if data["nome_do_arquivo"] == path_file:
            return

    lines = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(data)
    print(data)


def remove(instance: Queue):
    if not len(instance):
        print("Não há elementos")
        return

    path_file = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
