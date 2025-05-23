import json


def get_previous_conversation(filepath):
    if not filepath:
        print('File does not exist')
    try:
        with open(filepath, 'r') as conversation_data_object:
            data = conversation_data_object.read()
            # print(f'data==>\t{data}')
            return data
    except Exception as conversation_data_object_error:
        print(f'Exception has happened at\t --{__name__}-==>\t{conversation_data_object_error.args}')
        return []


def data_operation_recursion(data_object, fetched_key):
    get_data = ''
    if not data_object:
        print(f'Data is malformed')
        return []

    raw_data = json.loads(data_object)
    result = []
    for item in raw_data:
        tag = "Action" if item['type'] == fetched_key else "Non-action"
        print(f'{tag} data==>{item["content"]}')
        result.append(item["content"])

    print(f'result==>\t{result}')
    return result


if __name__ == '__main__':
    file_pth = '../agent_memory.json'
    raw_data = get_previous_conversation(file_pth)
    action_data = data_operation_recursion(raw_data, 'action')

