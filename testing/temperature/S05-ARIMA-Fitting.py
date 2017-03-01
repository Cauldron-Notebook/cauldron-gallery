import cauldron as cd

from _temperatures import arima
from _temperatures import plots

# Retrieve shared data
df_2016 = cd.shared.df_2016
df_history = cd.shared.df_history.sort_values(by='order', ascending=True)

# Run ARIMA models over a range of order combinations and create a list of
# all results
models = [
    arima.run(df_history, p, d, q)
    for p in range(5)
    for d in range(2)
    for q in range(5)
]

# Remove None results from modeling attempts that were unsuccessful
models = [m for m in models if m is not None]

for md in models:
    cd.display.bokeh(plots.create_arima_plot(df_history, md))

# Share models with other steps
cd.shared.models = models
