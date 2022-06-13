import pandas as pd
import plotly.express as px

#df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto89/incidencia_en_vacunados_edad.csv')
#fig = px.line(df, x = 'semana_epidemiologica', y = 'incidencia_def', title='Defunciones por semana')
#UCI POR TRAMO ETARIO
def UCIEtario():
	df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto9/HospitalizadosUCIEtario_T.csv')
	fig = px.line(df, x = 'Grupo de edad', y = ['<=39','40-49', '50-59', '60-69','>=70'] , title='Hospitalizados en UCI por Grupo Etario')
	fig.update_layout(
		legend_title_text='Grupo etario',
		xaxis_title='Fecha',
		yaxis_title='Cantidad',
		)
	fig.add_annotation(
		x = 1, y = -0.1, 
		text = 'Fuente: Datos obtenidos desde el Ministerio de Ciencia: https://github.com/MinCiencia/Datos-COVID19.', 
      	showarrow = False, xref='paper', yref='paper', 
      	xanchor='right', yanchor='auto', xshift=0, yshift=-20
		)
	fig.show()

def comorbilidades():	
	df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto35/Comorbilidad_T.csv')
	df2 = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto35/Comorbilidad.csv')
	obesidad = []
	hipertension = []
	diabetes = []
	asma = []
	cardiovascular = []
	pulmonar = []
	cardiopatia = []
	renal = []
	neurologica = []
	inmuno = []
	hepatica = []

	for i in range(len(df['Obesidad'])):
		if i >= 2:
			obesidad.append(int(float(df['Obesidad.1'][i])) - int(float(df['Obesidad.1'][i-1])))
			hipertension.append(int(float(df['Hipertensión arterial.1'][i])) - int(float(df['Hipertensión arterial.1'][i-1])))
			diabetes.append(int(float(df['Diabetes.1'][i])) - int(float(df['Diabetes.1'][i-1])))
			asma.append(int(float(df['Asma.1'][i])) - int(float(df['Asma.1'][i-1])))
			cardiovascular.append(int(float(df['Enfermedad cardiovascular.1'][i])) - int(float(df['Enfermedad cardiovascular.1'][i-1])))
			pulmonar.append(int(float(df['Enfermedad pulmonar crónica.1'][i])) - int(float(df['Enfermedad pulmonar crónica.1'][i-1])))
			cardiopatia.append(int(float(df['Cardiopatía crónica.1'][i])) - int(float(df['Cardiopatía crónica.1'][i-1])))
			renal.append(int(float(df['Enfermedad renal crónica.1'][i])) - int(float(df['Enfermedad renal crónica.1'][i-1])))
			neurologica.append(int(float(df['Enfermedad neurológica crónica.1'][i])) - int(float(df['Enfermedad neurológica crónica.1'][i-1])))
			inmuno.append(int(float(df['Inmunocomprometido.1'][i])) - int(float(df['Inmunocomprometido.1'][i-1])))
			hepatica.append(int(float(df['Enfermedad hepática crónica.1'][i])) - int(float(df['Enfermedad hepática crónica.1'][i-1])))
			#print(int(float(df['Fiebre'][i])) - int(float(df['Fiebre'][i-1])))

	obesidad.append(0)
	obesidad.append(0)
	hipertension.append(0)
	hipertension.append(0)
	asma.append(0)
	asma.append(0)
	cardiovascular.append(0)
	cardiovascular.append(0)
	pulmonar.append(0)
	pulmonar.append(0)
	cardiopatia.append(0)
	cardiopatia.append(0)
	renal.append(0)
	renal.append(0)
	neurologica.append(0)
	neurologica.append(0)
	inmuno.append(0)
	inmuno.append(0)
	hepatica.append(0)
	hepatica.append(0)
	diabetes.append(0)
	diabetes.append(0)

	ejey = pd.DataFrame(obesidad, columns = ['obesidad'])
	ejey2 = pd.DataFrame(hipertension, columns = ['hipertension'])
	ejey3 = pd.DataFrame(diabetes, columns = ['diabetes'])
	ejey4 = pd.DataFrame(asma, columns = ['asma'])
	ejey5 = pd.DataFrame(cardiovascular, columns = ['cardiovascular']) 
	ejey6 = pd.DataFrame(pulmonar, columns = ['pulmonar']) 
	ejey7 = pd.DataFrame(cardiopatia, columns = ['cardiopatia']) 
	ejey8 = pd.DataFrame(renal, columns = ['renal']) 
	ejey9 = pd.DataFrame(neurologica, columns = ['neurologica']) 
	ejey10 = pd.DataFrame(inmuno, columns = ['inmuno']) 
	ejey11 = pd.DataFrame(hepatica, columns = ['hepatica'])

	#print('Null: ' , df[df['Fiebre'].isnull()])
	#print(len(ejey))
	#print(df2['Comorbilidad'][11:])
	print(df.Comorbilidad)
	fig = px.bar(df, 
		x = df.Comorbilidad, 
		y = [ejey.obesidad, ejey2.hipertension, ejey3.diabetes, ejey4.asma, ejey5.cardiovascular, ejey6.pulmonar,
		 ejey7.cardiopatia, ejey8.renal, ejey9.neurologica, ejey10.inmuno, ejey11.hepatica ], 
		 title='Comorbilidades',
		 #color= df2['Comorbilidad'][11:],

		 )
	fig.show()



#comorbilidades()
UCIEtario()