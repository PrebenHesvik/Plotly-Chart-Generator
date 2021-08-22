def chart_styles(
        title='',
        title_alignment=0.5,
        title_color='lightgrey',
        title_font_family='sans-serif',
        title_size=24,
        x_title='',
        y_title='',
        width=None,
        height=None,
        ml=75,
        mr=50,
        mb=75,
        mt=75,
        pad=10,
        bg_color='#202534',
        grid_color='#3d4152',
        grid_width=0.5,
        zeroline_color='grey',
        axis_color='lightgrey',
        axis_fontfamily='sans-serif',
        axis_titlecolor='lightgrey',
        tick_color='lightgrey',
        yaxis_type='-',
        xaxis_type='-',
        yaxis_autorange=True,
        xaxis_autorange=True,
        yaxis_nticks=None,
        xaxis_nticks=None,
        yaxis_showgrid=True,
        xaxis_showgrid=False,
        yaxis_zeroline=True,
        xaxis_zeroline=False,
        yaxis_showline=False,
        xaxis_showline=False,
        yaxis_tickangle=0,
        xaxis_tickangle=0,
        yaxis_titlesize=18,
        xaxis_titlesize=18,
        yaxis_ticksize=13,
        xaxis_ticksize=13,
        yaxis_tickmode='auto',
        xaxis_tickmode='auto',
        yaxis_tickvals=None,
        xaxis_tickvals=None,
        yaxis_ticktext=None,
        xaxis_ticktext=None,
        yaxis_tick0=None,
        xaxis_tick0=None,
        yaxis_tickformat='',
        xaxis_tickformat='',
        yaxis_dtick=1,
        xaxis_dtick=1,
        yaxis_ticks='',
        xaxis_ticks='',
        yaxis_range=None,
        yaxis_showticklabels=True,
        xaxis_showticklabels=True,
        xaxis_range=None,
        yaxis_separatethousands=True,
        xaxis_separatethousands=True,
        legend_fontfamily='sans-serif',
        legend_fontsize=12,
        legend_fontcolor='lightgrey',
        legend_orientation='v',
        legend_x=1,
        legend_xanchor='left',
        legend_y=1,
        legend_yanchor='middle',
        legend_traceorder='normal',
        legend_bordercolor='#202534',
        showlegend=True,
        legend_borderwidth=0,
        legend_itemclick='toggle',
        legend_itemdoubleclick='toggleothers',
        legend_valign='middle',
        color_palette=None,
        *args,
        **kwargs):
    """Chart styling

    [extended_summary]

    Parameters
    ----------
    title : str, optional
        Sets the chart title, by default ''
    title_alignment : int or float, optional
        Sets the alignment of the title. 0='left',
        0.5='center', 1='right', by default 0.5
    title_color : str, optional
        Sets the title color, by default 'lightgrey'
    title_font_family : str, optional
        Sets title font-family, by default 'sans-serif'
    title_size : int, optional
        Sets title size, by default 24
    x_title : str, optional
        Sets title of x-axis, by default ''
    y_title : str, optional
        Sets title of y-axis, by default ''
    width : int, optional
        Sets chart width, by default 800
    height : int, optional
        Sets chart height, by default 600
    ml : int, optional
        Sets the left margin (in px), by default 75
    mr : int, optional
        Sets the right margin (in px), by default 50
    mb : int, optional
        Sets the bottom margin (in px), by default 75
    mt : int, optional
        Sets the top margin (in px), by default 75
    pad : int, optional
        Sets the amount of padding (in px) between the plotting
        area and the axis lines, by default 10
    bg_color : str, optional
        Sets chart background color, by default '#202534'
    grid_color : str, optional
        Sets grid color, by default '#3d4152'
    grid_width : float, optional
        Sets grid width, by default 0.5
    zeroline_color : str, optional
        Sets color of zero-line, by default 'grey'
    axis_color : str, optional
        Sets color of axis, by default 'lightgrey'
    axis_fontfamily : str, optional
        Sets axis-title font-family, by default 'sans-serif'
    axis_titlecolor : str, optional
        Sets color of axis-title, by default 'lightgrey'
    tick_color : str, optional
        Sets tick color on both axes, by default 'lightgrey'
    yaxis_type : str, optional
        Sets the axis type. By default, plotly attempts to determined
        the axis type by looking into the data of the traces that
        referenced the axis in question. Choose between '-',
        'linear', 'log', 'date', 'category', by default '-'
    xaxis_type : str, optional
        Sets the axis type. By default, plotly attempts to determined
        the axis type by looking into the data of the traces that
        referenced the axis in question. Choose between '-',
        'linear', 'log', 'date', 'category', by default '-'
    yaxis_autorange : bool, optional
        Determines whether or not the range of this axis is computed
        in relation to the input data. See `rangemode` for more info.
        If `range` is provided, then `autorange`
        is set to "False". Choose between 'True',
        'False', 'reversed', by default 'True'
    xaxis_autorange : bool, optional
        Determines whether or not the range of this axis is computed
        in relation to the input data. See `rangemode` for more info.
        If `range` is provided, then `autorange`
        is set to "False". Choose between 'True',
        'False', 'reversed', by default 'True'
    yaxis_nticks : bool or int, optional
        Specifies the maximum number of ticks for the particular axis.
        The actual number of ticks will be chosen automatically to be
        less than or equal to `nticks`. Has an effect only if
        `tickmode` is set to "auto". By default None
    xaxis_nticks : [type], optional
        Specifies the maximum number of ticks for the particular axis.
        The actual number of ticks will be chosen automatically to be
        less than or equal to `nticks`. Has an effect only if
        `tickmode` is set to "auto". By default None
    yaxis_showgrid : bool, optional
        Determines whether or not grid lines are drawn.
        If 'True', the grid lines are drawn at every
        tick mark. By default True
    xaxis_showgrid : bool, optional
            Determines whether or not grid lines are drawn.
        If 'True', the grid lines are drawn at every
        tick mark. By default False
    yaxis_zeroline : bool, optional
        Determines whether or not a line is drawn at along the 0 value of
        this axis. If "True", the zero line is drawn on top of the grid
        lines. By default True
    xaxis_zeroline : bool, optional
        Determines whether or not a line is drawn at along the 0 value of
        this axis. If "True", the zero line is drawn on top of the grid
        lines. By default True
    yaxis_showline : bool, optional
        Determines whether or not a line bounding this axis is drawn,
        by default False
    xaxis_showline : bool, optional
        Determines whether or not a line bounding this axis is drawn,
        by default False
    yaxis_tickangle : int, optional
        Sets the angle of the tick labels with respect to the horizontal.
        For example, a `tickangle` of -90 draws the tick labels vertically.
        By default 'auto
    xaxis_tickangle : int, optional
        Sets the angle of the tick labels with respect to the horizontal.
        For example, a `tickangle` of -90 draws the tick labels vertically.
        By default 'auto
    yaxis_titlesize : int, optional
        Sets the title size on the y-axis, by default 18
    xaxis_titlesize : int, optional
        Sets the title size on the x-axis, by default 18
    yaxis_ticksize : int, optional
        Sets the ticksize on the y-axis, by default 13
    xaxis_ticksize : int, optional
        Sets the ticksize on the x-axis, by default 13
    yaxis_tickmode : str, optional
        Sets the tick mode for this axis.
        options: 'auto', 'linear', 'array', by default 'auto'
        If 'auto', the number of ticks is set via `nticks`. If "linear",
        the placement of the ticks is determined by a starting position
        `tick0` and a tick step `dtick` ('linear' is the default value if
        `tick0` and `dtick` are provided). If 'array', the placement of
        the ticks is set via `tickvals` and the tick text is `ticktext`.
        ('array' is the default value if `tickvals` is provided).
    xaxis_tickmode : str, optional
        Sets the tick mode for this axis.
        options: 'auto', 'linear', 'array', by default 'auto'
        If 'auto', the number of ticks is set via `nticks`. If "linear",
        the placement of the ticks is determined by a starting position
        `tick0` and a tick step `dtick` ('linear' is the default value if
        `tick0` and `dtick` are provided). If 'array', the placement of
        the ticks is set via `tickvals` and the tick text is `ticktext`.
        ('array' is the default value if `tickvals` is provided).
    yaxis_tickvals : list, numpy array, or Pandas series, optional
        Sets the values at which ticks on this axis appear.
        Only has an effect if `tickmode` is set to "array".
        Used with `ticktext`. By default None
    xaxis_tickvals : list, numpy array, or Pandas series, optional
        Sets the values at which ticks on this axis appear.
        Only has an effect if `tickmode` is set to "array".
        Used with `ticktext`. By default None
    yaxis_ticktext : list, numpy array, or Pandas series, optional
        Sets the text displayed at the ticks position via `tickvals`.
        Only has an effect if `tickmode` is set to "array".
        Used with `tickvals`. By default None
    xaxis_ticktext : list, numpy array, or Pandas series, optional
        Sets the text displayed at the ticks position via `tickvals`.
        Only has an effect if `tickmode` is set to "array".
        Used with `tickvals`. By default None
    yaxis_tick0 : int, optional
        Sets the placement of the first tick on this axis. Use with `dtick`.
        If the axis `type` is "log", then you must take the log of your
        starting tick (e.g. to set the starting tick to 100, set the `tick0`
        to 2) except when `dtick`="L<f>" (see `dtick` for more info).
        If the axis `type` is "date", it should be a date string, like
        date data. If the axis `type` is "category", it should be a number,
        using the scale where each category is assigned a serial number
        from zero in the order it appears. By default None
    xaxis_tick0 : int, optional
        Sets the placement of the first tick on this axis. Use with `dtick`.
        If the axis `type` is "log", then you must take the log of your
        starting tick (e.g. to set the starting tick to 100, set the `tick0`
        to 2) except when `dtick`="L<f>" (see `dtick` for more info).
        If the axis `type` is "date", it should be a date string, like
        date data. If the axis `type` is "category", it should be a number,
        using the scale where each category is assigned a serial number
        from zero in the order it appears. By default None
    yaxis_tickformat : str, optional
        Sets the tick label formatting rule using d3 formatting.
        options:
            percent: '%'
            percent and decimals: ',.x%'
            thousand-separator: ',.xf'
        By default ''
    xaxis_tickformat : str, optional
        Sets the tick label formatting rule using d3 formatting.
        options:
            percent: '%'
            percent and decimals: ',.x%'
            thousand-separator: ',.xf'
        By default ''
    yaxis_dtick : int, optional
        Sets the step in-between ticks on this axis. Use with `tick0`.
        Must be a positive number, or special strings available to "log"
        and "date" axes. If the axis `type` is "log", then ticks are set
        every 10^(n"dtick) where n is the tick number. For example, to set
        a tick mark at 1, 10, 100, 1000, ... set dtick to 1. To set tick
        marks at 1, 100, 10000, ... set dtick to 2. By default 1
    xaxis_dtick : int, optional
        Sets the step in-between ticks on this axis. Use with `tick0`.
        Must be a positive number, or special strings available to "log"
        and "date" axes. If the axis `type` is "log", then ticks are set
        every 10^(n"dtick) where n is the tick number. For example, to set
        a tick mark at 1, 10, 100, 1000, ... set dtick to 1. To set tick
        marks at 1, 100, 10000, ... set dtick to 2. By default 1
    yaxis_ticks : str, optional
        Determines whether ticks are drawn or not.
        Options: '', 'outside', 'inside'
        If '', this axis' ticks are not drawn. If 'outside'
        ('inside'), this axis' are drawn outside (inside) the axis
        lines. By default ''
    xaxis_ticks : str, optional
        Determines whether ticks are drawn or not.
        Options: '', 'outside', 'inside'
        If '', this axis' ticks are not drawn. If 'outside'
        ('inside'), this axis' are drawn outside (inside) the axis
        lines. By default ''
    yaxis_showticklabels : bool, optional
        Determines whether or not the tick labels are drawn., by default True
    xaxis_showticklabels : bool, optional
        Determines whether or not the tick labels are drawn., by default True
    yaxis_range :  (list[min:max] or None), optional
        y-axis values, by default None
    xaxis_range :  (list[min:max] or None), optional
        x-axis values, by default None
    yaxis_separatethousands : bool, optional
        If "True", even 4-digit integers are separated
        By default True
    xaxis_separatethousands : bool, optional
        If "True", even 4-digit integers are separated
        By default True
    legend_fontfamily : str, optional
        legend font-family, by default 'sans-serif'
    legend_fontsize : int, optional
        legend font-size, by default 12
    legend_fontcolor : str, optional
        legend font-color, by default 'lightgrey'
    legend_orientation : str, optional
        legend orientation, by default 'v'
    legend_x : float, optional
        Sets the x position (in normalized coordinates) of the legend.
        By default 1.02
    legend_xanchor : str, optional
        Sets the legend's horizontal position anchor. This anchor binds
        the `x` position to the "left", "center" or "right" of the legend.
        Value 'auto' anchors legends to the right for `x` values greater
        than or equal to 2/3, anchors legends to the left for `x`
        values less than or equal to 1/3 and anchors legends with
        respect to their center otherwise.
        Options: 'auto', 'left', 'center', 'right', by default 'left'
    legend_y : int, optional
        Sets the y position (in normalized coordinates) of the legend.
        By default 1
    legend_yanchor : str, optional
        Sets the legend's vertical position anchor This anchor binds the
        `y` position to the "top", "middle" or "bottom" of the legend.
        Value "auto" anchors legends at their bottom for `y` values less
        than or equal to 1/3, anchors legends to at their top for `y`
        values greater than or equal to 2/3 and anchors legends with
        respect to their middle otherwise.
        Options: 'top', 'bottom', 'middle', 'auto', by default 'middle'
    legend_traceorder : str, optional
        Determines the order at which the legend items are displayed.
        options: any combination of 'reversed', 'grouped' joined with
        a '+' or 'normal'. By default 'normal'
    legend_bordercolor : str, optional
        Legend border color, by default '#202534'
    showlegend : bool, optional
        If True, legend is shown. If False, legend is not shown.
        By default True
    legend_borderwidth : int, optional
        legend border width, by default 0
    legend_itemclick : str, optional
        Determines the behavior on legend item click.
        Options: 'toggle', 'toggleothers', 'False', by default 'toggle'
    legend_itemdoubleclick : str, optional
        Determines the behavior on legend item double-click.
        Options: 'toggle', 'toggleothers', 'False',
        by default 'toggleothers'
    legend_valign : str, optional
        Sets the vertical alignment of the symbols with respect
        to their associated text.
        Options: 'top', 'middle', 'bottom', by default 'middle'
    color_palette : list, optional
        Color palette to use on traces. If no
        palette is provided Plotly uses a default
        palette. By default None

    EXAMPLES:
        Tickmode - array:
            tickmode = 'array',
            tickvals = [1, 3, 5, 7, 9, 11],
            ticktext = ['One', 'Three', 'Five', 'Seven', 'Nine', 'Eleven']
        Tickmode - linear:
            tickmode = 'linear',
            tick0 = 0.5,
            dtick = 0.75
        Tickformat
            integer: ',.0f',
            float: ',.xf' <-- insert number of decimals for x
            percent: ',.x%' <-- insert number of decimals for x

    """

    return dict(
        showlegend=showlegend,
        autosize=True,
        colorway=color_palette,
        height=height,
        width=width,
        plot_bgcolor=bg_color,
        paper_bgcolor=bg_color,
        margin=dict(l=ml, r=mr, b=mb, t=mt, pad=pad),
        title=dict(text=title, x=title_alignment),
        titlefont=dict(size=title_size,
                       color=title_color,
                       family=title_font_family),

        yaxis=dict(
            type=yaxis_type,
            range=yaxis_range,
            autorange=yaxis_autorange,
            showgrid=yaxis_showgrid,
            zeroline=yaxis_zeroline,
            zerolinecolor=zeroline_color,
            showline=yaxis_showline,
            showticklabels=yaxis_showticklabels,
            ticks=yaxis_ticks,
            tickmode=yaxis_tickmode,
            tickvals=yaxis_tickvals,
            ticktext=yaxis_ticktext,
            nticks=yaxis_nticks,
            tick0=yaxis_tick0,
            dtick=yaxis_dtick,
            gridwidth=grid_width,
            gridcolor=grid_color,
            tickformat=yaxis_tickformat,
            tickangle=yaxis_tickangle,
            title=y_title,
            color=axis_color,
            separatethousands=yaxis_separatethousands,
            titlefont=dict(
                size=yaxis_titlesize,
                color=axis_titlecolor,
                family=axis_fontfamily),
            tickfont=dict(
                size=yaxis_ticksize,
                color=tick_color)),

        xaxis=dict(
            type=xaxis_type,
            range=xaxis_range,
            autorange=xaxis_autorange,
            title=x_title,
            showticklabels=xaxis_showticklabels,
            ticks=xaxis_ticks,
            tickmode=xaxis_tickmode,
            tickvals=xaxis_tickvals,
            ticktext=xaxis_ticktext,
            nticks=xaxis_nticks,
            tick0=yaxis_tick0,
            dtick=xaxis_dtick,
            showgrid=xaxis_showgrid,
            zeroline=xaxis_zeroline,
            zerolinecolor=zeroline_color,
            showline=xaxis_showline,
            tickangle=xaxis_tickangle,
            tickformat=xaxis_tickformat,
            color=axis_color,
            separatethousands=xaxis_separatethousands,
            gridwidth=grid_width,
            gridcolor=grid_color,
            titlefont=dict(
                size=xaxis_titlesize,
                color=axis_titlecolor,
                family=axis_fontfamily),
            tickfont=dict(
                size=xaxis_ticksize,
                color=tick_color)),

        legend=dict(
            font=dict(
                family=legend_fontfamily,
                size=legend_fontsize,
                color=legend_fontcolor),
            valign=legend_valign,
            bordercolor=legend_bordercolor,
            borderwidth=legend_borderwidth,
            orientation=legend_orientation,
            traceorder=legend_traceorder,
            itemclick=legend_itemclick,
            itemdoubleclick=legend_itemdoubleclick,
            x=legend_x,
            xanchor=legend_xanchor,
            y=legend_y,
            yanchor=legend_yanchor)
    )
