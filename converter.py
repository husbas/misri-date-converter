from datetime import datetime
import bisect

# Ordinal number of days in the Misri Calendar
MISRI_YEAR_ORDINAL = {
    0:8231,
    30:18862,
    60:29493,
    90:40124,
    120:50755,
    150:61386,
    180:72017,
    210:82648,
    240:93279,
    270:103910,
    300:114541,
    330:125172,
    360:135803,
    390:146434,
    420:157065,
    450:167696,
    480:178327,
    510:188958,
    540:199589,
    570:210220,
    600:220851,
    630:231482,
    660:242113,
    690:252744,
    720:263375,
    750:274006,
    780:284637,
    810:295268,
    840:305899,
    870:316530,
    900:327161,
    930:337792,
    960:348423,
    990:359054,
    1020:369685,
    1050:380316,
    1080:390947,
    1110:401578,
    1140:412209,
    1170:422840,
    1200:433471,
    1230:444102,
    1260:454733,
    1290:465364,
    1320:475995,
    1350:486626,
    1380:497257,
    1410:507888,
    1440:518519,
    1470:529150,
    1500:539781
}


MISRI_30YEAR_ORDINAL = {
    1:0,
    2:354,
    3:709,
    4:1063, 
    5:1417,
    6:1772,
    7:2126,
    8:2480,
    9:2835,
    10:3189,
    11:3544,
    12:3898,
    13:4252,
    14:4607,
    15:4961,
    16:5315,
    17:5670,
    18:6024,
    19:6378,
    20:6733,
    21:7087,
    22:7442,
    23:7796,
    24:8150,
    25:8505,
    26:8859,
    27:9213,
    28:9568,
    29:9922,
    30:10277
}

MISRI_MONTH_ORDINAL = {
    1:0,
    2:30,
    3:59,
    4:89,
    5:118,
    6:148,
    7:177,
    8:207,
    9:236,
    10:266,
    11:295,
    12:325
}

MISRI_MONTH = [
    ("Moharram-ul-Haram", ),
    ("Safar-ul-Muzaffar",),
    ("Rabi-ul-Awwal",),
    ("Rabi-ul-Akhar",),
    ("Jamadil Awwal",),
    ("Jamadil Ukhra",),
    ("Rajab-ul-Asab","رجب الاصب"),
    ("Shabaan-ul-Karim",),
    ("Ramazan-ul-Moazzam",),
    ("Shawwal-ul-Mukarram",),
    ("Zilqadal Haram",),
    (" Zilhajjil Haram",),
]


GREG_CENTURY_ORDINAL = {
    600: 0,
    700: 36525,
    800: 73050,
    900: 109575,
    1000 :146100,
    1100:182625,
    1200: 219150,
    1300: 255675,
    1400:292200,
    1500:328725,
    1582: 358665,
    1600:365240,
    1700:401764,
    1800:438288,
    1900:474812,
    2000:511337
}

GREG_YEAR_ORDINAL = {
4:1461,
8:2922,
12:4383,
16:5844,
20:7305,
24:8766,
28:10227,
32:11688,
36:13149,
4:14610,
44:16071,
48:17532,
52:18993,
56:20454,
60:21915,
64:23376,
68:24837,
72:26298,
76:27759,
80:29220,
84:30681,
88:32142,
92:33603,
96:35064
}

GREG_MONTH_ORDINAL = {
    1:(0,366,731,1096),
    2:(31,397,762,1127),
    3:(60,425,790,1155),
    4:(91,456,821,1186),
    5:(121,486,851,1216),
    6:(152,517,882,1247),
    7:(182,547,912,1277),
    8:(213,578,943,1308),
    9:(244,609,974,1339),
    10:(274,639,1004,1369),
    11:(305,670,1035,1400),
    12:(335,700,1065,1430)
}



def convert(date):
    print(f"converting {date}")
    year = date.year
    month = date.month
    day = date.day

    c = int(year / 100) * 100
    o = GREG_CENTURY_ORDINAL[c]
    year = year - c
    l = year - int(year%4)
    if l > 0:
        o =  o + GREG_YEAR_ORDINAL[l] 
    o=o+GREG_MONTH_ORDINAL[month][year%4]

    """
        c = int(year / 100) * 100
        o = GREG_CENTURY_ORDINAL[c]
        years = list(GREG_YEAR_ORDINAL.keys())
        yo = years[bisect.bisect(years, year%100) - 1]
        o =  o + GREG_YEAR_ORDINAL[yo]
        o=o+GREG_MONTH_ORDINAL[month][year%100 - yo]
    """
    # years = list(GREG_YEAR_ORDINAL.keys())
    # yo = years[bisect.bisect(years, year%100) - 1]
    # o =  o + GREG_YEAR_ORDINAL[yo]

    # yo = 0 if (year%100 - yo) < 0 else (year%100 - yo)
    # o=o+GREG_MONTH_ORDINAL[month][yo]
    go=o+day

    yos = list(MISRI_YEAR_ORDINAL.values())
    i = bisect.bisect(yos, go) - 1
    year = list(MISRI_YEAR_ORDINAL.keys())[i]
    go = go - yos[i]
    yos = list(MISRI_30YEAR_ORDINAL.values())
    i = bisect.bisect(yos, go) - 1
    year = year+list(MISRI_30YEAR_ORDINAL.keys())[i]
    go = go - yos[i]
    yos = list(MISRI_MONTH_ORDINAL.values())
    i = bisect.bisect(yos, go) - 1
    m = list(MISRI_MONTH_ORDINAL.keys())[i]
    go = go - yos[i]
    d = go
    
    return(f"{d:02d}/{m:02d}/{year}")
