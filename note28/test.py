from sf_carrier import SFCarrier
from carrier import Carrier
carrier3 = SFCarrier()
print(isinstance(carrier3, Carrier))
print(issubclass(SFCarrier, Carrier))
# False
# False