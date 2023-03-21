from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/pml')
def pml():
    return render_template('pml.html')

@app.route('/brs')
def brs():
    return render_template('brs.html')

@app.route('/slc')
def slc():
    return render_template('slc.html')

@app.route('/cmpsg')
def cmpsg ():
    return render_template('cmpsg.html')

@app.route('/cmreal')
def cmreal ():
    return render_template('cmreal.html')

@app.route('/cmmanchester')
def cmmanchester ():
    return render_template('cmmanchester.html')

if __name__ == '__main__':
    app.run(debug=True)

