from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():

    return render_template('form.html')

@app.route('/status',methods=['POST'])
def status():
    name = request.form.get('name')
    dependents = request.form.get('dependents')
    education = request.form.get('education')

    print(name)
    print(dependents)
    print(education)
    return render_template('status.html')

if __name__ == '__main__':
    app.run(debug=True)
