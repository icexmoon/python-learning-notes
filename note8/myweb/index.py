from flask import Flask, render_template, request
from mydb import MyDB
web = Flask(__name__)


def writeLog(logInfo: dict) -> None:
    _SQL = '''INSERT INTO LOG (phrase,letters,ip,browser_string,results)
            VALUES (%s,%s,%s,%s,%s)'''
    params = (logInfo['formData']['phrase'], logInfo['formData']
              ['letters'], logInfo['userIp'], logInfo['userAgent'], logInfo['results'])
    db = MyDB()
    db.executeSQL(_SQL, params)


def getLog() -> list:
    lines = []
    # with open(file="http.log", mode="r") as fopen:
    #     for line in fopen:
    #         lines.append(line.split("|"))
    db = MyDB()
    _SQL = '''SELECT * FROM LOG'''
    results = db.executeSQL(_SQL, tuple())
    # with open(file='myweb.log', mode='a') as fopen:
    #     print(results, file=fopen)
    for logInfo in results:
        lines.append([logInfo[4],logInfo[3],logInfo[1],logInfo[2],logInfo[5]])
    return lines


@web.route('/')
def index() -> 'html':
    """展示一个字符串匹配的查询页面"""
    return render_template("entry.html", the_title="字符串匹配")


@web.route('/log')
def showLog() -> 'html':
    """展示日志页面"""
    logList = getLog()
    return render_template("log.html", the_title="服务器日志", log_list=logList)


@web.route("/results", methods=["POST"])
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


web.run(debug=True)
