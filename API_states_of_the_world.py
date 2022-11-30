from connect_to_mongodb import connect_to_mongodb
from flask import Flask

states_of_the_world_collection = connect_to_mongodb()

app = Flask(__name__)


@app.route('/')
def get_countries():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/top-10-countries-population')
def get_top_10_countries_population():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Population", -1).limit(10)
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Population")))
    return list_to_return


@app.route('/top-50-countries-population')
def get_top_50_countries_population():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Population", -1).limit(50)
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Population")))
    return list_to_return


@app.route('/top-100-countries-population')
def get_top_100_countries_population():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Population", -1).limit(100)
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Population")))
    return list_to_return


@app.route('/top-10-countries-densities')
def get_top_10_countries_densities():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Density", -1).limit(10)
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Density")))
    return list_to_return


@app.route('/top-50-countries-densities')
def get_top_50_countries_densities():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Density", -1).limit(50)
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Density")))
    return list_to_return


@app.route('/top-100-countries-densities')
def get_top_100_countries_densities():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Density", -1).limit(100)
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Density")))
    return list_to_return


@app.route('/top-10-countries-areas')
def get_top_10_countries_areas():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Area", -1).limit(10)
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Area")))
    return list_to_return


@app.route('/top-50-countries-areas')
def get_top_50_countries_areas():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Area", -1).limit(50)
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Area")))
    return list_to_return


@app.route('/top-100-countries-areas')
def get_top_100_countries_areas():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0}).sort("Area", -1).limit(100)
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Area")))
    return list_to_return


@app.route('/countries-capitals')
def get_countries_capitals():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Capital")))
    return list_to_return


@app.route('/countries-constitutional-form')
def get_countries_constitutional_form():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Constitutional form")))
    return list_to_return


@app.route('/countries-constitutional-form/republic')
def get_countries_constitutional_form_republic():
    document_returned = states_of_the_world_collection.find({"Constitutional form": "Republic"}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-constitutional-form/constitutional-monarchy')
def get_countries_constitutional_form_constitutional_monarchy():
    document_returned = states_of_the_world_collection. \
        find({"Constitutional form": "Constitutional monarchy"}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-constitutional-form/provisional')
def get_countries_constitutional_form_provisional():
    document_returned = states_of_the_world_collection.find({"Constitutional form": "Provisional"}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-constitutional-form/absolute-monarchy')
def get_countries_constitutional_form_absolute_monarchy():
    document_returned = states_of_the_world_collection.find({"Constitutional form": "Absolute monarchy"}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-neighbours')
def get_countries_neighbours():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        list_to_return.append((line.get("Country"), line.get("Neighbours")))
    return list_to_return


@app.route('/countries-languages')
def get_countries_languages():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Languages")) != 0:
            list_to_return.append((line.get("Country"), line.get("Languages")))
    return list_to_return


@app.route('/countries-languages/english')
def get_countries_languages_english():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Languages")) != 0:
            if 'English' in line.get("Languages"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-languages/german')
def get_countries_languages_german():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Languages")) != 0:
            if 'German' in line.get("Languages"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-languages/russian')
def get_countries_languages_russian():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Languages")) != 0:
            if 'Russian' in line.get("Languages"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-languages/arabic')
def get_countries_languages_arabic():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Languages")) != 0:
            if 'Arabic' in line.get("Languages"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-languages/portuguese')
def get_countries_languages_portuguese():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Languages")) != 0:
            if 'Portuguese' in line.get("Languages"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-languages/french')
def get_countries_languages_french():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Languages")) != 0:
            if 'French' in line.get("Languages"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-languages/spanish')
def get_countries_languages_spanish():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Languages")) != 0:
            if 'Spanish' in line.get("Languages"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-languages/romanian')
def get_countries_languages_romanian():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Languages")) != 0:
            if 'Romanian' in line.get("Languages"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone')
def get_countries_time_zone():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            list_to_return.append((line.get("Country"), line.get("Time Zone")))
    return list_to_return


@app.route('/countries-time-zone/PMST')
def get_countries_time_zone_pmst():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC−03:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/CET')
def get_countries_time_zone_cet():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC+01:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/AST')
def get_countries_time_zone_ast():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC−04:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/AoE')
def get_countries_time_zone_aoe():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC−12:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/ST')
def get_countries_time_zone_st():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC−11:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/HT')
def get_countries_time_zone_ht():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC−10:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/AKT')
def get_countries_time_zone_akt():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC−09:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/PT')
def get_countries_time_zone_pt():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC−08:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/MT')
def get_countries_time_zone_mt():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC−07:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/CT')
def get_countries_time_zone_ct():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC-06:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/ET')
def get_countries_time_zone_et():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC-05:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/ChT')
def get_countries_time_zone_cht():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC+10:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/GMT')
def get_countries_time_zone_gmt():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC±00:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/WAKT')
def get_countries_time_zone_wakt():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC+12:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/CXT')
def get_countries_time_zone_cxt():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC+07:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return


@app.route('/countries-time-zone/AWST')
def get_countries_time_zone_awst():
    document_returned = states_of_the_world_collection.find({}, {"_id": 0})
    list_to_return = []
    for line in document_returned:
        if len(line.get("Time Zone")) != 0:
            if 'UTC+08:00' in line.get("Time Zone"):
                list_to_return.append(line.get("Country"))
    return list_to_return
