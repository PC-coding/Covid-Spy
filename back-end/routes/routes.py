from flask import Flask, jsonify, request
from flask_cors import CORS
from models.continents import Continents
from models.countries import Countries
from models.states import States
from models.counties import Counties
from models.account import Account
import requests

API_BASE = 'https://disease.sh/v3/covid-19/countries'
API_BASE1= 'https://disease.sh/v3/covid-19/states'

app = Flask(__name__)
CORS(app)

# checking to see if localhost works

@app.route('/', methods=['GET'])
def hi():
    return 'hi'




# user routes

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
    pass_hash = Account.hash_password(data.get("password"))
    new_account = Account(data.get("username"), pass_hash, key, data.get("email"))
    new_account._insert()
    return jsonify({"session_id": new_account.api_key,
                    "username": new_account.username})




# favorites routes

@app.route("/covid/favorites", methods=["POST"])
def addFav():
    data = request.get_json()
    if data is None: 
        return jsonify({'Invalid': False})
    acc = Account.api_authenticate(data.get("api_key"))
    fav = acc.save_favorites(data.get("country", "active")["country"])
    return jsonify([fav])

@app.route("/covid/unfavorite", methods=["POST"])
def removeFav():
    data = request.get_json()
    account = Account.api_authenticate(data.get("api_key"))
    if account is None:
        return jsonify({'Deleted': False})    
    deleted = account.delete_favorites(data.get("country", "api_key"))
    return jsonify({'Deleted': deleted})

@app.route('/covid/countries/filter', methods=['POST'])
def filter_country():
    data = request.get_json()
    account = Account.api_authenticate(data.get("api_key"))
    favs = account.filter_favs()
    country_fav = []
    for country in favs:
        country_data = Countries.select_country(country[3]).country
        country_fav.append(country_data)
    return jsonify({'Favorites': country_fav})

# @app.route('/covid/countries/filter', methods=['POST'])
# def filter_country():
#     data = request.get_json()
#     account = Account.api_authenticate(data.get("api_key"))
#     favs = account.filter_favs()
#     country_fav = []
#     for country in favs:
#         country_data = Countries.select_country(country[1:]).country
#         country_fav.append(country_data)
#     return jsonify({'Favorites': country_fav})




# search by single location and updated

@app.route('/covid/countries/<country>', methods=['GET'])
def search_by_country(country):
    countries = Countries.select_country(country)
    return jsonify(countries.to_json())

@app.route('/covid/state/<state>', methods=['GET'])
def search_by_state(state):
    name = States.select_state(state)
    return jsonify({'State': name})

@app.route('/covid/state', methods=['POST'])
def update_states():
    data = request.get_json()
    lat = data.get('lat')
    long = data.get('long')
    state = data.get('state')
    update_list = States(lat=lat, long=long, state=state)
    update = update_list.update()
    return jsonify({'Success': update})




# search by all locations on a certain updated

@app.route('/covid/countries/', methods=['GET'])
def search_by_all_countries():
    countries = Countries.select_all_countries()
    return jsonify([country.to_json() for country in countries])

@app.route('/covid/states/', methods=['GET'])
def search_by_all_states():
    name = States.select_all_states()
    return jsonify({'State': name})




# saving country/state data to database

@app.route('/covid/save_country', methods=['GET'])
def save_countries():
    countries = requests.get(API_BASE).json()
    for country in countries:
        new_data = Countries(country.get('updated'), country.get('country'), 
                            country.get('active'), country.get('cases'), 
                            country.get('todayCases'), country.get('recovered'), 
                            country.get('todayRecovered'), country.get('deaths'), 
                            country.get('todayDeaths'), 
                            country.get('countryInfo')['iso2'], 
                            country.get('countryInfo')['lat'], 
                            country.get('countryInfo')['long'], 
                            country.get('countryInfo')['flag'])
        new_data.save()
    return jsonify({'Country': countries})

@app.route('/covid/save_state', methods=['GET'])
def save_states():
    states = requests.get(API_BASE1).json()
    for state in states:
        new_data = States(state.get('updated'), state.get('state'), 
                        state.get('active'), state.get('cases'), 
                        state.get('todayCases'), state.get('recovered'),
                        state.get('deaths'), state.get('todayDeaths'))
        new_data.save()
    return jsonify({'State': states})