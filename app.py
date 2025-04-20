from flask import Flask, render_template, request, redirect, url_for
import json
import os

# Nome do arquivo onde os dados serão salvos
ARQUIVO = "alunos.json"

app = Flask(__name__)

# Função para carregar os dados salvos
def carregar_alunos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Função para salvar os dados
def salvar_alunos(lista_alunos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista_alunos, f, indent=4)

# Função para cadastrar aluno
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

# Função para limpar os dados
def limpar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([], f)  # Escreve uma lista vazia no arquivo, apagando os dados

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    alunos = carregar_alunos()

    if request.method == "POST":
        try:
            nome = request.form["name"]
            idade = int(request.form["age"])
            morada = request.form["address"]
            notas = [
                float(request.form["grade1"]),
                float(request.form["grade2"]),
                float(request.form["grade3"]),
            ]
            aluno = cadastrar_aluno(alunos, nome, idade, morada, notas)

            media = sum(notas) / 3
            status = "Approved" if media >= 10 else "Failed"
            resultado = f"{nome}, media: {media:.2f}. Status: {status}"

        except Exception as e:
            resultado = f"Erro: {e}"

    return render_template("index.html", resultado=resultado, alunos=alunos)

# Rota para limpar os dados
@app.route("/limpar", methods=["POST"])
def limpar():
    limpar_dados()  # Chama a função que apaga os dados
    return redirect(url_for('index'))  # Redireciona de volta para a página inicial

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0")

