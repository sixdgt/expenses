from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages

# Create your views here.

@login_required(login_url='/authentication/login')
def index(request):
    categories = Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)
    context = {"categories": categories, "expenses": expenses}
    return render(request, 'expenses/index.html', context)

def add_expense(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
        "values": request.POST
    }

    if request.method == "POST":
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')
        category = request.POST.get('category')

        if not amount:
            messages.error(request, "Amount is required")
            return render(request, "expenses/add_expense.html", context)
        if not description:
            messages.error(request, "Description is required")
            return render(request, "expenses/add_expense.html", context)
        
        Expense.objects.create(amount=amount, description=description,
        category=category, date=date, owner=request.user)
        messages.success(request, "Expense added successfully")
        return redirect("expenses")

    return render(request, "expenses/add_expense.html", context)


def edit_expense(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        "values": expense,
        "categories": categories
    }
    if request.method == "GET":
        return render(request, "expenses/edit_expense.html", context)
    
    if request.method == "POST":
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')
        category = request.POST.get('category')

        if not amount:
            messages.error(request, "Amount is required")
            return render(request, "expenses/edit_expense.html", context)
        if not description:
            messages.error(request, "Description is required")
            return render(request, "expenses/edit_expense.html", context)
        
        expense.amount= amount
        expense.description=description
        expense.category=category
        expense.date=date
        expense.owner=request.user
        expense.save()
        messages.success(request, "Expense updated successfully")
        return redirect("expenses")

def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, "Expense removed")
    return redirect("expenses")

