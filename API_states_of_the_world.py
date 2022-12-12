from connect_to_mongodb import connect_to_mongodb
from flask import Flask, request

states_of_the_world_collection = connect_to_mongodb()

app = Flask(__name__)


@app.route('/')
def get_countries():
    """Return all countries from database"""
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/top-countries-population', methods=['GET'])
def get_top_countries_population():
    """Return top countries according to the population"""
    args = request.args
    constitutional_form = args.get('Top')
    if constitutional_form and constitutional_form.isnumeric():
        document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Population", -1). \
            limit(int(constitutional_form))
        list_to_return = []
        for line in document_returned:
            list_to_return.append((line.get("Country"), line.get("Population")))
    else:
        document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Population", -1)
        list_to_return = []
        for line in document_returned:
            list_to_return.append((line.get("Country"), line.get("Population")))
    return list_to_return


@app.route('/top-countries-densities', methods=['GET'])
def get_top_countries_densities():
    """Return top countries according to the densities"""
    args = request.args
    constitutional_form = args.get('Top')
    if constitutional_form and constitutional_form.isnumeric():
        document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Density", -1). \
            limit(int(constitutional_form))
        list_to_return = []
        for line in document_returned:
            list_to_return.append((line.get("Country"), line.get("Density")))
    else:
        document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Density", -1)
        list_to_return = []
        for line in document_returned:
            list_to_return.append((line.get("Country"), line.get("Density")))
    return list_to_return


@app.route('/top-countries-areas', methods=['GET'])
def get_top_countries_areas():
    """Return top countries according to the areas"""
    args = request.args
    constitutional_form = args.get('Top')
    if constitutional_form and constitutional_form.isnumeric():
        document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Area", -1). \
            limit(int(constitutional_form))
        list_to_return = []
        for line in document_returned:
            list_to_return.append((line.get("Country"), line.get("Area")))
    else:
        document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Area", -1)
        list_to_return = []
        for line in document_returned:
            list_to_return.append((line.get("Country"), line.get("Area")))
    return list_to_return


@app.route('/countries-capitals')
def get_countries_capitals():
    """Return all countries and capitals from database"""
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Capital")))
    return list_to_return


@app.route('/countries-constitutional-form', methods=['GET'])
def get_constitutional_form_param():
    """Return all countries according to constitutional form"""
    args = request.args
    constitutional_form = args.get('ConstitutionalForm')
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    if constitutional_form:
        for line in document_returned:
            if len(line.get("Constitutional form")) != 0:
                if constitutional_form in line.get("Constitutional form"):
                    list_to_return.append(line.get("Country"))
    else:
        for line in document_returned:
            if len(line.get("Constitutional form")) != 0:
                list_to_return.append((line.get("Country"), line.get("Constitutional form")))
    return list_to_return


@app.route('/countries-neighbours')
def get_countries_neighbours():
    """Return all countries and neighbours from database"""
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Neighbours")))
    return list_to_return


@app.route('/countries-languages', methods=['GET'])
def get_countries_languages_param():
    """Return all countries and languages from database"""
    args = request.args
    language = args.get('Language')
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    if language:
        for line in document_returned:
            if len(line.get("Languages")) != 0:
                if language in line.get("Languages"):
                    list_to_return.append(line.get("Country"))
    else:
        for line in document_returned:
            if len(line.get("Languages")) != 0:
                list_to_return.append((line.get("Country"), line.get("Languages")))
    return list_to_return


@app.route('/countries-time-zone', methods=['GET'])
def get_countries_time_zone_param():
    """Return all countries according to constitutional form"""
    args = request.args
    time_zone = args.get('TimeZone')
    time_zone = time_zone.replace(' ', '+')
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    if time_zone:
        for line in document_returned:
            if len(line.get("Time Zone")) != 0:
                if time_zone in line.get("Time Zone"):
                    list_to_return.append(line.get("Country"))
    else:
        for line in document_returned:
            if len(line.get("Time Zone")) != 0:
                list_to_return.append((line.get("Country"), line.get("Time Zone")))
    return list_to_return
