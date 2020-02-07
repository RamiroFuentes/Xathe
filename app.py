from flask import Flask,render_template
import Weather_solar_tracker

app = Flask(__name__)

@app.route('/')
def home():
    Weather = Weather_solar_tracker.weather_export()
    tittle = 'Xathe!'    
    return render_template('Home.html',Weather=Weather,tittle=tittle)
 
if __name__ == '__main__':
    app.run(port=8000, debug=True)

