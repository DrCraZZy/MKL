def parse_message(message: str) -> str:
    result = ''

    if "customer_data_pkey" in message:
        print(message)
        result = f"INN already exists."
    else:
        if result == '':
            result = message

    return result
