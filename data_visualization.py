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
rfriend_per =np.array([95.3, 86.6, 90.8, 91.5, 88.4,91.7, 94.8, 94.6, 92, 90.1, 
93.2, 89.9, 91.8, 94, 95.3])
# rfriend_per = sorted(rfriend_per)

font_styles = {
  'family' :'serif', 
  'color': 'purple', 
  'weight' : 'normal', 
  'size': 15
}


mpl.suptitle('Lonliness & Friends Trust per Country')
mpl.subplot(2,2,1)
mpl.grid()
mpl.title('Lonliness per Country plot')
mpl.ylabel('Countries')
mpl.xlabel('Lonliness in %')
mpl.plot(lonliness_per, countries, 'o-', color = "#15E79E")

mpl.subplot(2,2,3)
mpl.grid(axis = "y", color = "gray")
mpl.ylabel('Countries')
mpl.xlabel('Lonliness in %')
mpl.bar(lonliness_per, countries, color = "#15E79E")

mpl.subplot(2,2,2)
mpl.title('Friend Trust per Country')
mpl.grid()
mpl.ylabel('Countries')
mpl.xlabel('Friend trust in %')
mpl.plot(rfriend_per, countries, 'o-', color = "#6BCA00")


mpl.subplot(2,2,4)
mpl.grid(axis = "y", color = "gray")
mpl.ylabel('Countries')
mpl.xlabel('Friend trust in %')
mpl.bar(rfriend_per, countries, color = "#6BCA00")

mpl.show()
