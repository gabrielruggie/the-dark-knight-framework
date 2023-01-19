from main.utilities.create_obj_from_schema import ObjectBuilder

from main.schemas.schemas_player import PlayerSheets

'''
Tests that player is formatted correctly before being sent off as event
'''
def test_player_fmt_method ():

    player = PlayerSheets(
        first_name='     GABriel     ',
        last_name='RUGGIE ',
        email='  gruggie77@gmail.com  ',
        position='PG  ',
        player_number=1,
        grade=3,
        is_team_captain=0,
        team_church='  st. luke',
        team_cap_name='Ruggie',
        team_level=3
    )

    player_fmt = ObjectBuilder().format_new_player_input(player=player)

    assert dict(player_fmt) == {'email': 'gruggie77@gmail.com',
                                'first_name': 'gabriel',
                                'grade': 3,
                                'is_team_captain': 0,
                                'last_name': 'ruggie',
                                'player_number': 1,
                                'position': 'pg',
                                'team_cap_name': 'ruggie',
                                'team_church': 'st. luke',
                                'team_level': 3}