import os, sys, requests, json


def api_validator(api_endpoint: str):
    """
    :param api_endpoint:
    :return url string as valid: str
    """
    return api_endpoint


def caller_api(request_header: dict, request_body: dict):
    """
    Default function which will handle API calls independently through used params
    :param request_header: dict
    :param request_body: dict
    :return json object
    """
    url = api_validator('test string')
    if not request_header and not request_body:
        return {'Invalid request'}
    try:
        raw_response = requests.get(url, headers=request_header, data=request_body)
    except Exception as api_caller_error:
        print(f'Exception has happened at handler function for API call: \n\t=> {api_caller_error.args}')
    finally:
        print('Process continued with false-positive response')
    status_code = raw_response.status_code
    response_data = json.dumps(raw_response)        # Fix: Later will add more action to serialise json object data.

    return response_data, status_code


def response_validator_generator(response_data: dict, sort_keys: []):
    """
     :param response_data: Getting dict object from json data structure from response
     :param sort_keys Keys to be look into data as str
     :return string operation & data class
    """
    if not response_data:
        return {'Empty response or response is not valid'}
    try:
        if not sort_keys:
            return None
        data_obj = sort_keys[::-1]
    except Exception as response_validator_generator_error:
        print(f'Exception has happened at handler function for API call: \n\t=>{response_validator_generator_error.args}')





