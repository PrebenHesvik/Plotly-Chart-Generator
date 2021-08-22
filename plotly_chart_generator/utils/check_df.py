def check_dataframe_shape(df, orientation):
    if orientation == 'v':
        if df.shape[0] > df.shape[1]:
            raise ValueError(
                'Transpose your dataframe or change orientation to `h`.')

    elif orientation == 'h':
        if df.shape[0] < df.shape[1]:
            raise ValueError(
                'Transpose your dataframe or change orientation to `v`.')
