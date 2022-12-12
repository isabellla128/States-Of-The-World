import re
import requests
from bs4 import BeautifulSoup
from connect_to_mongodb import connect_to_mongodb


def get_right_name_of_country(country):
    """Return right name of country
    :param country: the country given for normalization"""
    if country.find("South") != -1 and country.find("Korea") != -1:
        country = "South Korea"
    elif country.find("North") != -1 and country.find("Korea") != -1:
        country = "North Korea"
    elif country == "Republic of China" != -1 or country.find("Taiwan") != -1:
        country = "Taiwan"
    elif country.find("China") != -1:
        country = "China"
    elif country.find("Gambia") != -1:
        country = "Gambia"
    elif country == "Nagorno-Karabakh Republic":
        country = "Artsakh"
    elif country.find("Micronesia") != -1:
        country = "Micronesia"
    elif country.find("Virgin Islands") != -1:
        country = "U.S. Virgin Islands"
    elif country.find("Saint Martin") != -1:
        country = "Saint Martin"
    elif country == "Côte d'Ivoire":
        country = "Ivory Coast"
    elif country.find("Congo") != -1 and country.find("Democratic") != -1:
        country = "DR Congo"
    elif country.find("Congo") != -1:
        country = "Congo"
    elif country.find("Myanmar") != -1:
        country = "Myanmar"
    elif country.find("Bahamas") != -1:
        country = "Bahamas"
    elif country.find("Verde") != -1:
        country = "Cape Verde"
    elif country.find("Lao") != -1:
        country = "Laos"
    elif country.find("Sahrawi") != -1:
        country = "Western Sahara"
    elif country.find("Netherlands") != -1:
        country = "Netherlands"
    return country


def get_right_name_of_country_in_a_list(list_of_countries):
    """Returns a list with the correct names of the countries
    :param country: the list of countries given for normalization"""
    new_list_of_countries = []
    for country in list_of_countries:
        if country[-1] != ']':
            new_list_of_countries.append(get_right_name_of_country(country))
    return new_list_of_countries


def add_small_capitals_and_areas(states_of_the_world_collection):
    """Add small capitals and areas in database
    :param states_of_the_world_collection: the database collection where we need to add the data"""
    states_of_the_world_collection.update_one(
        {"Country": "Burkina Faso"},
        {
            "$set": {"Capital": "Ouagadougou", "Area": 274}
        }
    )
    states_of_the_world_collection.update_one(
        {"Country": "Abkhazia"},
        {
            "$set": {"Capital": "Suhumi", "Area": 866}
        }
    )
    states_of_the_world_collection.update_one(
        {"Country": "Curaçao"},
        {
            "$set": {"Capital": "Willemstad", "Area": 152}
        }
    )
    states_of_the_world_collection.update_one(
        {"Country": "South spatia"},
        {
            "$set": {"Capital": "Țhinvali", "Area": 390}
        }
    )
    states_of_the_world_collection.update_one(
        {"Country": "Tokelau"},
        {
            "$set": {"Capital": "Nukunonu", "Area": 10.2}
        }
    )


def add_small_density(states_of_the_world_collection):
    """Add small densities in database"""
    states_of_the_world_collection.update_one(
        {"Country": "Abkhazia"},
        {
            "$set": {"Density": 28.47}
        }
    )
    states_of_the_world_collection.update_one(
        {"Country": "South Ossetia"},
        {
            "$set": {"Density": 13.7}
        }
    )


def add_countries_and_population_if_not_exist(states_of_the_world_collection, list_of_dictionaries):
    """Add countries and population if not exist"""
    list_of_dictionaries = sorted(list_of_dictionaries, key=lambda d: d['Country'])
    for dictionary in list_of_dictionaries:
        cursor = states_of_the_world_collection.find({"Country": dictionary["Country"]})
        ok = False
        for _ in cursor:
            ok = True
            break
        if not ok:
            states_of_the_world_collection.insert_one(dictionary)


def get_name_and_population_of_countries_and_create_list_of_dictionaries():
    """Return name and population of countries and create list of dictionaries"""
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    s = requests.Session()
    response = s.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    right_table = soup.find('table', {"class": "wikitable"})
    rows = right_table.findAll("tr")

    list_of_country_and_population = []

    for row in rows[3:]:
        data = [d.text.rstrip() for d in row.select('td')]
        country_name = [d.text.rstrip() for d in row.select('a')]
        if country_name[0] == "":
            data[0] = country_name[1]
        else:
            data[0] = country_name[0]
        data[1] = data[1].replace(",", "")
        del data[2:]
        list_of_country_and_population.append(data)

    list_of_dictionaries = []

    for line in list_of_country_and_population:
        header = ["Country", "Population", "Area", "Capital", "Density", "Constitutional form",
                  "Neighbours", "Time Zone", "Languages"]
        dictionary = dict.fromkeys(header)
        dictionary["Country"] = line[0]
        dictionary["Population"] = float(line[1])
        dictionary["Area"] = 0
        dictionary["Capital"] = ""
        dictionary["Density"] = 0
        dictionary["Constitutional form"] = ""
        dictionary["Neighbours"] = []
        dictionary["Time Zone"] = []
        dictionary["Languages"] = []
        list_of_dictionaries.append(dictionary)

    return list_of_dictionaries


def get_capital_and_area(states_of_the_world_collection):
    """Add capital and area of countries in database"""
    url = "https://en.wikipedia.org/wiki/List_of_national_capitals_by_area"
    s = requests.Session()
    response = s.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    right_table = soup.find('table', {"class": 'wikitable sortable'})
    rows = right_table.findAll("tr")

    list_of_country_capital_area = []
    for row in rows[2:]:
        capital = [d.text.rstrip() for d in row.find_all('b')]
        if len(capital) == 0:
            capital = "n/a"
        else:
            capital = capital[0]
        country = [d.text.rstrip() for d in row.find_all('a')][1]
        country = get_right_name_of_country(country)
        area = [d.text.rstrip() for d in row.select('td')][3]
        area = area.replace(",", "")
        if area[-1] == ']':
            area = area[:area.find('[')]
        if area == "n/a":
            area = 0
        list_of_country_capital_area.append([country, capital, area])

    for line in list_of_country_capital_area:
        states_of_the_world_collection.update_one(
            {"Country": line[0]},
            {
                "$set": {"Capital": line[1], "Area": float(line[2])}
            }
        )


def get_density(states_of_the_world_collection):
    """Add density of countries in database"""
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density"
    s = requests.Session()
    response = s.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    right_table = soup.find('table', {"class": 'wikitable'})
    rows = right_table.findAll("tr")

    list_of_densities = []
    for row in rows[2:]:
        density = [d.text.rstrip() for d in row.find_all('td')][3]
        country = [d.text.rstrip() for d in row.find_all('a')]
        country = country[0]
        density = density.replace(",", "")
        list_of_densities.append([country, density])

    for line in list_of_densities:
        states_of_the_world_collection.update_one(
            {"Country": line[0]},
            {
                "$set": {"Density": float(line[1])}
            }
        )


def get_constitutional_form(states_of_the_world_collection):
    """Add constitutional form of countries in database"""
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_system_of_government"
    s = requests.Session()
    response = s.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.findAll('table', {"class": 'wikitable'})
    list_of_constitutional_from = []

    for right_table in tables:
        rows = right_table.findAll("tr")
        for row in rows[1:]:
            constitutional_from = [d.text.rstrip() for d in row.find_all('td')][1]
            constitutional_from = constitutional_from.replace("\xa0", " ")
            country = [d.text.rstrip() for d in row.find_all('a')][0]
            country = get_right_name_of_country(country)
            list_of_constitutional_from.append([country, constitutional_from])

    for line in list_of_constitutional_from:
        states_of_the_world_collection.update_one(
            {"Country": line[0]},
            {
                "$set": {"Constitutional form": line[1]}
            }
        )


def get_neighbours(states_of_the_world_collection):
    """Add neighbours of countries in database"""
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_land_borders"
    s = requests.Session()
    response = s.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    right_table = soup.find('table', {"class": 'wikitable'})
    rows = right_table.findAll("tr")

    list_of_country_and_neighbours = []
    for row in rows[2:]:
        list_of_neighbours = []
        neighbours = [d.text.rstrip() for d in row.find_all('a')]
        country = get_right_name_of_country(neighbours[0])
        for neighbour in neighbours[1:]:
            if len(neighbour) > 0:
                if neighbour[0] != '[':
                    list_of_neighbours.append(get_right_name_of_country(neighbour))
        list_of_country_and_neighbours.append([country, list_of_neighbours])

    for line in list_of_country_and_neighbours:
        states_of_the_world_collection.update_one(
            {"Country": line[0]},
            {
                "$set": {"Neighbours": line[1:][0]}
            }
        )


def get_time_zones(states_of_the_world_collection):
    """Add time zones of countries in database"""
    url = "https://en.wikipedia.org/wiki/List_of_time_zones_by_country"
    s = requests.Session()
    response = s.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    right_table = soup.find('table', {"class": 'wikitable'})
    rows = right_table.findAll("tr")

    list_of_country_and_time_zones = []
    for row in rows[1:]:
        country = [d.text.rstrip() for d in row.find_all('a')][0]
        country = get_right_name_of_country(country)
        time_zones = [d.text.rstrip() for d in row.find_all('a', {'title': re.compile(r'\bUTC\b')})]
        list_of_country_and_time_zones.append([country, time_zones])

    for line in list_of_country_and_time_zones:
        states_of_the_world_collection.update_one(
            {"Country": line[0]},
            {
                "$set": {"Time Zone": line[1:][0]}
            }
        )


def get_spoken_languages(states_of_the_world_collection):
    """Add spoken languages of countries in database"""
    url = "https://en.wikipedia.org/wiki/List_of_official_languages_by_country_and_territory"
    s = requests.Session()
    response = s.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    right_table = soup.find('table', {"class": 'wikitable'})
    rows = right_table.findAll("tr")
    list_of_country_and_languages = []
    for row in rows[1:]:
        country = [d.text.rstrip() for d in row.find_all('a')][0]
        country = get_right_name_of_country(country)
        list_of_children = row.find_all('td')[1]
        if len(list_of_children) == 1:
            languages = [d.text.rstrip() for d in list_of_children]
        else:
            languages = [d.text.rstrip() for d in list_of_children.find_all('a')]
            languages = get_right_name_of_country_in_a_list(languages)
        list_of_country_and_languages.append([country, languages])

    for line in list_of_country_and_languages:
        states_of_the_world_collection.update_one(
            {"Country": line[0]},
            {
                "$set": {"Languages": line[1:][0]}
            }
        )


def crawler_wikipedia():
    """Create database and add name, capital, population, density,
    constitutional form, time zones, spoken languages of countries"""
    states_of_the_world_collection = connect_to_mongodb()
    list_of_dictionaries = get_name_and_population_of_countries_and_create_list_of_dictionaries()
    add_countries_and_population_if_not_exist(states_of_the_world_collection, list_of_dictionaries)
    get_capital_and_area(states_of_the_world_collection)
    add_small_capitals_and_areas(states_of_the_world_collection)
    get_density(states_of_the_world_collection)
    add_small_density(states_of_the_world_collection)
    get_constitutional_form(states_of_the_world_collection)
    get_neighbours(states_of_the_world_collection)
    get_time_zones(states_of_the_world_collection)
    get_spoken_languages(states_of_the_world_collection)


crawler_wikipedia()
