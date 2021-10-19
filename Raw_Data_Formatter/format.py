from Log_Writer.logger import  App_Logger
import pandas as pd


def format(data):
    log_writer=App_Logger()
    try:
        log_writer.log(log_message="Converting raw data to DataFrame")

        data=pd.DataFrame(data=data,columns=['age', 'sex', 'on_thyroxine', 'query_on_thyroxine',
                           'on_antithyroid_medication', 'sick', 'pregnant', 'thyroid_surgery',
                           'I131_treatment', 'query_hypothyroid', 'query_hyperthyroid', 'lithium',
                           'goitre', 'tumor', 'hypopituitary', 'psych', 'TSH', 'TSH_nan', 'T3',
                           'T3_nan', 'TT4', 'TT4_nan', 'T4U', 'FTI', 'FTI_nan', 'referral_source'])

        log_writer.log(log_message="Converted Raw Data to DataFrame")
        return data

    except Exception as e:
        log_writer.log(log_message="ERROR occured in converting Raw Data to DataFrame")
        return print(e)