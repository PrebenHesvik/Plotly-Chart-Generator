import plotly.graph_objs as go
import numpy as np


def line_chart(
        df,
        mode='lines',
        line_width=2,
        marker_size=None,
        marker_symbol='circle',
        text=None,
        text_position='bottom center',
        text_size=14,
        text_color='lightgrey',
        line_smoothing=1.3,
        marker_color=None,
        line_color=None,
        **kwargs):
    """
    Line chart

    Creates a single line chart or multiple-lines chart
    based on data in DataFrame.

    DataFrame must have the following shape
    ----------------------------------------

    +----------+----------+----------+----------+
    | Columns  | Header 1 | Header 2 | Header 3 |
    +==========+==========+==========+==========+
    | row name |    25    |    34    |    50    |
    +----------+----------+----------+----------+
    | row name |    25    |    34    |    50    |
    +----------+----------+----------+----------+


    Parameters
    ----------
    df : DataFrame
        Contains the to be charted
    layout : dict
        Chart layout, formatting and styles
    mode : str, optional
        Choose between `lines`, `markers` or `none`.
        `text` can also be added as an argument.
        by default 'lines'
    line_width : int, optional
        line width, by default 3
    marker_size : int or None, optional
        Sets the marker size of selected points., by default None
    marker_symbol: str, optional
        Sets the marker symbol type. Adding 100 is equivalent to
        appending "-open" to a symbol name. Adding 200 is
        equivalent to appending "-dot" to a symbol name. Adding 300
        is equivalent to appending "-open-dot" or "dot-open" to a
        symbol name. By default 'circle'.
    text : str, optional
        Sets text elements associated with each (x,y) pair, by default None
    text_position : str, optional
        Sets the positions of the `text` elements with respects
        to the (x,y) coordinates, one of (`top left`,  `top center`,
        `top right`, `middle left`, `middle center`, `middle right`,
        `bottom left`,`bottom center`, `bottom right` ),
        by default 'bottom center'
    text_size : int, optional
        size of text, by default 14
    text_color : str, optional
        text color, by default 'lightgrey'
    annotations : list, optional
        Text element that can be placed anywhere in the plot. It can be
        positioned with respect to relative coordinates in the plot or
        with respect to the actual data coordinates of the graph.
        By default None


    Example:
    ---------

    # create data
    index = [f'Day {x}' for x in range(10)]
    values = {'Solo line': [np.random.rand() for x in range(10)]}
    data = pd.DataFrame(index=index, data=values).transpose()

    # create chart
    color_palette = chart.
    layout = chart.layout(width=600, height=400)
    chart.line(data, layout)
    """

    if isinstance(line_width, int):
        line_width = np.repeat(line_width, df.index.size).tolist()

    traces = []
    for row in df.index:

        keyword_args = dict(
            x=df.columns,
            y=df.loc[row],
            mode=mode,
            line=dict(
                width=line_width.pop(0),
                color=line_color,
                shape='spline',
                smoothing=line_smoothing),
            text=text,
            name=row,
            textposition=text_position,
            textfont=dict(
                size=text_size,
                color=text_color),
            marker=dict(
                size=marker_size,
                symbol=marker_symbol,
                color=marker_color,
                gradient=dict(
                    type='radial',
                    color=['#2f323d', '#bbbe64']))
        )

        line = go.Scatter(dict(**keyword_args, **kwargs))
        traces.append(line)

    return traces
