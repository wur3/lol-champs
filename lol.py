
import requests
import json

def main():
    noSpaces = ''
    while(noSpaces != 'y' and noSpaces != 'n'):
        noSpaces = input('Do you want the words with spaces?(y/n)\n').strip().lower()
    if noSpaces == 'y':
        noSpaces = True
    elif noSpaces == 'n':
        noSpaces = False

    response = requests.get('http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json')
    if response:
        json_res = json.loads(response.content)
        champions = [champ['name'] for champ in json_res['data'].values()]
        f = open('lol_champion_names.txt', 'w')
        formatted = ',\n'.join(champions)
        if noSpaces:
            formatted = formatted.replace(' ','')
        print("Tailyah")
        f.write(formatted)
    else:
        print('API call failed')

if __name__ == '__main__':
    main()
