from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Strona główna"

@app.route("/o-nas")
def o_nas():
    return "Jesteśmy klasą 4 Technik Programista. Robimy sklep."

@app.route("/kontakt")
def kontakt():
    return "Napisz: sklep@example.com"

@app.route("/tajne")
def tajne():
    return "Brak dostępu", 403

if __name__ == "__main__":
    app.run(debug=True)