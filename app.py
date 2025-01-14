from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    if height and weight:
        bmi_value = calculate_bmi(height, weight)
        return jsonify({'BMI': round(bmi_value, 2)}), 200
    return jsonify({'error': 'Invalid input'}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    age = data.get('age')
    gender = data.get('gender')
    if height and weight and age and gender:
        bmr_value = calculate_bmr(height, weight, age, gender)
        return jsonify({'BMR': round(bmr_value, 2)}), 200
    return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
