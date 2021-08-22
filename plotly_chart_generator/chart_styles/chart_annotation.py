def chart_annotation(
        x=None,
        y=None,
        xref='x',
        yref='y',
        text='',
        showarrow=True,
        font_family="Courier New, monospace",
        font_size=16,
        font_color='#ffffff',
        align='center',
        arrow_head=2,
        arrow_size=1,
        arrow_color='#636363',
        ax=20,
        ay=-30,
        border_color=None,
        border_width=2,
        border_pad=4,
        bg_color='#ff7f0e',
        opacity=0.8,
        **kwargs):
    return dict(
        x=2,
        y=5,
        xref="x",
        yref="y",
        text="max=5",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
        ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4)