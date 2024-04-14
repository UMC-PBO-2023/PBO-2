from flask import Flask, render_template, request

app = Flask(__name__)
    
@app.route('/')
def index():

    return '<h1 style="font-family: sans-serif; text-align: center">Nama : Nana Handre Saputra</h1>'

@app.route('/template')
def template():
    return render_template('template.html')

@app.route('/hello')
def hello():
    nim = request.args.get('nim')
    return render_template('hello.html', nim=nim)


if __name__ == '__main__':
    app.run(debug=True)