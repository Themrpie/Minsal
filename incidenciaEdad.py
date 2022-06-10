import pandas as pd
import plotly.express as px
import numpy as np

def incidenciaEdad():	
	df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto89/incidencia_en_vacunados_edad.csv')
	xaxys = df.columns.values
	viejosVacunados = []
	viejosNoVacunados = []
	diferencia = []
	da = [43]
	for i in range(len(df)):		
		if(df.values[i][1] == 'Total'):
			
			if df.values[i][2] == 'sin esquema completo':
				viejosNoVacunados.append(df.values[i][9])
			elif df.values[i][2] == 'con esquema completo':
				viejosVacunados.append(df.values[i][9])							
		#viejos.append()

	diferencia = np.subtract(viejosNoVacunados, viejosVacunados)
	#print(diferencia)

	fig = px.bar(df, y = [diferencia,viejosVacunados, viejosNoVacunados], x = range(1,44), title='Incidencia en fallecidos por cada 100.000 personas según estado de vacunación (Todas las edades)')
	fig.show()

incidenciaEdad()