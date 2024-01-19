
## Modifying M-code in Power Query in Power Automate to send mail that only shows data from the weekday

This repo holds the dataset.

Below is the script you can use to create a table in SQL with similar data.


``` sql
CREATE TABLE SalesData (
    SalesDate date,
	Product	varchar(255),
	Qty int,
	Unit int,
	Amount int,
	Location varchar(255)
);
```
This INSERT statement will populate the table with the data

``` SQL
INSERT INTO SalesData 
( SalesDate, Product,	Qty, Unit, Amount,	Location)
VALUES
('12/20/2023',	'chocolate',	'9',	'870',	'7830',	'Ibadan'),
('	12/21/2023	',	'Instant noodles',	'9',	'250',	'2250',	'Lagos'),
('	12/22/2023	',	'coffee',	'13',	'200',	'2600',	'Lagos'),
('	12/23/2023	',	'Milk',	'5',	'1350',	'6750',	'Ibadan'),
('	12/24/2023	',	'chocolate',	'11',	'870',	'9570',	'Ibadan'),
('	12/25/2023	',	'chocolate',	'20',	'870',	'17400',	'Lagos'),
('	12/26/2023	',	'Milk',	'6',	'1350',	'8100',	'Ibadan'),
('	12/27/2023	',	'Instant noodles',	'6',	'250',	'1500',	'Lagos'),
('	12/28/2023	',	'coffee',	'19',	'200',	'3800',	'Lagos'),
('	12/29/2023	',	'coffee',	'6',	'200',	'1200',	'Lagos'),
('	12/30/2023	',	'Full Milk',	'15',	'800',	'12000',	'Lagos'),
('	12/31/2023	',	'Milk',	'16',	'1350',	'21600',	'Ibadan'),
('	1/1/2024	',	'coffee',	'19',	'200',	'3800',	'Ibadan'),
('	1/2/2024	',	'Instant noodles',	'8',	'250',	'2000',	'Ibadan'),
('	1/3/2024	',	'Full Milk',	'10',	'800',	'8000',	'Ibadan'),
('	1/4/2024	',	'Milk',	'20',	'1350',	'27000',	'Ibadan'),
('	1/5/2024	',	'chocolate',	'7',	'870',	'6090',	'Ibadan'),
('	1/6/2024	',	'Instant noodles',	'17',	'250',	'4250',	'Ibadan'),
('	1/7/2024	',	'Full Milk',	'6',	'800',	'4800',	'Ibadan'),
('	1/8/2024	',	'coffee',	'19',	'200',	'3800',	'Lagos'),
('	1/9/2024	',	'coffee',	'5',	'200',	'1000',	'Ibadan'),
('	1/10/2024	',	'coffee',	'15',	'200',	'3000',	'Ibadan'),
('	1/11/2024	',	'Instant noodles',	'19',	'250',	'4750',	'Ibadan'),
('	1/12/2024	',	'Instant noodles',	'14',	'250',	'3500',	'Ibadan'),
('	1/13/2024	',	'Full Milk',	'15',	'800',	'12000',	'Ibadan'),
('	1/14/2024	',	'Instant noodles',	'9',	'250',	'2250',	'Ibadan'),
('	1/15/2024	',	'Instant noodles',	'19',	'250',	'4750',	'Ibadan'),
('	1/16/2024	',	'Instant noodles',	'16',	'250',	'4000',	'Ibadan'),
('	1/17/2024	',	'chocolate',	'6',	'870',	'5220',	'Ibadan'),
('	12/20/2023	',	'Milk',	'7',	'1350',	'9450',	'Ibadan'),
('	12/21/2023	',	'chocolate',	'17',	'870',	'14790',	'Lagos'),
('	12/22/2023	',	'Instant noodles',	'8',	'250',	'2000',	'Ibadan'),
('	12/23/2023	',	'Full Milk',	'7',	'800',	'5600',	'Lagos'),
('	12/24/2023	',	'Instant noodles',	'11',	'250',	'2750',	'Ibadan'),
('	12/25/2023	',	'Instant noodles',	'9',	'250',	'2250',	'Ibadan'),
('	12/26/2023	',	'chocolate',	'11',	'870',	'9570',	'Lagos'),
('	12/27/2023	',	'coffee',	'13',	'200',	'2600',	'Lagos'),
('	12/28/2023	',	'Milk',	'5',	'1350',	'6750',	'Ibadan'),
('	12/29/2023	',	'coffee',	'14',	'200',	'2800',	'Ibadan'),
('	12/30/2023	',	'Instant noodles',	'7',	'250',	'1750',	'Lagos'),
('	12/31/2023	',	'chocolate',	'9',	'870',	'7830',	'Lagos'),
('	1/1/2024	',	'Instant noodles',	'14',	'250',	'3500',	'Ibadan'),
('	1/2/2024	',	'coffee',	'20',	'200',	'4000',	'Lagos'),
('	1/3/2024	',	'coffee',	'6',	'200',	'1200',	'Ibadan'),
('	1/4/2024	',	'Milk',	'7',	'1350',	'9450',	'Ibadan'),
('	1/5/2024	',	'coffee',	'12',	'200',	'2400',	'Lagos'),
('	1/6/2024	',	'chocolate',	'17',	'870',	'14790',	'Ibadan'),
('	1/7/2024	',	'Full Milk',	'10',	'800',	'8000',	'Ibadan'),
('	1/8/2024	',	'coffee',	'11',	'200',	'2200',	'Ibadan'),
('	1/9/2024	',	'Milk',	'19',	'1350',	'25650',	'Ibadan'),
('	1/10/2024	',	'coffee',	'10',	'200',	'2000',	'Ibadan'),
('	1/11/2024	',	'coffee',	'5',	'200',	'1000',	'Ibadan'),
('	1/12/2024	',	'Milk',	'17',	'1350',	'22950',	'Ibadan'),
('	1/13/2024	',	'Full Milk',	'6',	'800',	'4800',	'Lagos'),
('	1/14/2024	',	'Instant noodles',	'18',	'250',	'4500',	'Ibadan'),
('	1/15/2024	',	'Instant noodles',	'8',	'250',	'2000',	'Lagos'),
('	1/16/2024	',	'Full Milk',	'10',	'800',	'8000',	'Ibadan'),
('	1/17/2024	',	'chocolate',	'17',	'870',	'14790',	'Ibadan'),
('	1/18/2024	',	'coffee',	'10',	'200',	'2000',	'Ibadan'),
('	1/19/2024	',	'coffee',	'5',	'200',	'1000',	'Ibadan'),
('	1/20/2024	',	'Milk',	'17',	'1350',	'22950',	'Ibadan'),
('	1/21/2024	',	'Full Milk',	'6',	'800',	'4800',	'Lagos'),
('	1/22/2024	',	'Instant noodles',	'18',	'250',	'4500',	'Ibadan'),
('	1/23/2024	',	'Instant noodles',	'8',	'250',	'2000',	'Lagos'),
('	1/24/2024	',	'Full Milk',	'10',	'800',	'8000',	'Ibadan'),
('	1/25/2024	',	'chocolate',	'17',	'870',	'14790',	'Ibadan')

```
