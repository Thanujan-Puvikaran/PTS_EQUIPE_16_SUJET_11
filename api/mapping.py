import numpy as np


class defaultValue:
    """replace empty string or 0 by default value, here it's NaN"""

    DEFAULTVALUE = {"Age": -0.95197, "Education": -2.43591}

    def __init__(self, payload, flag=False):
        self.default(payload, flag)
        self.default_bool()
        self.gender()
        self.age()
        self.education()
        self.nscore()
        self.escore()
        self.oscore()
        self.ascore()
        self.cscore()
        self.ss()

    def default(self, payload, flag=False):
        if flag:
            self.value = {
                key: (np.NaN if value == "string" or value == 0 else value)
                for key, value in payload.items()
            }
        else:
            self.value = {
                key: ("" if value == "string" else value)
                for key, value in payload.items()
            }

    def default_bool(self):
        for key, val in self.value.items():
            if type(val) == bool:
                self.value[key] = 1 if val == True else 0

    def age(self):
        if self.value["Age"] >= 18 and self.value["Age"] <= 24:
            self.value["Age"] = -0.95197
        elif self.value["Age"] >= 25 and self.value["Age"] <= 34:
            self.value["Age"] = -0.07854
        elif self.value["Age"] >= 35 and self.value["Age"] <= 44:
            self.value["Age"] = 0.49788
        elif self.value["Age"] >= 45 and self.value["Age"] <= 54:
            self.value["Age"] = 1.09449
        elif self.value["Age"] >= 55 and self.value["Age"] <= 64:
            self.value["Age"] = 1.82213
        elif self.value["Age"] >= 65:
            self.value["Age"] = 2.59171
        else:
            self.value["Age"] = self.DEFAULTVALUE["Age"]

    def gender(self):
        self.value["Gender"] = (
            -0.48246
            if self.value["Gender"] in "malMmMalMalemale" and self.value["Gender"] != ""
            else 0.48246
        )

    def education(self):
        if self.value["Education"] == 1:
            self.value["Education"] = -2.43591
        elif self.value["Education"] == 2:
            self.value["Education"] = -1.73790
        elif self.value["Education"] == 3:
            self.value["Education"] = -1.43719
        elif self.value["Education"] == 4:
            self.value["Education"] = -1.22751
        elif self.value["Education"] == 5:
            self.value["Education"] = -0.61113
        elif self.value["Education"] == 6:
            self.value["Education"] = -0.05921
        elif self.value["Education"] == 7:
            self.value["Education"] = 0.45468
        elif self.value["Education"] == 8:
            self.value["Education"] = 1.16365
        elif self.value["Education"] == 9:
            self.value["Education"] = 1.98437
        else:
            self.value["Education"] = self.DEFAULTVALUE["Education"]

    def nscore(self):
        nsc = {
            "12": -3.46436,
            "13": -3.15735,
            "14": -2.75696,
            "15": -2.52197,
            "16": -2.42317,
            "17": -2.34360,
            "18": -2.21844,
            "19": -2.05048,
            "20": -1.86962,
            "21": -1.69163,
            "22": -1.55078,
            "23": -1.43907,
            "24": -1.32828,
            "25": -1.19430,
            "26": -1.05308,
            "27": -0.92104,
            "28": -0.79151,
            "29": -0.67825,
            "30": -0.58016,
            "31": -0.46725,
            "32": -0.34799,
            "33": -0.24649,
            "34": -0.14882,
            "35": -0.05188,
            "36": 0.04257,
            "37": 0.13606,
            "38": 0.22393,
            "39": 0.31287,
            "40": 0.41667,
            "41": 0.52135,
            "42": 0.62967,
            "43": 0.73545,
            "44": 0.82562,
            "45": 0.91093,
            "46": 1.02119,
            "47": 1.13281,
            "48": 1.23461,
            "49": 1.37297,
            "50": 1.49158,
            "51": 1.60383,
            "52": 1.72012,
            "53": 1.83990,
            "54": 1.98437,
            "55": 2.12700,
            "56": 2.28554,
            "57": 2.46262,
            "58": 2.61139,
            "59": 2.82196,
            "60": 3.27393,
        }
        key = self.value["Nscore"]
        self.value["Nscore"] = self.check(nsc, key)

    def escore(self):
        esc = {
            "16": -3.27393,
            "18": -3.00537,
            "19": -2.72827,
            "20": -2.53830,
            "21": -2.44904,
            "22": -2.32338,
            "23": -2.21069,
            "24": -2.11437,
            "25": -2.03972,
            "26": -1.92173,
            "27": -1.76250,
            "28": -1.63340,
            "29": -1.50796,
            "30": -1.37639,
            "31": -1.23177,
            "32": -1.09207,
            "33": -0.94779,
            "34": -0.80615,
            "35": -0.69509,
            "36": -0.57545,
            "37": -0.43999,
            "38": -0.30033,
            "39": -0.15487,
            "40": 0.00332,
            "41": 0.16767,
            "42": 0.32197,
            "43": 0.47617,
            "44": 0.63779,
            "45": 0.80523,
            "46": 0.96248,
            "47": 1.11406,
            "48": 1.28610,
            "49": 1.45421,
            "50": 1.58487,
            "51": 1.74091,
            "52": 1.93886,
            "53": 2.12700,
            "54": 2.32338,
            "55": 2.57309,
            "56": 2.85950,
            "58": 3.00537,
            "59": 3.27393,
        }
        key = self.value["Escore"]
        self.value["Escore"] = self.check(esc, key)

    def oscore(self):
        osc = {
            "24": -3.27393,
            "26": -2.85950,
            "28": -2.63199,
            "29": -2.39883,
            "30": -2.21069,
            "31": -2.09015,
            "32": -1.97495,
            "33": -1.82919,
            "34": -1.68062,
            "35": -1.55521,
            "36": -1.42424,
            "37": -1.27553,
            "38": -1.11902,
            "39": -0.97631,
            "40": -0.84732,
            "41": -0.71727,
            "42": -0.58331,
            "43": -0.45174,
            "44": -0.31776,
            "45": -0.17779,
            "46": -0.01928,
            "47": 0.14143,
            "48": 0.29338,
            "49": 0.44585,
            "50": 0.58331,
            "51": 0.72330,
            "52": 0.88309,
            "53": 1.06238,
            "54": 1.24033,
            "55": 1.43533,
            "56": 1.65653,
            "57": 1.88511,
            "58": 2.15324,
            "59": 2.44904,
            "60": 2.90161,
        }
        key = self.value["Oscore"]
        self.value["Oscore"] = self.check(osc, key)
        print(self.value)

    def ascore(self):
        asc = {
            "12": -3.46436,
            "16": -3.15735,
            "18": -3.00537,
            "23": -2.90161,
            "24": -2.78793,
            "25": -2.70172,
            "26": -2.53830,
            "27": -2.35413,
            "28": -2.21844,
            "29": -2.07848,
            "30": -1.92595,
            "31": -1.77200,
            "32": -1.62090,
            "33": -1.47955,
            "34": -1.34289,
            "35": -1.21213,
            "36": -1.07533,
            "37": -0.91699,
            "38": -0.76096,
            "39": -0.60633,
            "40": -0.45321,
            "41": -0.30172,
            "42": -0.15487,
            "43": -0.01729,
            "44": 0.13136,
            "45": 0.28783,
            "46": 0.43852,
            "47": 0.59042,
            "48": 0.76096,
            "49": 0.94156,
            "50": 1.11406,
            "51": 1.2861,
            "52": 1.45039,
            "53": 1.61108,
            "54": 1.81866,
            "55": 2.03972,
            "56": 2.23427,
            "57": 2.46262,
            "58": 2.75696,
            "59": 3.15735,
            "60": 3.46436,
        }
        key = self.value["Ascore"]
        self.value["Ascore"] = self.check(asc, key)

    def cscore(self):
        csc = {
            "17": -3.46436,
            "19": -3.15735,
            "20": -2.90161,
            "21": -2.72827,
            "22": -2.57309,
            "23": -2.42317,
            "24": -2.30408,
            "25": -2.18109,
            "26": -2.04506,
            "27": -1.92173,
            "28": -1.78169,
            "29": -1.64101,
            "30": -1.51840,
            "31": -1.38502,
            "32": -1.25773,
            "33": -1.13788,
            "34": -1.01450,
            "35": -0.89891,
            "36": -0.78155,
            "37": -0.65253,
            "38": -0.52745,
            "39": -0.40581,
            "40": -0.27607,
            "41": -0.14277,
            "42": -0.00665,
            "43": 0.12331,
            "44": 0.25953,
            "45": 0.4159,
            "46": 0.58489,
            "47": 0.7583,
            "48": 0.93949,
            "49": 1.13407,
            "50": 1.30612,
            "51": 1.46191,
            "52": 1.63088,
            "53": 1.81175,
            "54": 2.04506,
            "55": 2.33337,
            "56": 2.63199,
            "57": 3.00537,
            "59": 3.46436,
        }
        key = self.value["Cscore"]
        self.value["Cscore"] = self.check(csc, key)

    def ss(self):
        ss = {
            "71": -2.07848,
            "87": -1.54858,
            "103": 1.92173,
            "132": -1.18084,
            "169": -0.84637,
            "210": 1.22470,
            "211": -0.52593,
            "219": 0.07987,
            "223": -0.21575,
            "249": 0.40148,
        }
        key = self.value["SS"]
        self.value["SS"] = self.check(ss, key)

    def check(self, dic, key):
        lstkey = list(dic.keys())
        if key == 0:
            return 0
        if key < int(lstkey[0]):
            return dic[str(lstkey[0])]
        if key > int(lstkey[len(lstkey) - 1]):
            return dic[str(lstkey[len(lstkey) - 1])]
        if str(key) in lstkey:
            return dic[str(key)]
        i = key + 1
        j = key - 1
        flag = False
        while not flag:
            if str(i) in lstkey:
                key = i
                break
            elif str(j) in lstkey:
                key = j
                break
            else:
                pass
            i += 1
            j -= 1
        return dic[str(key)]
