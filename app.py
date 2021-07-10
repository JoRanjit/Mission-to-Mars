from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app=Flask(__name__)

#use flask_pymongo to set upmongo connecion
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#set up flask route for the home page of our webpage
@app.route("/")
def index():
    # find mars collection in our db and assign it to 'mars' variable
    mars=mongo.db.mars.find_one()
    #this will return an html template using index.html file, and mars data
    #we'll create index.html later
    return render_template("index.html",mars=mars)

#set up flask route for the scraping page of our webpage
#this will use the scrape function below
@app.route("/scrape")

def scrape():
    mars = mongo.db.mars
    #we'll use scrape_all function scraping.py file to scrape data and assign to mars_data variable
    mars_data = scraping.scrape_all()
    # updating the db s=using update function, upsert=true indicates that we'll create new one if it does not exist
    mars.update({},mars_data,upsert=True)
    # this will navigate back to the home page to see the refreshed content
    return redirect('/',code=302)

#calling the functions to run
if __name__ == "__main__":
    app.run()