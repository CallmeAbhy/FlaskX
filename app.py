from flask import Flask, jsonify
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['college']  # Use the name of your database ('college')
collection = db['students']  # Use the name of your collection ('students')


def get_data_from_mongodb():
    cursor = collection.find()
    data = []
    for document in cursor:
        document['_id'] = str(document['_id'])
        data.append(document)
    return data




# API endpoint to retrieve all data
@app.route('/api/data', methods=['GET'])
def get_all_data():
    data = get_data_from_mongodb()
    return jsonify(data)

# Example of filtering API endpoint
@app.route('/api/data/<topic>', methods=['GET'])
def filter_by_topic(topic):
    # Filter data by topic
    filtered_data = list(collection.find({'topic': topic}))
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
