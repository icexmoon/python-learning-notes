# class AggregateClass(ParentClass,Exp1Mixin,Exp2Mixin,Exp3Mixin):
#     '''这是一个将主体ParentClass和混入Exp1,Exp2,Exp3捏合在一起的聚合类'''
#     pass
from pkg.D import D
d = D()
d.showMe()
# A's showMe is called
# D's showMe is called
from pkg.A import A
A.showMe(d)
# A's showMe is called