
import requests
import pandas

def main():
    response = requests.get('http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json')
    if response:
        df = pandas.read_json(response.content)
        champions = df.index.values
        f = open('lol_champion_names.txt', 'w')
        for champ in champions:
            f.write(champ)
            f.write('\n')
        print("Tailyah")
    else:
        print('API call failed')

if __name__ == '__main__':
    main()
