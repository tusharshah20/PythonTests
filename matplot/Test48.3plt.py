from dateutil.parser import parse 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
#plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})
# Import data
ap = pd.read_csv('I:\\Trainings\\MyContent\\Books\\resources\\AirPassengers.csv', parse_dates=['date'])
x = ap['date'].values
y1 = ap['value'].values

# Plot
def plot_ap(ap, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.fill_between(x, y1=y1, y2=-y1, alpha=0.5, linewidth=2, color='seagreen')
    plt.ylim(-800, 800)
    plt.title('Air Passengers (Two Side View)', fontsize=16)
    #plt.hlines(y=0, xmin=np.min(ap.date), xmax=np.max(ap.date), linewidth=.5)
    plt.show()
plot_ap(ap, x=ap.index, y=ap.value) 
#Since its a monthly time series and follows a certain repetitive pattern every year,
# you can plot each year as a separate line in the same plot. This lets you compare 
# the year wise patterns side-by-side.