# HEALTH-COMMODITY-SHIPMENT-PRICE-PREDICTION

[![wakatime](https://wakatime.com/badge/user/8f2e3b3a-321e-4119-b4f0-3a33c3752953/project/f1c60e47-055d-4059-9946-5863bccf6e83.svg)](https://wakatime.com/badge/user/8f2e3b3a-321e-4119-b4f0-3a33c3752953/project/f1c60e47-055d-4059-9946-5863bccf6e83)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://thyroid-detection-pred-sundi.herokuapp.com/)&nbsp;
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)&nbsp;
<img src="https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg">&nbsp;
![GitHub repo size](https://img.shields.io/github/repo-size/Shashank-Sundi/HEALTH-COMMODITY-SHIPMENT-PRICE-PREDICTION)&nbsp;
![Lines of code](https://img.shields.io/tokei/lines/github/Shashank-Sundi/HEALTH-COMMODITY-SHIPMENT-PRICE-PREDICTION?style=flat)

Machine Learning Project to predict the price of health commodity (Antiretroviral (ARV) and HIV lab shipments) shipped to different countries 

<img src="static\images\alan-veas-z1oKOZjtvVQ-unsplash.jpg" alt="affair" />
<hr>

## Deployment

The model has been deployed using REST API using flask, on Heroku :  https://shipment-price-pred-sundi.herokuapp.com/


## Original Dataset and Python Notebook

Original Dataset :  https://data.usaid.gov/HIV-AIDS/Supply-Chain-Shipment-Pricing-Data/a3rc-nmf6

Python Notebook : https://shashank-sundi.github.io/HEALTH-COMMODITY-SHIPMENT-PRICE-PREDICTION/

Python Notebook : https://github.com/Shashank-Sundi/NOTEBOOKS/blob/main/SHIPMENT-PRICING.ipynb

<hr>

## Project Description

| PROBLEM | MODELS USED  |LIBRARIES USED   |IDE's USED|
| :-------- | :------- | :------------------------- | :-------|
| **Predicting if a patient suffers from Thyroid Disease**| `LINEAR REG,` `ELASTIC/RIDGE REG,` `KNN,` `KMEANS,` `SVM,` `DECISION TREE,` `RANDOM FOREST,` `XGBOOST` | `Sklearn ,` ` Seaborn ,` `Pandas ,` `Numpy ,` `Scipy ,` `Xgboost `|`PyCharm,` `VS Code,` `Jupyter Notebook`|

<hr>

## Project Execution

### (A) **Analysis in Jupyter Notebook**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1| Validated and rectified the data types of the features and analysed their statistical properties|
|2|Performed EDA on data - checked the distribution of data using NPP, KDE plots , visualized relation between the different features
|3| Performed Random Sample Imputation for Categorical columns and KNN imputation for Numerical Columns
|4|Encoded top 10 categories in all columns using Frequency Encoding and mapping
|6|Visualized Outliers via BoxPlots and removed the possible Outliers , by manually setting the threshold
|7| Visualized the correlation matrix and removed highly correlated columns
|9|Clustered the dataset into 3 clusters , using Kmeans and the elbow graph
|10| Metric used to evaluate models - Adjusted r2 score
|11| Trained and tested various models on the data clusters and for each cluster , chose the model which gave highest adj r2 score
|12|XGB Regressor gave highest adj r2 score for all clusters.Hence , we can conclude that models generalise worse after clustering ,as compared to the whole dataset.Hence we don't need to to cluster the data
|13| Exported all required models via pickle


### (B) **Building the Application**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1| Built Log Writer Package , for writing the log messages in a centralised log file
|2| Built the Data Formatter Package, for aggregating the inputs from the html form ; converting the input to a dataframe
|3| Buil the Valaidator Package , to validate the data types of inputs , column names , length etc.
|4| Built the Preprocessing Package ,for imputation , encoding and other transformations
|5| Built Package for finding the cluster to which the input data belongs ; exporting the model trained for the corresponding cluster
|5| Built REST API using Flask framework ; created routes for home page and prediction , by calling all the required modules 
|6| Created the requirements.txt , Procfile , etc. and all other requirements to be satisfied for deployment.
|7| Built html pages for data input and results prediction
|8| Deployed the model on Heroku via Git Bash terminal

<hr>

## Screenshots

### **Enter the required inputs in home page and press predict button**

<img src="static\images\homeww.PNG" alt="FIFA" style="height: 300px; width:700px;"/>

### **The Prediction Page**

<img src="static\images\resultt.PNG" alt="FIFA" style="height: 300px; width:700px;"/>

<hr>
  
## Contact

<a href="https://www.linkedin.com/in/shashank-sundi-4b78561b1"> ![alt text](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)</a>&emsp;
<a href="https://www.instagram.com/shashank_sundi13/">![alt text](https://img.shields.io/badge/Shashank_Sundi-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)</a>&emsp;
<a href="mailto:sundi.sn@gmail.com">![alt text](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>

<hr>
