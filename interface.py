from flask import Flask, request, jsonify,render_template
from utils import MedicalInsurance
import config

app = Flask(__name__)

@app.route("/")
def home():
    
    #return jsonify("Home Page of medical insurance Prediction")
    return render_template("index.html")


@app.route("/predict_charges",methods = ["GET","POST"])
def predict_charges():

    if request.method == "POST":
        data = request.form
        #print("Data",data)

        age = int(data["age"])
        gender = data["gender"]
        bmi = eval(data["bmi"])
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]


        obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
        pred_price = obj.get_predicted_price()[0]
        #return jsonify({"Result": f"Predicted Charges {pred_price}"})
        return render_template("index.html",result=pred_price.round())
    
    elif request.method == "GET":

        data = request.args.get
        #print("Data :",data)

        age = data('age')
        gender = data('gender')
        bmi = data('bmi')
        children = data('children')
        smoker = data('smoker')
        region = data('region')

        obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
        chrg = obj.get_predicted_price()[0]
        #return render_template("index.html", result = chrg)
        return jsonify({"Insurence Charges":chrg})

    
    


if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=config.PORT_NO,debug= False)
