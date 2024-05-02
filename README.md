# Basket-Association-Analysis
This project focuses on finding the basket Association (Which products are most likely sold together as a combo) to improve the company's sales.

I. Database Schema & Test Data
- OrderID: Order ID
- Product: Product name

II. Steps:  
  1. Data Wrangling:
    - Load and read data from path
    - Data preprocessing: Rename, Change data type, fill null cells,...
    - Filter data, only take OrderID and Product

  3. Data Analysis:
    - Get ProductType by using apply lambda to take the first 3 words in the Product column.
    - Using RegEx to filter Product Type.
    - Count how many products are there in the same OrderID and only take the first 2 products.
    - Pivot table: Index = 'OrderID', values = 'ProductType' to concatenate Product Type and get the combo name

III. Tools:
- Python: Pandas, RegEx
