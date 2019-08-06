class Customer:

    def __init__(self,name,age):
        print('constructor 1')
    def __init__(self,name,age,mob):
        print('Constructor 2')
# Here we dont have constructor overloading

obj = Customer('Test',25,555)
obj2 = Customer('Test2',55,456531325)

# def __init__(self,a):
#     print('This is Constructor', a)
#
# def testmethod():
#     print('Test method 1')
# def testmethod2():
#     print('Test method 2')
# def testmethod3():
#     print(__name__)
#
# if __name__ == '__main__':
#  testmethod()
#  testmethod2()
# testmethod3()