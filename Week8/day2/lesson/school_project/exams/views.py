from django.shortcuts import render
import random
import json
# Create your views here.
def home(request):
    questions = _read_file()
    question = random.choice(questions)
    return render(request, 'base.html', {'question':question})

def question(request, id):

    questions = _read_file()
    try:
        question = questions[id-1]
        return render(request, 'selectq.html', {'question':question})
    except IndexError:
        return render(request, '404page.html')

def _read_file():
    with open('questions.json', 'r') as f:
        data = json.load(f)

    questions = data['questions']
    return questions

    