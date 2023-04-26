# TimeSheet Generator Script

## Purpose

We have table below to plan each days hours to meet these requirements:

* Each row is a project or task, the sum of the values will equal to the total planned hours
* Each column is a day, we will need to fill each day's hours to make the sum of each day to the predefined amount, in our case, it's MAX_HOUR_PER_DAY = 7.5

Here is an example of 5 days timesheet
|Projects|Planed|Day 1|Day 2|Day 3|Day 4|Day 5|
|---|---|---|---|---|---|---|
|**Proj 1**|8.5|1.75|2.00|1.25|1.75|1.75
|**Proj 2**|10.5|2.00|3.00|0.50|2.75|2.25
|**Proj 3**|10|3.00|0.50|3.00|0.25|3.00
|**Proj 4**|8.5|0.75|2.00|2.75|2.50|0.50
|**Total**|37.5|7.5|7.5|7.5|7.5|7.5

This script will help you to generate timesheet like that to meet those requirements

Like the table above shows, we defined the rules like these
```
DAYS = 5
MAX_HOUR = [2, 3, 3, 2]
TOTAL_HOURS = [8.5, 10.5, 10, 8.5]
```
These means
* We need to generate totally 5 days time data
* There are 4 tasks/rows, each of them has a total amount for these days. We use `TOTAL_HOURS = [8.5, 10.5, 10, 8.5]` to specify
* MAX_HOUR is to tell the script that the maximum hour for a given day should not exceed that amount. For example [2,3,3,2] means for the task 1, max hour put in a single day can't be more than 2 and it can't be more than 3 for the 2nd task/row, so on and so forth.

We can also specify the `TIME_FACTOR` which by default is = 4

TIME_FACTOR is to control the smallest piece of time we can assign  
For instance, when we use TIME_FACTOR = 4, the minimum time slot we can allocate is 1 / TIME_FACTOR = 0.25. That is why all those values end up with 0, 0.25, 0.5, 0.75. There won't be other time fractions like 1.55 or 1.63 because we controlled the minimum time-slot it can assign to.

If you use 0.5h as your minimum time slot to report, you should set `TIME_FACTOR = 2` which means minimum time slot: 1 / TIME_FACTOR = 0.5

## How to use it

Modify the lines like these below for your use case
```
DAYS = 5
MAX_HOUR = [2, 3, 3, 2]
TOTAL_HOURS = [8.5, 10.5, 10, 8.5]
```
Run the script, it will generate the `timesheet.csv` file


```
Total Hours,Day 1,Day 2,Day 3,Day 4,Day 5
8.5,1.75,2.00,1.25,1.75,1.75
10.5,2.00,3.00,0.50,2.75,2.25
10,3.00,0.50,3.00,0.25,3.00
8.5,0.75,2.00,2.75,2.50,0.50
```

Open Google Sheet, use File -> Import -> Upload from own disk, then pick the CSV file

Once the CSV is uploaded, you can copy/paste it