from flask import Flask, request, render_template
from WordleSolver import WordleSolver

app = Flask(__name__,
            static_url_path='',
            static_folder='../static',
            template_folder='../templates')


@app.get('/')
def index():
    if not request.is_json:
        return render_template('index.html')
    data = request.get_json()
    
    try:
        placed_letters = data['green']
        unplaced_letters = data['yellow']
        blocked_letter = data['grey']
        solver = WordleSolver(placed_letters, unplaced_letters, blocked_letter)
        words = solver.solve()
        return words

    except Exception as e:
        return 'json lack the supporting data', 400    

if __name__ == '__main__':
    app.run()