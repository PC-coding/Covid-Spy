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

#checking to see if localhost works

@app.route('/', methods=['GET'])
def hi():
    return 'hi'



#user routes

@app.route("/covid/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    account = Account.login(username, password)
    print(username)
    print(password)
    print(account)
    if account:
        account.api_key = Account.random_api_key()
        account.save()
        print(account.api_key)
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

                    

#favorites routes
@app.route("/covid/favorites", methods=["POST"])
def addFav():
    data = request.get_json()
    print(data)
    if data is None: 
        return jsonify({'Invalid': False})
    account = Account.api_authenticate(data.get("api_key"))
    print(account)
    fav = account.save_favorites(data.get("country"))
    return jsonify({'Success': fav})

@app.route("/covid/unfavorite", methods=["POST"])
def removeFav():
    data = request.get_json()
    account = Account.api_authenticate(data.get("api_key"))
    if account is None:
        return jsonify({'Deleted': False})    
    deleted = account.delete_favorites(data.get("country", "api_key"))
    return jsonify({'Deleted': deleted})


#search by single location and updated

# @app.route('/covid/continent/<continent_name>/<updated>', methods=['GET'])
# def search_by_continent(continent_name, updated):
#     name = Continents.select_continent(continent_name, updated)
#     return jsonify({'Continent': name})

@app.route('/covid/countries/filter', methods=['POST'])
def filter_country():
    data = request.get_json()
    country_fav = []
    for country in data.get('favorites'):
        country_data = Countries.select_country(country)
        country_fav.append(country_data)
    return jsonify({'Favorites': country_fav})

@app.route('/covid/countries/<country>', methods=['GET'])
def search_by_country(country):
    countries = Countries.select_country(country)
    # return jsonify([country.to_json() for country in countries])
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
    print(lat,long)
    # update = States.update(lat, long)
    update_list = States(lat=lat, long=long, state=state)
    update = update_list.update()
    return jsonify({'Success': update})


# @app.route('/covid/county/<county_name>/<updated>', methods=['GET'])
# def search_by_county(county_name, updated):
#     name = Counties.select_county(county_name, updated)
#     return jsonify({'County': name})



#search by all locations on a certain updated

# @app.route('/covid/continents/<updated>', methods=['GET'])
# def search_by_all_continents(updated):
#     name = Continents.select_all_continents(updated)
#     return jsonify({'Continent': name})

@app.route('/covid/countries/', methods=['GET'])
def search_by_all_countries():
    countries = Countries.select_all_countries()
    return jsonify([country.to_json() for country in countries])

@app.route('/covid/states/', methods=['GET'])
def search_by_all_states():
    name = States.select_all_states()
    return jsonify({'State': name})

# @app.route('/covid/counties/<updated>', methods=['GET'])
# def search_by_all_counties(updated):
#     name = Counties.select_all_counties(updated)
#     return jsonify({'County': name})




# @app.route('/covid/save_continent', methods=['GET'])
# def save_continents():
#     return jsonify

@app.route('/covid/save_country', methods=['GET'])
def save_countries():
    countries = requests.get(API_BASE).json()
    # print(countries)
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

# @app.route('/covid/save_county', methods=['GET'])
# def save_counties():
#     return jsonify

# @app.route('/covid/', methods=[''])
# def ():
#     return jsonify