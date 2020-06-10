from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from . import models
from . import forms


class GetSlabData(View):
    def get(self, request):
        data = []
        slab_data = models.SlabDetails.objects.values()
        for slab in slab_data:
            data.append({"slab":slab['slab'], "id":slab['id'], "amount":slab["slab_amount"]})
        return JsonResponse(data, safe=False)

class GetSelectedData(View):
    def get(self, request):
        print(request.GET,"POSTTTTT")
        selected_slab = request.GET['data']
        comm_models = models.SetCommission.objects.filter(slab_id=selected_slab)
        ret_data = []
        for i in comm_models:
            print(i)
            ret_data.append({"slab":i.slab.slab, "comm":i.commission.commission, "share":i.share})
        return JsonResponse({"data":ret_data}, safe=False)

class CommissionView(View):
    def get(self, request):
        print("Get called...")
        return render(request, 'slab.html', {"data":"data"})

    def post(self, request):
        print("this is request...",request.POST)
        form = forms.MakeCommissionForm(request.POST)
        print("IS valid : ",form.is_valid())
        if form.is_valid():
            a = form.cleaned_data['dist_id']
            print(a)
            form.save()
        else:
            print("Form Errors : ",form.errors)
        return render(request, 'slab.html', {"form":form})

class PostCreateCommission(View):
    def post(self, request):
        print("Here request is",request.POST)
        form = forms.PostCommissionForm(request.POST)
        print("Is Valid : ",form.is_valid())
        if form.is_valid():
            form.save()
        else:
            print("Post create error : ",form.errors)
        return render(request, 'slab.html', {"form":form})
