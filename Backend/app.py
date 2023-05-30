from flask import Flask, request
from WordleSolver import WordleSolver

app = Flask(__name__)


@app.get('/')
def index():
    if not request.is_json:
        return 'unsupported format', 400
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

