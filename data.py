import requests

parameters ={
"amount":20,
"difficulty": "hard",
"type": "boolean",
}

questions_request = requests.get(url="https://opentdb.com/api.php",params=parameters)
questions_request.raise_for_status()
questions = questions_request.json()
questions = questions["results"]
question_data = questions

