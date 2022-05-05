from django.views.generic import TemplateView
class HomePage(TemplateView):
    template_name='index.html'

class AboutView(TemplateView):
    template_name='about.html'

class ContactView(TemplateView):
    template_name='contactUs.html'
