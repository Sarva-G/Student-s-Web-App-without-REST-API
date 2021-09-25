from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View
from without_rest_api_app.mixins import HttpResponseMixin


def employee_data_view(request):
    emp_data = {
        'eno': 100,
        'ename': 'Padmaja Rajagopalan',
        'esal': '45,000',
        'eaddress': 'Vizag'
    }
    resp = '<h3>Employee Number:{}<br>Employee Name:{}<br>Employee Salary:{}<br>' \
           'Employee Address:{}</h3>'.format(emp_data['eno'], emp_data['ename'], emp_data['esal'], emp_data['eaddress'])
    return HttpResponse(resp)


def employee_json_view1(request):
    emp_data = {
        'eno': 100,
        'ename': 'Padmaja Rajagopalan',
        'esal': '45,000',
        'eaddress': 'Vizag'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type='application/json')  # MIME - Multipurpose Internet Mail Extension


def employee_json_view2(request):  # import json
    emp_data = {
        'eno': 100,
        'ename': 'Padmaja Rajagopalan',
        'esal': '45,000',
        'eaddress': 'Vizag'
    }
    return JsonResponse(emp_data)


class JsonCBV(HttpResponseMixin, View):  # Multiple Inheritance used here, CBV - Class Based View
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from GET method'})
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from POST method'})
        return self.render_to_http_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from PUT method'})
        return self.render_to_http_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from DELETE method'})
        return self.render_to_http_response(json_data)
