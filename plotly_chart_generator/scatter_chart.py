import plotly.graph_objs as go


def scatter_chart(
        data,
        marker_size=2,
        mode='markers',
        marker_symbol='circle',
        text=None,
        text_pos='bottom center',
        text_size=14,
        text_color='grey',
        **kwargs):
    """Scatter chart


    Parameters
    ----------
    data : dict
        Contains the information to be charted. It consists of at
        least one 'key' of which itself contains a dictionary
        composed of two mandatory keys, labeled 'x', 'y',
        and two optional keys that must be labeled 'text'
        and 'colors' if they are to be used.
    layout : dict
        Chart layout, formatting and styles
    marker_size : int, optional
        Sets the marker size of selected points, by default 2
    marker_symbol: str, optional
        Sets the marker symbol type. Adding 100 is equivalent to
        appending "-open" to a symbol name. Adding 200 is
        equivalent to appending "-dot" to a symbol name. Adding 300
        is equivalent to appending "-open-dot" or "dot-open" to a
        symbol name. By default 'circle'.
    text : str, optional
        Sets text elements associated with each (x,y) pair, by default None
    text_pos : str, optional
        Sets the positions of the `text` elements with respects
        to the (x,y) coordinates, one of (`top left`,  `top center`,
        `top right`, `middle left`, `middle center`, `middle right`,
        `bottom left`,`bottom center`, `bottom right` ),
        by default 'bottom center'
    text_size : int, optional
        size of text, by default 14
    text_color : str, optional
        text color, by default 'lightgrey'
    """
    if not isinstance(data, dict):
        raise TypeError(
            f'You must pass the data as a dictionary. You passed {type(data)}')

    traces = []
    for key, value in data.items():

        keyword_args = dict(
            x=value['x'],
            y=value['y'],
            mode=mode,
            name=key,
            text=value.get('text', None),
            textposition=text_pos,
            textfont=dict(size=text_size),
            marker=dict(
                size=marker_size,
                symbol=marker_symbol,
                color=value.get('colors'))
        )

        scatter = go.Scatter(dict(**keyword_args, **kwargs))
        traces.append(scatter)

    return traces
