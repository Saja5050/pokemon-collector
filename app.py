from flask import Flask, render_template, redirect, url_for
import requests
import random
import json
import os

app = Flask(__name__)
POKEMON_JSON_PATH = "pokemons.json"

def get_random_pokemon_name():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
    response = requests.get(url)
    all_pokemons = response.json().get("results", [])
    return random.choice(all_pokemons)["name"] if all_pokemons else None

def load_pokemons():
    if not os.path.exists(POKEMON_JSON_PATH):
        return []
    with open(POKEMON_JSON_PATH, "r") as f:
        return json.load(f)

def save_pokemon(pokemon_data):
    pokemons = load_pokemons()
    pokemons.append(pokemon_data)
    with open(POKEMON_JSON_PATH, "w") as f:
        json.dump(pokemons, f, indent=2)

def fetch_pokemon_details(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "image": data["sprites"]["front_default"]
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/draw")
def draw():
    pokemons = load_pokemons()
    name = get_random_pokemon_name()
    for p in pokemons:
        if p["name"] == name:
            return render_template("result.html", pokemon=p)

    new_pokemon = fetch_pokemon_details(name)
    if new_pokemon:
        save_pokemon(new_pokemon)
        return render_template("result.html", pokemon=new_pokemon)

    return redirect(url_for("index"))

@app.route("/exit")
def exit_page():
    return render_template("exit.html")

@app.route("/collection")
def collection():
    pokemons = load_pokemons()
    return render_template("collection.html", pokemons=pokemons)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
