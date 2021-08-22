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
    return themes.get(theme)
