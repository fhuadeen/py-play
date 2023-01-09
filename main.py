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
epl_clubs[0].name = 'United' # returns 'AttributeError: can't set attribute' error