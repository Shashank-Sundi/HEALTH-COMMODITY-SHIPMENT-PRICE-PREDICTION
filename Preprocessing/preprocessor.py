from Log_Writer.logger import App_Logger
from Preprocessing.null_imputer import null_value_imputer

class Preprocessor:

    def __init__(self):
        self.log_writer=App_Logger()

    def preprocess(self,data):
        try:
            data=null_value_imputer(data)
            self.log_writer.log("Data Preprocessing Completed Successfully")
            return data

        except Exception as e:
            self.log_writer.log("ERROR occured while preprocessing data")
            return print(e)