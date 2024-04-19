# This Code was created on 2/22/2024
# Author: Miles Mercier
# Undergraduate of Department Physics and Astronomy 
import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

# Read data from Excel file
# Make sure that file is in same directory as this program!
data = pd.ExcelFile('022224_ORI.xlsx') 
sheet1 = data.parse(0) 
freq_obs = sheet1.iloc[:, 0] # This will read the first column of the Microsoft Excel file.
dBm = sheet1.iloc[:, 1] # This will read the seconf column of the Microsoft Excel file.

# Knowns
freq_emitt = 1420.405751768  # MHz (Rest frequency of Neutral Hydrogen)
c =299792458 # m/s (The Measured Speed of Light)
H_o = 69.8 #km/sec/Mpc (Hubbles constant)

# Find peak
peak_index = np.argmax(dBm)  # Index of maximum signal strength
peak_freq = freq_obs[peak_index]  # Frequency at the peak
peak_strength = dBm[peak_index]  # Signal strength at the peak

# Calculate the redshift from the Emitted and Observed frequency 
shift = (freq_emitt/peak_freq) -1

if shift >= 0:
    print('The red shift value from this data is Z = {}.'.format(shift))
    
if shift <= 0:
    print('The blue shift value from this data is Z = {}.'.format(shift))

# Calculate the Recessional Velocity of Peak
v_rec = shift*c *3.6# Shows the recessional velocity in kilometers per hour.
rec_unit = 'km/hr'
print('The recessional velocity from this data is: {} {}.'.format(v_rec, rec_unit))

# Calculate the Distance to the Observed portion of the sky.
d = (H_o / v_rec) * 3261563.7769
d_unit = 'ly'
print('The distance to the observed area is {}{}.'.format(d,d_unit))

# Calculate the rotational speed of the galaxy.
d_con = d * 9.461e12 # converts d from ly to km 
r = 2.44087e17 + d_con # radius to galaxy based on observation (units in lightyears)
rot_vel = v_rec/r
rot_units = 'km/s'
print('The rotational velocity of the Milky Way from this data is found to be {}{}'.format(rot_vel,rot_units))
 

# Plotting
fig, ax = pp.subplots()  # Creating figure and axis objects
pp.xticks(rotation=30)  # Rotating x-axis tick labels by 30 degrees for better readability
ax.plot(freq_obs, dBm)
ax.set_xlabel('Frequency, MHz')
ax.set_ylabel('Signal Strength, dBm')
pp.title('Signal Strength versus Frequency')

# Annotate the peak point
ax.annotate(f'Peak: ({peak_freq:.2f} MHz, {peak_strength:.2f} dBm)',
            xy=(peak_freq, peak_strength),
            xytext=(peak_freq + 10, peak_strength - 10),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Create a table to display peak value
table_data = [['Frequency (MHz)', 'Signal Strength (dBm)'],
              [peak_freq, peak_strength]]
table = ax.table(cellText=table_data, loc='upper right', edges='closed', colWidths=[0.15, 0.19]) #Adjust table to clear the data on graph.
table.auto_set_font_size(False)
table.set_fontsize(5)


#pp.savefig('Data_AUR030724.png') # Rename to Constellation and Data data was taken.
pp.show()
