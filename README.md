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

## 3. Exploratory Data Analysis

## 4. Model
## 5. Deployment
## 6. Reproducibility
## 7. References
