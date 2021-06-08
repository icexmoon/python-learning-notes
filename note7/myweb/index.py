from flask import Flask, render_template, request
web = Flask(__name__)


def writeLog(logInfo: list) -> None:
    with open(file="http.log", mode="a") as fopen:
        logStr = "|".join(logInfo)
        print(logStr, file=fopen)


def getLog() -> list:
    lines = []
    with open(file="http.log", mode="r") as fopen:
        for line in fopen:
            lines.append(line.split("|"))
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
    logInfo = [str(userAgent), str(remoteAddr), str(formData), str(results)]
    writeLog(logInfo)
    return render_template("results.html", the_phrase=string, the_letters=search, the_results=str(results))


web.run(debug=True)
