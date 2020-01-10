# Cloudbleed Project 


## Project Overview
The goal of this project is to provide a working framework to show how causal modeling can be used to assist in determining cybersecurity.

## References
This project builds off the previous paper by Dr. Suchitra Abel: [Causal Modeling for Cybersecurity](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8760379) 
We are looking at a generalized case of data breaches and testing out a working causal model using

We are using [DoWhy](https://github.com/microsoft/dowhy/tree/master/dowhy), Microsoft's Python library for Causal Inferences, for this project.

The dataset we used to gather information about data breaches is provided by the [Veris Community Database (VCDB)](http://veriscommunity.net/vcdb.html)

The graph causal model is provided below:
![Causal Model](https://raw.githubusercontent.com/paekman17/CloudBleed_Project_2019/master/causal_model.png)

**Causal Modeling Analysis Techniques Used:

- Linear Regression Estimator
- Propensity Score Stratification Estimator
- Propensity Score Matching Estimator

The project can be viewed by running vcdb_parse.ipynb.

