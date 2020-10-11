from flask import Flask, jsonify, request
from models.continents import Continents
from models.countries import Countries
from models.states import States
from models.counties import Counties
from models.account import Account

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    account = Account.login(username, password)
    if account:
        account.api_key = Account.random_api_key()
        account.save()
        return jsonify({"session_id": account.api_key,
                        "username": account.username})
    return jsonify({"session_id": None,
                        "username": ""})

@app.route("/create", methods=["POST"])
def create_user():
    data = request.get_json()
    key = Account.random_api_key()
    new_account = Account(data.get('username'), data.get('password'), key, data.get('email'))
    new_account.insert()
    return jsonify({"session_id": new_account.api_key,
                    "username": new_account.username})
                    



@app.route('/covid/continent/<continent_name>', methods=['GET'])
def search_by_continent(continent_name):
    name = Continents.select_continent(continent_name)
    return jsonify({'Continent': name})

@app.route('/covid/country/<country_name>', methods=['GET'])
def search_by_country(country_name):
    name = Countries.select_country(country_name)
    return jsonify({'Country': name})

@app.route('/covid/state/<state_name>', methods=['GET'])
def search_by_state(state_name):
    name = States.select_state(state_name)
    return jsonify({'State': name})

@app.route('/covid/county/<county_name>', methods=['GET'])
def search_by_county(county_name):
    name = Counties.select_county(county_name)
    return jsonify({'County': name})




@app.route('/covid/continents/<date>', methods=['GET'])
def search_by_all_continents(date):
    name = Continents.select_all_continents(date)
    return jsonify({'Continent': name})

@app.route('/covid/countries/<date>', methods=['GET'])
def search_by_all_countries(date):
    name = Countries.select_all_countries(date)
    return jsonify({'Country': name})

@app.route('/covid/states/<date>', methods=['GET'])
def search_by_all_states(date):
    name = States.select_all_states(date)
    return jsonify({'State': name})

@app.route('/covid/counties/<date>', methods=['GET'])
def search_by_all_counties(date):
    name = Counties.select_all_counties(date)
    return jsonify({'County': name})






@app.route('', methods=[''])
def ():
    return jsonify