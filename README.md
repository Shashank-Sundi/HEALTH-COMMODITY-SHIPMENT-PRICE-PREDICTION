# HEALTH-COMMODITY-SHIPMENT-PRICE-PREDICTION
Machine Learning Project to predict the price of health commodity (Antiretroviral (ARV) and HIV lab shipments) shipped to different countries 

<img src="static\images\alan-veas-z1oKOZjtvVQ-unsplash.jpg" alt="affair" />
<hr>

## Deployment

The model has been deployed using REST API using flask, on Heroku :  https://thyroid-detection-pred-sundi.herokuapp.com/


## Original Dataset and Python Notebook

Original Dataset : https://github.com/Shashank-Sundi/THYROID-DETECTION-CLASSIFICATION/blob/main/hypothyroid.csv

Python Notebook : https://github.com/Shashank-Sundi/NOTEBOOKS/blob/main/thyroid-prediction.ipynb

<hr>

## Project Description

| PROBLEM | MODELS USED  |LIBRARIES USED   |IDE's USED|
| :-------- | :------- | :------------------------- | :-------|
| **Predicting if a patient suffers from Thyroid Disease**| `LOGISTIC REG,KNN,SVC,NAIVE BAYES,RANDOM FOREST,XGBOOST` | `Sklearn , Seaborn ,Pandas ,Numpy ,Scipy ,Xgboost `|`PyCharm,` `VS Code,` `Jupyter Notebook`|

<hr>

## Project Execution

### (A) **Analysis in Jupyter Notebook**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1| Validated and rectified the data types of the features and analysed their statistical properties|
|2| Created some new features capturing the importance of missing values in some features
|3| Removed invalid data types and imputed missing values with corresponding feature means
|4|Encoded columns using Frequency Encoding and mapping
|5|Performed EDA on data - checked the distribution of data using NPP, KDE plots ; checked for outliers via boxplots
|6|Removed Extreme Outliers
|7| Oversampled the minority class , using SMOTE
|8| Visualixed the correlation matrix and removed Multi-Collinearity
|9|Clustered the dataset into 4 clusters , using Kmeans and the elbow graph
|10| Metric used to evaluate models - We use Accuracy and Recall
|11| Trained and tested various models on the data clusters and for each cluster , chose the model which gave highest recall score 
|12.1| Best Model for Cluster 1 : rf --Recall : 99.37%
|12.2|Best Model for Cluster 2 : xgb --Recall : 99.29%
|12.3|Best Model for Cluster 3 : Logreg --Recall : 99.43%
|12.4|Best Model for Cluster 4 : Logreg --Recall : 99.12%
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

<img src="static\images\homethyroid.PNG" alt="FIFA" style="height: 300px; width:700px;"/>

### **The Prediction Page**

<img src="static\images\resultthyroid.PNG" alt="FIFA" style="height: 300px; width:700px;"/>

<hr>
  
## Contact

<a href="https://www.linkedin.com/in/shashank-sundi-4b78561b1"> ![alt text](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)</a>&emsp;
<a href="https://www.instagram.com/shashank_sundi13/">![alt text](https://img.shields.io/badge/Shashank_Sundi-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)</a>&emsp;
<a href="mailto:sundi.sn@gmail.com">![alt text](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>

<hr>