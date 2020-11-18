import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
os.stat("MoviesOnStreamingPlatforms_updated.csv")
df = pd.read_csv ("MoviesOnStreamingPlatforms_updated.csv")

df.head()
st.title("Data App")








