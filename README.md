# Flask-Quiz-API - Readme

Table of Contents:

Introduction

Installation

Usage

Introduction
Welcome to Quiz API - a trivia quiz application that prompts users to fill in a form and, based on their input, generates questions for the user's trivia. It uses an open API to fetch the questions based on the user's preferences.

Installation
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.6 or higher
Flask 1.1.2 or higher
requests

Installing:

Clone the repository: git clone https://github.com/jorgeaponte1/Flask-Quiz-API.git

Navigate into the cloned repository: cd Quiz-API

Set up a virtual environment:

Install virtualenv: pip install virtualenv
Create a virtual environment: virtualenv venv
Activate the virtual environment: source venv/bin/activate (Linux/Mac) or .\venv\Scripts\activate (Windows)
Install the dependencies: pip install -r requirements.txt

Usage:
1. Run the application: python app.py

2. Open a web browser and navigate to http://127.0.0.1:5500/.

3. Fill out the form to select the category, number of questions, difficulty, and type of question. Click on "Submit" when done.

4. The questions will be displayed. Select an answer for each question and then click on "Submit".

5. Your score will be displayed along with the correct answers to the questions.

Endpoints
/ - Renders the landing page where the user can fill in the form to start the trivia quiz.
/categories - Returns JSON data of all categories available for the trivia quiz.
/questions - Based on the form data, fetches and displays the trivia questions.
/score - Displays the user's score and the correct answers to the questions.
