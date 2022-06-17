import pandas as pd
import plotly.express as px


def fabricanteEdad():
	df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto88/vacunacion_fabricantes_edad_4taDosis_T.csv')
	fig = px.bar(df, x = 'Fabricante', 
		y = ['Campaña SARS-CoV-2 (Moderna)','Campaña SARS-CoV-2 (Pfizer)', 'Campaña SARS-CoV-2 (AstraZeneca)', 
		'Campaña SARS-CoV-2 (Janssen)', 'Campaña SARS-CoV-2 (Sinovac)'] , 
		title='Cuarta dosis por edad y fabricante')

	fig.update_layout(
		legend_title_text='Fabricante',
		yaxis_title='Dosis administradas',
		xaxis_title='Edad'
		)
	fig.add_annotation(
		x = 1, y = -0.1, 
		text = 'Fuente: Datos obtenidos desde el Ministerio de Ciencia: https://github.com/MinCiencia/Datos-COVID19/blob/master/output/producto88/vacunacion_fabricantes_4taDosis_T.csv.', 
      	showarrow = False, xref='paper', yref='paper', 
      	xanchor='right', yanchor='auto', xshift=0, yshift=-20
		)
	fig.show()


fabricanteEdad()