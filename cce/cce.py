import pandas as pd

from plotly import __version__
from plotly import tools
from plotly.offline import download_plotlyjs, plot
from plotly.graph_objs import Scatter, Figure, Layout

df = pd.read_csv('cce_years.csv', encoding='utf-8')

trace1 = Scatter(
    x=df['year'],
    y=df['distinct_ids'],
    name='HathiTrust Volume Count<br /> (US publications)',
    line={'color': 'rgba(242, 60, 6, 0.2)'},
    visible = 'legendonly'
)
trace2 = Scatter(
    x=df['year'],
    y=df['distinct_hathitrust_records'],
    name='Unique HathiTrust<br /> Record Count<br /> (US publications)',
    line={'color': 'rgba(42, 212, 222, 1)'},
)

trace3 = Scatter(
   x=df['year'],
   y=df['distinct_oclc_numbers'],
   name='Unique HathiTrust<br /> OCLC Number Count<br /> (US publications)',
    line={'color': 'rgba(152, 230, 240, 1)'},
    visible = 'legendonly'
)


trace4 = Scatter(
    x=df['year'],
    y=df['cce_records'],
    name='Copyright Office Catalog of<br /> Copyright Entries Count',
    line={'color': 'rgba(156, 184, 5, 1)'},
)

data = [trace1, trace2, trace3, trace4]
layout = Layout(
    barmode='overlay',
    title="US Copyright Office CCE Record Count vs <br />Unique HathiTrust Record and OCLC Number Counts<br /> (all data limited to US place of publication)",
    xaxis=dict(
        title="Year",
    ),
    yaxis=dict(
        title='Count',
    ),
    bargap=0,
)

fig = Figure(data=data, layout=layout)

plot(fig, filename='cce_count.html')
