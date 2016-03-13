"""
actor_loader.py: Handles the scraping of actor data from IMDB

Copyright 2016 Jason Doucette, Thrust Labs Inc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import re
import urllib
from soup_util import SoupUtil


class ActorLoader(object):

    def __init__(self):
        self.actors = None

    def load(self, title):
        url = "http://www.imdb.com/title/{}/fullcredits".format(title)
        html = urllib.urlopen(url).read()
        return self.parse(html)

    def parse(self, html):
        util = SoupUtil()
        soup = util.soup(html)

        title_link = soup.find(class_='subnav_heading')
        title_id = re.search('/title/([^/]+)/',
                             title_link.get('href')).group(1)
        title_name = title_link.string

        actors = soup.find_all(itemprop='actor')
        result = []
        for actor in actors:
            url = actor.find(itemprop='url')
            imdb_id = re.search('/name/([^/]+)/', url.get('href')).group(1)
            name = url.find('span').string
            role_elem = actor.find_next_sibling('td', 'character').find('div')
            raw_role = ' '.join([text for text in role_elem.stripped_strings])
            role = Role(util.supertrim(unicode(raw_role)),
                        unicode(title_id),
                        unicode(title_name))
            result.append(Actor(unicode(name), unicode(imdb_id), role))
        return result


class Actor(object):
    def __init__(self, name=None, imdb_id=None, role=None):
        self.name = name
        self.imdb_id = imdb_id
        if role is not None:
            self.roles = [role]
        else:
            self.roles = None

    def add_role(self, role):
        if self.roles is None:
            self.roles = []
        self.roles.append(role)

    def __unicode__(self):
        return u"{} / {} / {}".format(self.name, self.imdb_id, self.roles)


class Role(object):
    def __init__(self, name=None, title_id=None, title_name=None):
        self.name = name
        self.title_id = title_id
        self.title_name = title_name

    def __unicode__(self):
        return u"{} / {} / {}".format(
            self.name, self.title_id, self.title_name)
