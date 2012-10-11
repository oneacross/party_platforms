import urllib2
import xml.etree.ElementTree as ET
from django.http import HttpResponse
from django.template import Context, loader

def index(request):

    # Fetch XML data
    # FIXME: cache this
    f = urllib2.urlopen('https://raw.github.com/tauberer/party-platforms/master/republican_platform_2012.xml')

    doc = ET.parse(f)

    t = loader.get_template('platform_game/index.html')
    c = Context({
        'party': doc.find('party').text,
        'proposal': doc.iter('proposal').next().text
    })

    return HttpResponse(t.render(c))
