from functools import wraps
from user_exception import UserException
from flask import redirect


def excetpionDeal(webRouteFunc):
    @wraps(webRouteFunc)
    def exceptionWrap(*params, **kvParams):
        try:
            return webRouteFunc()
        except UserException as e:
            with open(file='error.log', mode='a', encoding='UTF-8') as errorLogOpen:
                print(e.getErrorCode(), ':',
                      e.getErrorMessage(), file=errorLogOpen)
            return redirect('/showError/系统出错，请联系管理员/3')
        except Exception as e:
            with open(file='error.log', mode='a', encoding='UTF-8') as errorLogOpen:
                print(e, file=errorLogOpen)
            return redirect('/showError/系统出错，请联系管理员/3')
    return exceptionWrap
