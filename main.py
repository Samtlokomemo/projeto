from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota inicial
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Rota para visualizar algoritmos
@app.route('/algorithms', methods=['GET'])
def get_algorithms():
    # Esta rota retornará os algoritmos disponíveis
    algorithms = ["BST", "AVL", "B-Tree", "Fibonacci Tree", "Perfect Hashing", "Universal Hashing", "Skip List"]
    return jsonify(algorithms)

if __name__ == '__main__':
    app.run(debug=True)
