from multiprocessing import context
from django.shortcuts import render
from APP.models import Diak
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required(login_url='') ezt majd a masik view elejére kell
def fuggveny(request):
    
    context = {}

    if request.method == "POST":
        diak_id = request.POST['diakid']
        print(diak_id)
        if diak_id == "0":
            context['vaneinput'] = False
        else:
            context['vaneinput'] = True

            diak = Diak.objects.filter(oktatasi_azonosito = diak_id).first()
            if diak == None:
                context['voltilyen'] = False
            else:
                context['voltilyen'] = True
                context['felvettek'] = diak.felvettek_e
                context['nev'] = diak.nev

                


        

    template="index.html"
    
    
    return render(request, template, context)
