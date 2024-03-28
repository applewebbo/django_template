from django.template.response import TemplateResponse

def index(request):
    context = {"project_name": '{{ project_name }}'}
    return TemplateResponse(request, 'index.html', context)
 