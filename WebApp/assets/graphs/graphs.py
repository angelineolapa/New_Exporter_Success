import plotly.express as px
import pandas as pd
import numpy as np

#Variables of interest
selected_vars = ["region", "fta", "dpto1", "active_markets", "active_products", "active_years", "exports_value", 
                "success", "year", "gdp_pc"]

#Identify data types
data_types = {"region":"category", "fta":"category", "dpto1":str, "active_markets":int,"active_products":int, 
            "active_years":int, "exports_value":float, "success":int, "year":int, "gdp_pc":float}
              
#Import data
new_exporters = pd.read_csv("./data/NewExporters.csv", sep=";", usecols=selected_vars, dtype=data_types)

#Variable names for graphs
var_names ={"subregion":"World region for new market",
            "gdp_pc":"GPD per capita", 
            "active_markets":"Export markets in previous year", 
            "active_years":"Export experience in years",
            "active_products":"Export products in previous year", 
            "exports_value":"Exports Value in previous year (USD)", 
            "fta":"FTA in new market", 
            "success":"Success of new exporter"}

#Exporter regions
def region_identifier(depto):
    if depto in ["08", "13", "20", "23", "44", "47", "70"]:
        return "caribe"
    elif depto in ["05", "17", "63", "66"]:
        return "cafetera"
    elif depto in ["19", "27", "52", "76"]:
        return "pacifica"
    elif depto in ["11", "15", "25", "41", "54", "68", "73"]:
        return "central"
    elif depto in ["50", "81", "85", "99"]:
        return "llanos"
    else:
        return "amazonia"

new_exporters["exp_region"] = new_exporters["dpto1"].apply(region_identifier)
new_exporters["exp_region"] = new_exporters["exp_region"].astype("category") 
var_names["exp_region"] = "Colombian region where exporter is based"

#Graph function:
def graph_generator(var):
    return px.histogram(new_exporters, x=var, color_discrete_sequence=px.colors.qualitative.Prism)