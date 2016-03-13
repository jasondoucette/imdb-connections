"""
test_actor_loader.py: Test for the ActorLoader class

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
import unittest
from os.path import join, dirname
from lib.actor_loader import ActorLoader


class TestActorLoader(unittest.TestCase):

    def test_parser(self):
        sut = ActorLoader()
        test_file = join(dirname(__file__), 'test_data', 'credits.html')
        with open(test_file, 'r') as myfile:
            html = myfile.read()
            actors = sut.parse(html)
            self.assertIsNotNone(actors)
            self.assertEqual(30, len(actors))
            linked_char = next(x for x in actors if x.name == 'Kallan Holley')
            self.assertEqual('nm3961562', linked_char.imdb_id)
            self.assertEqual('tt3121722', linked_char.roles[0].title_id)
            self.assertEqual('PAW Patrol', linked_char.roles[0].title_name)
            self.assertEqual(
                'Skye (76 episodes, 2013-2016)', linked_char.roles[0].name)

            unlinked_char = next(
                x for x in actors if x.name == 'Moses Rankine')
            self.assertEqual('nm6663912', unlinked_char.imdb_id)
            self.assertEqual('tt3121722', unlinked_char.roles[0].title_id)
            self.assertEqual('PAW Patrol', unlinked_char.roles[0].title_name)
            self.assertEqual(
                'Julius (3 episodes)', unlinked_char.roles[0].name)
