from ting_file_management.queue import Queue


def search_word(word: str, instance: Queue, include_content: bool = False):
    data = []
    for index in range(len(instance)):
        file = instance.search(index)
        if any(word in line.lower() for line in file["linhas_do_arquivo"]):
            result = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": [
                    {"linha": i + 1, "conteudo": line}
                    if include_content
                    else {"linha": i + 1}
                    for i, line in enumerate(file["linhas_do_arquivo"])
                    if word in line.lower()
                ],
            }
            data.append(result)
    return data


def exists_word(word, instance):
    return search_word(word, instance, include_content=False)


def search_by_word(word, instance):
    return search_word(word, instance, include_content=True)
