import plotly.graph_objs as go


def sunburst_chart(labels, parents, values):
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
    """
    return go.Sunburst(
        labels=labels,
        parents=parents,
        values=values)
