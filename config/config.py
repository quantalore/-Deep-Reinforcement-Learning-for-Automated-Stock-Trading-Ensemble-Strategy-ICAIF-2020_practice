import pathlib
import pandas as pd
import datetime
import os

Training_data_file = "data/dow_30_2009_2020.csv"

now = datetime.datetime.now()
Trained_model_dir = f"trained_models/{now}"
os.makedirs(Trained_model_dir)
Turbulence_Data = "data/dow30_turbulence_index.csv"
Testing_data_file = "test.csv"
