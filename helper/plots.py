from geopandas import GeoDataFrame
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

def hist_plot(data: GeoDataFrame, column:str)-> None:
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data[column], bins=len(data[column].unique()), ax=ax)
    plt.title(f'Histogram of {column}', fontsize=12) 
    plt.tight_layout()