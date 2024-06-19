import requests


def generate_words():
    url = "https://random-word-api.herokuapp.com/word"
    params = {
        "number": 500,
        "length": 5
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    generated_text = " ".join(data)
    return generated_text


some_web = "Gold is a chemical element with the symbol Au (from the Latin word aurum) and the atomic number 79. In its pure form, it is a bright, slightly orange-yellow, dense, soft, malleable, and ductile metal. Chemically, gold is a transition metal, a group 11 element, and one of the noble metals. It is one of the least reactive chemical elements, being the second-lowest in the reactivity series. It is solid under standard conditions. Gold often occurs in free elemental (native state), as nuggets or grains, in rocks, veins, and alluvial deposits."