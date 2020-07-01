# Python-OTP-Verification
This repository allows, to create a phone number verification using sms/call OTP in python.

![Python-OTP-Verification](demo/demo.gif | width=600)

## Requirements
 - Python 3.7
 - Create a Free Account at Tiniyo [https://tiniyo.com]

## Setup

1. Clone the jwt-go into your go path and change directory to cloned repository.

```bash
$ git clone https://github.com/tiniyo-api/python-otp-verification.git
$ cd python-otp-verification
```
2. Setting up Virtual Environment

```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
2. Create your Free **TINIYO** Account and grab your **"API Key"**: <https://www.tiniyo.com>


3. Copy ```.env.example``` to ```.env``` and update it with your **Tiniyo** credentials.


4. Run the ```Phoneverify.py``` in your console.

```python
Phoneverify.py
```

5. Navigate to <http://localhost:5000/phone_verification> to try it out!
