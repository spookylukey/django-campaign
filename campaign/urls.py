from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^view/(?P<object_id>[\d]+)/$', 'campaign.views.view_online', {}, name="campaign_view_online"),
)
