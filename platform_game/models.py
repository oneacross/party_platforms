import urllib2
import xml.etree.ElementTree as ET
#from django.db import models

def party_url(party):
    if party == 'Republican':
        return 'https://raw.github.com/tauberer/party-platforms/master/republican_platform_2012.xml'
    elif party == 'Democratic':
        return 'https://raw.github.com/tauberer/party-platforms/master/democratic/democratic_platform_2012.xml'
    elif party == 'Libertarian':
        return 'https://raw.github.com/tauberer/party-platforms/master/libertarian_platform_2012.xml'

# API
def get_platform(party):

    url = party_url(party)

    # Fetch XML data
    # FIXME: cache this
    f = urllib2.urlopen(url)

    doc =  ET.parse(f)

    proposals = [x.text for x in list(doc.iter('proposal'))]

    platform = {
        'party': doc.find('party').text,
        'year': doc.find('year').text,
        'proposals': proposals,
    }

    return platform

