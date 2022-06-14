from http.client import HTTPResponse
from django.shortcuts import render
from django.conf import settings
from .myModels import *
from .models import *
# Create your views here.
def index(req):
    # f = open(settings.BASE_DIR/'primes1.txt', 'r')
    # f1 = open(settings.BASE_DIR/'primes2.txt', 'r')
    ctx = dict()
    # snts = f.read().replace("\n", "").split(" ")
    # snts.extend(f1.read().replace("\n", "").split(" "))
    # print(len(snts))
    # snts = list(filter(None, snts))
    # # snts = list(filter('\n', snts))
    # snts = list(map(int, snts))
    # print(len(snts))
    # f.close()
    # f1.close()

    # ctx['snts'] = snts
    if req.method == 'POST':
        # print(req.POST)
        q = int(req.POST['sntq'])
        p = int(req.POST['sntp'])
        b = int(req.POST['sntb'])
        n = int(req.POST['n'])
        phi = int(req.POST['phi'])
        bs1 = bs(phi, b)
        a = bs1.kq() % phi
        r = rsa(p=p,q=q,b=b,n=n,phi=phi,a=a)
        r.save()
        # rsa.objects.create(r)
        
        
    return render(req, 'mainApp/index.html', ctx)

def danhSachChia(req):
    ctx = dict()
    ctx['ds'] = list(rsa.objects.all())
    return render(req, 'mainApp/danhSachChia.html', ctx)