from flask import Flask, render_template, request
import re

app = Flask(__name__)

def is_valid_url(text):
    # Expressão regular simples para URLs
    pattern = re.compile(
        r'^(https?:\/\/)?'                     # http:// ou https://
        r'([\da-z\.-]+)\.([a-z\.]{2,6})'       # domínio
        r'([\/\w \.-]*)*\/?$'                  # path opcional
    )
    return re.match(pattern, text)

def format_query(query):
    query = query.strip()

    if is_valid_url(query):
        if not query.startswith('http'):
            query = 'https://' + query
        return query
    else:
        # Redireciona para busca do Google
        return f"https://www.google.com/search?q={query.replace(' ', '+')}"

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        search_query = request.form['search']
        if search_query:
            final_link = format_query(search_query)
            results = [final_link]
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
