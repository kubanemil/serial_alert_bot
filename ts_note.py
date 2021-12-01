from urllib.request import urlopen
from bs4 import BeautifulSoup as BS


def link_exist(link):   #Returns 'True' if links exist. Otherwise, returns 'False'
    try:
        html = urlopen(link)
        return True
    except:
        return False  #Returns 'True' if links exist. Otherwise, returns 'False'
############################################################################################################

def get_title(link):   #Returns show's title from this show's link
    html = urlopen(link)
    soup = BS(html.read(), 'html.parser')
    return soup.title.text  
############################################################################################################

def shows_link_list():    #Returns a list of shows' links
    f = open(r".\link.txt", 'r')
    titles = f.read().split('\n')
    titles = titles[:-1]
    return titles
############################################################################################################

def add_show():    #Adds new show in 'link.txt'
    add_write = input('Add or New?(add/Make New) ')
    print('..')
    if add_write == 'Make New':
        link_file = open(r'.\link.txt', 'w')
        link_file.write('')
    else:
        link_file = open(r'.\link.txt', 'a')

    while True:
        link = input('Send me FULL link of the serial:\n(For example:"https://www.ts.kg/show/rick_and_morty")\n\t=> ')
        if link == '':
            link_file.close()
            break
        elif link_exist(link):
            link_file.write(link+'\n')
        else:
            print('No such a serial in "ts.kg"')

    print('Your shows list: ')
    r = open(r'.\link.txt', 'r')
    link_list = r.read().split('\n')
    link_list = link_list[:-1]
    for show in link_list:
        print(get_title(show))
    link_file.close()
############################################################################################################
    
def isEpisode(link):    #Checks, wether a link is an episode or not
    link_segments = link.split('/')
    print(link_segments)
    if len(link_segments) > 5:
        if link_segments[5] != '':
            return True
        else:
            return False
    else:
        return False
############################################################################################################

def add_to_watched(show_link):   #Adds ALL episodes of show to watched list in 'dataset.txt'
    for i in range(2):
        try:
            r = open('.\\dataset.txt', 'r')
        except FileNotFoundError:
            r = open('.\\dataset.txt', 'w')
    episode_list = r.read().split('\n')
    r.close()
    r.close()
    domain_segments = show_link.split('/')
    season = 1
    isNextSeason = True
    while isNextSeason:
        episode = 1
        while True:
            episode_link = "/".join(domain_segments[:5])+'/'+str(season)+'/'+str(episode)+'/'
            if link_exist(episode_link):
                if episode_link not in episode_list:
                    f = open('.\\dataset.txt', 'a')
                    f.write(episode_link+'\n')
                    print(episode_link)
                episode += 1
            else: 
                season += 1
                break
        if episode < 2:
            isNextSeason = False
############################################################################################################

def add_one_watched(episode_link):       #Adds one episode of show to watched list in 'dataset.txt'
    if link_exist(episode_link):
        f = open('.\\dataset.txt', 'a')
        f.write(episode_link+'\n')
############################################################################################################

def new_episode(show_link):      #Returns new unwatched episode's link
    show_episodes = []
    domain_segments = show_link.split('/')
    new_episode_amount = 0
    season = 1
    isNextSeason = True
    while isNextSeason:
        episode = 1
        while True:
            episode_link = "/".join(domain_segments[:5])+'/'+str(season)+'/'+str(episode)+'/'
            if link_exist(episode_link):
                new_episode_amount += 1
                episode += 1
            else: 
                season += 1
                break
        if episode < 2:
            isNextSeason = False

    w = open('.\\dataset.txt', 'r')
    episode_link_list = w.read().split('\n')
    for episode in episode_link_list:
        if domain_segments[4] in episode:
            show_episodes.append(episode)
    if len(show_episodes) < new_episode_amount:
        last_episode_link = show_episodes[-1]
        lasts_segments = last_episode_link.split('/')
        show_domain = "/".join(lasts_segments[:5])
        next_episode = int(lasts_segments[6])+1
        next_season = int(lasts_segments[5])+1
        next_episode_link = show_domain + '/' + lasts_segments[5] + '/' + str(next_episode) + '/'
        if link_exist(next_episode_link):
            return next_episode_link
        else:
            next_episode_link = show_domain + '/' + str(next_season) + '/' + '1' + '/'
            if link_exist(next_episode_link):
                return next_episode_link
            else: return
    else:
        return 
############################################################################################################