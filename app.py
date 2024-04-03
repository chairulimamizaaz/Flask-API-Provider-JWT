from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required
import pandas as pd

app = Flask(__name__)
# token = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjAyMjEwMzMzIiwibmFtZSI6IkNoYWlydWwgSW1hbSBJJ3phYXoiLCJpYXQiOjEyMDIyMTAzMzN9.wYNImonVfSREQbgkX6ir72SQlW_0cbZW-7U-bY0KMhg
app.config['JWT_SECRET_KEY'] = 'ddc03ebf69784eb7be371980375fbe65'

jwt = JWTManager(app)

data = pd.read_csv('salary.csv')

@app.route('/api/data', methods=['GET'])
@jwt_required()
def get_all_data():
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/data/<int:data_index>', methods=['GET'])
@jwt_required()
def get_data_by_index(data_index):
    try:
        row = data.iloc[data_index]
        return jsonify(row.to_dict())
    except IndexError:
        return jsonify({'error': 'Data not found'}), 404

@app.route('/REGION/<region_name>', methods=['GET'])
@jwt_required()
def get_region_data(region_name):
    filtered_data = data[data['REGION'] == region_name]
    if filtered_data.empty:
        return jsonify({'error': 'Data not found for the given region'}), 404
    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('/<int:year>', methods=['GET'])
@jwt_required()
def get_data_by_year(year):
    filtered_data = data[data['YEAR'] == year]
    if filtered_data.empty:
        return jsonify({'error': 'Data not found for the given year'}), 404
    return jsonify(filtered_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

# import requests
# response = requests.get('http://localhost:5000/protected_endpoint', headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjAyMjEwMzMzIiwibmFtZSI6IkNoYWlydWwgSW1hbSBJJ3phYXoiLCJpYXQiOjEyMDIyMTAzMzN9.wYNImonVfSREQbgkX6ir72SQlW_0cbZW-7U-bY0KMhg'})
# print(response.json())
