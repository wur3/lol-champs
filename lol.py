
import requests
import json

def main():
    response = requests.get('http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json')
    if response:
        json_res = json.loads(response.content)
        champions = [champ['name'] for champ in json_res['data'].values()]
        print(champions)
        f = open('lol_champion_names.txt', 'w')
        f.write(', '.join(champions))
        print('Tailyah')
    else:
        print('API call failed')

if __name__ == '__main__':
    main()
