from flask import Flask,request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://127.0.0.1:5500"}})


@app.route('/predict', methods=['POST'])
def prediction():
    info = request.get_json()

    bed = info['bedrooms']
    bath = info['bathrooms']
    acre_lot = info['acre']
    house_size = info['size']
    location = info['city']

    util.locations()
    prediction = util.estimator(bed,bath,acre_lot,house_size,location)

    return jsonify({'Price_estimate' : prediction})

 
if __name__ == "__main__":
    app.run(debug=True)
    
 