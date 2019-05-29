import plotly
import plotly.graph_objs as go
import requests


def plotpatientdata(pid):

    # api-endpoint
    dataapiurl = "http://127.0.0.1:5000/pdata/"
    plotdata = []

    for i in range(0, 4):
        params = {'pid': pid, 'col': i}
        r = requests.get(url=dataapiurl, params=params)
        data = r.json()
        measurements = data['measurements']
        measurementsname = data['name']
        trace = go.Box(y=measurements, name=measurementsname, boxpoints='outliers')
        plotdata.append(trace)

    layout = go.Layout(
        yaxis=dict(
            title='Patient cardiological measurements',
            zeroline=True
        ),
        boxmode='group'
    )
    plotly.offline.plot(plotdata)


plotpatientdata('p3734')