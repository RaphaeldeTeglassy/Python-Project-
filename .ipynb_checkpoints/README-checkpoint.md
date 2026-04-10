# Discounts and Sales in Retail
Mini-project for the Programming & Data Analytics course.

**Research question:** What is the relationship between discounts and sales?  
**Dataset:** Superstore (Kaggle, ~10,000 transactions)  
**Method:** Exploratory analysis + simple linear regression (Sales ~ Discount)

## Why this project

Discounts are widely used in retail to increase sales, but their actual relationship with sales is not always straightforward. In this project, we find a result that may seem surprising at first: higher discounts are associated with slightly lower sales on average. This makes the analysis interesting, as it shows that what we observe in the data does not always match our initial intuition. This project helped me better understand how data should be interpreted carefully, especially when variables are linked to business decisions.

To be noted:
> The dataset (`superstore.csv`) is not committed to the repository.  
> Download it from [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) and place it in the same folder as the notebook.

## How to run the project

```bash
pip install -r requirements.txt
jupyter notebook project.ipynb
```
## Method
The analysis is done in three steps:

1. Data exploration and visualisation  
2. Computation of average sales by discount level  
3. Simple linear regression (Sales ~ Discount)  

## Key result
The OLS regression finds a statistically significant but very weak negative relationship between discount and sales (slope ≈ -85, R² < 0.001).
This result may seem counterintuitive, as we might expect discounts to increase sales. However, it likely reflects how discounts are used in practice rather than their direct effect.


## Main limitation 
The main limitation is endogeneity: discounts are not randomly assigned, so we cannot interpret this as a causal effect.

## Possible extensions

If we wanted to go further, we could improve this analysis in several ways. First, we could control for product category, since discount strategies are probably different across products. Second, we could also look at quantities sold instead of revenue, as discounts might increase volume even if the total amount per transaction decreases. Finally, a more advanced approach would be needed to identify a causal effect, for instance by comparing sales before and after a promotion.
