from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with link to Fortune page."""
    return render_template('index.html')

@app.route('/fortune')
def get_fortune():

    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_favorite_genre = request.args.get('genre')
    users_favorite_planet = request.args.get('planet')
    users_favorite_app = request.args.get('app')


    if users_favorite_genre == 'Rock':
        genre_fortune = "Someone is going to buy you an electric guitar in the next few days. "
    elif users_favorite_genre == 'EDM':
        genre_fortune = "Don't stop the Womp today...or Wub...whatever!!"

    elif users_favorite_genre == 'Jazz':
        genre_fortune = "Paul Desmond is a God, pick up the sax, u might get on his level!!!"
    else:
        genre_fortune = "You will soon find a link from the fibonnaci sequence to mozart's harmonic magic sounds. "

    if users_favorite_planet == 'Mars':
        planet_fortune = "Elon's about to dip to mars, u better hurry before he gets there. "
    elif users_favorite_planet == 'Pluto':
        planet_fortune = "I'm sorry, but pluto is not a planet, u played urself!! "

    elif users_favorite_planet == 'Krypton':
        planet_fortune = "Weird flex trying to compare yourself to lex luthor, but ok!!"
    else:
        planet_fortune = "Go pick up few plastics and be a part of a bigger cause to save our planet. "

    if users_favorite_app == 'YT':
        app_fortune = "The trending page on youtube is so AIDS "
    elif users_favorite_app== 'Slack':
        app_fortune = "No privacy on Slack!!"

    elif users_favorite_app == 'MealPal':
        app_fortune = "MealPal will rip you off this month. "
    else:
        app_fortune = "Cash app will soon surpass Venmo. "

    fortune_greetings_list = ["Hi silly goose! ", "Hi broke millenial! ", "Helllllloooo " ]
    random_greeting = random.choice(fortune_greetings_list)
    fortune = random_greeting+genre_fortune+planet_fortune+app_fortune

    return render_template('fortune_results.html', fortune=fortune)
@app.route('/weather')
def get_weather():
    return render_template('weather_form.html')

@app.route('/weather_results', methods=['GET'])
def weather_results_page():
    if request.method == "GET":
        users_city = request.args.get('city')
        params = {
            'q': users_city,
            'appid': '41f6784fa9f84526f0d6dd90647897bf'

        }
        response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)
        json = response.json()
        city = json['name']
        temp = json['main']['temp']
        celsius_temp = convert_to_celsius(temp)

        return render_template('weather_results.html', city=city, celsius_temp=celsius_temp)
def convert_to_celsius(kelvin_temp):

    celsius_temp = kelvin_temp-273.15

    return celsius_temp




if __name__ == '__main__':
    app.run()
