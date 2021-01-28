def myFunction(arg1, arg2, *args, **kwargs):
    print("arg1 : ", arg1)
    print("arg2 : ", arg2)

    print("args : ", args)
    print("args type : ", type(args))

    print("kwargs : ", kwargs)
    print("kwargs : ", type(kwargs))
    return arg1 + arg2


if __name__ == "__main__":

    myFunction(1, 2, 3, 4, 5, 6, 7, 8, 9, what=False, why=True, Hello="Hello world!")

"""
[출력 결과]
arg1 :  1
arg2 :  2
args :  (3, 4, 5, 6, 7, 8, 9)
args type :  <class 'tuple'>
kwargs :  {'what': False, 'why': True, 'Hello': 'Hello world!'}
kwargs :  <class 'dict'>
"""
