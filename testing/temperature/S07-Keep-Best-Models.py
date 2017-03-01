import cauldron as cd
from bokeh.plotting import Figure

models = sorted(cd.shared.models, key=lambda md: md.rmse)

figure = Figure()
figure.vbar(
    x=list(range(len(models))),
    top=[md.rmse for md in models],
    width=0.6
)

figure.xaxis.axis_label = 'ARIMA Order (p, d, q)'

figure.yaxis.axis_label = 'Model Fit RMSE'

cd.display.bokeh(figure)
