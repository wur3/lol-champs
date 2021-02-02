
import requests
import json

def main():
    noSpaces = ''
    noSpaces = input('Do you want the words with spaces?(y/n)\n').strip().lower()
    while(True):
        if noSpaces == 'n':
            noSpaces = True
            break
        elif noSpaces == 'y':
            noSpaces = False
            break
        else:
            noSpaces = input('Answer with \'y\' or \'n\':\n')
    # get the current patch number for League of Legends
    response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
    if response:
        json_res = json.loads(response.content)
        current_ver = json_res[0]
    else:
        print('API call for game patch number failed')

    # get the list of all champions
    response = requests.get('http://ddragon.leagueoflegends.com/cdn/{}/data/en_US/champion.json'.format(current_ver))
    if response:
        json_res = json.loads(response.content)
        champions = [champ['name'] for champ in json_res['data'].values()]
        f = open('lol_champion_names.txt', 'w')
        formatted = ',\n'.join(champions)
        if noSpaces:
            formatted = formatted.replace(' ','')
        print("Check lol_champion_names.txt")
        f.write(formatted)
    else:
        print('API call for champions failed')

if __name__ == '__main__':
    main()
