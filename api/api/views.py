from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

@api_view(['POST'])
def pitagorasCalculator(request):
    triangle_sides = {}
    for side,value in request.data.items():
        try:
            triangle_sides[side] = int(value) 
        except ValueError:
            error_msg = {"message": f'O campo {side} não possui um inteiro válido. o valor informado foi {value}'}
            status_code = 400
            response = Response(error_msg, status_code)
            return response

    if len(triangle_sides.keys()) != 3:
        error_msg = {"message":'É necessário informar os 3 lados'}
        status_code = 400
        response = Response(error_msg, status_code)
        return response
    
    calculation_msg = {
        "isvalid" : True
    }
    
    if triangle_sides['catetoOposto']**2 + triangle_sides['catetoAdjacente']**2 != triangle_sides['hipotenusa']**2:
        calculation_msg['isvalid'] = False
    
    return Response(calculation_msg)

