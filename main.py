# for table analysis
import pandas as pd
from connect_to_mongodb import connect_to_MongoDB
import quandl

# for performing your HTTP requests
import requests

# for xml & html scrapping
from bs4 import BeautifulSoup

def just_name(name):
    if name[0] == ' ':
        name = name[1:]
    if name[-1] == ']':
        name = name[0:-3]
    return name


def get_countries_and_population():
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

    s = requests.Session()
    response = s.get(url, timeout=10)

    soup = BeautifulSoup(response.content, 'html.parser')
    pretty_soup = soup.prettify()
    # find all the tables in the html
    all_tables = soup.find_all('table')
    # get right table to scrap
    right_table = soup.find('table', {"class": 'wikitable sortable'})
    # number of rows in the table including header
    rows = right_table.findAll("tr")
    # header attributes of the table
    header = [th.text.rstrip() for th in rows[0].find_all('th')][1:]
    del header[2:]
    # print(header)
    # print('------------')
    # print(len(header))

    lst_data = []
    for row in rows[2:]:
        data = [d.text.rstrip() for d in row.find_all('td')]
        lst_data.append(data)
    # select also works as find_all
    lst_data1 = []
    for row in rows[3:]:
        data = [d.text.rstrip() for d in row.select('td')]
        del data[2:]
        lst_data1.append(data)
    lst_data1 = pd.DataFrame(lst_data1, columns=header)
    df = lst_data1.copy()

    # Lets do some Clean Up !
    new_cols = ["Country", "Population"]
    df.columns = new_cols

    df['Population'] = df['Population'].apply(lambda x: float(x.split()[0].replace(',', '')))

    #states_of_the_world_collection.insert_many({id: df.to_json()})


def get_name_and_capital_of_countries_and_create_list_of_dictionaries():
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
        data[0] = country_name[0]
        data[1] = data[1].replace(",", "")
        del data[2:]
        list_of_country_and_population.append(data)

    list_of_dictionaries = []
    for line in list_of_country_and_population:
        header = ["Country", "Population"]
        dictionary = dict.fromkeys(header)
        dictionary["Country"] = line[0]
        dictionary["Population"] = line[1]
        list_of_dictionaries.append(dictionary)
    return list_of_dictionaries


if __name__ == '__main__':
    states_of_the_world_collection = connect_to_MongoDB()
    list_of_dictionaries = get_name_and_capital_of_countries_and_create_list_of_dictionaries()
    print(list_of_dictionaries)
    #for dictionary in list_of_dictionaries:
    #    states_of_the_world_collection.insert_one(dictionary)