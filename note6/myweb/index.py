from flask import Flask, render_template, request
web = Flask(__name__)


@web.route('/')
def index() -> 'html':
    """展示一个字符串匹配的查询页面"""
    return render_template("entry.html", the_title="字符串匹配")


@web.route("/results", methods=["POST"])
def results() -> 'html':
    """展示一个结果页面"""
    string = request.form['phrase']
    search = request.form['letters']
    results = set(string).intersection(set(search))
    return render_template("results.html", the_phrase=string, the_letters=search, the_results=str(results))


web.run(debug=True)
