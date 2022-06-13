import pandas as pd
import plotly.express as px

def sintomas():	
	df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto21/Sintomas_T.csv')
	df2 = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto21/Sintomas.csv')
	Cefalea = []
	Tos = []
	Mialgia = []
	Fiebre = []
	Odinofagia = []
	Anosmia = []
	Ageusia = []
	Disnea = []
	Diarrea = []
	DolorToracico = []
	DolorAbdominal = []
	Taquipnea = []
	Cianosis = []
	Postracion = []
	CongestionNasal = []

	for i in range(len(df['Cefalea'])):
		if i >= 29:
			Cefalea.append(int(float(df['Cefalea.1'][i])) - int(float(df['Cefalea.1'][i-1])))
			Tos.append(int(float(df['Tos.1'][i])) - int(float(df['Tos.1'][i-1])))
			Mialgia.append(int(float(df['Mialgia.1'][i])) - int(float(df['Mialgia.1'][i-1])))
			Fiebre.append(int(float(df['Fiebre.1'][i])) - int(float(df['Fiebre.1'][i-1])))
			Odinofagia.append(int(float(df['Odinofagia.1'][i])) - int(float(df['Odinofagia.1'][i-1])))
			Anosmia.append(int(float(df['Anosmia.1'][i])) - int(float(df['Anosmia.1'][i-1])))
			Ageusia.append(int(float(df['Ageusia.1'][i])) - int(float(df['Ageusia.1'][i-1])))
			Disnea.append(int(float(df['Disnea.1'][i])) - int(float(df['Disnea.1'][i-1])))
			Diarrea.append(int(float(df['Diarrea.1'][i])) - int(float(df['Diarrea.1'][i-1])))
			DolorToracico.append(int(float(df['Dolor torácico.1'][i])) - int(float(df['Dolor torácico.1'][i-1])))
			DolorAbdominal.append(int(float(df['Dolor abdominal.1'][i])) - int(float(df['Dolor abdominal.1'][i-1])))
			Taquipnea.append(int(float(df['Taquipnea.1'][i])) - int(float(df['Taquipnea.1'][i-1])))
			Cianosis.append(int(float(df['Cianosis.1'][i])) - int(float(df['Cianosis.1'][i-1])))						
			#print(int(float(df['Fiebre'][i])) - int(float(df['Fiebre'][i-1])))

	Cefalea.append(0)
	Cefalea.append(0)
	Tos.append(0)
	Tos.append(0)
	Mialgia.append(0)
	Mialgia.append(0)
	Fiebre.append(0)
	Fiebre.append(0)
	Odinofagia.append(0)
	Odinofagia.append(0)
	Anosmia.append(0)
	Anosmia.append(0)
	Ageusia.append(0)
	Ageusia.append(0)
	Disnea.append(0)
	Disnea.append(0)
	Diarrea.append(0)
	Diarrea.append(0)
	DolorToracico.append(0)
	DolorToracico.append(0)
	DolorAbdominal.append(0)
	DolorAbdominal.append(0)
	Taquipnea.append(0)
	Taquipnea.append(0)
	Cianosis.append(0)
	Cianosis.append(0)
	

	ejey = pd.DataFrame(Cefalea, columns = ['Cefalea'])
	ejey2 = pd.DataFrame(Tos, columns = ['Tos'])
	ejey3 = pd.DataFrame(Mialgia, columns = ['Mialgia'])
	ejey4 = pd.DataFrame(Fiebre, columns = ['Fiebre'])
	ejey5 = pd.DataFrame(Odinofagia, columns = ['Odinofagia']) 
	ejey6 = pd.DataFrame(Anosmia, columns = ['Anosmia']) 
	ejey7 = pd.DataFrame(Ageusia, columns = ['Ageusia']) 
	ejey8 = pd.DataFrame(Disnea, columns = ['Disnea']) 
	ejey9 = pd.DataFrame(Diarrea, columns = ['Diarrea']) 
	#ejey10 = pd.DataFrame(DolorToracico, columns = ['Dolor torácico']) 
	ejey11 = pd.DataFrame(DolorAbdominal, columns = ['Dolor abdominal'])

	#print('Null: ' , df[df['Fiebre'].isnull()])
	#print(len(ejey))
	#print(df2['Comorbilidad'][11:])
	
	fig = px.line(df, 
		x = df.Sintomas[27:], 
		y = [ejey.Cefalea, ejey2.Tos, ejey3.Mialgia, ejey4.Fiebre, ejey5.Odinofagia, ejey6.Anosmia,
		 ejey7.Ageusia, ejey8.Disnea, ejey9.Diarrea ], 
		 title='Sintomas de hospitalizados',
		 #color= df2['Comorbilidad'][11:],

		 )
	fig.add_annotation(
		x = 1, y = -0.1, 
		text = 'Fuente: Datos obtenidos desde el Ministerio de Ciencia: https://github.com/MinCiencia/Datos-COVID19.', 
      	showarrow = False, xref='paper', yref='paper', 
      	xanchor='right', yanchor='auto', xshift=0, yshift=-20
		)
	fig.show()

sintomas()