from django.views.generic import TemplateView

# Create your views here.

class AboutPage(TemplateView):
    """
    Displays about page"
    """
    template_name = 'about/about.html'