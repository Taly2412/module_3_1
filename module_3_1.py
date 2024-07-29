calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    string = str(string).lower()
    list_to_search = list(list_to_search)
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


print(string_info('воздух'))
print(string_info('Leningrad'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBaN']))
print(is_contains('ягода', ['малина', 'неягода', 'погода']))

print(calls)
