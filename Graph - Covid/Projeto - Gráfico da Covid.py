import requests as r
url = "https://api.covid19api.com/dayone/country/brazil"
resp = r.get(url)
resp.status_code

raw_data=resp.json()
raw_data[0]

final_data=[]

for obs in raw_data:
    final_data.append([obs["Confirmed"], obs["Deaths"],obs["Recovered"], obs["Active"], obs["Date"]])

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)):
    final_data[i][DATA]=final_data[i][DATA][:10]

import datetime as dt
import csv
with open('brasil-covid.csv', "w") as file:
    writer = csv.writer(file)
    writer.writerows(final_data)
for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

    def get_datasets(y, labels):
    if type(y[0]== list):
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'labels':labels[i], 
                'data' : y[i]
            })
        return datasets
    else:
        return [
            {
                'label': labels[0],
                'data': y
            }       
        ]
    
def set_title(title=''):
    if title != '':
        display= 'true'
    else:
        display='false'
    return{
        'title': title,
        'display': display
    }

def create_chart(x,y, label , kind='bar',title='' ):
    datasets=get_datasets(y,labels)
    options=set_title(title)
    chart = {
        'type': kind,
        'data': {
            'labels':x,
            'datasets': datasets
        },
        'options':options
    }
    return chart

def get_api_chart(chart):
    url_base="https://quickchart.io/chart"
    resp = r.get(f'{url_base}?c={str(chart)}')

def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)

from PIL import Image
from IPython.display import display

from PIL import Image
from IPython.display import display

def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)

y_data_1 =[]
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
    
y_data_2 =[]
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])
    
labels= ['Confirmados', 'Recuperados' ]

x=[]
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))

chart = create_chart(x, [y_data_1, y_data_2], labels , title='Gráfico confirmados vs recuperados')
chart_content= get_api_chart(chart)
save_image('meu-primeiro-grafico.png', chart_content)
display_image('meu-primeiro-grafico.png')
    return resp.content
