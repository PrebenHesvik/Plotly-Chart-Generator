__version__ = '0.1.0'

import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly as py
import numpy as np
import seaborn as sns
import pandas as pd


class PlotlyChart():

    def __init__(self, iplot):
        self.iplot = iplot

    def check_if_dataframe(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError('You must pass a DataFrame.')

    def bar(self, df, layout, orientation='v', bar_width=None,
            opacity=0.9, sort_by=None, ascending=False,
            mode=None, textpos=None, annotations=None,
            shapes=None, linewidth=1, linecolor='#2C3347',
            marker_color=None):
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

        self.check_if_dataframe(df)

        df = self.sort_table(df, sort_by, ascending, orientation)

        traces = []
        if orientation == 'v':
            traces = [go.Bar(x=[str(x) for x in df.columns],
                             y=df.iloc[row],
                             text=df.iloc[row],
                             textposition=textpos,
                             marker=dict(
                                 opacity=opacity,
                                 color=marker_color,
                                 line=dict(
                                     color=linecolor,
                                     width=linewidth)),
                             name=df.iloc[row].name,
                             width=bar_width,
                             orientation=orientation)
                      for row in range(df.index.size)]
        else:
            traces = [go.Bar(x=df.iloc[:, col],
                             y=[str(x) for x in df.index],
                             text=df.iloc[:, col],
                             textposition=textpos,
                             marker=dict(
                                 opacity=opacity,
                                 color=marker_color,
                                 line=dict(
                                     color=linecolor,
                                     width=linewidth)),
                             name=df.columns[col],
                             width=bar_width,
                             orientation=orientation)
                      for col in range(df.columns.size)]

        if annotations:
            layout['annotations'] = annotations

        # initialize figure
        fig = go.Figure(data=traces, layout=layout)

        # update layout to display either stacked/grouped barmode
        fig.update_layout(barmode=mode)

        # update shapes
        if shapes:
            for shape in shapes:
                fig.add_shape(shape)
            fig.update_shapes(dict(xref='x', yref='y'))

        # display chart
        if self.iplot:
            py.offline.iplot(fig)
        else:
            return fig

    def line(self, df, layout, mode='lines', line_width=2,
             marker_size=None, marker_symbol='circle', text=None,
             text_position='bottom center', text_size=14,
             text_color='lightgrey', annotations=None,
             line_smoothing=1.3, marker_color=None,
             line_color=None):
        """Line chart

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

        traces = [go.Scatter(x=df.columns, y=df.loc[row], mode=mode,
                             line=dict(width=line_width.pop(0),
                                       color=line_color,
                                       shape='spline', smoothing=line_smoothing),
                             text=text, name=row, textposition=text_position,
                             textfont=dict(size=text_size, color=text_color),
                             marker=dict(size=marker_size,
                                         symbol=marker_symbol,
                                         color=marker_color,
                                         gradient=dict(type='radial', color=['#2f323d', '#bbbe64'])))
                  for row in df.index]

        if annotations:
            layout['annotations'] = annotations

        # initialize figure
        fig = go.Figure(data=traces, layout=layout)

        return py.offline.iplot(fig) if self.iplot else fig

        # display chart
        if self.iplot:
            py.offline.iplot(fig)
        else:
            return fig

    def scatter(self, data, layout, marker_size=2,
                marker_symbol='circle', text=None,
                text_pos='bottom center', text_size=14,
                text_color='grey'):
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

        traces = [go.Scatter(x=value['x'], y=value['y'], mode='markers',
                             name=key, text=value.get('text', None),
                             textposition=text_pos,
                             textfont=dict(size=text_size),
                             marker=dict(size=marker_size,
                                         symbol=marker_symbol,
                                         color=value.get('colors')))
                  for key, value in data.items()]

        # initialize figure
        fig = go.Figure(data=traces, layout=layout)

        # display chart
        if self.iplot:
            py.offline.iplot(fig)
        else:
            return fig

    def pie(self, labels, values, layout, hole=.3, name='',
            hoverinfo='label+percent', textinfo='value',
            textfont_size=20, linewidth=2, linecolor='#202534',
            pull=[], pull_dist=0.2, titlecolor='lightgrey',
            titlesize=15, title=None, opacity=None, textposition=None):
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
        data = go.Pie(labels=labels, values=values, hole=hole, name=name,
                      title=dict(text=title), textposition=textposition,
                      opacity=opacity, hoverinfo=hoverinfo, textinfo=textinfo,
                      textfont_size=textfont_size, pull=pull,
                      marker=dict(line=dict(color=linecolor, width=linewidth)))

        # Display chart
        fig = go.Figure(data=data, layout=layout)

        # display chart
        if self.iplot:
            py.offline.iplot(fig)
        else:
            return fig

    def hist(self, layout, x=None, y=None, histnorm='percent', orientation='v',
             title='', x_title='', y_title='', name='', opacity=0.9,
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

        """
        traces = go.Histogram(x=x, y=y, histnorm=histnorm,
                              orientation=orientation, histfunc=histfunc,
                              marker=dict(opacity=opacity))

        # initialize figure
        fig = go.Figure(data=traces, layout=layout)

       # display chart
        if self.iplot:
            py.offline.iplot(fig)
        else:
            return fig

    def dot(self, df, layout):
        """Dot plot


        Parameters
        ----------
        df : DataFrame
            Contains the to be charted
        layout : dict
            Chart layout, formatting and styles
        """

        traces = [go.Scatter(x=df.loc[row], y=df.columns,
                             mode='markers', name=row)
                  for row in df.index]

        # initialize figure
        fig = go.Figure(data=traces, layout=layout)
        fig.update_yaxes(tickmode='array', tickvals=[*df.columns])

        # display chart
        if self.iplot:
            py.offline.iplot(fig)
        else:
            return fig

    def box(self, layout, y=None, x=None, boxpoints=False,
            boxmean=True, jitter=0.3, pointpos=-1.5, opacity=0.9):
        """Box plot

        Parameters
        ----------
        y : list, numpy array, pandas series, optional
            Sets the y sample data or coordinates, by default None
        x : list, numpy array, pandas series, optional
            Sets the x sample data or coordinates, by default None
        layout : dict
            Chart layout, formatting and styles
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
            traces = [go.Box(y=values, boxpoints=boxpoints,
                             name=values.name, boxmean=boxmean,
                             jitter=jitter, pointpos=pointpos,
                             opacity=opacity)
                      for values in y]
        else:
            traces = [go.Box(x=values, boxpoints=boxpoints,
                             name=values.name, boxmean=boxmean,
                             jitter=jitter, pointpos=pointpos,
                             opacity=opacity)
                      for values in x]

        # initialize figure
        fig = go.Figure(data=traces, layout=layout)

        # display chart
        if self.iplot:
            py.offline.iplot(fig)
        else:
            return fig

    def sunburst(self, labels, parents, values, layout):
        """Sunburst chart


        Parameters
        ----------
        labels : list, numpy array, or Pandas series
            Sets the labels of each of the sectors
        parents : list, numpy array, or Pandas series
            Sets the parent sectors for each of the sectors. Empty string
            items '' are understood to reference the root node in the
            hierarchy. If `ids` is filled, `parents` items are understood
            to be "ids" themselves. When `ids` is not set, plotly attempts
            to find matching items in `labels`, but beware they must be unique.
        values : list, numpy array, or Pandas series
            Sets the values associated with each of the sectors. Use with
            `branchvalues` to determine how the values are summed.
        layout : dict
            Chart layout, formatting and styles
        """
        data = go.Sunburst(
            labels=labels,
            parents=parents,
            values=values)

        fig = go.Figure(data=data, layout=layout)

        # display chart
        if self.iplot:
            py.offline.iplot(fig)
        else:
            return fig

    def scatter_subplots(self, data, layout, rows, cols, titles):
        """Scatter chart subplots

        Parameters
        ----------
        data : dict
            chart data
        layout : dict
            Chart layout, formatting and styles
        rows : int
            number of chart rows
        cols : int
            number of chart columns
        titles : list
            subplot titles
        """

        fig = make_subplots(rows=rows, cols=cols, subplot_titles=titles)

        col_nums = np.tile([*range(1, cols + 1)], rows)
        row_nums = np.repeat([*range(1, rows + 1)], cols)
        plot_order = list(zip(col_nums, row_nums))

        for key, value in data.items():
            col, row = plot_order.pop(0)
            fig.add_trace(
                go.Scatter(x=value['x'], y=value['y'], mode='markers',
                           text=value['names'], name=key,
                           marker=dict(size=None)),
                row=row.item(), col=col.item())

        # update layout
        fig.update_layout(layout)
        fig.update_yaxes(layout['yaxis'])
        fig.update_xaxes(layout['xaxis'])

        layout['annotations'] = dict(font=dict(size=12, color='lightgrey'))
        for i in fig['layout']['annotations']:
            i['font'] = layout['annotations']['font']

        # display chart
        if self.iplot:
            py.offline.iplot(fig)
        else:
            return fig

    def pie_subplots(self, data, rows, cols, titles,
                     layout, hole=.3, subplot_title_size=15,
                     subplot_title_color='lightgrey', linewidth=5,
                     linecolor='#202534', hoverinfo='label+percent',
                     textinfo='value'):
        """Pie chart subplots


        Parameters
        ----------
        data : dict
            chart data
        rows : int
            number of chart rows
        cols : int
            number of chart columns
        titles : list
            subplot titles
        layout : dict
            Chart layout, formatting and styles
        hole : float, optional
            Sets the fraction of the radius to cut out of the pie.
            Use this to make a donut chart. By default .3
        subplot_title_size : int, optional
            Size of subplot titles, by default 15
        subplot_title_color : str, optional
            color of subplot titles, by default 'lightgrey'
        linewidth : int, optional
            size of line between pieces, by default 5
        linecolor : str, optional
            Color of line around each piece, by default '#202534'
        hoverinfo : str, optional
            Determines which trace information appear on hover.
            Any combination of `label`, `text`, `value`, `percent`, `name`
            joined with a `+` OR `all` or `none` or `skip`.
            By default 'label+percent'
        textinfo : str, optional
            Determines which trace information appear on the graph.
            Any combination of `label`, `text`, `value`, `percent`
            joined with a `+` OR `none`. by default 'value'
        """
        specs = [[{'type': 'domain'}
                  for x in range(0, cols)] for x in range(0, rows)]
        fig = make_subplots(rows=rows, cols=cols,
                            subplot_titles=titles, specs=specs)

        col_nums = np.tile([*range(1, cols + 1)], rows)
        row_nums = np.repeat([*range(1, rows + 1)], cols)
        plot_order = list(zip(col_nums, row_nums))

        for key, value in data.items():
            col, row = plot_order.pop(0)
            fig.add_trace(
                go.Pie(labels=[*value.keys()], values=[*value.values()],
                       name=key, hole=hole, hoverinfo=hoverinfo,
                       textinfo=textinfo, marker=dict(line=dict(
                           color=linecolor, width=linewidth))),
                row=row.item(), col=col.item())

        # update layout
        fig.update_layout(layout)
        layout['annotations'] = dict(font=dict(size=12, color='lightgrey'))
        for i in fig['layout']['annotations']:
            i['font'] = layout['annotations']['font']

        # display chart
        if self.iplot:
            py.offline.iplot(fig)
        else:
            return fig

    @staticmethod
    def layout(title='', title_alignment=0.5, title_color='lightgrey',
               title_font_family='sans-serif', title_size=24, x_title='',
               y_title='', width=None, height=None, ml=75, mr=50, mb=75,
               mt=75, pad=10, bg_color='#202534', grid_color='#3d4152',
               grid_width=0.5, zeroline_color='grey', axis_color='lightgrey',
               axis_fontfamily='sans-serif', axis_titlecolor='lightgrey',
               tick_color='lightgrey', yaxis_type='-', xaxis_type='-',
               yaxis_autorange=True, xaxis_autorange=True,
               yaxis_nticks=None, xaxis_nticks=None, yaxis_showgrid=True,
               xaxis_showgrid=False, yaxis_zeroline=True,
               xaxis_zeroline=False, yaxis_showline=False,
               xaxis_showline=False, yaxis_tickangle=0,
               xaxis_tickangle=0, yaxis_titlesize=18,
               xaxis_titlesize=18, yaxis_ticksize=13, xaxis_ticksize=13,
               yaxis_tickmode='auto', xaxis_tickmode='auto',
               yaxis_tickvals=None, xaxis_tickvals=None, yaxis_ticktext=None,
               xaxis_ticktext=None, yaxis_tick0=None, xaxis_tick0=None,
               yaxis_tickformat='', xaxis_tickformat='', yaxis_dtick=1,
               xaxis_dtick=1, yaxis_ticks='', xaxis_ticks='', yaxis_range=None,
               yaxis_showticklabels=True, xaxis_showticklabels=True,
               xaxis_range=None, yaxis_separatethousands=True,
               xaxis_separatethousands=True, legend_fontfamily='sans-serif',
               legend_fontsize=12, legend_fontcolor='lightgrey',
               legend_orientation='v', legend_x=1, legend_xanchor='left',
               legend_y=1, legend_yanchor='middle', legend_traceorder='normal',
               legend_bordercolor='#202534', showlegend=True,
               legend_borderwidth=0, legend_itemclick='toggle',
               legend_itemdoubleclick='toggleothers', legend_valign='middle',
               color_palette=None, *args, **kwargs):
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
                tickmode=xaxis_tickmode,
                tickvals=xaxis_tickvals,
                ticktext=yaxis_ticktext,
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

    @staticmethod
    def sort_table(df, sort_by, ascending, orientation):
        """Sorts dataframe based on key

        This function does not get called directly by
        the user. Instead it gets called by bar-function.

        Parameters
        ----------
        df : dataframe
        sort_by : str
            Specifies which column to sort by
        ascending : bool
            if True, the table is sorted ascended.
            If False, the table is sorted descended.
        orientation : str
            'v' for vertical, 'h' for horizontal

        Returns
        -------
        dataframe
            sorted dataframe
        """
        if sort_by:
            axis = 1 if orientation == 'v' else 0
            na_pos = 'last' if orientation == 'v' else 'first'
            try:
                df = df.sort_values(sort_by, ascending=ascending,
                                    axis=axis, na_position=na_pos)
            except KeyError:
                print(f'{sort_by} is not a valid name. DataFrame not sorted.')
        return df

    @staticmethod
    def add_headings(df, orientation='h', font_color='lightgrey',
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

    def add_bar_values(self, df, orientation='h', font_size=15,
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
        for i in list(range(0, size)):
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

    @staticmethod
    def add_shape(x0, x1, y0, y1, type='rect', layer='above',
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
        return [go.layout.Shape(
            type=type, xref=xref, yref=yref, x0=x0, y0=y0,
            x1=x1, y1=y1, fillcolor=fill_color, opacity=opacity,
            line=dict(color=line_color, width=line_width,
                      dash=line_style))]

    @staticmethod
    def theme(theme):
        """Quick way to select a light chart theme

        Store the dict as an object and add it as an argument
        to chart.layout by unpacking it.

        Example:
        theme = chart.theme('light)
        layout = chart.layout(**theme)
        chart.bar(df, layout)

        """

        themes = {
            'light': {
                'bg_color': 'lightgrey',
                'title_color': '#202534',
                'axis_titlecolor': '#202534',
                'tick_color': '#202534',
                'grid_color': '#B3B4B4',
                'zeroline_color': 'black',
                'axis_color': '#202534',
                'legend_fontcolor': '#202534',
                'legend_bordercolor': 'lightgrey',
            },
        }
        return themes.get(theme, None)

    @staticmethod
    def color_palette(palette_type='color_palette', palette=None, n_colors=10,
                      start_pos=None, end_pos=None, step=None, desat=None,
                      input_type='rgb', reverse=False):
        """Creates list of hex colors


        This function lets the user use one of the following Seaborn
        library functions: 'color_palette', 'light_palette',
        'dark_palette' or 'xkcd_palette' to generate a list
        of hex-colors to be used in a chart.


        Parameters
        ----------
        palette_type : str, optional
            The type of color palette the user wants to
            generate. Must be one of these: 'color_palette',
            'light', 'dark' or 'xkcd' By default 'color_palette'
        palette : str or list, optional
            colors to include in palette. Look at extended summary
            above for more information. If None is chosen a
            default Seaborn color palette is chosen. By default None
        n_colors : int, optional
            Number of colors in palette, by default 10
        start_pos : int, optional
            Sets new start position to return a palette that
            starts at a different place than the orginial
            Seaborn generated palette. By default None
        end_pos : int, optional
            Sets new end position to retun a palete that
            ends at a different place than the original
            Seaborn generated palette. By default None
        step : int, optional
            The step part of the slice, by default None
        desat : float, optional
            Desaturates the colors, by default None
        input_type : str, optional
            Choose between ‘rgb’, ‘hls’, ‘husl’, ’xkcd’, by default 'rgb'
        reverse : bool, optional
            Reverses the palette, by default False

        Returns
        -------
        list of hex colors

        Raise
        ------
        ValueError
            Value error gets raised if palette_type is not
            among 'color_palette', 'light', 'dark' or
            'xkcd'.


        light_palette/dark_palette colors
        ---------------------------------
        Any of the following color formats are accepted: ‘rgb’,
        ‘hls’, ‘husl’, xkcd’. If a non-rgb color is chosen the
        correct color format must be specified in the input_type
        argument.


        xkcd_palette colors
        -------------------
        Any of the RGB monitor color names.
        Visit https://xkcd.com/color/rgb/ to view a long
        list of colors.

        color_palette colors
        --------------------
        There are six variations of the default theme, called deep,
        muted, pastel, bright, dark, and colorblind. A list of
        hex-colors can also be provided.

        I an addition the following list of keywords can be used:
        'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r',
        'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r',
        'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r',
        'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r',
        'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r',
        'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn',
        'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r',
        'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r',
        'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r',
        'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3',
        'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn',
        'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd',
        'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary',
        'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r',
        'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r',
        'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r',
        'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat',
        'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow',
        'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg',
        'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r',
        'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire',
        'icefire_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma',
        'magma_r', 'mako', 'mako_r', 'nipy_spectral', 'nipy_spectral_r',
        'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r',
        'prism', 'prism_r', 'rainbow', 'rainbow_r', 'rocket', 'rocket_r',
        'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r',
        'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r',
        'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r',
        'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r',
        'vlag', 'vlag_r', 'winter', 'winter_r'

        """

        slce = slice(start_pos, end_pos, step)
        kwargs = dict(color=palette, n_colors=n_colors,
                      input=input_type, reverse=reverse)

        if palette_type == 'color_palette':
            return sns.color_palette(
                palette=palette, n_colors=n_colors,
                desat=None).as_hex()[slce]

        elif palette_type == 'light':
            return sns.light_palette(**kwargs).as_hex()[slce]

        elif palette_type == 'dark':
            return sns.dark_palette(**kwargs).as_hex()[slce]

        elif palette_type == 'xkcd':
            return sns.xkcd_palette(palette).as_hex()

        else:
            raise ValueError((f'Chosen palette_type {palette_type} not'
                              ' available. Select between `color_palette`,'
                              ' `light`, `dark` and `xkcd`'))
