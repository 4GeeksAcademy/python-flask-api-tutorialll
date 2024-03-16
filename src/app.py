from flask import Flask, jsonify, request

app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
    todos_text = jsonify(todos)
    return todos_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)



@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todo_position = todos[position]
    todos.remove(todo_position)
    print("This is the position to delete:", position)
    return jsonify(todos)















# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)