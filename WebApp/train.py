#Import Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import average_precision_score

import pickle

#Select variables of interest
selected_vars = ["exporter", "market", "product", "dpto1", "success", "active_years", "fobdol", "product_national", 
                "active_markets", "active_products", "year", "region", "fta", "gdp_pc", "pnk", "other_expenses"]

#Define data types for importing data
data_types = {"exporter":str, "product":str, "market":str, "dpto1":str, "year":int, "success":int, 
              "fobdol": float, "product_national":float, "active_markets":int,"active_products":int, "active_years":int,
              "fta":"category", "region":"category", "gdp_pc":float, "pnk":float, "other_expenses":float}

#Import data - all steps to obtain this dataset are available in the notebook DatabaseGenerator.ipynb
new_exporters = pd.read_csv("./data/NewExporters.csv", sep=";", usecols=selected_vars, dtype=data_types)

#Drop records for which gdp_pc is not available - mostly small markets
new_exporters = new_exporters[new_exporters["gdp_pc"].isna()==False]
new_exporters.reset_index(inplace=True, drop=True)

#Drop records for which exporter department was not reported
new_exporters = new_exporters[new_exporters["dpto1"]!="55"]
new_exporters.reset_index(inplace=True, drop=True)

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

#Product classification by HS sections
hs_sections = pd.read_csv("./data/hs_sections.csv", usecols=["section", "chapter"], sep=";", encoding = "ISO-8859-1")

#Product classifications
def product_classifier(product):
    section = hs_sections[hs_sections["chapter"]==int(product[0:2])]["section"].values[0]
    return section

new_exporters["prod_class"] = new_exporters["product"].apply(product_classifier)
new_exporters["prod_class"] = new_exporters["prod_class"].astype("category") 

#Interaction terms
new_exporters = new_exporters.assign(overall_exp=new_exporters["active_years"]*new_exporters["active_markets"])

#Divide in train, validation and test sets
#Stratified sampling will be using to account for imbalanced nature of the data
df_train_full, df_test = train_test_split(new_exporters, test_size=0.2, random_state=1, 
                                          stratify=new_exporters.success)

#Reset index
df_train_full.reset_index(drop=True, inplace=True) 
df_test.reset_index(drop=True, inplace=True)

#Calculate y_train and y_test variable 
y_train = df_train_full.success.values
y_test = df_test.success.values
df_train_full.drop("success", axis=1, inplace=True)
df_test.drop("success", axis=1, inplace=True)

#Target variables for this model based on feature analysis and logistic regression fittin
target_vars = ["region", "prod_class", "exp_region", "fta", "active_years", "pnk", "other_expenses",
               "product_national","active_markets", "active_products", "overall_exp", "year"]
df_train_full = df_train_full[target_vars] 
df_test = df_test[target_vars]

#Encoding with DictVectorizer
train_dict = df_train_full.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
dv.fit(train_dict)

#Prepare feature matrix for model training
X_train = dv.transform(train_dict)

#Random Forest with parameters identified in jupyter notebook 
max_depth_target = 15
n_estimators_target = 20
min_samples_leaf_target = 1

model = RandomForestClassifier(n_estimators=n_estimators_target, max_depth=max_depth_target, 
                                min_samples_leaf=min_samples_leaf_target, random_state=1)
model.fit(X_train, y_train)

#Model validation
test_dict = df_test.to_dict(orient='records')
X_test = dv.transform(test_dict)
y_pred = model.predict_proba(X_test)[:, 1]

#AUC Score
print("AUC Score:", roc_auc_score(y_test, y_pred))

#Average Precision Score
print("Average Precision Score:", average_precision_score(y_test, y_pred))

#Save model for use in prediction tool
with open('./data/model.bin', 'wb') as f_out:
   pickle.dump((dv, model), f_out)
f_out.close()