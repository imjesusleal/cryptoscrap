
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import plotly.graph_objects as go

def main():

	url = 'https://www.binance.com/es-AR/markets'
	response = requests.get(url)
	doc = response.text
	sp = bs(doc, 'html.parser')
	cryptos = sp.find(class_='css-1vuj9rf')

	name = [x.text for x in cryptos.find_all(class_='css-1ap5wc6')]
	price = [x.text for x in cryptos.find_all(class_='css-ydcgk2')]
	volume = [x.text for x in cryptos.find_all(class_='css-102bt5g')]
	cap = [x.text for x in cryptos.find_all(class_='css-s779xv')]

	compress = np.stack((name, price, volume, cap), axis = 1)
	df = pd.DataFrame(compress, columns = ['Name', 'Prices', 'Volume', 'Cap'])

	fig = go.Figure(data=[go.Table(header=dict(values=list(df.columns), fill_color='paleturquoise',align='left'), 
					cells=dict(values=[df.Name,df.Prices,df.Volume, df.Cap], fill_color='lavender', align='left'))])
	fig.show()

if __name__ == '__main__':
	main()
