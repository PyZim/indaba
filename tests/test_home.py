import pytest

def test_home_page(rf):
    request = rf.get("/")
    response = TemplateView.as_view()(request)
    assert response.template_name == "home.html"

