def load_config():
    """
    Load configuration settings from the config.yaml file.
    Returns:
        dict: A dictionary containing the configuration settings.
    """
    import yaml

    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    return config