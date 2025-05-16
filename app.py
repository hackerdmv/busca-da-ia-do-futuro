from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    query = ''
    if request.method == 'POST':
        query = request.form.get('search')
        results = [
            f"https://www.google.com/search?q={query}",
            f"https://duckduckgo.com/?q={query}",
            f"https://www.bing.com/search?q={query}"
        ]
    return render_template('index.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)