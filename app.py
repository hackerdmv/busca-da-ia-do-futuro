from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('search')
        return render_template('index.html', query=query)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
