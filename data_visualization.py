import matplotlib.pyplot as mpl
import numpy as np

countries = np.array([
'Denmark',
'Switzerland', 
'Sweden',
'US',
'England',
'Netherlandas',
'Germany',
'Finland',
'Spain',
'Belgium',
'France',
'Austria',
'Italy',
'Israel',
'Greece'
])
percentage = np.array([25,26,30,30,33,35,37,39,40,42,45,46,47,48,62])

fig, ax  = mpl.subplots()
ax.bar(countries, percentage)
ax.set_xticklabels(countries, rotation=-90)

mpl.show()
