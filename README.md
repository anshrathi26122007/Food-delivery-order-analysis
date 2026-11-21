# Food Delivery Data Analysis

## 1) Project Objective

The objective of this beginner Python project is to explore food delivery order data and practice basic data analysis. It uses **pandas** to load, filter, group, and summarize data, and **NumPy** to calculate numeric statistics.

## 2) Project Overview

This is an interactive command-line program. After starting it, enter a command such as `revenue`, `city summary`, or `delivery` to choose what information to print. Type `help` to see all commands, or `exit` to close the program.

The project includes a synthetic dataset of 400 orders covering dates in 2025. The data is made for practice and does not represent real customers or businesses. Amounts and tax are illustrative.

### Setup and run

Install Python 3.9 or newer, then open a terminal in the project folder and run:

```bash
python -m venv .venv
```

Activate the environment in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux, activate it with:

```bash
source .venv/bin/activate
```

Install the libraries and start the program:

```bash
pip install -r requirements.txt
python analysis.py
```

Keep `orders.csv` beside `analysis.py`, or put it in a `data` subfolder. The script checks both locations.

## 3) Dataset

The file `orders.csv` contains 400 rows and 17 columns:

| Column | Description |
|---|---|
| `order_id` | Unique order number |
| `order_date` | Date the order was placed |
| `city` | Delivery city |
| `area` | Delivery area within the city |
| `restaurant` | Restaurant name |
| `cuisine` | Cuisine category |
| `item_count` | Number of items in the order |
| `subtotal` | Items total before discount, fee, and tax |
| `discount` | Discount applied to the order |
| `delivery_fee` | Delivery charge |
| `tax` | Illustrative tax amount |
| `order_value` | Subtotal minus discount, plus fee and tax |
| `distance_km` | Delivery distance in kilometers |
| `delivery_minutes` | Delivery time in minutes |
| `customer_rating` | Customer rating from 1 to 5; blank when no rating was recorded |
| `payment_method` | Payment type |
| `order_status` | Order outcome: delivered, delayed, or cancelled |

## 4) Working

When `analysis.py` starts, it locates `orders.csv` and loads it into a pandas DataFrame (a table of rows and columns). It then repeatedly asks what data you want to print.

The command handler checks your input and runs the matching calculation. Examples include:

| Command | Result |
|---|---|
| `all` | Prints every order row |
| `revenue` | Adds the `order_value` values |
| `average order value` | Calculates the mean order value |
| `delivery` | Prints average and median delivery times, plus the count under 30 minutes |
| `ratings` | Calculates the average customer rating |
| `city summary` | Groups orders by city and summarizes order value, discounts, and ratings |
| `area summary` | Groups the data by delivery area |
| `cuisine summary` | Groups the data by cuisine |
| `restaurant summary` | Groups the data by restaurant |
| `payment summary` | Groups the data by payment method |
| `status summary` | Counts orders by status |
| `discounts` | Totals discounts and counts orders that received one |
| `distance` | Prints average and longest delivery distance |
| `top order` | Shows the order with the highest recorded value |
| `city Delhi` | Prints orders for the named city |
| `cuisine Biryani` | Prints orders for the named cuisine |
| `help` / `exit` | Shows commands / closes the program |

Pandas `groupby()` puts rows with the same category together, while `agg()` calculates summaries such as counts, sums, and averages. NumPy is used for numeric calculations and counting conditions, such as deliveries under 30 minutes.

## 5) Key Insight

From the included synthetic dataset:

- There are **400 orders** with a total recorded `order_value` of about **593,797.57** and an average recorded order value of about **1,484.49**.
- **262 orders were delivered**, **76 were delayed**, and **62 were cancelled**. That is 65.5%, 19%, and 15.5%, respectively.
- **Kolkata** has the largest sum of recorded order values among the cities, at about **90,219.50**.

These totals include every row, including cancelled orders. Treat them as dataset summaries rather than realized sales; filter out cancelled orders if you want to estimate completed-order revenue.

## 6) Project Structure

```text
food_delivery_analysis/
├── analysis.py          # Interactive analysis program
├── requirements.txt     # pandas and NumPy dependencies
├── README.md            # Project guide
└── data/
    └── orders.csv       # 400 sample food delivery orders
```

## 7) Conclusion

This project demonstrates a simple end-to-end analysis workflow: load a CSV with pandas, inspect and filter its rows, calculate statistics with pandas and NumPy, and print results selected by the user. You can extend it by adding charts, monthly trends, cancellation rates by city, or comparisons between delivery distance and delivery time.

Author- ANSH RATHI
