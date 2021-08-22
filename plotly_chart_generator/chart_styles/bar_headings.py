def bar_headings(df, orientation='h', font_color='lightgrey',
                 font_family='sans-serif', font_size=15, y=1, x=0):
    """Chart headings

    [extended_summary]

    Parameters
    ----------
    df : dataframe
        Contains the chart data
    orientation : str, optional
        Bar chart orientation, by default 'h'
    font_color : str, optional
        Text color, by default 'lightgrey'
    font_family : str, optional
        Text font-family, by default 'sans-serif'
    font_size : int, optional
        text font-size, by default 15
    y : int, optional
        y-position of text, by default 1
    x : int, optional
        [description], by default 0

    Returns
    -------
    list of text annotations
    """

    values = df.iloc[-1] if orientation == 'h' else df.iloc[:, 0]
    names = df.columns if orientation == 'h' else df.index
    textangle = 0 if orientation == 'h' else -90
    xref, yref = ('x', 'paper') if orientation == 'h' else ('paper', 'y')

    annotations = []
    space = 0
    for i, tupl in enumerate(zip(values, names)):
        x = space + (tupl[0] / 2) if orientation == 'h' else x
        y = y if orientation == 'h' else space + (tupl[0] / 2)
        annotations.append(dict(xref=xref, yref=yref,
                                x=x, y=y, text=tupl[1],
                                textangle=textangle,
                                font=dict(family=font_family,
                                          size=font_size,
                                          color=font_color),
                                showarrow=False))
        space += tupl[0]
    return annotations
