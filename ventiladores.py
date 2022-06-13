import pandas as pd
import plotly.express as px

#df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto89/incidencia_en_vacunados_edad.csv')
#fig = px.line(df, x = 'semana_epidemiologica', y = 'incidencia_def', title='Defunciones por semana')
#UCI POR TRAMO ETARIO
def ventiladores():
	df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto20/NumeroVentiladores_T.csv')
	fig = px.line(df, x = 'Ventiladores', y = ['total','disponibles', 'ocupados'] , title='Ventiladores disponibles y ocupados')

	fig.update_layout(
		legend_title_text='Ventiladores',
		yaxis_title='Cantidad',
		)
	fig.add_annotation(
		x = 1, y = -0.1, 
		text = 'Fuente: Datos obtenidos desde el Ministerio de Ciencia: https://github.com/MinCiencia/Datos-COVID19.', 
      	showarrow = False, xref='paper', yref='paper', 
      	xanchor='right', yanchor='auto', xshift=0, yshift=-20
		)
	fig.show()

def tipoCama():
	df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto24/CamasHospital_Diario_T.csv')
	fig = px.line(df, x = 'Tipo de cama', y = ['Basica','Media', 'UTI', 'UCI'] , title='Tipo de cama ocupada')

	fig.update_layout(
		legend_title_text='Tipo de cama',
		yaxis_title='Cantidad',
		)
	fig.add_annotation(
		x = 1, y = -0.1, 
		text = 'Fuente: Datos obtenidos desde el Ministerio de Ciencia https://github.com/MinCiencia/Datos-COVID19.', 
      	showarrow = False, xref='paper', yref='paper', 
      	xanchor='right', yanchor='auto', xshift=0, yshift=-20
		)
	fig.show()


tipoCama()
#ventiladores()