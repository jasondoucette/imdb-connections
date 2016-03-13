# IMDB Connection Finder

Utilities to scrape IMDB to find actors in common across TV shows.

90% of the TV my kids watch is on the same channel (TVO Kids,) and in between
existential wonderings like "just who funds the Paw Patrol anyway?" I started
to notice the voices sound similar from show to show.

It turns out the voice acting community is relatively small, so I put together
some scripts to easily tell where I've heard an actor before.

## Installation / Usage

You'll need the Python modules listed in requirements.txt.  These can be
installed via `pip install -r requirements.txt`

Next, you'll want to update [titles.json] with the shows your kids watch.
`id` is the IMDB ID from the URL for the show. `name` is just for your
reference and doesn't have to be exact.

Run `getactors.py` to scrape IMDB and save the data locally. This only has to
be done once (unless you change your titles.json file.)

To compare shows, run `findconnections.py` and it'll tell you where the
actors for a given show also appeared.

## License

[MIT](./MIT.LICENSE)
