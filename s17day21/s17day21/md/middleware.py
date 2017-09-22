from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class M1(MiddlewareMixin):
    def process_request(self, request):
        print('m1.process_request')
        # return HttpResponse('ok')

    def process_response(self, request, response):
        print('m1.process_reponse')
        return response


class M2(MiddlewareMixin):
    def process_request(self, request):
        print('m2.process_request')
        # return HttpResponse('ok')
    def process_response(self, request, response):
        print('m2.process_reponse')
        return response
