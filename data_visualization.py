import matplotlib.pyplot as mpl
from matplotlib.ticker import FixedLocator, FixedFormatter
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
lonliness_per = np.array([25,26,30,30,33,35,37,39,40,42,45,46,47,48,62])
rfriend_per =np.array([95.3,94, 91.8, 89.9, 93.2,90.1, 92, 94.6, 94.8, 91.7, 88.5,
91.5, 90.8, 86.6, 82.3])
rfriend_per = sorted(rfriend_per)

mpl.subplot(2,2,1)
mpl.grid()
mpl.plot(lonliness_per, countries)

mpl.subplot(2,2,2)
mpl.grid()
mpl.bar(lonliness_per, countries)

mpl.subplot(2,2,3)
mpl.plot(rfriend_per, countries)
mpl.grid()

mpl.subplot(2,2,4)
mpl.bar(rfriend_per, countries)
mpl.grid()

mpl.show()
