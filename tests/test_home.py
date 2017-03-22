import pytest
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

def test_page(rf):
    request = rf.get(reverse("home"))
    response = TemplateView.as_view(template_name="home.html")(request)
    assert response.template_name[0] == "home.html"

