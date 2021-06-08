from functools import wraps
def wrapContent(contentFunc):
    @wraps(contentFunc)
    def wrapContentFunc(*params,**vkParams):
        print("this is a before action")
        beforeReturn = [1,2,3]
        vkParams['beforeReturn'] = beforeReturn
        contentFunc(*params,**vkParams)
        print("this is a after action")
    return wrapContentFunc

@wrapContent
def contentFunc(beforeReturn):
    print("this is a content")
    print(beforeReturn)

contentFunc()
# this is a before action
# this is a content
# [1, 2, 3]
# this is a after action