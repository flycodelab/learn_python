def merge_string(*text_list):
    result = ''
    for s in text_list:
        result = result + s
    return result

print(merge_string('아버지가', '방에', '들어가신다'))

