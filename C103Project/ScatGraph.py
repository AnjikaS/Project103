import pandas as pd
import plotly_express as px

data=pd.read_csv("CovidData.csv")
print(data)

figure = px.scatter(data,x="date",y="cases",size="cases",color="country",title="Record of all COVID cases in 6 countries", size_max=50)
figure.show()