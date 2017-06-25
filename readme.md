# API Crawler

A API Crawler serve para contar uma palavra especifica no código fonte de um site

## Como usar

url: api/{url}/{palavra}

A API retornara um JSON com a seguinte estrutura

{

    'status': ,

    'url': ,

    'palavra': ,

    'resultado': {

        'identicas': ,

        'ocorrencias':

    }

}

Em resultado, é possível encontrar as quantidade de ocorrências totais da palavra no código fonte e também

a quantidade de ocorrências identicas da palavra.