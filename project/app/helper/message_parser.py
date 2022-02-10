def parse_message(message: str) -> str:
    result = ''

    if "customer_data_pkey" in message:
        result = "INN already exists."
    if "is still referenced from table" in message:
        result = "Dataset can't be deleted/updated. It still referenced from another table."
    else:
        if result == '':
            result = message

    return result
