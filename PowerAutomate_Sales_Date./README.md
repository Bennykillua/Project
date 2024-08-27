
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




CREATE TABLE KaggleCustomerProductFeedbackDataset (
	ID int NOT NULL,
    Review_Title varchar(max),
	Customer_name varchar(255),
	Rating varchar(255),
	Date date,
	Category	varchar(255),
	Comments	varchar(max),
	Useful varchar(255)
);


INSERT INTO KaggleCustomerProductFeedbackDataset
( ID, Review_Title,	Customer_name,	Rating, [Date], Category,
	Comments, Useful)
VALUES

('1','Another Midrange killer Smartphone by Xiaomi','Rishikumar Thakur','4.0 out of 5 stars','7/1/2024','Display','Another Midrange killer Smartphone by Xiaomi

Major Highlights
• The Redmi 6 Pro sports a 584-inch full-HD+ display with a notch
• Powered by the Qualcomm Snapdragon 625 SoC
• The phone is priced at Rs 10999 for the 3GB RAM variant (Start Point)
• Battery of 4000 mAh and its Durability
• The Tripple Slots
• Dual AI Camera

Well in Redmi 6 Series you will get 3 Different Smartphones with different specsand from all of themRedmi 6 pro is most powerful and advanced (as said by Redmi India in their launch event)

Xiaomi Redmi 6 Pro design
Being the most premium phone of the new Redmi 6 familythe Redmi 6 Pro has been given somewhat better materialsin the form of a metal backplate Howeverthe overall design isnt too different from what weve already seen from Xiaomi at around this price point This is a fairly thick phoneand its a bit hefty toobut its manageable The buttons have good feedback without being noisyand on the left sideyou get a single tray which can hold two SIM cards and a separate microSD card Something worth noting is that the Redmi 6 Pro does not support dual 4G VoLTEwhich means that only one SIM can connect to a 4G network at a timeThe placement of ports is good The mono speaker is on the bottom rightso chances of blocking it when using the phone in landscape mode are slim The headphone socket is placed on the topand you also get an infrared (IR) emitter which can be used to control IR appliances through the Mi Remote app

Xiaomi Redmi 6 Pro specifications and software
The phone uses Qualcomms Snapdragon 625 SoCwhich is a couple of years old now but is still a capable chip for general tasks Gaming performance isnt greatas some popular games like PUBGand asphalt default to the lowest graphics settingsand even thengameplay isnt smooth Our unit was running on a pre-release version of its MIUI softwarewhich prevented us from running most benchmarks

Storage Options
Well I am impressed with the Xiaomi as they provided triple Slot in sim tray (2 for nano sim & one for SD card)

Heating Issues
WellI do not find any heating issues in this phone while playing games like PubG and Asphalt

Camera in Redmi 6 pro
The rear 12-megapixel camera has a f/22 aperture with PDAF Autofocus was decently quick in good light Theres auto-HDRwhich did a good job of balancing the exposure in our experience We observed good detail in landscape shots in daylightand colours were pleasing too The main sensor stumbled a bit with macrosas it simply wasnt able to resolve finer detail The white balance was a bit of a hit or a miss in close-upsand we often found ourselves having to tap-to-focus to get the white balance back on track Saving HDR images takes a good couple of seconds in daylight I would be very happy if they have provided the Flash in Portrait Modestillyou can Tap on Torch icon to switchon the torchyou will get the flash in Portrait Mode

Battery in Redmi 6 Pro
Battery life is one of the strong suits of the Redmi 6 Pro The 4000mAh battery easily lasted us a full day and a bit more on one charge Playing heavy games didnt drain the battery too much either In a single round of PUBG (around 30 minutes)in which we survived till the very endwe recorded a drop of around seven percentwhich is not bad In our internal video loop testwe got a runtime of 16 hours and 45 minuteswhich is very good The Redmi 6 Pro doesnt support fast chargingbut the bundled 10W adapter gave us roughly a 55 percent charge in an hourand it took us roughly 2 hours and 35 minutes to charge it completely from zero
Well before buying this phone I have heard many issues regarding inbuilt Advertisement in Xiaomi devicesand I checked that too in my previous Xiaomi phone which I am using since 2 Years And actuallyI found inbuilt ads in those phones You will see ads in inbuilt developers apps like MI AppsMi MusicMi VideosSecurityFile ManagerThemessometimes you will see full-screen ads which are really irritating for Mi Fansbut there is a cooler way to stop those ads those who wanted to know contact me

Final Verdict
Well for the people who want a notch DisplayBig Battery and Descent Camera you they can buy this phone blindly
Suggestion for Xiaomi India You should stop those inbuilt Ads present in your devices because we customers dont find those ads Valuable Because we are not Surfing any website where many ads are present So please stop it

Note Pics Included in this Review are captured by Redmi Note 3',' '),
('2','vry small size mobile','Raza ji','3.0 out of 5 stars','7/21/2024','Others','All ok but vry small size mobile','7 people found this helpful'),
('3','Full display not working in all application.','Vaibhav Patel','3.0 out of 5 stars','2/13/2024','Others','Quite good','7 people found this helpful'),
('4','Value for Money','Amazon Customer','5.0 out of 5 stars','5/27/2024','Display','Redmi has always have been the the king of budget segmentAnd yet another they gave us the Redmi 6 proIts a beautifully designedstrong and durableAnd the camera is awesome just like the Note 5 proDisplay is crisp and the notch is in good shapemeans it does take whole screenSound quality is clear and loudBut the headset experience is awesomeThe Battery is 4000mah which is crazily optimizedIn heavy useage it will give 2 day and a half in normal useage it give 3 daysAnd best thing is the inbuild Mi sercurity which loaded with featuresYou dont need third security appsAnd the phone do charge little faster on its stock adapterAtleast 2hrs 
and 45minsAs its a Qualcomm Chipset
Verdict The Base model is actually the Value for money deal 3/32 GB
I have been using the Redmi 6 pro for 3 weeks now This is totally tested','2 people found this helpful'),
('5','Not worth for the money','Sudhakaran Wadakkancheri','2.0 out of 5 stars','4/18/2024','Others','worst product from MI I am a hardcore fan of MI But this one really disappointing','6 people found this helpful'),
('6','Redmi 6 pro (3/32 GB) review after using for one week.','Arun Yajurvedi','3.0 out of 5 stars','1/19/2024','Display','Over prised by at least around Rs1000/- Low light photos are bad Only one SIM support VOLTE
Good things are best soundgood displaysmooth touchexcellent battery 
life managementcompactnice photos and videos under good light It never gets over heated while using or 
charging I dont play games I like MIUI I have already Redmi 4 A (Rs6000/-only) using for more than 14 months 
working superbly I have good opinion about Redmi mobiles','2 people found this helpful'),
('7','Fabulous!','Irukulla bharath','4.0 out of 5 stars','6/7/2024','Display','Pros
notch display
Dual camera
Face unlock
4000 mah battery
Cons
Some of the apps donot work in full screen mode
No Front flash

Great product to purchase finally and its value for moneyI got this phone for 10500 and thanks to Xiaomi','3 people found this helpful'),
('8','Fantastic','Amazon Customer','4.0 out of 5 stars','5/21/2024','Camera','Front camera is poor rest things are good','5 people found this helpful'),
('9','Good','Amazon Customer','5.0 out of 5 stars','4/29/2024','Others','Wooo','5 people found this helpful'),
('10','All youtubers are paid','Sharad','5.0 out of 5 stars','6/5/2024','Others','Realme is sub brand of oppo
He give money to all techi youtubers including big ones and tell him to promote more realme
But MI 6 Pro is much better than real me
Dont worry mi have given value for money as always','2 people found this helpful'),
('11','Another Midrange killer Smartphone by Xiaomi','Rishikumar Thakur','4.0 out of 5 stars','6/26/2024','Display','Another Midrange killer Smartphone by Xiaomi

Major Highlights
• The Redmi 6 Pro sports a 584-inch full-HD+ display with a notch
• Powered by the Qualcomm Snapdragon 625 SoC
• The phone is priced at Rs 10999 for the 3GB RAM variant (Start Point)
• Battery of 4000 mAh and its Durability
• The Tripple Slots
• Dual AI Camera

Well in Redmi 6 Series you will get 3 Different Smartphones with different specsand from all of themRedmi 6 pro is most powerful and advanced (as said by Redmi India in their launch event)

Xiaomi Redmi 6 Pro design
Being the most premium phone of the new Redmi 6 familythe Redmi 6 Pro has been given somewhat better materialsin the form of a metal backplate Howeverthe overall design isnt too different from what weve already seen from Xiaomi at around this price point This is a fairly thick phoneand its a bit hefty toobut its manageable The buttons have good feedback without being noisyand on the left sideyou get a single tray which can hold two SIM cards and a separate microSD card Something worth noting is that the Redmi 6 Pro does not support dual 4G VoLTEwhich means that only one SIM can connect to a 4G network at a timeThe placement of ports is good The mono speaker is on the bottom rightso chances of blocking it when using the phone in landscape mode are slim The headphone socket is placed on the topand you also get an infrared (IR) emitter which can be used to control IR appliances through the Mi Remote app

Xiaomi Redmi 6 Pro specifications and software
The phone uses Qualcomms Snapdragon 625 SoCwhich is a couple of years old now but is still a capable chip for general tasks Gaming performance isnt greatas some popular games like PUBGand asphalt default to the lowest graphics settingsand even thengameplay isnt smooth Our unit was running on a pre-release version of its MIUI softwarewhich prevented us from running most benchmarks

Storage Options
Well I am impressed with the Xiaomi as they provided triple Slot in sim tray (2 for nano sim & one for SD card)

Heating Issues
WellI do not find any heating issues in this phone while playing games like PubG and Asphalt

Camera in Redmi 6 pro
The rear 12-megapixel camera has a f/22 aperture with PDAF Autofocus was decently quick in good light Theres auto-HDRwhich did a good job of balancing the exposure in our experience We observed good detail in landscape shots in daylightand colours were pleasing too The main sensor stumbled a bit with macrosas it simply wasnt able to resolve finer detail The white balance was a bit of a hit or a miss in close-upsand we often found ourselves having to tap-to-focus to get the white balance back on track Saving HDR images takes a good couple of seconds in daylight I would be very happy if they have provided the Flash in Portrait Modestillyou can Tap on Torch icon to switchon the torchyou will get the flash in Portrait Mode

Battery in Redmi 6 Pro
Battery life is one of the strong suits of the Redmi 6 Pro The 4000mAh battery easily lasted us a full day and a bit more on one charge Playing heavy games didnt drain the battery too much either In a single round of PUBG (around 30 minutes)in which we survived till the very endwe recorded a drop of around seven percentwhich is not bad In our internal video loop testwe got a runtime of 16 hours and 45 minuteswhich is very good The Redmi 6 Pro doesnt support fast chargingbut the bundled 10W adapter gave us roughly a 55 percent charge in an hourand it took us roughly 2 hours and 35 minutes to charge it completely from zero
Well before buying this phone I have heard many issues regarding inbuilt Advertisement in Xiaomi devicesand I checked that too in my previous Xiaomi phone which I am using since 2 Years And actuallyI found inbuilt ads in those phones You will see ads in inbuilt developers apps like MI AppsMi MusicMi VideosSecurityFile ManagerThemessometimes you will see full-screen ads which are really irritating for Mi Fansbut there is a cooler way to stop those ads those who wanted to know contact me

Final Verdict
Well for the people who want a notch DisplayBig Battery and Descent Camera you they can buy this phone blindly
Suggestion for Xiaomi India You should stop those inbuilt Ads present in your devices because we customers dont find those ads Valuable Because we are not Surfing any website where many ads are present So please stop it

Note Pics Included in this Review are captured by Redmi Note 3',' '),
('12','vry small size mobile','Raza ji','3.0 out of 5 stars','3/18/2024','Others','All ok but vry small size mobile','7 people found this helpful'),
('13','Full display not working in all application.','Vaibhav Patel','3.0 out of 5 stars','2/6/2024','Others','Quite good','7 people found this helpful'),
('14','Value for Money','Amazon Customer','5.0 out of 5 stars','3/26/2024','Display','Redmi has always have been the the king of budget segmentAnd yet another they gave us the Redmi 6 proIts a beautifully designedstrong and durableAnd the camera is awesome just like the Note 5 proDisplay is crisp and the notch is in good shapemeans it does take whole screenSound quality is clear and loudBut the headset experience is awesomeThe Battery is 4000mah which is crazily optimizedIn heavy useage it will give 2 day and a half in normal useage it give 3 daysAnd best thing is the inbuild Mi sercurity which loaded with featuresYou dont need third security appsAnd the phone do charge little faster on its stock adapterAtleast 2hrs and 45minsAs its a Qualcomm Chipset

Verdict The Base model is actually the Value for money deal 3/32 GB
I have been using the Redmi 6 pro for 3 weeks now This is totally tested','2 people found this helpful'),
('15','Not worth for the money','Sudhakaran Wadakkancheri','2.0 out of 5 stars','3/13/2024','Others','worst product from MI I am a hardcore fan of MI But this one really disappointing','6 people found this helpful'),
('16','Redmi 6 pro (3/32 GB) review after using for one week.','Arun Yajurvedi','3.0 out of 5 stars','7/9/2024','Display','Over prised by at least around Rs1000/- Low light photos are bad Only one SIM support VOLTE
Good things are best soundgood displaysmooth touchexcellent battery life managementcompactnice photos and
videos under good light It never gets over heated while using or charging I dont play games I like MIUI I 
have already Redmi 4 A (Rs6000/-only) using for more than 14 months working superbly I have good opinion about 
Redmi mobiles','2 people found this helpful'),
('17','Fabulous!','Irukulla bharath','4.0 out of 5 stars','3/9/2024','Display','Pros
notch display
Dual camera
Face unlock
4000 mah battery
Cons
Some of the apps donot work in full screen mode
No Front flash
Great product to purchase finally and its value for moneyI got this phone for 10500 and thanks to Xiaomi','3 people found this helpful'),
('18','Fantastic','Amazon Customer','4.0 out of 5 stars','5/24/2024','Camera','Front camera is poor rest things are good','5 people found this helpful'),
('19','Good','Amazon Customer','5.0 out of 5 stars','5/2/2024','Others','Wooo','5 people found this helpful'),
('20','All youtubers are paid','Sharad','5.0 out of 5 stars','5/19/2024','Others','Realme is sub brand of oppo
He give money to all techi youtubers including big ones and tell him to promote more realme
But MI 6 Pro is much better than real me
Dont worry mi have given value for money as always','2 people found this helpful'),
('21','Awesome product','Debashis Das','5.0 out of 5 stars','4/2/2024','Others','awesome product at this range','4 people found this helpful'),
('22','45573','Braveheartboy_vinai','4.0 out of 5 stars','4/16/2024','Camera','Very nice looks smooth operation camera could have been better','3 people found this helpful'),
('23','Nice handy phone with good camera with notch','Abhishek Gupta','4.0 out of 5 stars','1/15/2024','Others','Like every things but fullscreen video playing option is not available in default player','3 people found this helpful'),
('24','dont buy these product. these copy of the product','KHAN SONU RAFI AHMED','1.0 out of 5 stars','5/29/2024','Others','Please dont buy these product I have 3-mobile of MI but i did not face these type of issue mobile data getting on and off automatically same things are happening with wifihot-spot and bluetooth The handset behaving like cheap quality i think its duplicate or copy of original handset','2 people found this helpful'),
('25','Thanks alot Amazon','sonu','5.0 out of 5 stars','3/15/2024','Battery','Thanks alot Amazonecom & sellerperfect product no compromise in qualitygood battery backupsmooth working no hanging problemno heating issueaccording to note 5 dual camera working properlyproduct packing is perfect again thanks alot Amazonsellerecom &&&&MI','One person found this helpful'),
('26','Pros and cons','Amazon Customer','5.0 out of 5 stars','6/11/2024','Display','No company can provide u these features
Pros
AWESOME display
Great video stablisation
Great battery
Great performance
Looks beatifull

Cons
Okk front camera( not very bad considering price)','2 people found this helpful'),
('27','Design can be better','Rahul Mhatre','3.0 out of 5 stars','6/19/2024','Others','The product is great with quite good features I am great fan of xiaomi and I have been always using Xiaomi phones But I am disappointed with mobile designing of Xiaomi as most of all the lower range and mid range phones have same design Xiaomi always being giving with so many features but being realme entering in market Xiaomi has to be more creative to attract more indian customers','One person found this helpful'),
('28','Mi 6pro review','darpan n parekh','3.0 out of 5 stars','4/9/2024','Camera','Camera clarity is not good and average mobile I purchased first time mi mobile but not good compare to expect','3 people found this helpful'),
('29','Best phone u can get in this and within 20k budget','Amazon Customer','5.0 out of 5 stars','2/12/2024','Display','Superb job by Xiaomi
Handy phone Not huge size not slippery
Better battery display processing speed Overall its the best phone','2 people found this helpful'),
('30','Superb Phone. Good for Performance.','Tharun','5.0 out of 5 stars','6/23/2024','Display','Good phone at such a valuable price Notch display
Value for money','2 people found this helpful'),
('31','Nice','Rohit Mengal','5.0 out of 5 stars','5/5/2024','Others','Good phone','One person found this helpful'),
('32','Fantastic','RAHEEL','5.0 out of 5 stars','5/9/2024','Others','Great productfully met my expectations','One person found this helpful'),
('33','Good','rajkumar kumawat','4.0 out of 5 stars','5/13/2024','Others','Good','One person found this helpful'),
('34','Not good as expected','Bidyut Majumder','1.0 out of 5 stars','6/27/2024','Others','Do not buy','One person found this helpful'),
('35','High thinker','Joshi Dharmesh kumar','2.0 out of 5 stars','5/19/2024','Others','No dual 4g if you think new mobile you buy realme 1','2 people found this helpful'),
('36','good phone','ANUPOM BHUNIYA','5.0 out of 5 stars','2/13/2024','Others','very good phone of this budgetred colour very beautiful','2 people found this helpful'),
('37','Good service','Manowar','4.0 out of 5 stars','4/2/2024','Delivery','Nice product Delivery guy also','2 people found this helpful'),
('38','Bad camera','JAWED HUSSAIN','2.0 out of 5 stars','5/18/2024','Camera','Bad camera quality and heating problem','2 people found this helpful'),
('39','Good phone in budget','Amazon Customer','4.0 out of 5 stars','5/7/2024','Battery','Good phone in budget Good camerabattery and performance for normal use Call sound is very good',' '),
('40','Redmi Pro 6','Amazon Customer','3.0 out of 5 stars','3/27/2024','Battery','Awesome sound quality battery life is good gaming is good no lags there Very poor camera if you r buying for a camera phone the m this is not the one Moto 5 MP camera works better than this','One person found this helpful'),
('41','Nice','Rohit Mengal','5.0 out of 5 stars','1/2/2024','Others','Good phone','One person found this helpful'),
('42','Fantastic','RAHEEL','5.0 out of 5 stars','3/8/2024','Others','Great productfully met my expectations','One person found this helpful'),
('43','Good','rajkumar kumawat','4.0 out of 5 stars','2/4/2024','Others','Good','One person found this helpful'),
('44','Not good as expected','Bidyut Majumder','1.0 out of 5 stars','7/13/2024','Others','Do not buy','One person found this helpful'),
('45','High thinker','Joshi Dharmesh kumar','2.0 out of 5 stars','3/15/2024','Others','No dual 4g if you think new mobile you buy realme 1','2 people found this helpful'),
('46','good phone','ANUPOM BHUNIYA','5.0 out of 5 stars','4/20/2024','Others','very good phone of this budgetred colour very beautiful','2 people found this helpful'),
('47','Good service','Manowar','4.0 out of 5 stars','6/1/2024','Delivery','Nice product Delivery guy also','2 people found this helpful'),
('48','Bad camera','JAWED HUSSAIN','2.0 out of 5 stars','6/9/2024','Camera','Bad camera quality and heating problem','2 people found this helpful'),
('49','Good phone in budget','Amazon Customer','4.0 out of 5 stars','5/3/2024','Battery','Good phone in budget Good camerabattery and performance for normal use Call sound is very good',' '),
('50','Redmi Pro 6','Amazon Customer','3.0 out of 5 stars','5/10/2024','Battery','Awesome sound quality battery life is good gaming is good no lags there Very poor camera if you r buying for a camera phone the m this is not the one Moto 5 MP camera works better than this','One person found this helpful'),
('51','Best Mobile in this price category.','Rahul.K.R','4.0 out of 5 stars','6/25/2024','Battery','Nice mobilebattery backup is goodcamera gudone limitation is front camera- 5 noslim & light weight mobile','One person found this helpful'),
('52','THIK THAK.','Sudipto Ghosh','4.0 out of 5 stars','6/23/2024','Display','Like everything besides display','One person found this helpful'),
('53','Upto You','CHANDRESH KHUNTIA','3.0 out of 5 stars','1/22/2024','Others','A Bit Pricey compared to the competitors
Nice and Sleek body feels Good on Hand
Overall Performance Is good Enough less heat compered to mi redmi devices','One person found this helpful'),
('54','Batytery is not good mentioned 4000mah but not good','Amazon Customer','1.0 out of 5 stars','6/11/2024','Battery','Please dontt bye camera is good but battery back up not good','2 people found this helpful'),
('55','Best phone with notch in this price','Amazon Customer','4.0 out of 5 stars','6/24/2024','Camera','Worth 
the priceno hybrid slim slot very good pointfront camera is poor only 5mp and the handset is too heavy in 
weight Handy phone small size full screen','One person found this helpful'),
('56','Quality is not good','Vamshi Vadikari','1.0 out of 5 stars','3/2/2024','Others','Worst phone from MI and Amazon
Touch was not good and didnot working as expected
Without touching the screen click is happening and unnecessary apps are opening','One person found this helpful'),
('57','Weste of money','......','1.0 out of 5 stars','1/25/2024','Camera','Both Camera quality is bedits price is too high and quality are lowest','2 people found this helpful'),
('58','Dual 4G support','Manoj Kumar','1.0 out of 5 stars','5/6/2024','Others','I have purchsed this item and two jio sim are not working togeher But in specification it is given that it supports dual 4g sim What is this? Please dove my problem','One person found this helpful'),
('59','Trust or not trust as your wish','Mayur shingne','5.0 out of 5 stars','6/14/2024','Display','This product is very nice and battery life and notch display is very awesome','2 people found this helpful'),
('60','Awesome fantastic jhakass. lajawaab.','Tarikul Islam','5.0 out of 5 stars','4/17/2024','Battery','Its very fantastic awesome mobile and nice sound quality Awesome camera Nice battery life Awesome look but I think its small size','One person found this helpful'),
('61','Redmi 6 pro is best in the same money range','Gautam Roy ','5.0 out of 5 stars','4/14/2024','Display','Battery life is awesome including display is too goodfast charging makes it extremely well Good value for money',' '),
('62','Not value for money','Amazon Customer','3.0 out of 5 stars','3/1/2024','Others','Good phone but not value for moneyPrefer Redmi note 5 over this but was not in stock since last 2 months',' '),
('63','Good budget phone','Vinamra','4.0 out of 5 stars','5/11/2024','Battery','Works pretty good for a budget phone Battery life is amazing but camera is a let down Finger print is very fast',' '),
('64','Charger not received in the box','Avinash ','5.0 out of 5 stars','1/17/2024','Delivery','Charger not received in the box','One person found this helpful'),
('65','Good phone','sudevan','5.0 out of 5 stars','6/27/2024','Others','Width is little less Still good phone Face unlock and finger print unlocks are awasome',' '),
('66','Nice product','Vaibhav','5.0 out of 5 stars','4/23/2024','Others','Nice',' '),
('67','Nice performance','Amazon Customer','5.0 out of 5 stars','6/4/2024','Others','Redmi is always good for me and Redmi 6 pro performance is very good and good Bettry backup',' '),
('68','and brand like MI.','Abinash Dash','5.0 out of 5 stars','6/12/2024','Others','Midrange phone with a notchand brand like MI
Aur kya chahiye',' '),
('69','Missing part','Santosh','1.0 out of 5 stars','4/5/2024','Others','disapointing','One person found this helpful'),
('70','Not value for msny','Amazon Customer','1.0 out of 5 stars','4/21/2024','Others','Worst phone','One person found this helpful'),
('71','Powerful device','Anand bharti','5.0 out of 5 stars','2/24/2024','Delivery','Powerful device I love mi thnax Amazon for quick delivery',' '),
('72','Ok','Prashanta KN','1.0 out of 5 stars','1/26/2024','Others','Ok','One person found this helpful'),
('73','Awesome device','RamanJakhar','5.0 out of 5 stars','6/3/2024','Others','Top class device No words!!!',' '),
('74','Quality.','Pankaj kumar','4.0 out of 5 stars','7/23/2024','Others','Mobile is good also service of Amazon is better than other like paytm',' '),
('75','Aswasom','Aniket ','5.0 out of 5 stars','7/3/2024','Camera','I love amezon
Good packing
Good product
Camera battry good',' '),
('76','Awesome','Parmar kailash','5.0 out of 5 stars','1/15/2024','Others','Sup up model in MI thank u  low price best features available',' '),
('77','Fully satisfied','Mishra Food N Agro','5.0 out of 5 stars','2/16/2024','Others','One of the best In the price range',' '),
('78','Awesome phone','Amazon Customer','5.0 out of 5 stars','5/24/2024','Display','Phone is good Quality Dual Camera is Very Best
Full display show good dimensions',' '),
('79','Desh ka smartphone','Alok','5.0 out of 5 stars','6/1/2024','Others','One of the best of my purchases',' '),
('80','Nice look','Amazon Customer','4.0 out of 5 stars','2/15/2024','Display','Nice look with notch displaybut sound is little bit low',' '),
('81','Nice','Pintu rai','4.0 out of 5 stars','5/25/2024','Others','Good phone','NULL'),
('82','Overall a nice phone','anant vasantrao bhamare','3.0 out of 5 stars','1/16/2024','Others','Sound quality is not so good
Either way the mobile best in its segment','NULL'),
('83','Smart brand.','Amazon Customer','5.0 out of 5 stars','3/28/2024','Display','Display is best','NULL'),
('84','Waste of money compare another phone','Praveen gurjar','1.0 out of 5 stars','1/14/2024','Battery','Sometimes automatically speaker on and little hanging problem camera battery good','NULL'),
('85','Great looking','Tuhin Kundu','5.0 out of 5 stars','7/25/2024','Battery','Picture perfect camera
Great sound
Good battery life
Value for money','NULL'),
('86','Redmi 6 Pro','GKM','5.0 out of 5 stars','5/1/2024','Display','Best phone with notch Display Battery BackupQuality Rear CameraValue for Money','NULL'),
('87','Nice one again from xiomi...','Amazon Customer','5.0 out of 5 stars','6/14/2024','Others','Fabulous products by fabulous xiomi','NULL'),
('88','Redmi 6 pro excellent Product','Amazon Customer','5.0 out of 5 stars','4/4/2024','Battery','this mobile awesome i loved it best battery life and performance','NULL'),
('89','Awesome','Deepan','5.0 out of 5 stars','5/4/2024','Others','Best to buyi love it??','NULL'),
('90','5/4.5','manoranjan kumat','5.0 out of 5 stars','5/13/2024','Battery','Battery is good
Phone is good
Camera is good
Praformens is good','NULL'),
('91','Great product','Sonu Bhasker','5.0 out of 5 stars','1/4/2024','Delivery','Very happy with this mobile
Fast delivery got my parcel in just 22 hours','NULL'),
('92','Look like I phn x. ????????????????????','Parvinder singh','5.0 out of 5 stars','2/19/2024','Camera','No change in camera quality Other functions super se v uper ????????????','NULL'),
('93','Wow phone','Ramiz Sayyed','5.0 out of 5 stars','2/10/2024','Others','Awesome phoneall features availablem super happy with phone','NULL'),
('94','Good','Amazon Customer','5.0 out of 5 stars','6/29/2024','Battery','Sound and battery life good','NULL'),
('95','Thanks to Amazon','Salman','5.0 out of 5 stars','2/25/2024','Others','Very very nice and budget smartphone good xiaomi

Thanks Amazon','NULL'),
('96','Awesome phone','GOURAB ROY','5.0 out of 5 stars','5/25/2024','Battery','Good mobile battery backup good','NULL'),
('97','Very good desain','MAHAVIRSINH R JADEJA','3.0 out of 5 stars','7/21/2024','Others','Sound qulity not dolby and processor performance not ok','NULL'),
('98','Not A camera fone','Amazon Customer','4.0 out of 5 stars','3/24/2024','Camera','Looking wise sexy but camera quality is not worth over all good','NULL'),
('99','Super phone','mahi kumar','5.0 out of 5 stars','1/9/2024','Others','This is the best phone mi phone','NULL'),
('100','Ek jakas cellphone','Amazon Customer','5.0 out of 5 stars','5/29/2024','Others','This cellphone is good & economical more features available','NULL'),
('101','Ek jakas cellphone','Amazon Customer','5.0 out of 5 stars','3/17/2024','Others','This cellphone is good & economical more features available','NULL'),
('102','Awesome','Amazon Customer','5.0 out of 5 stars','6/28/2024','Others','One of best mobile compare to nokia 6 1 plus','NULL'),
('103','Redmi 6 pro reviee','Amazon Customer','5.0 out of 5 stars','7/29/2024','Display','Display Quality and battery backup is good','NULL'),
('104','No dual volte','Sunil kumar kulhari','1.0 out of 5 stars','1/16/2024','Others','Im fan MI but No dual volte waste of money','NULL'),
('105','Product is good','Suman Bag','5.0 out of 5 stars','5/7/2024','Battery','This product is very goodbattery backup is very good','NULL'),
('106','nice phone','Abhinav more','5.0 out of 5 stars','7/18/2024','Others','In this budget phone is good and Sound quality is also awesome','NULL'),
('107','Best smartphone','Pradeep kumar','5.0 out of 5 stars','7/22/2024','Others','I use this phone and I like all quality','NULL'),
('108','Best quality phone','Rehan shaikh ','5.0 out of 5 stars','5/7/2024','Others','Best notch light weight phon','NULL'),
('109','Looking osm','Amazon Customer','4.0 out of 5 stars','2/9/2024','Camera','Nice product and durability also good
Best for cameras','NULL'),
('110','Battery','Bilal Ahmed','5.0 out of 5 stars','1/12/2024','Others','The Product is Bulky would have bring the weight down','NULL'),
('111','Good','P.T.Hanuman','4.0 out of 5 stars','7/7/2024','Camera','Camera is good','NULL'),
('112','Good','sameer','4.0 out of 5 stars','6/12/2024','Others','Good mm??????','NULL'),
('113','Good','RAM','4.0 out of 5 stars','5/17/2024','Others','I didnt get 500/- discount  Buy through HDFC bank','NULL'),
('114','Gud Phone','Al Mustaq','5.0 out of 5 stars','5/18/2024','Others','Better phone','NULL'),
('115','Good','Amazon Customer','5.0 out of 5 stars','5/3/2024','Others','Good','NULL'),
('116','Nyc','gaurav kumar','5.0 out of 5 stars','2/28/2024','Others','Good','NULL'),
('117','Good','Darshan V','5.0 out of 5 stars','6/9/2024','Others','Good','NULL'),
('118','Np','Y2 user','5.0 out of 5 stars','2/8/2024','Others','Good phone','NULL'),
('119','Sound v acha nhi hai','Md shahab','4.0 out of 5 stars','2/7/2024','Camera','Front camera low hai cost jyada hair 9999 take think tha','NULL'),
('120','A good product from MI at an affordable price tag.','Amazon Customer','4.0 out of 5 stars','2/15/2024','Others','Overall the product build and handling quality is good','NULL'),
('121','Love this product','Deepak kumar','5.0 out of 5 stars','7/21/2024','Others','Wonderful phone','NULL'),
('122','Good','Jay','3.0 out of 5 stars','5/7/2024','Others','Low pictures clarity','NULL'),
('123','Good','Uttam singh','5.0 out of 5 stars','1/19/2024','Others','Hello','NULL'),
('124','Very good','Jalindar dhondabare','5.0 out of 5 stars','5/6/2024','Others','Good quality','NULL'),
('125','Awesome','Upender','5.0 out of 5 stars','1/3/2024','Delivery','Fast delivery great','NULL'),
('126','Best budget phone','Akash Sharma','5.0 out of 5 stars','6/6/2024','Others','This phone is simply awesome in this price range??','NULL'),
('127','Superb','Rishad','5.0 out of 5 stars','5/22/2024','Others','Good','NULL'),
('128','Good job Amazon','Shashikumar','5.0 out of 5 stars','2/29/2024','Others','One of the best phone under 12k','NULL'),
('129','Value for money','THAMIZH ARASU','4.0 out of 5 stars','2/23/2024','Others','Nice mobile in this price range','NULL'),
('130','Good product','Aakash','5.0 out of 5 stars','1/20/2024','Others','Awesome product','NULL'),
('131','Average','pradeep k','3.0 out of 5 stars','5/14/2024','Others','Average','NULL'),
('132','Excellent.','Mohd Nazeer','5.0 out of 5 stars','6/4/2024','Display','Excellent mobile good display quality','NULL'),
('133','Sound speaker is not working','Janardhan','1.0 out of 5 stars','5/1/2024','Others','Out of 2 only 1 speaker is working from day 1','NULL'),
('134','Amazing','Emad choudhury','5.0 out of 5 stars','5/26/2024','Delivery','Value for money
Dislike late delivery','NULL'),
('135','Bad service for return','GAURANG T.Nakarani','1.0 out of 5 stars','5/8/2024','Others','Bad facility for replacement','NULL'),
('136','Ive fallen in love!','Aahil Asad Ahmad ','5.0 out of 5 stars','1/23/2024','Others','Ive fallen in love!','NULL'),
('137','Poor','Rishab tripathi','3.0 out of 5 stars','7/26/2024','Others','Poor','NULL'),
('138','Good','Suraj','5.0 out of 5 stars','6/10/2024','Others','Good','NULL'),
('139','Not value of money.','Jaydeep Parikh ','1.0 out of 5 stars','2/6/2024','Others','worst product ever dont buy it','NULL'),
('140','Excellent','Mahesha','5.0 out of 5 stars','6/19/2024','Others','Awesome mobilevalue of money','NULL'),
('141','Gud','Imtiyaz','5.0 out of 5 stars','6/26/2024','Others','Nice phn','NULL'),
('142','battery life good','Hardeep singh','4.0 out of 5 stars','3/26/2024','Display','notch display better','NULL'),
('143','Better bakup osm','Amazon Customer','5.0 out of 5 stars','1/12/2024','Others','Nice products ??   ','NULL'),
('144','waste of money','Rameez Rashid Parray','1.0 out of 5 stars','3/21/2024','Others','waste of money','NULL'),
('145','Amazing','Ritesh verma','5.0 out of 5 stars','6/23/2024','Others','Nice and super mobile','NULL'),
('146','best phone in budget','mohammed imroz','5.0 out of 5 stars','4/28/2024','Others','awosome phone','NULL'),
('147','Battery life','Aman Rana','4.0 out of 5 stars','5/29/2024','Others','Phone system is nice','NULL'),
('148','Very nice','Shiva','4.0 out of 5 stars','2/14/2024','Others','Mobile is very nice','NULL'),
('149','Good','yahoo','5.0 out of 5 stars','6/28/2024','Others','Good Product','NULL'),
('150','Must buy','Amazon Customer','5.0 out of 5 stars','3/1/2024','Others','Great phone@','NULL'),
('151','Super farfamens','SambasivaraoAmazon Customer','3.0 out of 5 stars','4/16/2024','Others','Nice mobaile','NULL'),
('152','Amazing','Himanshu','5.0 out of 5 stars','2/18/2024','Others','Mind blowing','NULL'),
('153','Camera','Friends ','5.0 out of 5 stars','5/12/2024','Others','Nice product','NULL'),
('154','Nice','Arpan patel','5.0 out of 5 stars','3/21/2024','Others','Like','NULL'),
('155','.','PRINCE KUMAR GUPTA','4.0 out of 5 stars','6/7/2024','Others','Nice','NULL'),
('156','Good, very good','Bivash das','5.0 out of 5 stars','6/21/2024','Others','Good product Amazon','NULL'),
('157','Marvellous','Rakesh','5.0 out of 5 stars','5/10/2024','Others','Its awesome phone','NULL'),
('158','Nice product in cheap price',' NANDKISHOR WANARE','5.0 out of 5 stars','3/2/2024','Others','I have fall in love','NULL'),
('159','Great phone','Buyer','4.0 out of 5 stars','3/11/2024','Display','I loved the display','NULL'),
('160','Munish gupta','Munish ','3.0 out of 5 stars','5/2/2024','Others','All is well','NULL'),
('161','Good work.','Korjani Yogesh','5.0 out of 5 stars','1/21/2024','Others','Nice phone','NULL'),
('162','Value for money','Gajanana Malji','5.0 out of 5 stars','7/14/2024','Others','Superb????????????','NULL'),
('163','Bad video quality','bikash maji','3.0 out of 5 stars','1/13/2024','Others','Video screen short','NULL'),
('164','??','sagar kute','4.0 out of 5 stars','2/10/2024','Others','??','NULL'),
('165','Value for money very good','MOHD AARISH','5.0 out of 5 stars','3/28/2024','Others','Very good product','NULL'),
('166','Mi is best','tarun','5.0 out of 5 stars','1/4/2024','Others','Simply Mi ia best','NULL'),
('167','Very good','Raju Dudhawade','5.0 out of 5 stars','4/29/2024','Others','Very nice','NULL'),
('168','Excellent','????? ?????','5.0 out of 5 stars','6/17/2024','Others','Excellent','NULL'),
('169','No thanks','KAILAS Ramchandra Throat','5.0 out of 5 stars','4/24/2024','Others','No thanks','NULL'),
('170','Good phone','Danish','5.0 out of 5 stars','4/15/2024','Battery','Battery and camera','NULL'),
('171','Gud product','Jyoti thakur','5.0 out of 5 stars','6/26/2024','Others','Value for money','NULL'),
('172','battery','Yaden Wap','5.0 out of 5 stars','5/15/2024','Others','daaaaaaaam good','NULL'),
('173','Super','Josyula','5.0 out of 5 stars','1/9/2024','Others','Value for money','NULL'),
('174','Coustly','Nasreen','1.0 out of 5 stars','7/26/2024','Others','Selfi flesh not','NULL'),
('175','Value for money, must buy','Amazon Customer','5.0 out of 5 stars','2/3/2024','Others','Perfect','NULL'),
('176','Value of money','Ahir Dipak Ram','4.0 out of 5 stars','3/7/2024','Others','Superb product','NULL'),
('177','Best','Vinayak shinde','5.0 out of 5 stars','5/22/2024','Others','Best for price','NULL'),
('178','Very good product','vikram sharma ','5.0 out of 5 stars','7/9/2024','Others','Really like it','NULL'),
('179','Not ok','RAKESH kumar mandal','5.0 out of 5 stars','3/15/2024','Others','Not ok','NULL'),
('180','Good','Manju','5.0 out of 5 stars','5/7/2024','Others','User friendly','NULL'),
('181','Handy','Nitish','5.0 out of 5 stars','1/1/2024','Battery','Slow charging','NULL'),
('182','Good service','Shaikh shahrukh.','5.0 out of 5 stars','3/15/2024','Others','Good product','NULL'),
('183','Good rear camera','Amazon Customer','3.0 out of 5 stars','7/25/2024','Others','Overall good','NULL'),
('184','Looking smart','SUJEET KUMAR','4.0 out of 5 stars','6/13/2024','Others','Good','NULL'),
('185','Nice','Kamlesh purohit','5.0 out of 5 stars','3/28/2024','Others','Nice','NULL'),
('186','Good','Amazon Customer','4.0 out of 5 stars','3/18/2024','Others','Good','NULL'),
('187','Awesome','Vimalnathan.s','5.0 out of 5 stars','5/19/2024','Others','Good','NULL'),
('188','Best Phone from Redmi Series','Mohammad Ayyub','5.0 out of 5 stars','7/25/2024','Others','Best','NULL'),
('189','super','Kiran ','5.0 out of 5 stars','2/5/2024','Others','super','NULL'),
('190','nice for value','AMIT KUMAR','5.0 out of 5 stars','7/26/2024','Others','all is fine','NULL'),
('191','Mi','Mohammed altaf','4.0 out of 5 stars','3/27/2024','Others','Nice mobile','NULL'),
('192','Camera','Arjun ','5.0 out of 5 stars','1/26/2024','Others','Nice mobile','NULL'),
('193','Very good','Mansukh','5.0 out of 5 stars','2/21/2024','Others','Yes','NULL'),
('194','Great','SUNIL YADAV','4.0 out of 5 stars','1/16/2024','Others','Best phone','NULL'),
('195','Best mobile','Rakesh Baraiya','5.0 out of 5 stars','6/15/2024','Others','Too good','NULL'),
('196','Worthy','Sourav Maparu','4.0 out of 5 stars','4/6/2024','Others','Good one','NULL'),
('197','Case back no ritan','Pappu Kumar varma','5.0 out of 5 stars','5/9/2024','Others','Case back','NULL'),
('198','Best Phone','Rishikesh metkar','5.0 out of 5 stars','7/25/2024','Others','Mi Best','NULL'),
('199','Battery','jagbir singh saini','5.0 out of 5 stars','4/3/2024','Others','Its osm','NULL'),
('200','Fantastic','Amazon Customer','3.0 out of 5 stars','2/17/2024','Others','Super','NULL'),
('201','Excellent','Hosain sekh','5.0 out of 5 stars','7/11/2024','Others','Good','NULL'),
('202','Good','Najim ','5.0 out of 5 stars','3/25/2024','Others','Good','NULL'),
('203','Nice','Amazon Customer','4.0 out of 5 stars','1/2/2024','Others','Nice','NULL'),
('204','Awesome','Shubham','5.0 out of 5 stars','4/26/2024','Others','Good','NULL'),
('205','Nice','Saif','5.0 out of 5 stars','5/10/2024','Others','Nice','NULL'),
('206','good','sohan lal','5.0 out of 5 stars','5/22/2024','Others','good','NULL'),
('207','Good','Raj kumar','5.0 out of 5 stars','1/12/2024','Others','Good','NULL'),
('208','Midil','Deva bhoi','5.0 out of 5 stars','7/17/2024','Others','Nice','NULL'),
('209','Gty','Shakeel ahamad','5.0 out of 5 stars','7/19/2024','Others','Jiiy','NULL'),
('210','Good','ayush','5.0 out of 5 stars','1/29/2024','Others','Good','NULL'),
('211','Superb','Harsha','5.0 out of 5 stars','4/24/2024','Others','Good','NULL'),
('212','Joordaar maja aaa gya','Joginder Singh ahuja','5.0 out of 5 stars','4/19/2024','Others','Nice','NULL'),
('213','res for custmer','Sachin Wadhawan','5.0 out of 5 stars','7/24/2024','Others','like','NULL'),
('214','Best display and advance features','Girish Basone','5.0 out of 5 stars','3/12/2024','Others','Nice','NULL'),
('215','Nice phone','Ok','5.0 out of 5 stars','1/14/2024','Others','Ok','NULL'),
('216','Ni','Amazon Customer','1.0 out of 5 stars','3/27/2024','Others','No','NULL'),
('217','Launch display','pintu sahoo','5.0 out of 5 stars','6/4/2024','Others','Ok','NULL'),
('218','Super','Jawed Ansari','5.0 out of 5 stars','2/22/2024','Others','Good','NULL'),
('219','Worst front camera on a Mi device till date.','Ram Rajkishore','1.0 out of 5 stars','6/11/2024','Camera','It has a worst front camera I have ever seen on a Mi deviceIts just disgusting to see such a poor front camera on a Rs11000 deviceVery much disappointed','NULL'),
('220','Look some other options guys.... Its just a crap.','Shubham jaishwal','1.0 out of 5 stars','6/17/2024','Display','Guysjust dont 
buy Redmi 6 pro for now atleast Got it delivered yesterdayI have both Gold and Black Variant Black looks nice But waitIts 
just an unpolished product The Pinch to fill the video doesnt work in Mi Video app The left edge remains like this and right 
even this happens in Youtube Both apps leave way too much on both sides if I let it to original 
Making it a 5 inch screen display There is No Indian City name in Time Zoneits shown as GMT+530 It 
automatically detects the time zone as China Why?? Has to change timemanually!!!! ThenHow the heck they say 
that this is Made in India While setting up the phonethe Limitless theme has Icons written in chinese 
The camera app is inconsistent The so called AI doesnt seem to be going well with SD625 My friend has RN5 pro 
I think they both have same app But his camera shows icon within screen top as if its going to shoot it with Flash or HDR 
Butno this is just a crap Soa 584 screen display is just a waste if I cannt watch video to its limit Whats the
purpose served by notch then and what am I supposed to do with that 584 inch screen???? 
No more notification icons in the notification barNo more connection speed and battery 
percentage toountil you drop that notification panel Stupid MI !!!!','NULL'),
('221','#Horrible experience of Redmi 6pro - Readon to know more##','Bhaskar Shanmugam','1.0 out of 5 stars','1/19/2024','Camera','Please dont buy!!
Horrible phone from Xiaomi!!

The phone is just for people who like showing off the new iPhone notch design The phone uses an outdated processor and lags terrible in term of performance When we use more than 4apps at a timethe phone will get hanged and you will be forced to restart the phone Watching videos for more than 20mins the phone gets extrmely heated and you will have to put it to stanby fir a while before resarting the use of the phone Very bad multi-tasking The build quality is okaybut not as good as other budget phone A flat drop on the front screen side if hit hardly will crack the screen The front camera is extremely poor and has been downgraded and doesnt produce even a decent quality picture Selfie loversplease dont even buy this phone you will get a heart ache after looking at your pix The rear camera picture quality is average and is very unlike of xiaomi

On the other sidethe basic things like the output from the speaker phone and and the earphone are extremely poor and distorted

The only con is a decent screenhowever that is contributed by low quality video while played in amazon or netflix

Had complained to Amazon on the above low quality issuesunfortunately Amazon is not willing to listenthey are saying technically the phone is working and hence it cant taken back Unfortunatelyin this case Amazon has put its sellers over it buyers who are their bread and butter Hope Amazon listens 
to my complaint here and takes measures to improve their service Just to put things
into perspectivean average 6-7k phone is sold at an extremely abnoxiously at a high price of 11k 
You can find many better phone at this high price Please stop buying this phone Thanks for reading 
Extremely sadened on buying this phone','10 people found this helpful'),
('222','Got a defective one and requested for a replacement','Anoopcbose','1.0 out of 5 stars','2/25/2024','Display',
'Phone is really nice and good looking
I think I got a defective one Because there is a blue colour appears on the side of the screen You can 
see it on the image shown below I dont know Im the one who facing this or is it a common problem Plz let me 
know if youre facing the same Also there is some touch issues when we using keyboard for typing 
The typing is not smooth and it lag a lot But the problem appears only on keyboard 
I dont know wether its a physical problem or a software problem I wish the replacement 
phone will dont have these problems Dear MI team you should consider the blue colour problem on resmi 6 pro display 
It may affect your smartphone marketing Dear MI Please make quality product as shows in your TV Advertising 
Im waiting to get the replacement Amazon lag in replacement policy without a hand to hand replacement Hate to purchase from Amazon',' '),
('223','cant connect to camera','Desh Deepak APS Chauhan','3.0 out of 5 stars','2/3/2024','Camera','good rear camera and bad front camera but software problem so cant connect to camera error comes on startup of camera!
Far better than asus zenfone max pro m1
Now feeling the Sony camera quality
Front camera is wow (5mp) still taking better than 13mp pics
I am using this phone as a pro photographer now
Wait for one month and you will get 1000/- off on it
Thanks amazon
Thanks Mi India',' '),
('224','Worst Camera','Pawan Dwivedee ','2.0 out of 5 stars','3/5/2024','Camera','Front camera of this phone is like a VGA camerahaving very noisy effect I recommend that please dont buy this phone','10 people found this helpful'),
('225','This mobile is defective','Anand harsh','1.0 out of 5 stars','6/7/2024','Display','I say this product is very defective camera is not working proper and speed is very slow and company Refunding my money the amazon customers care representative s behavior is very bad there is option of return on display the amazon companys app but not return this product so I request to all customers be care full','8 people found this helpful'),
('226','Camera not good','rohan sulgekar','1.0 out of 5 stars','1/20/2024','Others','Not good photo crirati','11 people found this helpful'),
('227','Not worth the money paid. Worst camera & screen size','Sreenath Bettanna','1.0 out of 5 stars','1/15/2024','Camera','Camera is too worst considering price of the phone Front camera worst than other ordinary mobiles Processor not that much fast than other 2 ghz speed mobiles of redmi Notch is only for namesake and size sake Its a big let down Bought this phone considering notch option But redmi disappointed here Is redmi started thinking India as dump yard Redmi Y2 is better option than this','5 people found this helpful'),
('228','UNBOXING AND CAMERA SHOTS!','TECHBORED! Himanshu Chatra','5.0 out of 5 stars','1/25/2024','Display','Hey guys this is TECHBORED! and this is unboxing and also will adding some camera shots
-----------------------
IN THE BOX
-----------------------
1 Manuals with warranty information
2 Charging cable
3 5V 2A power adapter
4 Transparent TPU case
5 Redmi 6 Pro
----------
DESIGN
----------
1 The transparent case fits well and is a perfect fit Gives nice feel in hands
2 It comes with a notch that is small and I really liked itAt least Xiaomi has tried to cut out the bezels at this budget segment
3 It sports a FULL HD + display with that 199 aspect ratio
4 On the top of the phone there is this infrared sensor secondary noise cancellation microphone and wow there is this 35mm headphone jack Always happy to see this port
5 Now moving to the button than there is this micro USB port situated with microphone and the speaker that is loud but decent sounding speaker
6 Redmi 6 Pro body is made up of both metal and plastic So this is only where metal is used but on the top bottom and on the sides it is plastic Also the sim tray is made up of plastic Buttons are made up of metal thats nice and gives very nice feedback
----------------------------
DUAL 4G STANDBY
----------------------------
There is DUAL SIM with dual 4G standby so you can use both sims on 4G at same time And here is a
good thing that I liked about this and it is that it has dedicated Micro SD card slot
---------------------------
FACE UNLOCK
---------------------------
There is also the finger print sensor that is fast enough to unlock and it also come with this face unlock that is pretty fast and I think it is very much secure At least it will not be unlocked with your pictures
-----------------------
CAMERA SETUP
-----------------------
1 The best thing that Xiaomi has put in to this Redmi 6 Pro and it is the same camera setup as on Redmi Note 5 Pro So it has 12Mp with 5mp dual camera setup with aperture of 22 and the single LED flash in the middle Just now I cannot tell in detail that how how camera performs but I have included some shots that are taken on Redmi 6 Pro and I think they are nicedecent and are almost the the same as on Redmi Note 5 Pro
2 This camera setup can record upto 1080p videos at 30fps and it supports EIS and the videos are not much shaky and EIS performs well Where as on the front is 5MP with aperture of 20 camera and its decent
-------------------
HARDWARE
-------------------
1 So it is powered with the same old Snaprdragon 625 and I think think that it is good for the budget smartphones for now and it performs well on this smartphone
2 Redmi 6 Pro is backed up with 4000mAh battery that is great
3 Running on Android 81 Oreo and on the top of that there is custom MIUI 9 It will soon get a stable update of MIUI10
4 So the Redmi 6 pro comes in 3GB RAM with 32GB internal mermory and 4GB RAM with 64 GB internal memory variants',' '),
('229','Battery','Pardeep sharma','5.0 out of 5 stars','2/1/2024','Battery','NYC camera and battery backup',' '),
('230','This Time Mi cheats..','aanik azad','1.0 out of 5 stars','6/11/2024','Camera','A very worst mobile in such a BiG cost paid in 11K rs There are so many best mobiles are present in every companyThe very disappointing thing is its front camerain today selfie days there is a very dirty and disappointing front camraa big loss of Rs',' '),
('231','A compact power pack Device with great battery and a decent camera','kunal Sethi','5.0 out of 5 stars','5/7/2024','Display','This device feels great in hand because it is compact enough and doesnt feels bulky at all Thanks to its notch display and 199 aspect ratio
Directly coming to its pros and cons after 1 day of use (will update soon)
Pros
1 Design - Compact design as compared to redmi note 5 pro 584"" screen looks way too compact as compared to 6"" in note 5 pro Design 9/10
2 Rear Camera - Rear Camera is fair enough If note 5 pro is 20 then its 19 It captures detailed image in good lights but struggles a bit in low light Rating 8/10
3 Audio 9/10
4 Looks like a typical Xiaomi Device Still ok because it is having unibody metal design 85/10
5 Price - Price of this device is fair in all aspects 10/10

Cons
The only con I felt is front camera If the camera would be at least 12 MP shooter then this deal would be great or I must say greatest

For people who are confused between realme 2 and redmi 6 pro I would suggest them to buy redmi 6 pro

Pls hit like if u thought this review was helpful','NULL'),
('232','Good Phone but price HIGHER','MALLA TULASI SANKAR GANESH','4.0 out of 5 stars','7/23/2024','Display','Pros
Good DisplayBetter Battey PerformanceProper Phone size to fit in a wallet or hand Excellent Build Quality looks premium
Cons
Outdated Snapdragon 625 processorRear Camera above averageFront camera below averageSpeaker Sound is low
Charger Cable length is shortened
Recommend to buy if its price is 10000','NULL'),
('233','Best phone forever.','Manish Singh','5.0 out of 5 stars','1/21/2024','Others','Best phone with face unlock full hd video recording and all latest features','NULL'),
('234','Not impressive, Y2 is better','Mudasar Nazar','2.0 out of 5 stars','3/16/2024','Others','Overall Phone seems to be good with performance perspective under this range category Do not buy if you are looking for wider screen and thinner phone I felt Y2 would have been better choice in the same range which I already brought one for the family

Not satisfied with the looksscreen size and it is a fatty phone','NULL'),
('235','Very Terrible, Worst Smartphone.','Aniket Sidanale','1.0 out of 5 stars','1/28/2024',
'Camera','Looks is poor Very bad PerformanceCamera quality Totally Worst 
Please everybody do not buy Redmi 6 pro Go to Realme 2 I wasted my money','NULL'),
('236','Dont buy this mobile mi 6 pro','Vasudevan','1.0 out of 5 stars','2/20/2024','Display','Very poor quality in front facing cameraand sound quality very poorfull display not working all appsvideo clear videosnot good zoom photos not clear picturers 10999 not worth this mobile waste of manyreturn option not available this phonereturn my phone please Amazon','NULL'),
('237','Good phone','Vaibhav Agarwal','5.0 out of 5 stars','7/27/2024','Others','I loved the fact that Lenovo gave me such a nice transparent back cover Very happy with phone and cover quality','NULL'),
('238','Disappointed.','Dinesh Kumar P','1.0 out of 5 stars','7/9/2024','Battery','Worstdont go for it Performance wisecamera wisebattery wise waste Please go for any other good brand In second time replacement also having the same front camera portrait issuetotally wasteaudio quality is too low to audible','NULL'),
('239','dont buy these product. these copy of the product','KHAN SONU RAFI AHMED','1.0 out of 5 stars','6/25/2024','Others','Please dont buy these product I have 3-mobile of MI but i did not face these type of issue mobile data getting on and off automatically same things are happening with wifihot-spot and bluetooth The handset behaving like cheap quality i think its duplicate or copy of original handset','NULL'),
('240','average phone','sarfaraz alam','3.0 out of 5 stars','4/3/2024','Battery','after using two weeks i just analyse that it is a average phone in this price catagory price should not be more than 10000/- for this phone
here i analyse some pros and cons of this phone after countinious using of this phone
PROS-
1screen resolution is preety good 1080 x 2280 pixelscolours contrast also very impressive
2two days battery backup if you not playing heavy games on it like PUBG
3Snapdragon 625 is old but till now its performance is awsm you did not face any lag in games in low graphic setting
4camera pictures quality is goodalso portrait mode captures the good depth effect in photos but only in Day light condition in night you will face high noice in pictures
5front facing camera also have AI depth effect it not too much good but you can take good selfy in day light condition
6process optimization in this phone is good
7there are a little notch which increase the looks and design of phone
CONS-
1one thing i hate in this phone is its notifaction baryou will not get all notification on top barevery time you need to scroll down the ntification bar to see app notifications net speed meter is also not shown and no whatsapp icon notification on the top of the bar because of the notch on the screen Mi company should needs to fix these minaor issues by new updatess
2Downloading process in background is little bit slow in this phone as compare to other redmi phones
3 video recording quality of this phone is not good
4only 5MP front facing camera and quality is very average in this price segment there are many phones avilabe which have better
front cameras','NULL'),
('241','A compact power pack Device with great battery and a decent camera','kunal Sethi','5.0 out of 5 stars','7/2/2024','Display','This device feels great in hand because it is compact enough and doesnt feels bulky at all Thanks to its notch display and 199 aspect ratio
Directly coming to its pros and cons after 1 day of use (will update soon)
Pros
1 Design - Compact design as compared to redmi note 5 pro 584"" screen looks way too compact as compared to 6"" in note 5 pro Design 9/10
2 Rear Camera - Rear Camera is fair enough If note 5 pro is 20 then its 19 It captures detailed image in good lights but struggles a bit in low light Rating 8/10
3 Audio 9/10
4 Looks like a typical Xiaomi Device Still ok because it is having unibody metal design 85/10
5 Price - Price of this device is fair in all aspects 10/10

Cons
The only con I felt is front camera If the camera would be at least 12 MP shooter then this deal would be great or I must say greatest

For people who are confused between realme 2 and redmi 6 pro I would suggest them to buy redmi 6 pro

Pls hit like if u thought this review was helpful','2 people found this helpful'),
('242','Good Phone but price HIGHER','MALLA TULASI SANKAR GANESH','4.0 out of 5 stars','2/2/2024','Display','Pros
Good DisplayBetter Battey PerformanceProper Phone size to fit in a wallet or hand Excellent Build Quality looks premium
Cons
Outdated Snapdragon 625 processorRear Camera above averageFront camera below averageSpeaker Sound is low
Charger Cable length is shortened
Recommend to buy if its price is 10000',' '),
('243','Best phone forever.','Manish Singh','5.0 out of 5 stars','6/26/2024','Others','Best phone with face unlock full hd video recording and all latest features','20 people found this helpful'),
('244','Not impressive, Y2 is better','Mudasar Nazar','2.0 out of 5 stars','1/22/2024','Others','Overall Phone seems to be good with performance perspective under this range category Do not buy if you are looking for wider screen and thinner phone I felt Y2 would have been better choice in the same range which I already brought one for the family

Not satisfied with the looksscreen size and it is a fatty phone',' '),
('245','Very Terrible, Worst Smartphone.','Aniket Sidanale','1.0 out of 5 stars','4/19/2024','Camera','Looks is poor Very bad PerformanceCamera quality Totally Worst Please everybody do not buy Redmi 6 pro Go to Realme 2 I wasted my money',' '),
('246','Dont buy this mobile mi 6 pro','Vasudevan','1.0 out of 5 stars','3/22/2024','Display','Very poor quality in front facing cameraand sound quality very poorfull display not working all appsvideo clear videosnot good zoom photos not clear picturers 10999 not worth this mobile waste of manyreturn option not available this phonereturn my phone please Amazon',' '),
('247','Good phone','Vaibhav Agarwal','5.0 out of 5 stars','6/2/2024','Others','I loved the fact that Lenovo gave me such a nice transparent back cover Very happy with phone and cover quality','3 people found this helpful'),
('248','Disappointed.','Dinesh Kumar P','1.0 out of 5 stars','2/20/2024','Battery','Worstdont go for it Performance wisecamera wisebattery wise waste Please go for any other good brand In second time replacement also having the same front camera portrait issuetotally wasteaudio quality is too low to audible',' '),
('249','dont buy these product. these copy of the product','KHAN SONU RAFI AHMED','1.0 out of 5 stars','1/22/2024','Others','Please dont buy these product I have 3-mobile of MI but i did not face these type of issue mobile data getting on and off automatically same things are happening with wifihot-spot and bluetooth The handset behaving like cheap quality i think its duplicate or copy of original handset',' '),
('250','average phone','sarfaraz alam','3.0 out of 5 stars','4/11/2024','Battery','after using two weeks i just analyse that it is a average phone in this price catagory price should not be more than 10000/- for this phone
here i analyse some pros and cons of this phone after countinious using of this phone
PROS-
1screen resolution is preety good 1080 x 2280 pixelscolours contrast also very impressive
2two days battery backup if you not playing heavy games on it like PUBG
3Snapdragon 625 is old but till now its performance is awsm you did not face any lag in games in low graphic setting
4camera pictures quality is goodalso portrait mode captures the good depth effect in photos but only in Day light condition in night you will face high noice in pictures
5front facing camera also have AI depth effect it not too much good but you can take good selfy in day light condition
6process optimization in this phone is good
7there are a little notch which increase the looks and design of phone
CONS-
1one thing i hate in this phone is its notifaction baryou will not get all notification on top barevery time you need to scroll down the ntification bar to see app notifications net speed meter is also not shown and no whatsapp icon notification on the top of the bar because of the notch on the screen Mi company should needs to fix these minaor issues by new updatess
2Downloading process in background is little bit slow in this phone as compare to other redmi phones
3 video recording quality of this phone is not good
4only 5MP front facing camera and quality is very average in this price segment there are 
many phones avilabe which have better front cameras',' '),
('251','Bad experience ever battery% doesnt show.Low quality flash light, Sound very low..Nnot a metal','Subbhajit jana','1.0 out of 5 stars','4/29/2024','Display','Bad experience ever battery% doesnt showLow quality flash lightSound very lowNnot a metal bodycheaper metal used Only Display quality is excellent price should be 9000-9500Damaged charger given Amazon is cheating people','NULL'),
('252','Redmi 6 pro looking good, better performance.','Sanu','5.0 out of 5 stars','2/16/2024','Others','Good','NULL'),
('253','I love mi 6 pro','Anuj kr gupta','5.0 out of 5 stars','7/20/2024','Battery','Osm product
Amazon is better then flipkart I never buy on 1st sale of mi phones on flipkart but in Amazon I order 2 phones in 1st sale quickly
This phone is very good and its battery backup is amazing I love it very much
And its camera is very good quality','NULL'),
('254','Always Mi Best in Mobile ??','Manish Bavaliya ','5.0 out of 5 stars','3/17/2024','Battery','Very nice lookingslimlight weightsound qualitybattery back up all factors are niceMI 6 Pro is Nice mobile satisfied with prize and quality what I expected before purchasing','NULL'),
('255','I am satisfying this phone','Jit saha','5.0 out of 5 stars','2/12/2024','Others','Bettary so good','NULL'),
('256','excellent this redmi 6 Pro','Dalowar','5.0 out of 5 stars','7/6/2024','Others','excellent this redmi 6 Pro so nice product of redmi product thank you for xiaomi','NULL'),
('257','It Hangs','Ranjeet','1.0 out of 5 stars','5/3/2024','Others','After using it for 10 daysI am writing itthis phone as well MI A2 Hangsplease do not purchase','NULL'),
('258','Value for money...','Amazon Customer','5.0 out of 5 stars','6/4/2024','Camera','Working good with Snapdragon 625 which is its best part Camera is also good in this price rangecamera clarity is good Just go for it','NULL'),
('259','Rock u','KALINDI DEVI','5.0 out of 5 stars','1/25/2024','Others','Really nice one
Thankd','NULL'),
('260','Good for sharp use','Shankar','4.0 out of 5 stars','4/22/2024','Others','Dislike snapdragon 425','NULL'),
('261','turn out amazing to be amazing worth it','Pranay chaudhari','5.0 out of 5 stars','2/26/2024','Camera','the camera is goodphone is fast overall work well in all department','2 people found this helpful'),
('262','Dont buy camera quality extreme poor.','shivam p.','1.0 out of 5 stars','3/15/2024','Camera','I got this product today camera both front and back are not upto mark
Pixels are scattered Please dont buy this phone just because u r getting it for 11k',' '),
('263','Overall Nice','Protap G.','4.0 out of 5 stars','1/27/2024','Camera','Overall really goodFingerprint and Face unlock is really fastNo lag problems while working or gaming
Back camera is awesome
Butif you are a selfie lover so then you should not go with this
It contains Ir blasterthere are no other phones provides that','One person found this helpful'),
('264','Satisfied','Kamlesh Bajpai','4.0 out of 5 stars','1/4/2024','Display','Very good phone at this price Display quality perfect',' '),
('265','Dual 4G support','Manoj Kumar','1.0 out of 5 stars','3/5/2024','Others','I have purchsed this item and two jio sim are not working togeher But in specification it is given that it supports dual 4g sim What is this? Please dove my problem',' '),
('266','Very good','Amazon Customer','4.0 out of 5 stars','7/23/2024','Others','Good purchase nice phone with good features like 3 slots and face lock','3 people found this helpful'),
('267','Not good as expected','Bidyut Majumder','1.0 out of 5 stars','3/8/2024','Others','Do not buy',' '),
('268','Heating issues and battery is not upto the mark.','anoop vp','1.0 out of 5 stars','6/9/2024','Others','Phone has heating issue Amazon return policy is very bad they will check our phone with blancco app The app is designed to say phone is perfect always Go for realme 2 much better phone and u can save 2000 rupees also',' '),
('269','Wonder full mobile','SILAMBARASAN J','5.0 out of 5 stars','4/23/2024','Display','Amazing phone like a iphone
Nice built quality
Super camera
Super display
Better battery
Using in single hands to happy
Value for money',' '),
('270','Value for money','Amazon Customer','5.0 out of 5 stars','2/26/2024','Others','Best value for money',' '),
('271','Batytery is not good mentioned 4000mah but not good','Amazon Customer','1.0 out of 5 stars','4/24/2024','Battery','Please dontt bye camera is good but battery back up not good','NULL'),
('272','19:9 display awesome','Surendra namdev','5.0 out of 5 stars','7/13/2024','Battery','i love it awesome phone 11k camera battery super b','NULL'),
('273','Nice mobile','Kuldeep Singh','4.0 out of 5 stars','7/7/2024','Display','This is a good mobile at this price
Pros  Good displayfast processing and large battery
Cons  Camera is good but nothing special having dual camera setup','NULL'),
('274','Dont Buy','Sameet S.','1.0 out of 5 stars','5/10/2024','Battery','Charging issue
Lagging issue
hanging issue
multiple issue','NULL'),
('275','Nice mobile','Aniket','3.0 out of 5 stars','5/7/2024','Camera','Nice product
Front or rear camera thoda accha hona chahiye tha','NULL'),
('276','Cemera quality,face unlock most important in this phone','Rahul','5.0 out of 5 stars','4/4/2024','Others','I like This PhoneAwesome look and design
Im using this phone','NULL'),
('277','Mi is best phone','Sunil Soni','4.0 out of 5 stars','1/11/2024','Others','Product is avasome but invoice is note include','NULL'),
('278','Its a OK Phone','D.C.Padhi','3.0 out of 5 stars','5/14/2024','Battery','Redmi Note4Note5now 6proIt seems the older the model the better was the performance as I used all 3 models in the line The notch designhides the battery % and network speedone has to pull down a bit to see these 2 things Note 5 and 6pro both have a common issue-- after switching the swipe up (to unlock) does not work smoothly every time The escape is to switch off the swipe up feature After Note4in the newer models the length of USB cable has become shorterwhichis a problem if you are little away from the plug point How much cost does Xiaomi saves by shortening the cable? 6pro came with a smaller ejection tooladditional cost saving by cutting 2gm of metal The front flash if Note5 has been removed in 6pro These manufacturers seem to be idiots and fooling public by launching new models without any real additional feature or improvement Anywayits an OK phone for 10000 (3GB/32GB) For 11000 a customer expects a little moreand Xiaomi disappoints here','NULL'),
('279','Redmi','Mahesh','5.0 out of 5 stars','2/10/2024','Others','I love mi','NULL'),
('280','Not worth for the price.','Vinod','1.0 out of 5 stars','4/15/2024','Camera','Same old configurations with higher price
Not worth for money
Camera quality is not up to mark
Notch - I personally feel this as a feature which is not useful for this size (584) of phone Infact that makes phone looks smaller than 584 as notch is also included in size

There are better options available in same price range','NULL')


