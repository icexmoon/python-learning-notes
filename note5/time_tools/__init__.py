#__init__.py
#比较两个时间戳大小
__all__=["date","time"]
def compareTimestamp(time1,time2):
    if time1>time2:
        return 1
    elif time1==time2:
        return 0
    else:
        return -1