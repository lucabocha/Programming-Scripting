# This script is used as a program that is able to covert to or from excel files. 
# Although conversion can be achived via an online converter I rather convert files locally if possible and specially if they contain sensitive information

# Please install the following modules before execution: 
  # pandas
  # openpyxl
  # IPython

# Visualize the contents of the xlsx file: 

from IPython.display import display
import pandas as pd

df = pd.DataFrame(pd.read_excel("myrouterinformation.xlsx")) 

display(df)
