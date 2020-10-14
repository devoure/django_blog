from django.shortcuts import render
#the next import is for finding your templates
from django.template.loader import get_template
from django.http import HttpResponse
#from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.forms import UserCreationForm
from article.forms import ArticleForm, CommentForm
from article.models import Article,Comment
from django.template.context_processors import csrf
from django.utils import timezone
# Create your views here.

def hello (request):
    name = "Athman"
    html = "<html><body>Hi %s ,this seems to have worked, CONGRATS!!</body></html>"%name
    return HttpResponse(html)

def hello_template (request):
    name = "Athman"
    t = get_template('hello.html')
    ctx={'name':name}
    html =t.render(ctx)
    return HttpResponse(html)

class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_context_data (self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = "Athman"
        return context
@requires_csrf_token
def articles (request):
    language = 'en-us'
    session_language = 'en-us'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    args = {}
    args.update(csrf(request))

    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language



    return render(request, 'articles.html', args)
                 # content_type='application/xhtml+xml')


def article (request, article_id=1):
    return render(request,
                  'article.html',{
                      'article': Article.objects.get(id=article_id)})
                  #content_type='application/xhtml+xml')

def language (request, language ='en-us'):
    response = HttpResponse("setting language to %s "% language)
    response.set_cookie('lang', language)

    request.session['lang'] = language
    return response

@requires_csrf_token
def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/articles/all')
    else:
        form = ArticleForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
    return render(request, 'create_article.html', args)

def like_article (request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()

    return redirect('/articles/get/%s' % article_id)

@requires_csrf_token
def add_comment (request, article_id):
    a = Article.objects.get(id = article_id)

    if request.method == 'POST':
        f = CommentForm(data=request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()

            return redirect('/articles/get/%s' % article_id)
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    args['article'] = a
    args['form'] = f

    return render(request, 'add_comment.html', args)


def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    articles = Article.objects.filter(title__contains = search_text)
    return render(request, 'ajax_search.html', {'articles' : articles})
