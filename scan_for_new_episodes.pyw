from ts_note import *

for show in shows_link_list():
    print(show)
    if new_episode(show):
        print(new_episode(show))
        add_one_watched(new_episode(show))
    else:
        print('No new episodes')
