#reading, transforming and manipulating FCS files
#Date Modified: Noveber 24
#Make sure you have Flow Kit installed


import flowkit as fk
import numpy as np
import pandas as pd

#here is the fcs file we will read. 
fcs_path = 'sampleFCS.fcs'

#read in the FCS file
sample = fk.Sample(fcs_path)

#print to see how manny cells and channels there are
#doing so tells us that there are 268796 cells (events) and 49 channels
print(sample)

#convert to numpy array
dm = sample.get_raw_events()

#now we will look at the channel names. This is helpful because we will get comprehsnible marker names.
#we will then be only selecting channel corresponding to our marker of interest
CNames = np.array(sample.pns_labels)

#for downstream analysis we will keep the following channels corresponding to phenotypic and functional markers
#you will need to customize this for your own analysis
toKeep = [9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45]

##################################################################
#yfinally create your data matrix for further analysis
##################################################################

#now we will transform the data and select our columns/markers of interest
dm_trans= np.arcsinh(1./5 * dm[:,toKeep])
CNames=CNames[toKeep]

#you could have stopped there, but we can make a 'nice' dataframe
df_nice = pd.DataFrame(dm_trans,columns=CNames)
print(df_nice)


