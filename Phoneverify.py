import os
import requests
import json
import base64
from base64 import b64encode
from dotenv import load_dotenv
from flask import (
    Flask, 
    render_template, 
    redirect,
    request,
    url_for,
    session,
)
load_dotenv()

app = Flask(__name__)
app.secret_key = "ssssh don't tell anyone"

auth_id= os.getenv('AUTH_ID')
secret_auth_id= os.getenv('AUTH_SECRET_ID')

def header(x,y):
    auth_id=bytes(x, 'utf-8')
    auth_secret=bytes(y, 'utf-8')
    auth_token = auth_id + b':' + auth_secret
    auth_token =b64encode(auth_token).decode('ascii')
    header ={"Content-Type" : "application/json","Authorization" : "Basic "+ auth_token}
    return header



def verification_(x,y):
    a={"dst": x+y}
    data=json.dumps(a)
    headers= header(auth_id,secret_auth_id)
    response = requests.post("https://api.tiniyo.com/v1/Account/"+auth_id+"/Verifications", data=data, headers=headers)
    data = response.json()
    print(data)
    print(response)
    print("verification")
    return response

def verification_check(x,y,otp):
    a={"dst": x+y}
    b={"code": otp}
    c={**b,**a}
    data1 = json.dumps(c)
    headers= header(auth_id,secret_auth_id)
    response = requests.post("https://api.tiniyo.com/v1/Account/"+auth_id+"/VerificationsCheck", data=data1, headers=headers)
    data1 = response.json()
    print(data1)
    print(response)
    print("check")
    if response.status_code==200:
        return 1
           


@app.route("/phone_verification", methods=["GET","POST"])
def phone_verification():
    if request.method =="POST":
        cc = request.values.get('cc')
        pn = request.values.get('pn')
        
        session['country_code'] = cc
        session['phone_number'] = pn

        verification_(cc,pn)
        
        return redirect(url_for("phone_verification_check"))
        
    else:
        return render_template("phone_verification.html")
    

@app.route("/phone_verification_check", methods=["POST","GET"])
def phone_verification_check():
    if request.method =="POST":
        otp = request.values.get("otp")
        country_code = session.get('country_code')
        phone_number = session.get('phone_number')   
        if(verification_check(country_code,phone_number,otp))==1:
            return redirect(url_for("success"))

    else:
        return render_template("phone_verification_check.html") 

@app.route("/success")
def success():
    return render_template("success.html")
if __name__ == '__main__':
    app.run(debug=True)