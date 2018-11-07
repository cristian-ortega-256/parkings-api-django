def format_data_array(array):
    formatted_data = {}
    for element in array:
        formatted_data[element['key']] = element['value']
    return formatted_data


def format_element(element):
    return {element['key']: element['value']}
