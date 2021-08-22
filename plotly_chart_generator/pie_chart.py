import plotly.graph_objs as go


def pie_chart(
        labels,
        values,
        hole=.3,
        name='',
        hoverinfo='label+percent',
        textinfo='value',
        textfont_size=20,
        linewidth=2,
        linecolor='#202534',
        pull=[],
        pull_dist=0.2,
        titlecolor='lightgrey',
        titlesize=15,
        title=None,
        opacity=None,
        textposition=None):
    """Creates pie chart

    Create a pie chart by passing two lists, numpy arrays
    or Pandas series of the labels and corresponding values.

    Parameters
    ----------
    labels : list, numpy array, Pandas series
        Sets the sector labels
    values : list, numpy array, Pandas series
        Sets the values of the sectors. If omitted, occurrences
        of each label are counted.
    layout : dict
        Chart layout, formatting and styles
    hole : float, optional
        Sets the fraction of the radius to cut out of the pie.
        Use this to make a donut chart. By default .3
    name : str, optional
        Insert name inside dougnut circle, by default ''
    hoverinfo : str, optional
        Determines which trace information appear on hover.
        Any combination of `label`, `text`, `value`, `percent`, `name`
        joined with a `+` OR `all` or `none` or `skip`.
        By default 'label+percent'
    textinfo : str, optional
        Determines which trace information appear on the graph.
        Any combination of `label`, `text`, `value`, `percent`
        joined with a `+` OR `none`. by default 'value'
    textfont_size : int, optional
        Size of textinfo, by default 20
    linewidth : int, optional
        size of line between pieces, by default 10
    linecolor : str, optional
        Color of line around each piece, by default '#202534'
    pull : int or list, optional
        Sets the fraction of larger radius to pull the sectors out from
        the center. This can be a constant to pull all slices apart
        from each other equally or an array to highlight one or more
        slices. By default 0.2, by default []
    titlecolor : str, optional
        Color of title, by default 'lightgrey'
    titlesize : int, optional
        Size of title, by default 15
    title : float, optional
        Title text, by default None
    opacity : float, optional
        Sets the opacity of the trace., by default None
    """

    pull = [pull_dist if x in pull else 0 for x in labels]
    data = go.Pie(
        labels=labels,
        values=values,
        hole=hole,
        name=name,
        title=dict(text=title),
        textposition=textposition,
        opacity=opacity,
        hoverinfo=hoverinfo,
        textinfo=textinfo,
        textfont_size=textfont_size,
        pull=pull,
        marker=dict(
            line=dict(
                color=linecolor,
                width=linewidth))
    )
    return data
