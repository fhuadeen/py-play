import collections
from pprint import pprint

# to create an immutable data structure,
# following functional programming standards
EPLClubs = collections.namedtuple('EPLClubs', [
    'name',
    'location',
    'manager',
    'won_ucl',
])

print(EPLClubs)

epl_clubs = (
    EPLClubs(name='Manchester United', location='Manchester', manager='Erik ten Hag', won_ucl=True),
    EPLClubs(name='Manchester City', location='Manchester', manager='Pep Guardiola', won_ucl=False),
    EPLClubs(name='Arsenal', location='London', manager='Mikel Arteta', won_ucl=False),
    EPLClubs(name='Liverpool', location='Merseyside', manager='Jurgen Klopp', won_ucl=True),
)

pprint(epl_clubs)

# can get different things from the data
print(epl_clubs[0].name)

# can not edit it though
# epl_clubs[0].name = 'United' # returns 'AttributeError: can't set attribute' error

# filtering using filter
fc = tuple(filter(lambda y: y.won_ucl is True, epl_clubs))
print('filter:', fc)

# filtering using list comprehension
lc = tuple([x for x in epl_clubs if x.won_ucl is True])
print('comprehension:', lc)

# filtering using generator expression
gc = tuple(x for x in epl_clubs if x.won_ucl is True)
print('generator:', gc)

# using map to transform the data
mc = tuple(map(lambda x: {x.name, x.won_ucl }, epl_clubs))
# mc = tuple(map(lambda y: y.won_ucl, epl_clubs))
print('map:', mc)