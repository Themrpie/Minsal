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
	edad = 'Total'
#Columna 7 es incidencia_casos, 8 incidencia_uci, 9 incidencia_def
# edades: 71 - 80 años	
	for i in range(len(df)):		
		if(df.values[i][1] == edad):
			
			if df.values[i][2] == 'sin esquema completo':
				viejosNoVacunados.append(df.values[i][7])
			elif df.values[i][2] == 'con esquema completo':
				viejosVacunados.append(df.values[i][7])							
		#viejos.append()

	diferencia = np.subtract(viejosNoVacunados, viejosVacunados)
	total = np.add(viejosNoVacunados, viejosVacunados)
	diferenciaRelativa = np.divide(diferencia, total)
	vacunadosRelativo = np.divide(viejosVacunados, total)
	noVacundosRelativo = np.divide(viejosNoVacunados, total)

	fig = px.bar(df, y = [diferenciaRelativa,vacunadosRelativo, noVacundosRelativo], 
		x = range(1,45),
		color_discrete_map= {'wide_variable_0':'red', 'wide_variable_1': 'blue', 'wide_variable_2': 'green'},
		category_orders={"Estado de vacunación": ["Oceania", "Europe", "Asia"]},
		title='Incidencia en fallecidos por cada 100.000 personas según estado de vacunación ('+ edad+')')

	fig.update_layout(
		legend_title_text='Estado de vacunación',
		xaxis_title="Semana",
		yaxis_title="Incidencia",
		)
	fig.show()

incidenciaEdad()