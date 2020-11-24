# Objective

We will learn how to read and pre-process FCS files using both R and Python. The main components of dealing with FCS files are as follows
* Reading an FCS file
* Applying an Arcsinh transformation
* Getting interpretable marker names that correspond to the antibodies in the experiments
* Subset only the channels of interest (e.g. phenotypic and functional markers) 

These examples show you how to create your `cells x marker` matrices that can be used for downstream tasks.

# Using FlowKit in python

First, make sure you have FlowKit installed: 

```bash
pip3 install FlowKit` 
```

You can read the following for more info about FlowKit,
* https://pypi.org/project/FlowKit/
* https://flowkit.readthedocs.io/en/develop/index.html

You can check out `sampleFCSProcess.py` to see steps with instructions or,

```bash
python3 sampleFCSProcess.py
```

It will print a preview of the cell x marker data matrix.

# Using flowCore in R

Makre sure you have flowCore installed,

```R
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("flowCore")
```

You can read more about flowCore here,

* https://bioconductor.org/packages/release/bioc/html/flowCore.html

You can check out  `flowCoreProcess.R` to see steps with instructions or,

```R
source('flowCoreProcess.R')
```

It will print a sample of your data matrix, which is the same as with flowkit :) 