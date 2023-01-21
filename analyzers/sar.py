
import math

import pandas
import pandas as pd
from talib import abstract




class SAR():
    def analyze(self,high,low):

        result = abstract.SAR(high,low,acceleration=0.02, maximum=0.2)
        results = pd.DataFrame(result, columns=['sar'])

        return results
