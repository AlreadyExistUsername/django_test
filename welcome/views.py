# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django import forms
from models import Msg
from django.http import HttpResponseRedirect


class MsgForm(forms.Form):
    msg = forms.CharField(label='Сообщение', max_length=200)


def main(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MsgForm(request.POST)
        if form.is_valid():
            msg = form.cleaned_data['msg']
            if len(msg) > 0:
                Msg(body=msg).save()
        return HttpResponseRedirect('/thanks/')
    else:
        form = MsgForm()

        return render(request, 'index.html', {"stories": Msg.objects.all(), 'form': form})
