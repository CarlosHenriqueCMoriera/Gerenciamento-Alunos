# app.py
from flask import Flask, render_template, request
from app import carregar_alunos, cadastrar_aluno

app = Flask(__name__)

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
            resultado = f"{nome}, média: {media:.2f}. Status: {status}"

        except Exception as e:
            resultado = f"Erro: {e}"

    return render_template("index.html", resultado=resultado, alunos=alunos)

if __name__ == "__main__":
    app.run(debug=True)
