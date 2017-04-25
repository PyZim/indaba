from django.conf.urls import  url, include
from indaba.talks.views import (CreateTalk, TalkView, TalkListView,)

urlpatterns = [
    url(r'^submit_talk', CreateTalk.as_view(), name='create_talks'),
    url(r'^talks', TalkListView.as_view(), name='talks_list'),
    url(r'^(?P<pk>\d+)/$', TalkView.as_view(), name='indaba_talk'),
    ]

