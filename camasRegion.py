import pandas as pd
import plotly.graph_objects as go
import numpy as np

def camasRegion():  
    df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto52/Camas_UCI.csv')
    region = "Atacama"
    Regiones = df['Region'].drop_duplicates()

    for x in Regiones:
    	print(x)

    target_region = df.query('Region == @region').drop('Region', axis=1).set_index('Serie').T
    chart = []
    for i in target_region:
        if i != 'Camas base (2019)':  #or you can easily drop it from your dataset
            chart += [go.Scatter(x=target_region.index,y=target_region[i], name=i, mode='lines')]
            
    fig = go.Figure(chart)
    fig.update_layout(title={'text':f'Camas UCI por región: ({region})', 'x':.45},
                      template='plotly_white', hovermode='x',
                      legend_title_text='Estado de cama',
                      xaxis_title="Días",
                      yaxis_title="Cantidad de camas")

    fig.add_annotation(
        x = 1, y = -0.1, 
        text = 'Fuente: Datos obtenidos desde el Ministerio de Ciencia: https://github.com/MinCiencia/Datos-COVID19/blob/master/output/producto52/Camas_UCI.csv', 
        showarrow = False, xref='paper', yref='paper', 
        xanchor='right', yanchor='auto', xshift=0, yshift=-20
        )
    fig.show()


camasRegion()