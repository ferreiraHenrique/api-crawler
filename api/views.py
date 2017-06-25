from django.shortcuts import render, HttpResponse
from requests import get
import json


def run_crawler(request, url, palavra):
    if request.method == 'GET':
        if 'http://' not in url:
            url = 'http://' + url

        try:
            res = get(url)
            codigo_fonte = res.text

            ocorrencia, ocorrencia_identica = 0, 0
            for i, c in enumerate(codigo_fonte):
                if palavra.lower() == codigo_fonte[i:i + len(palavra)].lower():
                    ocorrencia += 1
                if palavra == codigo_fonte[i:i + len(palavra)]:
                    ocorrencia_identica += 1

            context = {
                'status': 200,
                'url': url,
                'palavra': palavra,
                'resultado': {
                    'occorencias': ocorrencia,
                    'identicas': ocorrencia_identica
                },
            }
        except:
            context = {
                'status': 400,
                'url': url,
                'palavra': palavra,
            }
    else:
        context = {
            'status': 403,
            'url': url,
            'palavra': palavra,
        }

    return HttpResponse(json.dumps(context), content_type="application/json")
