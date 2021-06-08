from flask import Flask, render_template, request, redirect, session
from mydb2 import MyDB2
from login_check import loginCheck
from user_exception import UserException
from exception_deal import excetpionDeal
web = Flask(__name__)
web.secret_key = "sfdfjk@.sfdsf"


def writeLog(logInfo: dict) -> None:
    with MyDB2() as cursor:
        _SQL = '''INSERT INTO LOG (phrase,letters,ip,browser_string,results)
                VALUES (%s,%s,%s,%s,%s)'''
        params = (logInfo['formData']['phrase'], logInfo['formData']
                ['letters'], logInfo['userIp'], logInfo['userAgent'], logInfo['results'])
        cursor.execute(_SQL, params)


def getLog() -> list:
    lines = []
    results = []
    with MyDB2() as cursor:
        _SQL = '''SELECT * FROM LOG'''
        cursor.execute(_SQL)
        results = cursor.fetchall()
    for logInfo in results:
        lines.append(
            [logInfo[4], logInfo[3], logInfo[1], logInfo[2], logInfo[5]])
    return lines


@web.route('/')
@excetpionDeal
def index() -> 'html':
    """展示一个字符串匹配的查询页面"""
    return render_template("entry.html", the_title="字符串匹配")


@web.route('/log')
@excetpionDeal
@loginCheck
def showLog() -> 'html':
    """展示日志页面"""
    logList = getLog()
    return render_template("log.html", the_title="服务器日志", log_list=logList)


@web.route("/results", methods=["POST"])
@excetpionDeal
def results() -> 'html':
    """展示一个结果页面"""
    userAgent = request.user_agent
    remoteAddr = request.remote_addr
    formData = request.form
    string = request.form['phrase']
    search = request.form['letters']
    results = set(string).intersection(set(search))
    logInfo = {"userAgent": str(userAgent), "userIp": str(
        remoteAddr), "formData": formData, "results": str(results)}
    writeLog(logInfo)
    return render_template("results.html", the_phrase=string, the_letters=search, the_results=str(results))


@web.route("/showRegist", methods=["GET"])
@excetpionDeal
def showRegist():
    '''用户注册页面'''
    return render_template("regist.html")


@web.route("/doRegist", methods=["POST"])
@excetpionDeal
def doRegist():
    '''注册用户'''
    name = request.form['name']
    password = request.form['password']
    redirectUrl = ''
    with MyDB2() as cursor:
        _SQL = '''SELECT * FROM user
WHERE name=%s LIMIT 1'''
        cursor.execute(_SQL, (name,))
        users = cursor.fetchall()
        if len(users) > 0:
            # 已存在同名用户
            redirectUrl = "/showError/already has same user/1"
        else:
            # 注册用户
            _SQL = '''INSERT INTO `myweb`.`user` (`name`, `password`) VALUES (%s, %s); '''
            params = (name, password)
            cursor.execute(_SQL, params)
            redirectUrl = '/'
    if redirectUrl != '':
        return redirect(redirectUrl)


@web.route("/showError/<msg>/<type>", methods=["GET"])
def showError(msg, type):
    '''错误显示页面'''
    if type == 1:
        url = '/showRegist'
    elif type == 2:
        url = '/login'
    elif type == 3:
        url = '/'
    else:
        url = '/showRegist'
    return render_template('error.html', msg=msg, url=url)


@web.route("/login", methods=["GET"])
@excetpionDeal
def login():
    '''登录页面'''
    return render_template('login.html')


@web.route("/logout", methods=["GET"])
@excetpionDeal
def logout():
    '''登出'''
    session['uid'] = 0
    session['name'] = ''
    return redirect('/login')


@web.route('/doLogin', methods=["POST"])
@excetpionDeal
def doLogin():
    '''执行登录逻辑'''
    name = request.form['name']
    password = request.form['password']
    checkResult = checkUserPassword(name, password)
    if not checkUserPassword:
        return redirect('/showError/password is error/2')
    # 登录成功，写入session
    session['uid'] = checkResult['uid']
    session['name'] = checkResult['name']
    return redirect('/')


def checkUserPassword(user, password):
    with MyDB2() as cursor:
        _SQL = '''SELECT * FROM USER
WHERE NAME=%s LIMIT 1;'''
        params = (user,)
        cursor.execute(_SQL, params)
        users = cursor.fetchall()
    if len(users) == 0:
        return False
    realPassword = users[0][2]
    if password != realPassword:
        return False
    user = users[0]
    userInfo = {'name': user[1], 'uid': user[0]}
    return userInfo


web.run(debug=True)
