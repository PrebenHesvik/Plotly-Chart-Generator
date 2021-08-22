import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly as py
import numpy as np


def scatter_subplots(data, layout, rows, cols, titles, iplot=True):
    """Scatter chart subplots

    Parameters
    ----------
    data : dict
        chart data
    layout : dict
        Chart layout, formatting and styles
    rows : int
        number of chart rows
    cols : int
        number of chart columns
    titles : list
        subplot titles
    """

    fig = make_subplots(rows=rows, cols=cols, subplot_titles=titles)

    col_nums = np.tile([*range(1, cols + 1)], rows)
    row_nums = np.repeat([*range(1, rows + 1)], cols)
    plot_order = list(zip(col_nums, row_nums))

    for key, value in data.items():
        col, row = plot_order.pop(0)
        fig.add_trace(
            go.Scatter(x=value['x'], y=value['y'], mode='markers',
                       text=value['names'], name=key,
                       marker=dict(size=None)),
            row=row.item(), col=col.item())

    # update layout
    fig.update_layout(layout)
    fig.update_yaxes(layout['yaxis'])
    fig.update_xaxes(layout['xaxis'])

    layout['annotations'] = dict(font=dict(size=12, color='lightgrey'))
    for i in fig['layout']['annotations']:
        i['font'] = layout['annotations']['font']

    # display chart
    if iplot:
        py.offline.iplot(fig)
    else:
        return fig
