from django.shortcuts import render
from random import randint


def home(request):
    return render(request, 'home.html', {})


def add(request):
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error handling if question left unanswered
        if not answer:
            my_answer = "You forgot to type your answer"
            color = 'warning'
            return render(request, 'add.html', {
                'color': color,
                'my_answer': my_answer,
                'answer': answer,
                'num_1': num_1,
                'num_2': num_2,
            })

        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = ("Incorrect! " + old_num_1 + " + " + old_num_2 + " is not " + answer + " it is " +
                         str(correct_answer))
            color = "danger"
        return render(request, 'add.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })

    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def subtract(request):
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error handling if question left unanswered
        if not answer:
            my_answer = "You forgot to type your answer"
            color = 'warning'
            return render(request, 'subtract.html', {
                'color': color,
                'my_answer': my_answer,
                'answer': answer,
                'num_1': num_1,
                'num_2': num_2,
            })

        correct_answer = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + old_num_1 + " - " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = ("Incorrect! " + old_num_1 + " - " + old_num_2 + " is not " + answer + " it is " +
                         str(correct_answer))
            color = "danger"
        return render(request, 'subtract.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })

    return render(request, 'subtract.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def multiply(request):
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        # Error handling if question left unanswered
        if not answer:
            my_answer = "You forgot to type your answer"
            color = 'warning'
            return render(request, 'multiply.html', {
                'color': color,
                'my_answer': my_answer,
                'answer': answer,
                'num_1': num_1,
                'num_2': num_2,
            })

        correct_answer = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + old_num_1 + " x " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = ("Incorrect! " + old_num_1 + " x " + old_num_2 + " is not " + answer + " it is " +
                         str(correct_answer))
            color = "danger"
        return render(request, 'multiply.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })
    return render(request, 'multiply.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def divide(request):
    num_1 = randint(0, 10)
    num_2 = randint(1, 10)

    if request.method == "POST":
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']
        # Error handling if question left unanswered
        if not answer:
            my_answer = "You forgot to type your answer"
            color = 'warning'
            return render(request, 'divide.html', {
                'color': color,
                'my_answer': my_answer,
                'answer': answer,
                'num_1': num_1,
                'num_2': num_2,
            })

        correct_answer = int(old_num_1) / int(old_num_2)
        if float(answer) == correct_answer:
            my_answer = "Correct! " + old_num_1 + " / " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = ("Incorrect! " + old_num_1 + " / " + old_num_2 + " is not " + answer + " it is " +
                         str(correct_answer))
            color = "danger"
        return render(request, 'divide.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
        })
    return render(request, 'divide.html', {
        'num_1': num_1,
        'num_2': num_2,
    })
