import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Data
df = pd.read_excel(r"data\Dataset.xlsx")

# Initial Exploration
df.info()
print("---------------------------------------")

print(df.sample(10))
print("---------------------------------------")

print(df.describe())
print("---------------------------------------")

# # Missing Values Check
# # CouponCode contains 309 missing values
print(f"Count Null Values (Before Cleaning) : \n{df.isnull().sum()}")
print("---------------------------------------")

# # Duplicate Check
print("Duplicated Rows :", df.duplicated().sum())  # 0
print("Duplicated OrderID :", df['OrderID'].duplicated().sum())  # 0
print("---------------------------------------")

# # Date Validation
# Convent Date column to proper date format.
df['Date'] = pd.to_datetime(df['Date'])
print("Missing Date :", df['Date'].isna().sum())  # 0
print("---------------------------------------")

# Handling Missing Values
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')

# # Final Validation
print(f"Count Null Values (After Cleaning) : \n{df.isnull().sum()}")  # 0
print("---------------------------------------")

assert df.duplicated().sum() == 0
assert df['OrderID'].duplicated().sum() == 0
assert df['Date'].isna().sum() == 0

# Calculate basic statistics
print('Calculate basic statistics : ')
print(df[['Quantity','UnitPrice','TotalPrice']].agg(['mean','median','count']).round(2))
print("---------------------------------------")

# Identify trends and outliers
# Outliers
print(f"TotalPrice Agg : \n{df['TotalPrice'].agg(['mean','median','max']).round(2)}")
Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['TotalPrice'] < lower_bound) | (df['TotalPrice'] > upper_bound)]
print(f"Outlier Orders : \n{outliers[['OrderID','Product','TotalPrice']]}")
print(f"Count of outliers : {len(outliers)}")

plt.figure(figsize=(8,4))
sns.boxplot(x=df['TotalPrice'])
plt.show()
print("---------------------------------------")

# Trends
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['DayName'] = df['Date'].dt.day_name()
monthly_sales = df.groupby('Month')['TotalPrice'].sum().round(2).sort_values(ascending=False)
print("Monthly Sales : \n",monthly_sales)
print("---------------------------------------")

# Product Analysis
SumOfTotalPrice = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)
print(f"Sum Of TotalPrice by Product : \n{SumOfTotalPrice}")
print("---------------------------------------")
SumOfQuantity = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print(f"Sum Of Quantity by Product : \n{SumOfQuantity}")
print("---------------------------------------")

# Customer Analysis
SumOfTotalPriceByCustomer = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(5)
print(f"Top 5 Customers by Total Price : \n{SumOfTotalPriceByCustomer}")
print("---------------------------------------")

# Payment Method Analysis
# Payment methods generating the highest revenue
SumOfTotalPriceByPaymentMethod = df.groupby('PaymentMethod')['TotalPrice'].sum().sort_values(ascending=False)
print(f"Sum Of Total Price By Payment Method : \n{SumOfTotalPriceByPaymentMethod}")
print("---------------------------------------")
# Count of Payment Method
CountOfPaymentMethod = df['PaymentMethod'].value_counts()
print(f"Count Of Payment Method : \n{CountOfPaymentMethod}")
print("---------------------------------------")

# Coupon Analysis
df['UsedCoupon'] = df['CouponCode'].apply(lambda x:'Not Used' if x == 'No Coupon' else "Used Coupon")

SumOfTotalPriceByCoupon = df.groupby('UsedCoupon')['TotalPrice'].sum().sort_values(ascending=False)
print(f"Sum Of Total Price By Coupon : \n{SumOfTotalPriceByCoupon}")
print("---------------------------------------")
AvgOfTotalPriceByCoupon = df.groupby('UsedCoupon')['TotalPrice'].mean().sort_values(ascending=False)
print(f"Avg Of Total Price By Coupon : \n{AvgOfTotalPriceByCoupon}")
print("---------------------------------------")

# Order Status Analysis
CountOrderStatus = df['OrderStatus'].value_counts()
print(f"Count Of Orders Status : \n{CountOrderStatus}")
print("---------------------------------------")

# Day Analysis
CountDay = df['DayName'].value_counts()
print(f"Count Of Orders By Day : \n{CountDay}")
print("---------------------------------------")
SumOfTotalPriceByDay = df.groupby('DayName')['TotalPrice'].sum().sort_values(ascending=False)
print(f"Sum Of Total Price By Day : \n{SumOfTotalPriceByDay}")
print("---------------------------------------")

# Item Cart Analysis
ItemInCartByProducts = df.groupby('Product')['ItemsInCart'].sum().sort_values(ascending=False)
print(f"Sum Of Itmes In Cart By Product : \n{ItemInCartByProducts}")
print("---------------------------------------")

# Revenue Drivers
Revenue = df.groupby('Product')[['Quantity', 'UnitPrice', 'TotalPrice']].sum().sort_values(by='TotalPrice', ascending=False)
print(f"Revenue Analysis : \n{Revenue}")
print("---------------------------------------")

# Referral Source Analysis
referral_analysis = df.groupby('ReferralSource').agg({
    'OrderID': 'count',
    'TotalPrice': 'sum'
}).sort_values(by='TotalPrice', ascending=False)
print(f"Referral Source Performance: \n{referral_analysis}")
print("---------------------------------------")

# Average Order Value
aov = df['TotalPrice'].mean()
print(f"Average Order Value (AOV): {aov.round(2)}")
print("---------------------------------------")