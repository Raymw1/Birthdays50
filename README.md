# Birthdays50

<img width="728" style="border-radius:10px" src="https://i.imgur.com/2C5mSSh.png" alt="Demo"></a>

## Think about it

Have you ever forgotten the birthday of someone very important to you? Maybe, you have been blaming yourself for a long time.
Wouldn't it be great if you remember the birthday of everyone you want?

That's why Birthdays50 exists!

## Installation

### Prerequisites
- Make sure you have Python3 installed and **you use it to run this program**.
#### [] Install Flask in your machine
Furthermore, you have to make sure you have Flask installed. If not you can use pip or your favorite package manager to install it.
```
pip install flask
```
or in case you use pip3
```
pip3 install flask
```
- The following Packages should be preinstalled but if something is missing make sure these are also ready to use: Sqlite3

### Cloning the Repo
```
mkdir Birthdays50
cd Bithdays50
git clone https://github.com/Raymw1/Birthdays50.git
cd CS50-Final-Project
```

#### Setup

[] Export the application
First you have to set the FLASK_APP environment variable.
Standard Way
```
$ export FLASK_APP=application.py
```
For Windows
```
set FLASK_APP=application.py
```
For Powershell
```
$env:FLASK_APP = "application.py"
```

#### Running it

[] Run the application
```
$ python3 -m flask run
```

## Techs

In this project, I have worked with:
- HTML5 / CSS3
- Python(Flask)
- SQL

## Usage

In this WebApp, you can:

### Add birthdays

On the index page, you shall be able to add the birthdays of anyone you want. You need to write the name of the person, assuming that you didn't use it yet, with a minimum of 3 letters. Then, you need to add the day of the person's birthday. And, finally, you just need to add the month of the person's birthday. Be sure to provide a valid day! After that, the birthday added shall be displayed on your screen, where you can see the name, day, and month of the person. If you want to remove any of these, you just need to click on the button, that is on the right side of the birthday.

### Share birthdays

On the share page, you can select birthdays that you want to share with other people. At the end of the form, you just need to put the receiver username on the platform. Be sure that the username is already registered!

### Receive birthdays

On the friends page, it will be displayed on your screen, the birthdays that other people shared with you. You will see the username of the person that has sent to you, and below, the birthdays they have sent. When you want, you can remove those you don't want anymore.

---
### Do you want to collaborate?

Feel free to make some pull requests, and to tell me some extra ideas!!
