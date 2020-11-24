#Here is how we can read FCS files in R using the flowCore package
#Date Modified: November 24, 2020
#Make sure you have 

library('flowCore')

#our file name
fileName='sampleFCS.fcs'

#define the parameters of our transformation
cytoftrans=arcsinhTransform(transformationId='cytofTransform',a=0,b=(1/5),c=0)

#read fcs file to be a 'flowFrame'
frame=read.FCS(fileName)

#apply transformation
translist=transformList(colnames(exprs(frame)),cytoftrans)
frame=transform(frame,translist)
X=exprs(frame)

#get the marker names in a comprehensible format
MN=pData(parameters(frame))[,2]
colnames(X)=MN

#let's keep only the markers we are interetsed in
toKeep=c(9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45)
toKeep=toKeep+1

#here is your data matrix 
X=X[,toKeep]

print(X[1:5,1:5])