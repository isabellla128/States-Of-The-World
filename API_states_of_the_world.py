from connect_to_mongodb import connect_to_MongoDB
from flask import Flask, jsonify, request

states_of_the_world_collection = connect_to_MongoDB()

app = Flask(__name__)
@app.route('/top-10-countries-population')
def get_top_10_countries_population():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Population", -1).limit(10)
    list_to_return = []
    for line in document_returned:
        #print(x)
        list_to_return.append((line.get("Country"), line.get("Population")))
    return list_to_return



