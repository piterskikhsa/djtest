from django.conf.urls import url

from .views import list_new_questions, list_popular_questions, question_detail

urlpatterns = [
    url(r'^$', list_new_questions, name='new_question'),
    url(r'^popular/$', list_popular_questions, name='popular_question'),
    url(r'question/(?P<pk>\d+)/$',question_detail, name='question_detail'),
]