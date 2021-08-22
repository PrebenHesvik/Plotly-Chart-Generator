import plotly.graph_objs as go


def dot_chart(df):
    """Dot plot


    Parameters
    ----------
    df : DataFrame
        Contains the data to be charted
    """

    traces = []
    for row in df.index:
        trace = go.Scatter(
            x=df.loc[row],
            y=df.columns,
            mode='markers',
            name=row)

        traces.append(trace)

    return traces

    # # initialize figure
    # fig = go.Figure(data=traces, layout=layout)
    # fig.update_yaxes(tickmode='array', tickvals=[*df.columns])
