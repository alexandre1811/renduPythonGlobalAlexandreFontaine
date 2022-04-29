from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question
from .forms import QuestionForm


def index(request):
    questions = Question.objects.all()
    context = {'questions': questions, }
    return render(request, "crud/index.html", context)


def create(request):
    context = {}
    formulaireCreate = QuestionForm(request.POST or None)
    if formulaireCreate.is_valid():
        formulaireCreate.save()
        return HttpResponseRedirect("/")
    context['formulaireCreate'] = formulaireCreate
    return render(request, "crud/create.html", context)


def details(request, id):
    context = {"data": Question.objects.get(id=id)}
    return render(request, "crud/details.html", context)


def update(request, id):
    context = {}
    recuperation = get_object_or_404(Question, id=id)
    formulaireUpdate = QuestionForm(request.POST or None, instance=recuperation)
    if formulaireUpdate.is_valid():
        formulaireUpdate.save()
        return HttpResponseRedirect("/")
    context["formulaireUpdate"] = formulaireUpdate
    return render(request, "crud/update.html", context)


def delete(request, id):
    recuperation = get_object_or_404(Question, id=id)
    if request.method == "POST":
        recuperation.delete()
        return HttpResponseRedirect("/")

    return render(request, "crud/delete.html")
