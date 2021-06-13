from pprint import pprint

from clickupv2 import ClickupV2Client

if __name__ == '__main__':
    client = ClickupV2Client(
        'CLIENT_ID',
        'CLIENT_SECRET',
        'REDIRECT_URL'
    )
    # print(client.oauth2_url)
    # client.set_oauth2_code('CODE')
    client.set_access_token('ACCESS_TOKEN')

    teams = client.get_teams()
    team = teams[0]
    spaces = client.get_spaces(team.get('id'))
    folders = client.get_folders(next(x for x in spaces if x.get('name') == 'Develop').get('id'))
    lists = client.get_lists(folder_id=next(x for x in folders if x.get('name') == 'Backlog').get('id'))
    hierarchy = client.get_shared_hierarchy(teams[0].get('id'))
    target_list = next(x for x in lists if x.get('name').startswith('Sprint 01'))
    views = client.get_views(list_id=target_list.get('id'))
    activity_view = next(x for x in views if x.get('name') == 'Activity')
    all_members = [x.get('user') for x in team.get('members')]
    for member in all_members:
        print(f'Member {member.get("username")}')
        pprint(member)
