from django.shortcuts import render

calculos = []


def index(request):
    
    if request.method == 'POST':
        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        anio =  int(request.POST.get('año'))

        tasa = tasa / 100 / 12
        anio = anio * 12
        cuota = (monto * tasa) / (1 - (1 + tasa) ** -anio)
        total_pagar = cuota * anio
      
        tasa  = int(tasa * 100 * 12)
        anio = int(anio / 12)
        cuota = format(cuota, ".3f")
        total_pagar = format(total_pagar, ".3f")
        


        calculos.append({
            'monto': monto,
            'tasa':tasa,
            'anio':anio,
            'cuota':cuota,
            'total':total_pagar
        })  

        ctx = {'calculos' : calculos}
        return render(request,'registro/index.html',ctx)
    else :
        ctx = {'calculos' : calculos}
        return render(request,'registro/index.html',ctx)
