# donationApp

*** 

## Table of content

* [Introduction](#introduction)
* [Installation](#installation)
* [Technologies](#technologies)
* [Requirements](#requirements)
* [Features](#features)
* [To-do](#to-do)
* [Additional info](#additional-info)


***

## Introduction

This app makes it possible to donate your unwanted items to a charity of your choosing. No matter, clothes, toys, books - you can simply choose a charity that handles such things, put in your adress and choose a date for a courier to pick those up. Using the app is free of charge and makes all the difference for people in need.

***

## Installation
Fork this repository and clone it. Remember to make local_settings.py in your main directory and put your database connection details in there! After all of that, simply make migration to your DB and then migrate the necessary tables.

***
## Technologies

The app was created using:

```
* Python 3.11
* Django 4.2.3
* HTML 5
* JavaScript
* PostgreSQL
```

## Requirements

```
* Django==4.2.3
* psycopg2-binary 2.9.6
```

***

## Features

+ ADMIN (PAGE)
  * login
  * manage admins
  * manage supported charities
  * browse donations
    
+ USER
  * register
  * login
  * make donations
  * browse own donations
    - each donation show information on what charity it's for, how many bags and what do they contain
    - sorted by "delivered" or "to be picked up"
    - delivered donations have time stamps when it was checked as picked up
  * confirm that a donation was picked up
  * change password
    
+ LANDING PAGE
  * number of all bags donated
  * number of charities helped
  * list of charities that are working with one's company
    
+ DONATION FORM
  * make donation
  * summary of a donation is visible at the end of the form
  * only registered users can make donations
    

***

## To-do
+ USER
  - [ ] user being able to change their data
  - [ ] e-mail verification for creating an account / verification
  - [ ] "I forgot my password" option using an e-mail
  - [ ] user's password validation (at leats 8 characters long, containg at least 1 capital letter, 1 number and a special character)
  - [ ] contact form

+ ADMIN (PAGE)
  - [ ] a superuser cannot delete all admins

+ DONATION FORM
  - [ ] live validation of donation form
  - [ ] filtering charities by previously chosen categories of items to donate

+ LANDING PAGE
  - [ ] pagination of charities working with one's company

***

## Additional info

This app uses Polish time (UTC+01:00) and language.
Original page layoput and CSS were delivered by [Coder's Lab](https://github.com/CodersLab).
