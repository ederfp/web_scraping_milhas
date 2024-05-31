from bs4 import BeautifulSoup
import requests


smiles_url = 'https://www.smiles.com.br/home'

page = requests.get(smiles_url, verify=False)
resposta = page.text
soup = BeautifulSoup(resposta, 'html.parser')

title1 = soup.find_all('span', {'id': 'part1'})
title2 = soup.find_all('span', {'id': 'part2'})
desc = soup.find_all('p', {'id': 'banner_description'})
link = soup.find_all('a', {'class': 'liferay-home-banner-action'})

title1_list = [i1.text for i1 in title1]
title2_list = [i2.text for i2 in title2]
desc_list = [i3.text.strip() for i3 in desc]
link_list = [i4['href'] for i4 in link]

print('Promoções Smiles \n')
for i, promo in enumerate(title1_list):
    # print(title1_list)
    try:
        print(
            f'{title1_list[i]} - {title2_list[i]} \n{desc_list[i]} \nLink: {link_list[i]}\n')
    except:
        continue
