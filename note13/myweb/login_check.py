from flask import session, redirect
from functools import wraps


def isLogged():
    '''判断当前是否登录状态'''
    if not 'uid' in session:
        return False
    uid = int(session['uid'])
    if uid <= 0:
        return False
    return True


def loginCheck(webRoute):
    '''函数修饰符，用于给webroute增加登录检查'''
    @wraps(webRoute)
    def loginCheckWebRoute(*params, **kvParams):
        if not isLogged():
            return redirect('/login')
        return webRoute(*params, **kvParams)
    return loginCheckWebRoute
