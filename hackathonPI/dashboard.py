from flask import Flask, render_template

app = Flask(__name__)


status = {
    'banana': {
        'cor': 'amarela',
        'sabor': 'doce',
        'preco': 2.5,
        'origem': 'Brasil'
    },
    'maca': {
        'cor': 'vermelha',
        'sabor': 'azedo',
        'preco': 1.8,
        'origem': 'Estados Unidos'
    },
    'uva': {
        'cor': 'roxa',
        'sabor': 'doce',
        'preco': 5.0,
        'origem': 'Itália'
    },
    'laranja': {
        'cor': 'laranja',
        'sabor': 'cítrico',
        'preco': 3.0,
        'origem': 'Espanha'
    }
}

@app.route("/")
def homepage():
    return render_template("homepage.html", status=status)

if __name__ == "__main__":
    app.run(debug=True)

app.run()   