from flask import Flask,render_template,url_for,request #requirments flask app
import pickle#import pickle
import numpy as np#numpy

model=pickle.load(open('model.pkl','rb'))#imported model

app = Flask(__name__)#normal syntax

@app.route("/")
def home():
    return render_template("home.html",title = "home page" )

@app.route("/predict",methods = ["POST","GET"])
def predict():
    int_features =[float(x) for x in request.form.values()]#fetching values from the html form
    final=[np.array(int_features)]#converting raw string into numpy array
    prediction = model.predict(final)#model prediction
    output = prediction[0]#saved into output variable 
    if output == 1:
        return render_template('home.html',pred = "You may high chances of being diabetic")
    else:
        return render_template("home.html",pred = "The chances that you have diabetes are very less")

if __name__ == "__main__":
       app.run(debug = True)#normal syntax
