
# Laptop Zone-A laptop selling business website
This site is built with Django 3.0.7 and Python 3.8.5


## Key Features

- Login with Google and Facebook using Django Authentication System.
- Payment Gateway integration with SSLCommerz
- User can enquiry about a particular laptop and contact with the laptop dealer through Email using SMTP
    backend.
- Deployed on Heroku Server (Gunicorn, Whitenoise).




## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```bash
  pip install virtualenv
```
Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project
```bash
  virtualenv env
```
That will create a new folder env in your project directory. Next activate it with this command on mac/linux or windows:
```bash
  source env/bin/active
```
Then install the project dependencies with
```bash
  pip install -r requirements.txt
```
Now you can run the project with this command
```bash
  python manage.py runserver
```

## For Admin Login

To run this project, you will need to add the following environment variables to your .env file

`Username : efan06`

`Password : efan1234`

## Visit Website

https://laptopzone.herokuapp.com/


## ScreenShots

```bash
  Home Page
```
![Homepage](https://user-images.githubusercontent.com/43490591/176752417-d4aaeea0-356a-4f06-9f0a-58dde1d16044.jpg)
```bash
  Login UI with facebook and Gmail
```
![Login](https://user-images.githubusercontent.com/43490591/176752617-97955108-3914-40b1-81b2-6765d913135f.jpg)
```bash
  Featured laptop
```
![Featured laptop](https://user-images.githubusercontent.com/43490591/176752690-c09405b9-92f5-4825-8015-6fa490abdfb2.jpg)
```bash
  Laptop Detail
```
![Laptop Detail](https://user-images.githubusercontent.com/43490591/176752789-c2d4ed78-0bad-4728-8dd8-3ac9b8591769.jpg)
```bash
  Cart
```
![Cart Detail](https://user-images.githubusercontent.com/43490591/176752843-758029d0-9d91-404a-b5df-ef31f8d78ec6.jpg)
```bash
  Payment Gateway
```
![Payment Gateway](https://user-images.githubusercontent.com/43490591/176752905-07a9b69b-68c3-422c-9c47-51375c37f25a.jpg)
```bash
  OTP Page
```
![OTP Page](https://user-images.githubusercontent.com/43490591/176752965-29b16a4c-f91d-47f0-a175-4d7d52b6b92f.jpg)
```bash
  Order Detail
```
![Order Detail](https://user-images.githubusercontent.com/43490591/176753027-c757055a-3123-42b0-bb52-c1614e5372c6.jpg)





