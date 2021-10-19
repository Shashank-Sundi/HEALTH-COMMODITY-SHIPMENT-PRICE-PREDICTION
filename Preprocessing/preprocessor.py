from Log_Writer.logger import App_Logger
from Preprocessing.null_imputer import null_value_imputer
from Preprocessing.categ_encoding import encode

class Preprocessor:

    def __init__(self):
        self.log_writer=App_Logger()

    def preprocess(self,data):
        try:
            data=encode(data)
            data=null_value_imputer(data)
            self.log_writer.log("Data Preprocessing Completed Successfully")
            return data

        except Exception as e:
            self.log_writer.log("\nERROR occured while preprocessing data\n")
            return print(e)