import sys
from networksecurity.logging import logger

class networksecurityexception(Exception):
    def __init__(self, error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()

        self.line_no=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occured in python script '{self.file_name}' in the line '{self.line_no}' and it is a '{self.error_message}' error."
    
if __name__=="__main__":
    try:
        logger.logging.info("Enterd the try block")
        a=1/0
        print("this willl not be printed",a)

    except Exception as e:
        raise networksecurityexception(e,sys)
    
