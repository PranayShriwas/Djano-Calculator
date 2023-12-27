from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        num1 = eval(request.POST['num1'])
        num2 = eval(request.POST['num2'])
        opr = request.POST['opr']
        if opr == '+':
            result = num1 + num2
        elif opr == '-':
            result = num1 - num2
        elif opr == '*':
            result = num1 * num2
        elif opr == '/':
            result = num1 / num2
        else:
            result = "Invalid Operator"

        return render(request, 'index.html', {'result': result, 'num1': num1, 'num2': num2, 'opr': opr})

    return render(request, 'index.html')
