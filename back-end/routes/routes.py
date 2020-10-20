from flask import Flask, jsonify, request
from models.continents import Continents
from models.countries import Countries
from models.states import States
from models.counties import Counties
from models.account import Account
import requests

API_BASE = 'https://disease.sh/v3/covid-19/countries'

app = Flask(__name__)

#checking to see if localhost works
@app.route('/', methods=['GET'])
def hi():
    return 'hi'



#login routes
@app.route("/covid/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    account = Account.login(username, password)
    if account:
        account.api_key = Account.random_api_key()
        account.save()
        return jsonify({"session_id": account.api_key,
                        "username": account.username})
    return jsonify({"session_id": None,
                        "username": ""})

@app.route("/covid/create", methods=["POST"])
def create_user():
    data = request.get_json()
    key = Account.random_api_key()
    new_account = Account(data.get("username"), data.get("password"), key, 
                data.get("email"))
    new_account.insert()
    return jsonify({"session_id": new_account.api_key,
                    "username": new_account.username})
                    


#search by single location and time_stamp
@app.route('/covid/continent/<continent_name>/<time_stamp>', methods=['GET'])
def search_by_continent(continent_name, time_stamp):
    name = Continents.select_continent(continent_name, time_stamp)
    return jsonify({'Continent': name})

@app.route('/covid/country/<country_name>/<time_stamp>', methods=['GET'])
def search_by_country(country_name, time_stamp):
    # data = requests.get(API_BASE).json()
    # name = Countries.select_country(country_name, time_stamp)
    # name = Countries(data.get('country_name'), data.get('time_stamp'))
    country = Countries.select_country(country_name, time_stamp)
    return jsonify({'Country': country})

@app.route('/covid/state/<state_name>/<time_stamp>', methods=['GET'])
def search_by_state(state_name, time_stamp):
    name = States.select_state(state_name, time_stamp)
    return jsonify({'State': name})

@app.route('/covid/county/<county_name>/<time_stamp>', methods=['GET'])
def search_by_county(county_name, time_stamp):
    name = Counties.select_county(county_name, time_stamp)
    return jsonify({'County': name})



#search by all locations on a certain time_stamp
@app.route('/covid/continents/<time_stamp>', methods=['GET'])
def search_by_all_continents(time_stamp):
    name = Continents.select_all_continents(time_stamp)
    return jsonify({'Continent': name})

@app.route('/covid/countries/<time_stamp>', methods=['GET'])
def search_by_all_countries(time_stamp):
    # countries = requests.get(API_BASE).json()
    # print(countries)
    country = Countries.select_all_countries(time_stamp)
    # country = countries.save
    return jsonify({'Country': country})

@app.route('/covid/states/<time_stamp>', methods=['GET'])
def search_by_all_states(time_stamp):
    name = States.select_all_states(time_stamp)
    return jsonify({'State': name})

@app.route('/covid/counties/<time_stamp>', methods=['GET'])
def search_by_all_counties(time_stamp):
    name = Counties.select_all_counties(time_stamp)
    return jsonify({'County': name})




# @app.route('/covid/save_continent', methods=['GET'])
# def save_continents():
#     return jsonify

@app.route('/covid/save_country/', methods=['GET'])
def save_countries():
    countries = requests.get(API_BASE).json()
    # print(countries)
    for country in countries:
        new_data = Countries(country.get('updated'), country.get('country'), country.get('active'), 
                        country.get('recovered'), country.get('deaths'), 
                        country.get('cases'), country.get('iso2'), country.get('lat'),
                        country.get('long'), country.get('flag'))
        new_data.save()
    return jsonify({'Country': countries})

# @app.route('/covid/save_state', methods=['GET'])
# def save_states():
#     return jsonify

# @app.route('/covid/save_county', methods=['GET'])
# def save_counties():
#     return jsonify

# @app.route('/covid/', methods=[''])
# def ():
#     return jsonify