from unittest import result

from test import get_data
from analyzers import adx


pairs=['BTC-USDT','ETH-USDT','ADA-USDT','AXS-USDT','SOL-USDT','IOST-USDT','FLOW-USDT','IOTX-USDT','XMR-USDT','ETC-USDT','XTZ-USDT'
        ,'EGLD-USDT','SAND-USDT','BNB-USDT','ADA-USDT','XRP-USDT','CAKE-USDT','DOGE-USDT','DOT-USDT','AVAX-USDT','MATIC-USDT'
        ,'ALGO-USDT','ICP-USDT','VET-USDT','AAVE-USDT','AXS-USDT','UNI-USDT','FIL-USDT','SHIB-USDT','EOS-USDT','KCS-USDT'
        ,'NEAR-USDT','LTC-USDT','ATOM-USDT','LINK-USDT','BCH-USDT','TRX-USDT','XLM-USDT','MANA-USDT','HBAR-USDT','APE-USDT','FTM-USDT','GRT-USDT'
        ,'THETA-USDT','MKR-USDT']
for pair in pairs:
    ohlc = get_data(pair)
    results = adx.analyze(ohlc,14)

    dmi_count = results.shape[0]-1

    pdi1 = results.pdi[dmi_count]
    ndi1= results.ndi[dmi_count]
    adx1 = results.adx[dmi_count]

    pdi2 = results.pdi[dmi_count-1]
    ndi2 = results.ndi[dmi_count-1]
    adx2 = results.adx[dmi_count-1]

    pdi3 = results.pdi[dmi_count-2]
    ndi3 = results.ndi[dmi_count-2]
    adx3 = results.adx[dmi_count-2]

    if pdi1>ndi1 and pdi2<ndi2:
        if(adx1>=23 and adx2<23 and adx2>adx3):
            print("up adx signal")

    elif pdi1<ndi1 and pdi2>ndi2:
        if(adx1>=23 and adx2<23 and adx2>adx3):
            print("down adx signal")

    if(adx1>=23 and adx2<23 and adx2>adx3):
        if pdi1>ndi1:
            print("up adx signal")
        elif pdi1<ndi1:
            print("down adx signal")
