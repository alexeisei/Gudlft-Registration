import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         for comp in listOfCompetitions:
            if datetime.strptime(comp['date'], "%Y-%m-%d %H:%M:%S") < datetime.now():
                comp['finish'] = True
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html', clubs=clubs)


@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        flash("Sorry, that email wasn't found.")
        return redirect(url_for('index'))
    return render_template('welcome.html',club=club,competitions=competitions, clubs=clubs)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong , please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    
    if placesRequired > 12:
        flash("You can't take more than 12 places")
    else:
        if placesRequired*3 < int(club['points']) and int(competition['numberOfPlaces'])-placesRequired >= 0:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            club['points'] = int(club['points']) - placesRequired*3
            flash('Great-booking complete!')
        else:
            flash("Sorry, you don't have enough points")
            
    return render_template('welcome.html', club=club, competitions=competitions, clubs=clubs)


@app.route('/displayclubsPoints')
def displayclubsPoints():
    return render_template('clubstable.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
