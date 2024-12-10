from flask import Flask, request, jsonify
from checking import validate_field, find_matching_template

app = Flask(__name__)

@app.route('/get_form', methods=['POST'])
def get_form():
    form_data = request.form.to_dict()

    result = find_matching_template(form_data)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)