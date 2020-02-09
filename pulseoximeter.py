# -*-coding:utf-8-*-
import re
from statistics import median

import max30102
import hrcalc

class MAXREFDES117():

    def get(self):
        # MAXREFDES117から値を取得
        m = max30102.MAX30102()

        ir = []
        red = []
        red, ir = m.read_sequential(1000)

        m.shutdown()

        # 取得した値を整形
        hr = []
        spo2 = []
        for i in range(37):
            measure = hrcalc.calc_hr_and_spo2(ir[25*i:25*i+100], red[25*i:25*i+100])
            l = list(measure)
            # True のものを取り出す
            if l[1] == True:
                hr.append(l[0])
            if l[3] == True:
                spo2.append(l[2])

        # 中央値を取り出す
        hr = median(hr)
        spo2 = round(median(spo2))
        return hr, spo2

if __name__ == '__main__':
    maxrefdes = MAXREFDES117()
    hr, spo2 = maxrefdes.get()
    print(hr, spo2)

