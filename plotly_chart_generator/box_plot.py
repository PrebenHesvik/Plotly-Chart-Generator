import plotly.graph_objs as go


def box_plot(y=None, x=None, boxpoints=False,
             boxmean=True, jitter=0.3, pointpos=-1.5, opacity=0.9):
    """Box plot

    Parameters
    ----------
    y : list, numpy array, pandas series, optional
        Sets the y sample data or coordinates, by default None
    x : list, numpy array, pandas series, optional
        Sets the x sample data or coordinates, by default None
    boxpoints : str, bool, optional
        Choose between 'all', 'outliers', suspectedoutliers and False.
        If "outliers", only the sample points lying outside the whiskers
        are shown If "suspectedoutliers", the outlier points are shown
        and points either less than 4'Q1-3'Q3 or greater than 4'Q3-3'Q1
        are highlighted (see `outliercolor`) If "all", all sample points
        are shown If "False", only the box(es) are shown with no sample
        points Defaults to "suspectedoutliers" when `marker.outliercolor`
        or `marker.line.outliercolor` is set. Defaults to "all" under
        the q1/median/q3 signature. Otherwise defaults to "outliers".
        By default False
    boxmean : one of ( True | "sd" | False ), optional
        If "True", the mean of the box(es)' underlying distribution is
        drawn as a dashed line inside the box(es). If "sd" the standard
        deviation is also drawn. Defaults to "True" when `mean` is set.
        Defaults to "sd" when `sd` is set Otherwise defaults to "False".
        By default True
    jitter : float, int between or equal to 0 and 1, optional
        Sets the amount of jitter in the sample points drawn. If '0', the
        sample points align along the distribution axis. If '1', the
        sample points are drawn in a random jitter of width equal to the
        width of the box(es)., by default 0.3
    pointpos : float, int between or equal to -2 and 2, optional
        Sets the position of the sample points in relation to the box(es).
        If '0', the sample points are places over the center of the
        box(es). Positive (negative) values correspond to positions to the
        right (left) for vertical boxes and above (below) for horizontal
        boxes. By default -1.5
    opacity : float, optional
        Sets the opacity of the trace, by default 0.9
    """

    if y:
        return [go.Box(y=values, boxpoints=boxpoints,
                       name=values.name, boxmean=boxmean,
                       jitter=jitter, pointpos=pointpos,
                       opacity=opacity)
                for values in y]
    else:
        return [go.Box(x=values, boxpoints=boxpoints,
                       name=values.name, boxmean=boxmean,
                       jitter=jitter, pointpos=pointpos,
                       opacity=opacity)
                for values in x]
