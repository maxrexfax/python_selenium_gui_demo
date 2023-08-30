def get_env(name):
    if name == 'main_url':
        return 'https://duckduckgo.com/'

    # If an exact match is not confirmed, this last case will be used if provided
    else:
        return 'error'
