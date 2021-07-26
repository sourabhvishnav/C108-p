import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

data = pd.read_csv("data.csv")

fig = ff.create_distplot([data["Avg Rating"].tolist()], [
                         "Avg Rating"], show_hist=True)
fig.show()
