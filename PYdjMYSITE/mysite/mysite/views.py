from django.http import HttpResponse
from django.template import loader
from mysite.parser import Parser

def index(request):
    
    p = Parser()
    p.setUrl("https://habr.com/ru/all/")
    p.setSession()
    p.doRequest()
    p.parseUrl()
    latest_question_list = []#['habr', 'mail.ru','yandex']# paser.get()

    for a in p.getLinkA("tm-article-snippet__title-link"):
        # if len(a)>10:
        # print(a.text, "https://habr.com/"+a['href'])
        latest_question_list.append(
            {   "text": a.text,
                "url":"https://habr.com"+a['href']
            }
            )
    
    
    print(__file__)
    print(__file__)
    print(__file__)
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))