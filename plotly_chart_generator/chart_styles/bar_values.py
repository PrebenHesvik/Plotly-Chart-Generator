def bar_values(
        df, orientation='h', font_size=15,
        font_color='lightgrey',
        font_family='sans-serif'):
    """Bar values placed in the center of each bar.

    [extended_summary]

    Parameters
    ----------
    df : dataframe
        Contains the data to be charted
    orientation : str
        Orientation of the bar chart.'v' for vertical,
        'h' for horizontal. By default 'h'.
    font_size : int, optional
        Bar values font-size, by default 15
    font_color : str, optional
        Bar values font-color, by default 'lightgrey'
    font_family : str, optional
        Bar values font-family, by default 'sans-serif'

    Returns
    -------
    list of annotations containing bar values
    """
    annotations = []
    size = df.index.size if orientation == 'h' else df.columns.size
    for i in list(range(size)):
        arr = df.iloc[i] if orientation == 'h' else df.iloc[:, i]
        space = 0
        for ii, val in enumerate(arr):
            x = space + (val / 2) if orientation == 'h' else arr.name
            y = arr.name if orientation == 'h' else space + (val / 2)
            annotations.append(dict(xref='x', yref='y', x=x, y=y,
                                    text=str(val), showarrow=False,
                                    font=dict(family=font_family,
                                              size=font_size,
                                              color=font_color)))
            space += val
    return annotations
