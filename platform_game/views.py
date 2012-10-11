from django.http import HttpResponse
from django.template import Context, loader
from platform_game.models import get_platform

def index(request):

    platform = get_platform('Republican')

    t = loader.get_template('platform_game/index.html')
    c = Context(platform)

    return HttpResponse(t.render(c))
