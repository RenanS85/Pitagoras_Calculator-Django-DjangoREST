from django.shortcuts import render
import requests
import json

def calculator_index(request):
    if request.method == 'GET':
        return render(request, "calculator_index/calculator_index.html")
    else:
        hipotenusa = request.POST.get('hipotenusa')
        catetoOposto = request.POST.get('catetoOposto')
        catetoAdjacente = request.POST.get('catetoAdjacente')
        if (
            hipotenusa and catetoOposto or 
            hipotenusa and catetoAdjacente or 
            catetoOposto and catetoAdjacente or 
            hipotenusa and catetoOposto and catetoAdjacente
        ):
            r = requests.post('https://api-pitagoras.herokuapp.com/',json= {"hipotenusa": hipotenusa, "catetoOposto": catetoOposto, "catetoAdjacente": catetoAdjacente})
            apiresponse = r.json()
            if apiresponse['isvalid']:
                isvalid = 'Os 3 lados são válidos'
            else:
                isvalid = 'A soma dos quadrados dos catetos não correspodem ao quadrado da hipotenusa'
          

        return render(request, "calculator_index/calculator_index.html",context={'apiresponse': isvalid, 'hipotenusa': hipotenusa, 'catetoOposto': catetoOposto, 'catetoAdjacente': catetoAdjacente})

