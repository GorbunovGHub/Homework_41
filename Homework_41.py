import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)

    def methods():
        return methods.__dir__()

    module = obj.__class__.__module__
    function = inspect.getmembers(obj, inspect.isfunction)

    my_dict = {'type': obj_type, 'attributes': attributes, 'methods': methods(), 'module': module,
               'function': inspect}
    return my_dict


number_info = introspection_info(42)
print(number_info)
print('* * * * * * * * * * * * * * * * ')
string_info = introspection_info('Urban')
print(string_info)
