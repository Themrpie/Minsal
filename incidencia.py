import pandas as pd
import plotly.express as px

def sintomas():	
	df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto90/incidencia_en_vacunados.csv')
	
	sin_vac_uci = []
	una_dosis_uci = []
	dos_dosis_uci = []
	dos_dosis_comp_uci = []
	dosis_unica_uci = []
	dosis_unica_comp_uci = []
	dosis_ref_comp_uci = []

	for i in range(len(df['sin_vac_uci'])):
		if i >= 2:
			sin_vac_uci.append(int(float(df['sin_vac_uci'][i])))
			una_dosis_uci.append(int(float(df['una_dosis_uci'][i])))
			dos_dosis_uci.append(int(float(df['dos_dosis_uci'][i])))
			dos_dosis_comp_uci.append(int(float(df['dos_dosis_comp_uci'][i])))
			dosis_unica_uci.append(int(float(df['dosis_unica_uci'][i])))
			dosis_unica_comp_uci.append(int(float(df['dosis_unica_comp_uci'][i])))
			dosis_ref_comp_uci.append(int(float(df['dosis_ref_comp_uci'][i])))
								

	sin_vac_uci.append(0)
	sin_vac_uci.append(0)
	una_dosis_uci.append(0)
	una_dosis_uci.append(0)
	dos_dosis_uci.append(0)
	dos_dosis_uci.append(0)
	dos_dosis_comp_uci.append(0)
	dos_dosis_comp_uci.append(0)
	dosis_unica_uci.append(0)
	dosis_unica_uci.append(0)
	dosis_unica_comp_uci.append(0)
	dosis_unica_comp_uci.append(0)
	dosis_ref_comp_uci.append(0)
	dosis_ref_comp_uci.append(0)
	

	ejey = pd.DataFrame(sin_vac_uci, columns = ['sin_vac_uci'])
	ejey2 = pd.DataFrame(una_dosis_uci, columns = ['una_dosis_uci'])
	ejey3 = pd.DataFrame(dos_dosis_uci, columns = ['dos_dosis_uci'])
	ejey4 = pd.DataFrame(dos_dosis_comp_uci, columns = ['dos_dosis_comp_uci'])
	ejey5 = pd.DataFrame(dosis_unica_uci, columns = ['dosis_unica_uci']) 
	ejey6 = pd.DataFrame(dosis_unica_comp_uci, columns = ['dosis_unica_comp_uci']) 
	ejey7 = pd.DataFrame(dosis_ref_comp_uci, columns = ['dosis_ref_comp_uci']) 

	
	#print(df.columns[8:].values)

	fig = px.line(df, 
		y = [ejey.sin_vac_uci, ejey2.una_dosis_uci, ejey3.dos_dosis_uci, ejey4.dos_dosis_comp_uci, ejey5.dosis_unica_uci, ejey6.dosis_unica_comp_uci,
		 ejey7.dosis_ref_comp_uci],
		x = range(1,75),
		 title='Incidencia en UCI',
		 #color=df.columns[8:].values, 
		 )
	fig.add_annotation(
		x = 1, y = -0.1, 
		text = 'Fuente: Datos obtenidos desde el Ministerio de Ciencia: https://github.com/MinCiencia/Datos-COVID19.', 
      	showarrow = False, xref='paper', yref='paper', 
      	xanchor='right', yanchor='auto', xshift=0, yshift=-20
		)
	fig.show()

sintomas()