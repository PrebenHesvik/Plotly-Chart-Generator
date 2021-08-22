import plotly.graph_objs as go
import plotly as py


def display_chart(
        traces,
        layout,
        annotations=None,
        shapes=None,
        mode=None,
        iplot=True,
        **kwargs):

    # initialize figure
    fig = go.Figure(data=traces, layout=layout)

    # update layout to display either stacked/grouped barmode
    if mode:
        fig.update_layout(barmode=mode)

    # add annotations
    if annotations:
        for annotation in annotations:
            fig.add_annotation(**annotation)

    # update shapes
    if shapes:
        for shape in shapes:
            fig.add_shape(shape)
        fig.update_shapes(dict(xref='x', yref='y'))

    if iplot:
        return py.offline.iplot(fig)
    else:
        return fig


# class Chart:
#     def __init__(self, iplot=True):
#         self.iplot = iplot

#     def display(
#             self,
#             traces,
#             layout,
#             annotations=None,
#             shapes=None,
#             mode=None,
#             **kwargs):

#         # initialize figure
#         fig = go.Figure(data=traces, layout=layout)

#         # update layout to display either stacked/grouped barmode
#         if mode:
#             fig.update_layout(barmode=mode)

#         # add annotations
#         if annotations:
#             for annotation in annotations:
#                 fig.add_annotation(**annotation)

#         # update shapes
#         if shapes:
#             for shape in shapes:
#                 fig.add_shape(shape)
#             fig.update_shapes(dict(xref='x', yref='y'))

#         if self.iplot:
#             return py.offline.iplot(fig)
#         else:
#             return fig
