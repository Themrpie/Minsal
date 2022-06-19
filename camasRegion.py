import pandas as pd
import plotly.express as px
import numpy as np

def camasRegion():	
	df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto52/Camas_UCI_t.csv')
	regiones = df.columns.values[1:]
	habilitadas = []
	ocupadasCovid = []
	ocupadasNoCovid = []

	diferencia = []
	region = 'Tarapacá'

	#for i in range(len(df)):				
	#	if(df.values[0][i] == 'Camas UCI habilitadas'):
	#		habilitadas.append(df.values[i]) 
	#print(df.values[0][10])

	for i in range(len(df.columns)):
		if df.columns.values[0][i] == region and df.values[1][i] == 'Camas UCI habilitadas':
			for x in range(len(df) -1):
				print(df.values[x][i])



	#for i in range(len(df)):
	#	print(df.values[i][1])
	
	#fig.show()


camasRegion()