def get_dict_from_json(data: str):
    """
    Convert JSON to dictionary
    :param data: JSON string form API response
    :return: a dictionary that contains the data
    """

    import json

    data = json.loads(data)
    return data

