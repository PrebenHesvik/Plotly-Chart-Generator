======================
Plotly Chart Generator
======================
.. image:: https://img.shields.io/pypi/l/plotly_chart_generator   :alt: PyPI - License

Description
-----------
This package allows the user to quickly generate plotly charts with customized
styling and formatting from Pandas dataframes and other data structures with as
little as one line of code.

The following chart types can be created:

* Bar charts (from dataframe)
* Line charts (from dataframe)
* Scatter charts (from dictionary)
* Pie charts (from lists, numpy arrays, Pandas series)
* Histograms (from lists, numpy arrays, Pandas series)
* Dot charts (from dataframe)
* Box charts (from lists, numpy arrays, Pandas series)
* Sunburst charts (from lists, numpy arrays, Pandas series)
* Scatter charts subplots (from dictionary)
* Pie chats subplots (from dictionary)

Chart examples are available at https://github.com/PrebenHesvik/Plotly-Chart-Generator


Installation
------------

.. code:: python

    pip install plotly_chart_generator

Usage
-----
.. code:: python

    from plotly_chart_generator import PlotlyChart
    chart = PlotlyChart()

    # create data
    index = ['Product A', 'Product B', 'Product C']
    values = {'Products': [37.5, 40.2, 27.8]}
    data = pd.DataFrame(data=values, index=index).transpose()


    # create chart
    color_palette = chart.color_palette()

    layout = chart.layout(color_palette=color_palette, width=500, height=400,
                        title='Sales per product (millions)',
                        title_size=16, xaxis_ticksize=14)

    chart.bar(data, layout=layout, orientation='v', sort_by='Products',
                ascending=False, bar_width=0.4, textpos='inside', linewidth=1)

Disclaimer
----------
Most of the descriptions of arguments have been copied form the Plotly Figure
Reference Guide at https://plotly.com/python/reference/