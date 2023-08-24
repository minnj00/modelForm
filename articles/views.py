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
    # 모든 경우의 수
    # 1. GET: From 만들어서 html 문서를 사용자에게 리턴
    # 2. POST invalid data: 데이터 검증에 실패한 경우 
    #     => 검증에 성공한 데이터만 가지고 form을 만들어 html 문서를 사용자에게 리턴
    # 3. POST valid data: 데이터 검증에 성공한 경우
    #    => DB에 데이터 저장 후 detail로 redirect 

    

    # create 에 해당하는 기능 
    # 사용자가 입력한 데이터를 가져와서 DB에 저장
    # 5. POST요청( 데이터가 잘못 들어온 경우) 
    # 10. POST요청( 데이터가 잘 들어온 경우)
    if request.method == 'POST':
        # 6. Form 에 사용자가 입력한 정보(완전히자 않음)를 담아서 form을 생성
        # 11. form 에 사용자가 입력한 정보(완전함)를 담아서 form을 생성
        form = ArticleForm(request.POST)
        # ArticleForm은 request.POST에서 가져온 데이터들을(title, content)
        # 알맞은 위치에 title 과 content를 넣어줌.
        # 또 required 와 같이 적합하지 않은 데이터가 들어오는 것을 막아주는 html코드 자동 작성
        # 여기까지는 frontend의 역할

        # 백엔드에서 한번 더 적합한 데이터인지 검증(프론트엔드는 얼마든지 조작 가능하므로!!)
        # .is_valid() -> T, F 로 출력
        # 7. form 을 검증(실패하면 밑에 else 문이 끝난 곳으로 이동)
        # 12. form 을 검증(검증에 성공한 경우!)
        if form.is_valid(): 
            article = form.save()
            return redirect('articles:detail', id=article.id)
        
        # 만약 잘못된 정보를 입력하였다면 잘 입력한 칸은 유지해줘야 좋음.

    # new 에 해당하는 기능
    # 사용자가 데이터를 입력할 수 있도록 빈 종이를 리턴 
    # 1. GET 요청(맨 처음 게시물 create 할 때는 입력한 값이 아직 없기 때문에)
    else: 
        # 2. 비어있는 form을 만들어서 
        form = ArticleForm()
    # 3. context dict에 담고 
    context = {
        'form': form,

    }
    # 4. create.html을 랜더링
    # 9. create.huml을 랜더링
    return render(request, 'create.html', context)

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    
    return redirect('articles:index')

def update(request, id):
    #기존정보
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        # instance 가 없으면 새로운 게시글 생성이라고 인식함.
        form = ArticleForm(request.POST, instance=article) # 새로 입력한 정보


        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id = article.id)

    else:
        # 기존 정보를 인스턴스에 넣음.
        form = ArticleForm(instance=article)
    
    context ={
        'form': form,
    }
    return render(request, 'update.html', context)

