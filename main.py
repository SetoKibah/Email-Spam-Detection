# Reference: https://www.youtube.com/watch?v=cNLPt02RwF0

# Description: Program detects if an email is spam (1) or not (0).

# Import libraries
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string


# Load the data
#from google.colab import files
#uploaded = files.upload(emails.csv)

# Read the CSV file
df = pd.read_csv('emails.csv')
# Print the first 5 rows rows of data
