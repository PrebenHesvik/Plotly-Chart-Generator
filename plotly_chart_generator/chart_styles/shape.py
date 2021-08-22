import plotly.graph_objs as go


def shape(x0, x1, y0, y1, type='rect', layer='above',
          line_color='royalblue', line_width=1,
          line_style='solid', fill_color=None,
          xref='x', yref='paper', opacity=1):
    """Add shape to chart

    [extended_summary]

    Parameters
    ----------
    x0 : int, float
        Sets the shape's starting x position.
    x1 : int, float
        Sets the shape's end x position.
    y0 : int, float
        Sets the shape's starting y position.
    y1 : int, float
        Sets the shape's end y position.
    type : str, optional
        Specifies the shape type to be drawn.
        Options: 'rect', 'circle', 'line', 'path'.
        If 'line', a line is drawn from (`x0`,`y0`) to (`x1`,`y1`) with
        respect to the axes' sizing mode. If "circle", a circle is drawn
        from ((`x0`+`x1`)/2, (`y0`+`y1`)/2)) with radius (|(`x0`+`x1`)/2 -
        `x0`|, |(`y0`+`y1`)/2 -`y0`)|) with respect to the axes' sizing
        mode. If "rect", a rectangle is drawn linking (`x0`,`y0`),
        (`x1`,`y0`), (`x1`,`y1`), (`x0`,`y1`), (`x0`,`y0`) with respect
        to the axes' sizing mode. If "path", draw a custom SVG path using
        `path`. with respect to the axes' sizing mode., by default 'rect'
    layer : str, optional
        Specifies whether shapes are drawn below or above traces.
        Choose between 'above' and 'below', by default 'above'
    line_width : int, optional
        Sets the line width (in px)., by default 1
    line_color : str, optional
        Line color, by default 'royalblue'
    line_style : str, optional
        Sets the dash style of lines.
        Options: 'solid', 'dot', 'dash', 'longdash', 'dashdot',
        'longdashdot', by default 'solid'
    fill_color : [type], optional
        Shape fill color, by default None
    xref : str, optional
        Sets the shape's x coordinate axis. If set to an x axis id (e.g.
        'x' or 'x2'), the `x` position refers to an x coordinate. If set
        to "paper", the `x` position refers to the distance from the left
        side of the plotting area in normalized coordinates where '0' ('1')
        corresponds to the left (right) side. If the axis `type` is "log",
        then you must take the log of your desired range. If the axis
        `type` is "date", then you must convert the date to unix time in
        milliseconds., by default 'x'
    yref : str, optional
        Sets the annotation's y coordinate axis. If set to an y axis id
        (e.g. 'y' or 'y2'), the `y` position refers to an y coordinate If
        set to "paper", the `y` position refers to the distance from the
        bottom of the plotting area in normalized coordinates where '0'
        ('1') corresponds to the bottom (top)., by default 'paper'
    opacity : int, optional
        Sets the opacity of the shape., by default 1



    Returns
    -------
    Shape object
    """
    return go.layout.Shape(
        type=type, xref=xref, yref=yref, x0=x0, y0=y0,
        x1=x1, y1=y1, fillcolor=fill_color, opacity=opacity,
        line=dict(color=line_color, width=line_width,
                  dash=line_style))
