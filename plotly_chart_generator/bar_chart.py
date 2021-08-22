import plotly.graph_objs as go


def bar_chart(
        df,
        orientation='v',
        bar_width=None,
        opacity=0.9,
        textpos=None,
        linewidth=1,
        linecolor='#2C3347',
        marker_color=None,
        **kwargs):
    """Horizontal and vertical bar-charts.

    Create a horizontal or vertical chart by passing a pandas dataframe,
    and a layout dictionary which is created by calling chart.layout().

    DataFrame layout for vertical bar-chart
    ---------------------------------------

    +----------+----------+----------+----------+
    | Columns  | Header 1 | Header 2 | Header 3 |
    +==========+==========+==========+==========+
    | row name |    25    |    34    |    50    |
    +----------+----------+----------+----------+
    | row name |    25    |    34    |    50    |
    +----------+----------+----------+----------+

    DataFrame layout for horizontal bar-chart
    -----------------------------------------

    +----------+------+
    |          | name |
    +----------+------+
    | Header 1 |  25  |
    +----------+------+
    | Header 2 |  34  |
    +----------+------+
    | Header 3 |  50  |
    +-----------------+


    Parameters
    ----------
    df : DataFrame
        Contains the data to be charted
    layout : dict
        Chart layout, formatting and styles
    orientation : str, optional
        Chart-orientation. Choose between 'v'and 'h',
        by default 'v'
    bar_width : float, optional
        Bar-widths, by default 0.5
    opacity : float, optional
        Bar opacity, by default 0.9
    sort_by : str, optional
        Column/row to sort dataframe by, by default None
    ascending : bool, optional
        Choose between ascending and descending sort order.
        True indicates ascending, while False indicates
        descending, by default False
    mean : bool, optional
        Set to True if you want a mean-line across
        your chart, by default False
    median : bool, optional
        Set to True if you want a median-line across
        your chart, by default False
    mode : str, optional
        Choose between Stack and Group chart types,
        by default None
    textpos : str, optional
        Set position of bar values. Choose between inside,
        outside auto or None, by default None
    annotations : list, optional
        Insert annotations like bar values or headers,
        by default None
    shapes : list, optional
        Insert geometric shapes to highlight something on the
        chart, by default None
    linewidth : int, optional
        Width of outer border of each bar, by default 1
    linecolor : str, optional
        Color of outer border of each bar, by default '#2C3347'
    """

    traces = []
    rng = df.index.size if orientation == 'v' else df.columns.size
    otn = orientation
    for i in range(rng):
        x = [str(x) for x in df.columns] if otn == 'v' else df.iloc[:, i]
        y = df.iloc[i] if otn == 'v' else [str(x) for x in df.index]
        text = df.iloc[i] if otn == 'v' else df.iloc[:, i]
        name = df.iloc[i].name if otn == 'v' else df.columns[i]

        preset_args = dict(
            x=x,
            y=y,
            text=text,
            textposition=textpos,
            marker=dict(
                opacity=opacity,
                color=marker_color,
                line=dict(
                    color=linecolor,
                    width=linewidth)),
            name=name,
            width=bar_width,
            orientation=orientation
        )

        all_args = {**preset_args, **kwargs}
        bar = go.Bar(all_args)
        traces.append(bar)

    return traces
