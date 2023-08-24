# Project

## 0. setting

1. 폴더 생성 후 이동
2. vscode 실행
3. django-admin startproject
4. 가상환경 설정 및 활성화
5. django 설치
6. `README.md`, `.gitignore` 생성

## 1. App 생성 
1. django-admin startapp articles

## 2. settings.py

1. 앱등록
2. 공용 templates 공간 등록(`DIRS`)
3. TIME_ZONE

## 3. Model

1. 모델링(models.py 작성) : 어떤 데이터들을 어디 저장할지 정하는 것들 
ex) 인스타그램: 게시물, 팔로우, 팔로잉, 프로필 등등
2. makemigrations