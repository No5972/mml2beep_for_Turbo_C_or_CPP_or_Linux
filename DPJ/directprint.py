# -*- coding: utf-8 -*-
"""
将beep谱（频率、持续时间）转换为循环次数
"""

import json

# 晶振频率(Hz)
CRYSTAL_FREQUENCY = 11059200
# 计数周期（机器周期）(s)
COUNT_PERIOD = 1 / (CRYSTAL_FREQUENCY / 12)
# 一次循环几个机器周期，通过定时器实验得到
COUNT_PER_LOOP = 38
# 一次循环时间(ms)
MS_PER_LOOP = COUNT_PERIOD * 1000 * COUNT_PER_LOOP


def tone_to_loop_count(notes):
    res = []
    for frequency, duration in notes:
        if frequency == 0:
            # 延时
            loop_count = 65535
            period_count = round(duration / MS_PER_LOOP)
        else:
            period = 1000 / frequency
            loop_count = round(period / 2 / MS_PER_LOOP)
            period_count = round(duration / period)
        # 最低频率0.185，loop_count = 65534
        assert 0 <= loop_count <= 65535, f'frequency = {frequency}, loop_count = {loop_count}，不在unsigned int范围内'
        # 把一个时间过长的音符拆成多个音符
        while period_count > 65535:
            res.append((loop_count, 65535))
            period_count -= 65535
        res.append((loop_count, period_count))
    for i in range(0, len(res), 6):
        print('\t')
        for loop_count, period_count in res[i: i + 6]:
            print(f'{{{loop_count}, {period_count}}}, ')
        print('\n')



def main():
    f = """
	粘贴乐谱，格式[[频率, 持续时间], [频率, 持续时间], ...]
	"""
    notes = json.loads(f)
    tone_to_loop_count(notes)


if __name__ == '__main__':
    main()
