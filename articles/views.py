from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

# 인덱스가 하는 일은 게시물들을 보여주는 것
def index(request):
    articles = Article.objects.all()

    context ={
        'articles': articles
    }
    return render(request, 'index.html', context )

def detail(request, id):
    article = Article.objects.get(id=id)
    context ={
        'article': article,

    }
    return render(request, 'detail.html', context)

def create(request):
    # create 에 해당하는 기능 
    # 사용자가 입력한 데이터를 가져와서 DB에 저장
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # ArticleForm은 request.POST에서 가져온 데이터들을(title, content)
        # 알맞은 위치에 title 과 content를 넣어줌.
        # 또 required 와 같이 적합하지 않은 데이터가 들어오는 것을 막아주는 html코드 자동 작성
        # 여기까지는 frontend의 역할

        # 백엔드에서 한번 더 적합한 데이터인지 검증(프론트엔드는 얼마든지 조작 가능하므로!!)
        # .is_valid() -> T, F 로 출력
        if form.is_valid(): 
            article = form.save()
            return redirect('articles:detail', id=article.id)
        
        # 만약 잘못된 정보를 입력하였다면 잘 입력한 칸은 유지해줘야 좋음.
        else: 
            # form = ArticleForm()

            context = {
                'form': form,
            
            }
            return render(request, 'create.html', context)
        
    # new 에 해당하는 기능
    # 사용자가 데이터를 입력할 수 있도록 빈 종이를 리턴 
    else: 
        form = ArticleForm()
    
        context = {
            'form': form,

        }

        return render(request, 'create.html', context)
    