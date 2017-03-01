# Time-Series Model

Next we're going to create an ARIMA model for the historical
time series data (2006-2015) to see how well we can predict the actual 2016
values with it.

ARIMA models are specified by their AR, I and MA orders. A specific ARIMA model 
is generally described by the vector of these three orders as (p, d, q). While
the best choice of what specific ARIMA model to use depends on the specific 
dataset, the lowest order that provides a _good_ fit is generally a good 
solution.

We will run the temperature dataset through a number of different ARIMA models
and then ascertain the one that _fits_ best. It should be noted that not all 
ARIMA models are capable of generating fits to the data. Such cases
produce fitting errors and will be excluded from the final output.

The following graphs show the ARIMA fit results of the historical
temperature data for the models that were able to fit the data.
