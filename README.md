# PyClickupV2

Python client to access Clickup platform, over version2 API version.

## Client

#### First time authentication (first time only, using oauth2):

```python
from clickupv2 import ClickupV2Client

client = ClickupV2Client(
    'CLIENT_ID',
    'CLIENT_SECRET',
    'REDIRECT_URL'
)
print(f'Open {client.oauth2_url} on your browser and get the CODE after authorization')
...
client.set_oauth2_code('CODE (read from browser redirect url query string)')
access_token = client.ensure_access_token()
print(f'Use this access token: {access_token}')
```

#### Using the client, using access token

```python
from clickupv2 import ClickupV2Client

client = ClickupV2Client(
    'CLIENT_ID',
    'CLIENT_SECRET',
    'REDIRECT_URL'
)
client.set_access_token('ACCESS_TOKEN (from previous step)')

teams = client.get_teams()
team = teams[0]
spaces = client.get_spaces(team.get('id'))
folders = client.get_folders(next(x for x in spaces if x.get('name') == 'Develop').get('id'))
lists = client.get_lists(folder_id=next(x for x in folders if x.get('name') == 'Sprints').get('id'))
hierarchy = client.get_shared_hierarchy(teams[0].get('id'))
target_list = next(x for x in lists if x.get('name').startswith('Sprint 01'))
views = client.get_views(list_id=target_list.get('id'))
some_view = next(x for x in views if x.get('name') == 'Some')
all_members = [x.get('user') for x in team.get('members')]
```

## Apps

Coming soon!

References:

* [Clickup API Docs](https://clickup.com/api)
* [Create your own API key](https://docs.clickup.com/en/articles/2171168-api-create-your-own-app)

