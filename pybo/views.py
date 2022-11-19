from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 배지님 민혁서버에 오신것을 환영합니다.")