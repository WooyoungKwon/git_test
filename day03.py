class OopsException(Exception):
    print('Caught an oops')


try:
    raise OopsException()
except OopsException as exc:
    print(exc)
