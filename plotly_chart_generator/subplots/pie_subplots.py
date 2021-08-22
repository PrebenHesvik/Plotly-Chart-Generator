import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly as py
import numpy as np


def pie_subplots(data, rows, cols, titles,
                 layout, hole=.3, subplot_title_size=15,
                 subplot_title_color='lightgrey', linewidth=5,
                 linecolor='#202534', hoverinfo='label+percent',
                 textinfo='value', iplot=True):
    """Pie chart subplots


    Parameters
    ----------
    data : dict
        chart data
    rows : int
        number of chart rows
    cols : int
        number of chart columns
    titles : list
        subplot titles
    layout : dict
        Chart layout, formatting and styles
    hole : float, optional
        Sets the fraction of the radius to cut out of the pie.
        Use this to make a donut chart. By default .3
    subplot_title_size : int, optional
        Size of subplot titles, by default 15
    subplot_title_color : str, optional
        color of subplot titles, by default 'lightgrey'
    linewidth : int, optional
        size of line between pieces, by default 5
    linecolor : str, optional
        Color of line around each piece, by default '#202534'
    hoverinfo : str, optional
        Determines which trace information appear on hover.
        Any combination of `label`, `text`, `value`, `percent`, `name`
        joined with a `+` OR `all` or `none` or `skip`.
        By default 'label+percent'
    textinfo : str, optional
        Determines which trace information appear on the graph.
        Any combination of `label`, `text`, `value`, `percent`
        joined with a `+` OR `none`. by default 'value'
    """
    specs = [[{'type': 'domain'} for x in range(cols)] for x in range(rows)]

    fig = make_subplots(rows=rows, cols=cols,
                        subplot_titles=titles, specs=specs)

    col_nums = np.tile([*range(1, cols + 1)], rows)
    row_nums = np.repeat([*range(1, rows + 1)], cols)
    plot_order = list(zip(col_nums, row_nums))

    for key, value in data.items():
        col, row = plot_order.pop(0)
        fig.add_trace(
            go.Pie(labels=[*value.keys()], values=[*value.values()],
                   name=key, hole=hole, hoverinfo=hoverinfo,
                   textinfo=textinfo, marker=dict(line=dict(
                       color=linecolor, width=linewidth))),
            row=row.item(), col=col.item())

    # update layout
    fig.update_layout(layout)
    layout['annotations'] = dict(font=dict(size=12, color='lightgrey'))
    for i in fig['layout']['annotations']:
        i['font'] = layout['annotations']['font']

    # display chart
    if iplot:
        py.offline.iplot(fig)
    else:
        return fig
