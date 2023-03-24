from django.shortcuts import render
from myapp1.models import Parsing

# Create your views here.
def index_page(request):    
    parsing_result_list = Parsing.objects.all()
    
    print('')
    print(parsing_result_list)
    print('')
    
    for i in parsing_result_list:
        print(f'{i.id} :: {i.title}')
    print('')
    
    return render(request, "index.html")