# Restaurant Growth Potential Modeling & Strategic Classification System

## Project Overview

This project looks at restaurant data to understand how different restaurants are performing. I analysed their orders, growth, costs, profit margins and delivery channels to identify patterns and group restaurants with similar performance using K-Means clustering.

## Objectives

- Analyse restaurant orders, revenue, profit margins and costs.
- Calculate a Growth Potential Index (GPI) to compare restaurants.
- Use K-Means clustering to group restaurants with similar performance.
- Understand the differences between clusters and suggest possible business strategies.

## Tools and Technologies

- Python
- Pandas
- Matplotlib and Seaborn
- Scikit-learn
- StandardScaler
- PCA
- K-Means Clustering
- Jupyter Notebook

## Methodology

I started by checking the dataset for missing values and duplicates. Then I explored the data, analysed the main business measures and calculated the GPI. I used StandardScaler to scale the selected features, PCA to visualise the data in two dimensions, and K-Means to create five restaurant groups. Finally, I reviewed the cluster results and assigned strategy recommendations using simple rules based on the restaurant data.

## Results

The analysis resulted in five restaurant clusters with different performance characteristics. I also created a scorecard containing GPI scores and strategy recommendations for individual restaurants. The cluster profiles help compare the groups and understand where improvements may be needed.

## Limitations

The GPI weights and strategy recommendations are based on the rules used in this project. The results depend on the available dataset and should be treated as a way to compare restaurant performance, not as a guarantee of future growth.
