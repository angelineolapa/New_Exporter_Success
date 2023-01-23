**ML Zoomcamp - Capstone Project 2**
# New exporter success prediction tool

## 1. Problem Description

By engaging in exports, firms gain access to a wider consumer base, which can allow them to expand their production, potentially leading to lower costs through economies of scale and permitting the creation of new jobs. Firms can also benefit from exposure of more competitive markets, being forced to implement new sanitary and quality controls and increase tracebility. Additionally, international trade often attracts foreign investment and technological progress that can further contribute to economic growth. Therefore, the success and growth of new exporters is of importance, not only for the profitability of firms, but also for economic development. Unfortunately, the survival of exporters in new markets is significantly low; related studies indicate that more than 50% of new exporters do not continue exporting after the first year in a new market. 

Can firms be more strategic when selecting new export markets to maximize their potential of success? This project aims to shed some light on this question about bussiness decisions for new exporters. The main objective of is to develop a ML model to predict whether an exporter entering a new market with a new product will be successful based on their previous experience, as well as the products traded and the new market selected. The measure of success employed will be that the exporter continues to actively export to the new market in the year following the decision of market entry.

## 2. Dataset

The dataset selected for this project contains all record of new export transactions, defined as any combination of exporter-market-product not recorded in the previous year, registered in Colombia between 2017 and 2021. 

This dataset was obtained by aggregrating all export transactions filed to the Colombia Tax Authority - DIAN between 2016 and 2022. Only commercial transactions were considered, temporary exports, exports for exhibition purposes, exports by diplomatic missions and exports to free trade zones were excluded. One time exporters were also excluded from the analysis and export-market-product transactions with annual value of less than USD$1000 were also eliminated from the dataset, to ensure that only exporters with true bussiness commitments were studied.

The aggregate records were explored to tag all the new exports transactions each year and these transactions were examined to determine succesful and unsuccesful outcomes, as previously defined. The data was filtered to only contain new export records with their correspondent success marker. 

The dataset was completed by adding additional features about the new market, such as world region and size, as well as on the new product traded, such as classifications by section in the harmonized system. Prior exporter experience from the previous year obtained from the original records, was also appended to the dataset were available. These features were selected based on literature and experience, for consideration and evaluation in the exploratory data analysis.    

All steps to obtain the dataset from original export records (available for download at https://microdatos.dane.gov.co/index.php/catalog/472/get-microdata) are included in notebook1.ipynb. 

## 3. Exploratory Data Analysis (EDA)

To build a successful model for prediction of exporter success, it is key to explore different factors that could have an impact on this outcome and select those that appear to have the most incidence. As described in the previous section, for this project additional data was added to export records in order to create new features that could be relevant. Features added include gdp per capita, region and language of new market, exporter experience and region in Colombia were it is located, export product classifications and free trade agreement information. These features were explored graphically and analysis of feature importance was also conducted. 

In addition, the dependant variable - success - was also explored to verify whether data was imbalanced and consider measures to address this problem if present. The variable fortunately did not have this problem so it was not necessary to take additional steps for modelling.

All results of the EDA are available in notebook2.ipynb and some visualizations were included in the webapp developed for this project.

## 4. Model

Considering the characteristics of the dependent variable, three types of model were tested in this project. A first approach was to build a logistic regression with the variables that were identified as relevant in the EDA. Adjustments on the target features were made based on their significance, to derive a set of target varaibles for training a final selected logistic regression model. Different metrics were considered to evaluate this model and cross validation was also conducted. The performance of logistic regression was not outstanding

Two other models, random forest and XGBoost were also trained with the same selected features and evaluated. Parameter tuning was conductedin both cases. Metrics for the resulting models after the tuning showed a significant improvement and were very similar among them. A random forest was selected as the final model. 

All steps in modelling, review of feature significance and parameter tuning are available in notebook2.ipynb.

## 5. Deployment

## 6. Reproducibility

This project can be reproduced locally in three ways after cloning the repository and opening a command line in the corresponding folder:
1. Create a local environment with the pipfiles and run the test-predict.py script which serves a simple flask app with data from a sample exporter and returns the probability of success.
2. Create a local environment with the pipfiles and run the app.py to create the WebApp designed for this project. A test version of the app will run locally at the IP address provided once the script finishes running.
3. Build the docker container - docker build -t exporter-success . - and run it - docker run -it -p 9696:9696 exporter-success:latest. The WebApp is served using unicorn so it will not work in Windows-based environments. 

As mentioned previously, all the notebooks that contain all the steps for creating the dataset and tuning the model are also available in this repository.

## 7. References
