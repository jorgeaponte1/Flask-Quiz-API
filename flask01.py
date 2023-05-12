#!/usr/bin/env python3
""" Jorge Aponte | jorgealyaponte@yahoo.com
   A simple Flask server. This server has the following endpoints:
   
   /               - GET Renders Landingpage html
   
   /categories     - GET Sends JSON data of all the categories we showcase in the trivia.
   
   /questions      - a POST will have the form read for all the data in the form
                   
   /score          - POST response display the user's score and showcase how many questions they got correct.
                     Also, renders answers.html which will display the questions and answers of the trivia.                
                   """

from flask import Flask, render_template, request, jsonify
import requests
from html import unescape
from random import shuffle

app= Flask(__name__)

# URL of the API I'm referring for data
API_BASE_URL= "https://opentdb.com/api.php?"

# Declaring variables I will need for all functions to communicate with
questionslist = {}

## start of the changes

# Gets the questions from the Quiz API and returns the data of the questions, correct answers, and wrong answers
def questions_from_trivia(category,numberOfQuestions,difficulty,questionType):
    global questionslist
    endpoint = f"{API_BASE_URL}&category={category}&amount={numberOfQuestions}&difficulty={difficulty}&type={questionType}"
    print(endpoint)
    data = requests.get(endpoint).json()
    i = 1
    if data:
        for question in data['results']:
            choices = question['incorrect_answers'] + [question['correct_answer']]
            shuffle(choices)
            questionslist.update({i: {'question': unescape(question['question']), 
                                    'incorrect_answers': unescape(question['incorrect_answers']), 
                                    'correct_answer': unescape(question['correct_answer']), 
                                    'answers': unescape(choices)}})
            i += 1

# Returns a list of all the categories from the Quiz API so I may use on the "/" and "/categories" endpoint
def fetch_category_data():
    category_data = requests.get("https://opentdb.com/api_category.php").json()
    category_list = []
    for category in category_data['trivia_categories']:
        category_list.append(category)
    return category_list

# Landing Page route endpoint to display index.html file
@app.route('/',methods=['GET'])
def landingpage():
    category_data = fetch_category_data()
    questionslist.clear()
    return render_template('index.html', category_data=category_data)

#supplies random questions to the user based on their form submission or request
@app.route('/questions', methods=["POST"])
def questions():
    # Return new questions when form is submitted
    if request.method == "POST":
        category= request.form['trivia_category']
        numberOfQuestions= request.form['trivia_amount']
        difficulty = request.form['trivia_difficulty']
        questionType= request.form['trivia_type']
        
        questions_from_trivia(category,numberOfQuestions,difficulty,questionType)
        return render_template('questions.html', questionsData=questionslist.values())

# Routes endpoint will render the answers.html with the data from the last form submission.
@app.route('/score', methods=['POST'])
def score():  
    user_answers = []
    score = 0
    num_questions = len(questionslist)
    for i in range(1, num_questions + 1):
        user_answers.append(request.form.get(f'user_answer_{i}'))
        
    for i in range(1, len(user_answers) + 1):
        if user_answers[i-1] == questionslist[i]['correct_answer']:
            score += 1
    score_percentage = ((score/len(user_answers))*100)
    score_str = f"{score}/{len(user_answers)} ({score_percentage:.2f}%)"
    return render_template('answers.html', score=score_percentage, score_prompt=score_str ,questionsData=questionslist.values(), user_answers=user_answers)
    
# Returns JSON data of all the categories that are used in the Quiz API. Adjusted the OG dictionary to be easily readible.
@app.route('/categories', methods=['GET'])
def category():
    category_list = fetch_category_data()
    return jsonify(category_list)

    
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5500, debug=True)