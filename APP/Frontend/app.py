from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')

@app.route('/atencion', methods=["GET"])
def atencion_clientes():
    return render_template('atencion.html')

@app.route('/redirect_to_atencion', methods=["GET"])
def handle_redirect():
    return redirect(url_for('atencion'))

if __name__ == '__main__':
    app.run(debug=True)

