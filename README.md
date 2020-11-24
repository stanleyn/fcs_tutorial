# Objective

We will learn how to read and pre-process FCS files using both R and Python. The main components of dealing with FCS files are as follows
* Reading an FCS file
* Applying an Arcsinh transformation
* Getting interpretable marker names that correspond to the antibodies in the experiments
* Subset only the channels of interest (e.g. phenotypic and functional markers) 

These examples show you how to create your `cells x marker` matrices that can be used for downstream tasks.

# Using FlowKit in python

First, make sure you have FlowKit installed: 

`pip3 install FlowKit` 

You can check out `sampleFCSProcess.py` to see steps with instructions or,

```python
python3 sampleFCSProcess.py
```

It will print a preview of the cell x marker data matrix.

