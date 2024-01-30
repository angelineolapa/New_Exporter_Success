**ML Zoomcamp - Capstone Project 2**
# New Exporter Success Prediction Tool

WebApp: [New-Exporter-Success](https://new-exporter-success.onrender.com/)

## 1. Project Overview

* Created a tool to help predict success of new Colombian exporters when entering a new market. The objective is to help new exporters select target markets for future expansions based on their exporting activity, product portfolio and other relevant variables.
* Cleaned, explored, agregated and analized all export records presented to the Colombian tax authorities between 2016 and 2022.
* Optimized logistic regression, random forest and xgboost models to reach the best model.
* Built a client facing API using plotly.Dash to serve the model. 
  
## 2. Problem Description

By engaging in export activities, firms gain access to a wider consumer base, which can allow them to expand their production, potentially leading to lower costs through economies of scale and permitting the creation of new jobs. Firms can also benefit from exposure to more competitive markets, by having to implement more rigurous sanitary and quality controls, or by needing to increase tracebility. Additionally, international trade often attracts foreign investment and technological progress that can further contribute to economic growth. Therefore, the success and growth of new exporters is of importance, not only for the profitability of firms, but also for economic development. Unfortunately, the survival of exporters in new markets is significantly low; related studies indicate that more than 50% of new exporters do not continue exporting after the first year in a new market. 

Can firms be more strategic when selecting new export markets to maximize their potential of success? This project aims to shed some light on this question about bussiness decisions for new exporters. The main objective is to develop a ML model, to predict whether an exporter entering a new market with a new product will be successful based on their previous experience, as well as the products traded and characteristics of the new market selected. The measure of success employed will be that the exporter continues to actively export to the new market in the year following the decision of market entry.

Besides exploring potential determinants of exporter success, the model developed could help new exporters select target markets for future expansions of their export activities.

## 3. Dataset

The dataset selected for this project contains all record of new export transactions, defined as any combination of exporter-market-product not recorded in the previous year, registered in Colombia between 2017 and 2021. This dataset was obtained by aggregrating all export transactions filed to the Colombia Tax Authority - DIAN between 2016 and 2022. 

Only commercial transactions were considered; temporary exports, exports for exhibition purposes, exports by diplomatic missions and exports to free trade zones were excluded. One time exporters were also excluded from the analysis and export-market-product transactions with annual value of less than USD$1000 were also eliminated from the dataset, to ensure that only exporters with true bussiness commitments were studied.

The aggregate records were explored to tag all the new exports transaction each year and these transactions were examined to determine successful and unsuccessful outcomes, as previously defined. The data was filtered to only contain new export records with their correspondent success marker. 

The dataset was completed by adding additional features, some of them were generated from the original data and others that were obtained from additional data sources such as the [IMF World Economic Outlook datset](https://www.imf.org/en/Publications/SPROLLs/world-economic-outlook-databases#sort=%40imfdate%20descending). Features added include information on the new market, such as gdp per capita, world region and language, as well as product classification by the sections of the [WTO Harmonized system] (https://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-nomenclature-2022-edition/hs-nomenclature-2022-edition.aspx). Prior exporter experience obtained from the original records and information on available free trade agreements as reported by Colombian authorities, were also appended to the dataset where available. These features were selected based on literature and experience, and added to the dataset for consideration and evaluation in the exploratory data analysis.    

All steps to obtain the dataset from original export records (available for download at [microdatos](https://microdatos.dane.gov.co/index.php/catalog/472/get-microdata)) are included in [notebook1.ipynb](https://github.com/angelineolapa/New_Exporter_Success/blob/main/Notebooks/notebook1.ipynb). 

## 4. Exploratory Data Analysis (EDA)

To build a successful model for prediction of exporter success, it is key to explore the different factors that could have an impact on this outcome and select those that appear to have the most incidence. As described in the previous section, for this project additional data was added to export records in order to create new features that could be relevant. These features were explored graphically and analysis of feature importance was also conducted. In addition, the dependant variable - success - was also explored to verify whether data was imbalanced and consider measures to address this problem if present. Fortunately, the variable did not have this problem so it was not necessary to take additional steps for modelling.

All results of the EDA are available in [notebook2.ipynb](https://github.com/angelineolapa/New_Exporter_Success/blob/main/Notebooks/notebook2.ipynb) and some visualizations were included in the webapp developed for this project.

## 5. Model

Considering the characteristics of the dependent variable, three types of model were tested in this project. A first approach was to build a logistic regression with the variables that were identified as relevant in the EDA. Adjustments on the target features were made based on their significance, to derive a set of target variables for training a final selected logistic regression model. Different metrics were considered to evaluate this model and cross validation was also conducted. The performance of logistic regression was not outstanding.

Two other models, random forest and XGBoost were also trained with the same selected features and evaluated. Parameter tuning was conducted in both cases. Metrics for the resulting models after the tuning showed a significant improvement and were very similar among them. A random forest was selected as the final model. 

All steps in modelling, review of feature significance and parameter tuning are available in [notebook2.ipynb](https://github.com/angelineolapa/New_Exporter_Success/blob/main/Notebooks/notebook2.ipynb).

## 6. Deployment

A multipage plotly.Dash app was created to serve the model. The home page provides some visualizations to give context on the profile of new Colombian exporter. The market pages provides insights on the new markets chosen by new exporters. The model page, which is the central part of this project, provides a user form that upon submission indicates the probability of success for a new exporter trading a specific product to a specific market based on its experience and shipment information. Market and product details have to be encoded following ISO country codes and WTO harmonized system nomenclature respectively, so links to information on these standars have been provided 

A pipenv environment and a docker container were created for deployment. After testing locally, the app was deployed to [Render](https://render.com/) following these steps:
1. Create render account
2. Start a free web service
3. Give access to github repository 
4. Manually deploy container
The app is available at: https://new-exporter-success.onrender.com/.

## 7. Reproducibility

After cloning this repository, this project can be reproduced locally in three ways:

1. Through a simple flash app that serves the model:
  - Open the WebApp folder in a terminal.
  - Create a local environment with the pipfiles: `pipenv install` + `pipenv shell`.
  - Run the predict.py script to start the flask app that serves the model,
  - Open another command line in the folder, run the test-predict.py that sends a request with data from a sample exporter.
  The probability of success will appear in the command prompt.
  
2. Building the dash app locally:
  - Open the WebApp folder in a terminal.
  - Create a local environment with the pipfiles: `pipenv install` + `pipenv shell`.
  - Run the app.py script to create the WebApp designed for this project. 
  A test version of the app will run locally at the IP address provided once the script finishes running.

3. From the docker container: 
  - Open the WebApp folder in a terminal.
  - Build the docker container: `docker build -t exporter-success . `.
  - Run it: `docker run -it -p 9696:9696 exporter-success:latest`. 
  Please note that this WebApp is served using gunicorn so it will not work in Windows-based environments. 
  
The training script can also be run to train the model and create the model.bin file:
- Open the WebApp folder in a terminal.
- Create a local environment with the pipfiles: `pipenv install` + `pipenv shell`.
- Run the train.py script.
The model file will be created in the data folder

As mentioned previously, all the [notebooks](https://github.com/angelineolapa/New_Exporter_Success/blob/main/Notebooks/) that contain all the steps for creating the dataset and tuning the model are also available in this repository. The exports.csv file used in notebook1 is too large for this repository. To create it, download the 2016-2022 zip files available in [microdatos](https://microdatos.dane.gov.co/index.php/catalog/472/get-microdata) and extract them in the notebook folder. Ensure that file estructure for all years is for all files is Expo_{Year}/{Month} and run the originaldata.ipynb notebook. All datasets used in notebook2 are available in the [data folder for the WebApp](https://github.com/angelineolapa/New_Exporter_Success/blob/main/Notebooks/). 

## 8. References
- DataTalksClub (2023), Machine Learning Zoomcamp Course Materials. Available at: https://github.com/DataTalksClub/machine-learning-zoomcamp.
- Eaton, Jonathan and Eslava (2007), Export Dynamics in Colombia: Firm-Level Evidence. Available at: https://back.nber.org/bibliographic/w13531.bib.
- International Trade Administration, Why Export? Available at: https://www.trade.gov/why-export.

 
