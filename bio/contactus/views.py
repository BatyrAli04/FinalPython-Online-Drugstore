from django.shortcuts import render, redirect

from .forms import ContactUsForm


def contactus(request):
    context = {}

    form = ContactUsForm(request.POST or None)
    context['form'] = form
    if form.is_valid():
        form.save()

        return redirect('contactus:contactus')

    return render(request, 'contactus.html', context)