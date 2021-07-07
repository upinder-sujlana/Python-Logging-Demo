import logging
import sys

a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
a_logger.addHandler(handler)

#--------------------------------------------------------
days_of_week=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
weekend=["sunday","saturday"]
def printToStdout():
    for i in days_of_week:
        if i not in weekend:
            a_logger.debug(str(i) + "    - Weekday you gotta work it !!!" )
        else:
            a_logger.debug(str(i) + "    - Weekend you sleep, unless its the dreaded BIC  :) " )
#--------------------------------------------------------
if __name__ == "__main__":
    printToStdout()