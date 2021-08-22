import seaborn as sns


def chart_colors(
        palette_type='xkcd',
        color=None,
        n_colors=10,
        start_pos=None,
        end_pos=None,
        step=None,
        desat=None,
        input_type='rgb',
        reverse=False):
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
    kwargs = dict(color=color, n_colors=n_colors,
                  input=input_type, reverse=reverse)

    if palette_type == 'palette':
        return sns.color_palette(
            palette=color, n_colors=n_colors,
            desat=None).as_hex()[slce]

    elif palette_type == 'light':
        return sns.light_palette(**kwargs).as_hex()[slce]

    elif palette_type == 'dark':
        return sns.dark_palette(**kwargs).as_hex()[slce]

    elif palette_type == 'xkcd':
        if isinstance(color, str):
            color = [color, ]
        return sns.xkcd_palette(color).as_hex()

    else:
        raise ValueError((f'Chosen palette_type {palette_type} not'
                          ' available. Select between `color_palette`,'
                          ' `light`, `dark` and `xkcd`'))
