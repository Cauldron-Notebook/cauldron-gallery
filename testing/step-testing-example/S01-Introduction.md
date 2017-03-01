# Step Testing Example

A farmer has a large field in which she has placed 10 ground-level temperature 
sensors to investigate variations in temperature throughout her crops. She also 
has an aerial temperature sensor on top of her barn at the edge of the field.

She is interested in understanding how the ground-level temperature sensors at 
different locations in the field relate to the aerial temperature sensor on 
the barn that she uses as a guide for planting and caring for her crops.

The temperature sensors record a temperature value every 15 minutes over a 24 
hour period and then save that days data to CSV files for analysis.

We begin by loading the data and then calculating the lag factor, which is the
phase difference between aerial temperature readings and ground-level 
temperature readings. This is an indication of how long it takes for the 
ground-level temperatures to catch up to changes in air temperature.
