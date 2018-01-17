from django.core.cache import cache
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'home.html'

    def get_hit_count(self):
        try:
            return cache.incr('home_page_hits')
        except ValueError as e:
            cache.set('home_page_hits', 1)
            return cache.get('home_page_hits')

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['hits'] = self.get_hit_count()
        return context
