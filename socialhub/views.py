from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class SocialPage(generic.TemplateView):
    template_name = "social-media.html"
