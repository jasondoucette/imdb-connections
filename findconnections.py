#!/usr/bin/env python
"""
findconnections.py: Finds connections between IMDB titles

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
import jsonpickle

try:
    with open('actors.pickled.json') as json_data:
        actors = jsonpickle.decode(json_data.read()).values()
except:
    exit("Error loading actors file, did you run getactors.py yet?")

roles = [role for actor in actors for role in actor.roles]
titles = list(set([r.title_name for r in roles]))

for idx, title in enumerate(titles):
    print u"{}: {}".format(idx+1, title)
option = raw_input("Which show? ")

if not option.isdigit() or int(option) < 1 or int(option) > len(titles):
    print "Invalid option."
else:
    title = titles[int(option) - 1]
    multirole_actors = [actor for actor in actors if len(actor.roles) > 1]
    title_actors = [actor for actor in multirole_actors if title in
                    [role.title_name for role in actor.roles]]
    for actor in title_actors:
        print actor.name
        for role in actor.roles:
            print u"    Played {} in {}".format(role.name, role.title_name)
        print
