from django.shortcuts import render
from django.urls import reverse
from django.template.loader import get_template
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Bb

from .models import Rubric

#классы для ввода
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import BbForm
from django.http import StreamingHttpResponse
from django.http import FileResponse


def add_and_save (request):
    if request.method == 'POST':
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
        else:
            context = {'form': bbf}
            return render(request, 'bboard/create.html', context)
    else:
        bbf = BbForm()
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context)



def add(request):
    bbf = BbForm()
    context = {'form':bbf}
    return render(request,'bboard/create.html',context)

def add_save(request):
    bbf = BbForm(request.POST)
    if bbf.is_valid():
        bbf.save()
        return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id':bbf.cleaned_data['rubric'].pk}))
    else:
        context ={'form':bbf}
        return render(request,'bboard/create.html',context)



#форма ввода данных
class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')
    #success_url = '/bboard/'
#выводим или добавляем список рубрик
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics']=Rubric.objects.all()
        return context



def by_rubric(request,rubric_id):
    bbs=Bb.objects.filter(rubric=rubric_id)
    #print(bbs)
    rubrics = Rubric.objects.all()
    #print(rubrics)
    current_rubric = Rubric.objects.get(pk=rubric_id)
    contex = {'bbs':bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render(request,'bboard/by_rubric.html',contex)

def index5(request):
    filename = r'c:/temp/q1.jpg'
    return FileResponse(open(filename, 'rb'), as_attachment=True)


def index4(request):
    resp_content = ('Здесь', 'будет главная страница сайта')
    resp=StreamingHttpResponse(resp_content, content_type='text/plain; charset=utf-8')
    resp['keywords'] = 'Python, Django'
    return resp

def index3(request):
    #вывод страницы с группами/разделами
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics':rubrics}
    template = get_template('bboard/index.html')
    return HttpResponse(template.render(context=context, request=request))

def index2(request):
    resp = HttpResponse('Здесь будет', content_type='text/plain; charset=utf-8')
    resp.write(' главная')
    resp.writelines({' страница', ' сайта'})
    resp['keywords'] = 'Python, Django'
    return resp

def index(request):
    #вывод страницы с группами/разделами
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics':rubrics}
    return render(request,'bboard/index.html', context)


    #вывод страницы по шаблону
    #bbs = Bb.objects.order_by('-published')
    #return render(request,'bboard/index.html',{'bbs':bbs,'zz':'Текст переменная'})

    #template = loader.get_template('bboard/index.html')
    #bbs = Bb.objects.order_by('-published')
    #context = {'bbs':bbs,'zz':'Какая то Переменная'}
    #print(template.render(context,request))
    #return HttpResponse(template.render(context,request))

    #s='Список объявлений\r\n\r\n\r\n'
    #for bb in Bb.objects.order_by('-published'):
    #    s+=str(bb.id)+' '+bb.title+'\r\n'+bb.content+'\r\n\r\n'
    #return HttpResponse(s, content_type='text/plain; charset=utf-8')

    #return HttpResponse("Здесь будет выведен список объявлений.")


