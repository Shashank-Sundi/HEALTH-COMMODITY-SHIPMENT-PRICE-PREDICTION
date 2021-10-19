from Log_Writer.logger import App_Logger
from sklearn.impute import KNNImputer

def null_value_imputer(data):
    log_writer=App_Logger()
    try:
        #getting columns with null values
        null_cols=find_null_cols()

        for col in null_cols:
            imputer = KNNImputer(n_neighbors=10)
            imputer.fit(clean_data)
            data[col] = imputer.transform(data[[col]])

        log_writer.log(log_message="Null Value Imputation Completed Successfully")
        return data
    except Exception as e:
        log_writer.log(log_message="ERROR occured in null value imputation")
        return print(e)

