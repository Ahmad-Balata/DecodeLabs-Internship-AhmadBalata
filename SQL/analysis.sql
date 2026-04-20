-- create database DecodeLaps_Intern
-- use DecodeLaps_Intern
-- go

-- * import dataset *


select top 10 * from sales

-- =====================================
-- Sum Of Total Price
select round(Sum(TotalPrice),2) as Sum_Of_Total_Price from sales
-- 1264761.96
-- =====================================

-- =====================================
-- Count Null Coupon
select count(*) as null_coupon from sales 
where CouponCode IS Null
-- 309 Null Coupon
-- =====================================

-- =====================================
-- Product Analysis
select Product, round(Sum(TotalPrice),2) as Sum_Of_Total_Price
from sales
group by Product
order by Sum_Of_Total_Price desc
-- high -> Chair = 195620.11 / low -> Phone = 151722.39
-- =====================================

-- =====================================
-- Customer Analysis
-- Top 5 Customer
select TOP 5 CustomerID, round(Sum(TotalPrice),2) as Total_Spending
from sales
group by CustomerID
order by Total_Spending desc
-- C38840    5723.23
-- C57276    3456.40
-- C67260    3390.80
-- C13877    3384.90
-- C18404    3370.20
-- =====================================

-- =====================================
-- Payment Method Analysis
select PaymentMethod, round(Sum(TotalPrice),2) as Sum_Of_Total_Price
from sales
group by PaymentMethod
order by Sum_Of_Total_Price desc
-- high -> Credit Card = 263847.63 / low -> Debit Card = 232361.18
-- =====================================
select PaymentMethod, Count(*) as Count_Payment_Method
from sales
group by PaymentMethod
-- high -> online = 258 / low -> Credit Card = 234
-- =====================================

-- =====================================
-- Orders by Status
select OrderStatus, Count(OrderID) as Count_Orders
from sales
group by OrderStatus
order by Count_Orders desc
-- high -> Cancelled = 250 / low Delivered = 231
-- =====================================

-- =====================================
-- CouponCode Analysis
select CouponCode, round(Avg(TotalPrice), 2) as Avg_Total_Price
from sales
group by CouponCode
order by Avg_Total_Price Desc
-- high -> FREESHIP = 1070.41 / low WINTER15 = 1035.9
-- =====================================
select count(OrderID) Count_Orders ,
	Case when CouponCode Is Null Then 'No Coupon'
	else CouponCode
	End As CouponCode
from sales
group by 
	CASE 
        WHEN CouponCode IS NULL THEN 'No Coupon'
        ELSE CouponCode
    END
order by Count_Orders desc
-- high -> FREESHIP = 313 / low SAVA10 = 286
-- =====================================

-- =====================================
-- Monthly Trend 
select Month(Date) as Month, round(Sum(TotalPrice),2) as Sum_Of_Total_Price
from sales
group by Month(Date) 
order by Month(Date)
-- high -> 6 = 170616.13 / low -> 9 = 69321.65
-- =====================================




