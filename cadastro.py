import json
import os

ARQUIVO = "alunos.json"

def carregar_alunos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_alunos(lista_alunos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista_alunos, f, indent=4)

def cadastrar_aluno(lista_alunos, nome, idade, morada, notas):
    aluno = {
        "nome": nome,
        "idade": idade,
        "morada": morada,
        "notas": notas
    }

    lista_alunos.append(aluno)
    salvar_alunos(lista_alunos)
    return aluno
