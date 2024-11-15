from django.shortcuts import render, get_object_or_404,HttpResponseRedirect

from .models import Article

# Create your views here.


def main(request):
    return render(request, 'python1HTML.html')


def karim(request):
    return render(request, 'python1HTML.html', {'name': 'karim', 'age': '20', 'job': 'enginer', 'salary': '100k', 'phone': '01234567890', 'location': 'october'})


def elias(request):
    return render(request, 'python1HTML.html', {'name': 'elias', 'age': '30', 'job': 'manager', 'salary': '100k', 'phone': '01234567890', 'location': 'october'})


def yousef(request):
    return render(request, 'python1HTML.html', {'name': 'yousef', 'age': '22', 'job': 'enginer', 'salary': '100k', 'phone': '01234567890', 'location': 'october'})


def ahmed(request):
    return render(request, 'python1HTML.html', {'name': 'ahmed', 'age': '26', 'job': 'HR', 'salary': '100k', 'phone': '01234567890', 'location': 'october'})


def sief(request):
    return render(request, 'python1HTML.html', {'name': 'sief', 'age': '23', 'job': 'assistant manager', 'salary': '100k', 'phone': '01234567890', 'location': 'october'})


def ramy(request):
    return render(request, 'python1HTML.html', {'name': 'ramy', 'age': '29', 'job': 'Enginer', 'salary': '100k', 'phone': '01234567890', 'location': 'october'})


def malak(request):
    return render(request, 'python1HTML.html', {'name': 'malak', 'age': '27', 'job': ' Enginer ', 'salary': '100k', 'phone': '01234567890', 'location': 'october'})


def abdelrahman(request):
    return render(request, 'python1HTML.html', {'name': 'abdelrahman', 'age': '20', 'job': 'main manager', 'salary': '100k', 'phone': '01234567890', 'location': 'october'})


def second(request):
    return render(request, 'second page.html')


def ahmed_hani(request):
    return render(request, 'second page.html', {'name': 'Ahmed_Hani', 'work_h': '100'})


def yousef_hamada(request):
    return render(request, 'second page.html', {'name': 'Yousef_Hamada', 'work_h': '55'})


def retag_yasser(request):
    return render(request, 'second page.html', {'name': 'Retag_Yasser', 'work_h': '70'})


def all_articles(request):
    return render(request, 'article.html', {'data': Article.objects.all()})


def article_details(request, n=None):
    return render(request, 'details.html', {'data': get_object_or_404(Article,id=n)})


#def css(request):
#    return render(request, 'zeko.html')


def form(request):
    return render(request,"form.html")


def add_article(request):
    if request.method == "POST":
        if request.POST.get('id') and request.POST.get('title') and request.POST.get('author') and request.POST.get('depart') and request.POST.get('content'):
           art = Article()
           art.id = request.POST.get('id')
           art.title = request.POST.get('title')
           art.author = request.POST.get('author')
           art.depart = request.POST.get('depart')
           art.content = request.POST.get('content')
           art.save()

           return HttpResponseRedirect ("/articles/")

    else:
        return render(request,"form.html")


def delete_article(request,n=None):
    Article.objects.filter(id=n).delete()
    return HttpResponseRedirect("/articles/")
    return render(request,"form.html")


def update_article(request,n=None):
    if request.method == "POST":
       if request.POST.get("id") and request.POST.get("title") and request.POST.get("author") and request.POST.get("depart") and request.POST.get("content"):
          Article.objects.filter(id=n).update(id=request.POST.get("id"),title=request.POST.get("title"),author=request.POST.get("author"),depart=request.POST.get("depart"),content=request.POST.get("content"))

          return HttpResponseRedirect ("/articles/")
    else:
        return render(request,'form.html',{'data':get_object_or_404(Article,id=n)})


def Home(request):
    return render(request,"index.html")


#def Home2(request):
#    return render(request,"index2''.html")


#def About(request):
#    return render(request,"about.html")


#def cate(request):
#    return render(request,"category.html")


#def WORK(request):
#    return render(request,"work.html")


#def Home3(request):
#    return render(request,"index3.html")


#def Home4(request):
#    return render(request,"index-4''.html")


#def contact(request):
#    return render(request,"contact.html")


#def Home5(request):
#    return render(request,"index5.html")


#def Team(request):
#    return render(request,"team.html")


#def ser(request):
#    return render(request,"service.html")


#def About2(request):
#    return render(request,"about2(4).html")








































