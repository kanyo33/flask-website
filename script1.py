from flask import Flask, render_template
import requests
import json

spacex_mission = 'https://api.spacexdata.com/v3/missions'
spacex_launches = 'https://api.spacexdata.com/v3/launches/latest'

app=Flask(__name__)

@app.route('/')
def home():
    r = requests.get(spacex_launches)
    return render_template("home.html",
    response=json.loads(r.text))

@app.route('/apps/')
def apps():
    r = requests.get(spacex_mission)

    
    return render_template("apps.html",
    response=json.loads(r.text)
    )

if __name__=="__main__":
    app.run(debug=True)
