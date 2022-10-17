# SQL Murder Mystery: Can you find out whodunnit?

This project will solve and document the responses to SQL Murder Mystery
Can you find out whodunnit?

To learn more about it check out [mystery.knightlab.com](https://mystery.knightlab.com/)

Wanna watch a video explaining it ? check out []()

# Steps taken

This command in this file is specific to SQLite. You can try it out on the IDE in this [website](https://mystery.knightlab.com/)

## what do we know? 

A crime has taken place and the detective needs your help. The detective gave you the crime scene report, but you somehow lost it. You vaguely remember that the crime was a ​murder​ that occurred sometime on ​Jan.15, 2018​ and that it took place in ​SQL City​.

## 1. Exploring the Database Structure

We would start by exploring the Run this query to find the names of the tables in this database.

```
SELECT name 
  FROM sqlite_master
 where type = 'table'
```

![fork repository](https://github.com/Bennykillua/sql-mysteries-SOLVED/blob/master/Solved%20solution/images/Table%20overview.png)

## 2. Exploring the `crime_scene_report` table
This will give us details about the police report to find out what other informations the police knows.

Run this query.

```
Select * from crime_scene_report
where date = 20180115
and type = "murder" and city = "SQL City"
```

### Clue: 

- Security footage shows that there were 2 witnesses. 
- The first witness lives at the last house on "Northwestern Dr".
- The second witness, named Annabel, lives somewhere on "Franklin Ave".

## 3. Exploring the `person` table

Run this query.
```
Select * from person
where address_street_name = "Northwestern Dr"
order by address_number desc
```

```
Select * from person
where address_street_name = "Franklin Ave"
and name like "Annabel%"
```

### Clue:

Witness one 
- Morty Schapiro whou has Id numner: 14887, license_id: 118009,	and stays at 4919	Northwestern Dr. ssn is 	111564949

Witness Two
- Annabel Miller with id number 16371 and license_id 490173 but stays at 103	Franklin Ave. ssn is	318771143

## 4. Exploring the `interview` table

Run this query.
```
Select * from interview
where person_id = 14887	or person_id = 16371
```

### clue:

![fork repository](https://github.com/Bennykillua/sql-mysteries-SOLVED/blob/master/Solved%20solution/images/2.png)

- Shooter is a man
- He had a "Get Fit Now Gym" bag. 
- The membership number on the bag started with "48Z". 
- Only gold members have those bags. 
- The man got into a car with a plate that included "H42W".
- I recognized the killer from my gym when I was working out last week on January the 9th.

## 5. Exploring the `get_fit_now_member` and `get_fit_now_check_in` table
Run this query.
```
Select * from get_fit_now_member
join get_fit_now_check_in
ON get_fit_now_member.id=get_fit_now_check_in.membership_id
where get_fit_now_member.id like "48Z%"
and get_fit_now_member.membership_status = "gold"
and get_fit_now_check_in.check_in_date = 20180109
```

### clue:

![fork repository](https://github.com/Bennykillua/sql-mysteries-SOLVED/blob/master/Solved%20solution/images/3.png)

- We have two suspect
- Joe Germuska who has Id number 48Z7A

OR 
- Jeremy Bowers who has Id number 48Z55	

Lastly clue we had was the car, our suspect got into a car with a plate that included "H42W".

Who has the car?

## 5. Exploring the `person` and `drivers_license` table

Run this query.
```
Select * from person
join drivers_license
on person.license_id = drivers_license.id
where drivers_license.plate_number like "%H42W%"
and person.id = 28819 or person.id = 67318
```

![fork repository](https://github.com/Bennykillua/sql-mysteries-SOLVED/blob/master/Solved%20solution/images/4.PNG)

Jeremy Bowers is the KILLER!

## Is Jeremy Bowers really the killer?
Run this query.
```
INSERT INTO solution VALUES (1, 'Jeremy Bowers');
        
        SELECT value FROM solution;
```     


## 6. Who hired him Jeremy Bowers?

Run this query.
```
SELECT * FROM person
JOIN drivers_license
ON person.license_id = drivers_license.id
WHERE drivers_license.car_make LIKE "Tesla%"
AND drivers_license.gender LIKE "female%"
AND drivers_license.hair_color LIKE "red%"
AND (drivers_license.height = 65 OR drivers_license.height = 67)
```

![fork repository](https://github.com/Bennykillua/sql-mysteries-SOLVED/blob/master/Solved%20solution/images/Capture.PNG)


Killer = Jeremy Bowers 

Hired by Red Korb

# Congratulation 🎉 

Wanna watch a video explaining it ? check out []()

### Wanna explore more SQL datasets?

To Explore more SQL datasets, check [observablehq.com](https://observablehq.com/@observablehq/curated-datasets)




