import plotly.graph_objs as go


def histogram(
        x=None,
        y=None,
        histnorm='percent',
        orientation='v',
        title=None,
        name=None,
        text=None,
        opacity=0.9,
        marker_color=None,
        marker_colorscale=None,
        line_width=0,
        line_color=None,
        line_colorscale=None,
        histfunc='count'):
    """Creates a histogram


    Parameters
    ----------
    data : list, numpy array or pandas series
        The data to base the chart on
    layout : dict
        Chart layout, formatting and styles
    histnorm : str, optional
        Specifies the type of normalization used for
        this histogram trace. Choose between 'percent',
        'probability', 'density' and
        'probability density'. By default 'percent'
    orientation : str, optional
        Sets the orientation of the bars. With "v" ("h"),
        the value of the each bar spans along the vertical
        (horizontal). By default 'v'
    title : str, optional
        Sets chart title, by default ''
    x_title : str, optional
        Sets title of x-axis, by default ''
    y_title : str, optional
        Sets title of y-axis, by default ''
    opacity : float, optional
        Sets the opacity of the bars, by default 0.9
    histfunc : str, optional
        Specifies the binning function used for this histogram trace.
        If "count", the histogram values are computed by counting the
        number of values lying inside each bin. If 'sum', 'avg', 'min',
        'max', the histogram values are computed using the sum,
        the average, the minimum or the maximum of the values lying
        inside each bin respectively.

    documentation: https://plotly.com/python/reference/#histogram

    """
    return go.Histogram(
        x=x,
        y=y,
        histnorm=histnorm,
        orientation=orientation,
        histfunc=histfunc,
        name=name,
        text=text,
        marker=dict(
            opacity=opacity,
            color=marker_color,
            colorscale=marker_colorscale,
            line=dict(
                width=line_width,
                color=line_color,
                colorscale=line_colorscale,
            )))
