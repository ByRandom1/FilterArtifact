import json

data = []
atk_base = 950
life_base = 15000
def_base = 800


class Artifact(object):
    def __init__(self, name, position, main_type, main_value, vice_type1, vice_value1, vice_type2, vice_value2,
                 vice_type3, vice_value3, vice_type4, vice_value4, level):
        self.name = self.name_convert(name)
        self.position = position
        self.main_type = main_type
        self.main_value = main_value
        self.vice_type1 = vice_type1
        self.vice_value1 = vice_value1
        self.vice_type2 = vice_type2
        self.vice_value2 = vice_value2
        self.vice_type3 = vice_type3
        self.vice_value3 = vice_value3
        self.vice_type4 = vice_type4
        self.vice_value4 = vice_value4
        self.level = level

        self.life_num = 0
        self.atk_num = 0
        self.def_num = 0
        self.em_num = 0
        self.er_num = 0
        self.cr_num = 0
        self.cd_num = 0
        self.cal_entries()

        self.general_life_num = 0
        self.general_atk_num = 0
        self.general_num_em = 0
        self.general_num_er = 0
        self.general_react_num = 0
        self.useful_type = self.simple_judge()

    def name_convert(self, name):
        if name == 'blizzardStrayer':
            new_name = '冰风迷途的勇士'
        elif name == 'Thundersoother':  # ?
            new_name = '平息鸣雷的尊者'
        elif name == 'lavaWalker':
            new_name = '渡过烈火的贤人'
        elif name == 'maidenBeloved':
            new_name = '被怜爱的少女'
        elif name == 'gladiatorFinale':
            new_name = '角斗士的终幕礼'
        elif name == 'viridescentVenerer':
            new_name = '翠绿之影'
        elif name == 'wandererTroupe':
            new_name = '流浪大地的乐团'
        elif name == 'thunderingFury':
            new_name = '如雷的盛怒'
        elif name == 'crimsonWitch':
            new_name = '炽烈的炎之魔女'
        elif name == 'noblesseOblige':
            new_name = '昔日宗室之仪'
        elif name == 'Bloodstained Chivalry':  # ?
            new_name = '染血的骑士道'
        elif name == 'Archaic Petra':  # ?
            new_name = '悠古的磐岩'
        elif name == 'Retracing Bolide':  # ?
            new_name = '逆飞的流星'
        elif name == 'heartOfDepth':
            new_name = '沉沦之心'
        elif name == 'tenacityOfTheMillelith':
            new_name = '千岩牢固'
        elif name == 'paleFlame':
            new_name = '苍白之火'
        elif name == 'shimenawaReminiscence':
            new_name = '追忆之注连'
        elif name == 'emblemOfSeveredFate':
            new_name = '绝缘之旗印'
        elif name == 'Husk of Opulent Dreams':  # ?
            new_name = '华馆梦醒形骸记'
        elif name == 'Ocean-Hued Clam':  # ?
            new_name = '海染砗磲'
        elif name == 'VermillionHereafter':
            new_name = '辰砂往生录'
        elif name == 'EchoesOfAnOffering':
            new_name = '来歆余响'
        elif name == 'Deepwood Memories':  # ?
            new_name = '深林的记忆'
        elif name == 'GildedDreams':
            new_name = '饰金之梦'
        else:
            print(name)
            new_name = name
        return new_name

    def cal_entries(self):
        # Vice_type1_match = 'none'
        # Vice_type2_match = 'none'
        # Vice_type3_match = 'none'
        # Vice_type4_match = 'none'

        if self.main_type == 'lifeStatic':
            self.main_type = 'hp'
        if self.vice_type1 == 'lifeStatic':
            self.life_num += (self.vice_value1 / life_base) / 0.05
            self.vice_type1 = 'hp'
            # Vice_type1_match = 'lifeStatic'
        if self.vice_type2 == 'lifeStatic':
            self.life_num += (self.vice_value2 / life_base) / 0.05
            self.vice_type2 = 'hp'
            # Vice_type2_match = 'lifeStatic'
        if self.vice_type3 == 'lifeStatic':
            self.life_num += (self.vice_value3 / life_base) / 0.05
            self.vice_type3 = 'hp'
            # Vice_type3_match = 'lifeStatic'
        if self.vice_type4 == 'lifeStatic':
            self.life_num += (self.vice_value4 / life_base) / 0.05
            self.vice_type4 = 'hp'
            # Vice_type4_match = 'lifeStatic'

        if self.main_type == 'lifePercentage':
            self.main_type = 'hp%'
        if self.vice_type1 == 'lifePercentage':
            self.life_num += self.vice_value1 / 0.05
            self.vice_type1 = 'hp%'
            # Vice_type1_match = 'lifePercentage'
        if self.vice_type2 == 'lifePercentage':
            self.life_num += self.vice_value2 / 0.05
            self.vice_type2 = 'hp%'
            # Vice_type2_match = 'lifePercentage'
        if self.vice_type3 == 'lifePercentage':
            self.life_num += self.vice_value3 / 0.05
            self.vice_type3 = 'hp%'
            # Vice_type3_match = 'lifePercentage'
        if self.vice_type4 == 'lifePercentage':
            self.life_num += self.vice_value4 / 0.05
            self.vice_type4 = 'hp%'
            # Vice_type4_match = 'lifePercentage'

        if self.main_type == 'attackStatic':
            self.main_type = 'atk'
        if self.vice_type1 == 'attackStatic':
            self.atk_num += (self.vice_value1 / atk_base) / 0.05
            self.vice_type1 = 'atk'
            # Vice_type1_match = 'attackStatic'
        if self.vice_type2 == 'attackStatic':
            self.atk_num += (self.vice_value2 / atk_base) / 0.05
            self.vice_type2 = 'atk'
            # Vice_type2_match = 'attackStatic'
        if self.vice_type3 == 'attackStatic':
            self.atk_num += (self.vice_value3 / atk_base) / 0.05
            self.vice_type3 = 'atk'
            # Vice_type3_match = 'attackStatic'
        if self.vice_type4 == 'attackStatic':
            self.atk_num += (self.vice_value4 / atk_base) / 0.05
            self.vice_type4 = 'atk'
            # Vice_type4_match = 'attackStatic'

        if self.main_type == 'attackPercentage':
            self.main_type = 'atk%'
        if self.vice_type1 == 'attackPercentage':
            self.atk_num += self.vice_value1 / 0.05
            self.vice_type1 = 'atk%'
            # Vice_type1_match = 'attackPercentage'
        if self.vice_type2 == 'attackPercentage':
            self.atk_num += self.vice_value2 / 0.05
            self.vice_type2 = 'atk%'
            # Vice_type2_match = 'attackPercentage'
        if self.vice_type3 == 'attackPercentage':
            self.atk_num += self.vice_value3 / 0.05
            self.vice_type3 = 'atk%'
            # Vice_type3_match = 'attackPercentage'
        if self.vice_type4 == 'attackPercentage':
            self.atk_num += self.vice_value4 / 0.05
            self.vice_type4 = 'atk%'
            # Vice_type4_match = 'attackPercentage'

        if self.main_type == 'defendStatic':
            self.main_type = 'def'
        if self.vice_type1 == 'defendStatic':
            self.def_num += (self.vice_value1 / def_base) / 0.062
            self.vice_type1 = 'def'
            # Vice_type1_match = 'defendStatic'
        if self.vice_type2 == 'defendStatic':
            self.def_num += (self.vice_value2 / def_base) / 0.062
            self.vice_type2 = 'def'
            # Vice_type2_match = 'defendStatic'
        if self.vice_type3 == 'defendStatic':
            self.def_num += (self.vice_value3 / def_base) / 0.062
            self.vice_type3 = 'def'
            # Vice_type3_match = 'defendStatic'
        if self.vice_type4 == 'defendStatic':
            self.def_num += (self.vice_value4 / def_base) / 0.062
            self.vice_type4 = 'def'
            # Vice_type4_match = 'defendStatic'

        if self.main_type == 'defendPercentage':
            self.main_type = 'def%'
        if self.vice_type1 == 'defendPercentage':
            self.def_num += self.vice_value1 / 0.062
            self.vice_type1 = 'def%'
            # Vice_type1_match = 'defendPercentage'
        if self.vice_type2 == 'defendPercentage':
            self.def_num += self.vice_value2 / 0.062
            self.vice_type2 = 'def%'
            # Vice_type2_match = 'defendPercentage'
        if self.vice_type3 == 'defendPercentage':
            self.def_num += self.vice_value3 / 0.062
            self.vice_type3 = 'def%'
            # Vice_type3_match = 'defendPercentage'
        if self.vice_type4 == 'defendPercentage':
            self.def_num += self.vice_value4 / 0.062
            self.vice_type4 = 'def%'
            # Vice_type4_match = 'defendPercentage'

        if self.main_type == 'elementalMastery':
            self.main_type = 'em'
        if self.vice_type1 == 'elementalMastery':
            self.em_num += self.vice_value1 / 20
            self.vice_type1 = 'em'
            # Vice_type1_match = 'elementalMastery'
        if self.vice_type2 == 'elementalMastery':
            self.em_num += self.vice_value2 / 20
            self.vice_type2 = 'em'
            # Vice_type2_match = 'elementalMastery'
        if self.vice_type3 == 'elementalMastery':
            self.em_num += self.vice_value3 / 20
            self.vice_type3 = 'em'
            # Vice_type3_match = 'elementalMastery'
        if self.vice_type4 == 'elementalMastery':
            self.em_num += self.vice_value4 / 20
            self.vice_type4 = 'em'
            # Vice_type4_match = 'elementalMastery'

        if self.main_type == 'recharge':
            self.main_type = 'er%'
        if self.vice_type1 == 'recharge':
            self.er_num += self.vice_value1 / 0.055
            self.vice_type1 = 'er%'
            # Vice_type1_match = 'recharge'
        if self.vice_type2 == 'recharge':
            self.er_num += self.vice_value2 / 0.055
            self.vice_type2 = 'er%'
            # Vice_type2_match = 'recharge'
        if self.vice_type3 == 'recharge':
            self.er_num += self.vice_value3 / 0.055
            self.vice_type3 = 'er%'
            # Vice_type3_match = 'recharge'
        if self.vice_type4 == 'recharge':
            self.er_num += self.vice_value4 / 0.055
            self.vice_type4 = 'er%'
            # Vice_type4_match = 'recharge'

        if self.main_type == 'critical':
            self.main_type = 'cr%'
        if self.vice_type1 == 'critical':
            self.cr_num += self.vice_value1 / 0.033
            self.vice_type1 = 'cr%'
            # Vice_type1_match = 'critical'
        if self.vice_type2 == 'critical':
            self.cr_num += self.vice_value2 / 0.033
            self.vice_type2 = 'cr%'
            # Vice_type2_match = 'critical'
        if self.vice_type3 == 'critical':
            self.cr_num += self.vice_value3 / 0.033
            self.vice_type3 = 'cr%'
            # Vice_type3_match = 'critical'
        if self.vice_type4 == 'critical':
            self.cr_num += self.vice_value4 / 0.033
            self.vice_type4 = 'cr%'
            # Vice_type4_match = 'critical'

        if self.main_type == 'criticalDamage':
            self.main_type = 'cd%'
        if self.vice_type1 == 'criticalDamage':
            self.cd_num += self.vice_value1 / 0.066
            self.vice_type1 = 'cd%'
            # Vice_type1_match = 'criticalDamage'
        if self.vice_type2 == 'criticalDamage':
            self.cd_num += self.vice_value2 / 0.066
            self.vice_type2 = 'cd%'
            # Vice_type2_match = 'criticalDamage'
        if self.vice_type3 == 'criticalDamage':
            self.cd_num += self.vice_value3 / 0.066
            self.vice_type3 = 'cd%'
            # Vice_type3_match = 'criticalDamage'
        if self.vice_type4 == 'criticalDamage':
            self.cd_num += self.vice_value4 / 0.066
            self.vice_type4 = 'cd%'
            # Vice_type4_match = 'criticalDamage'

        if self.main_type == 'cureEffect':
            self.main_type = 'cure%'
        if 'Bonus' in self.main_type:
            self.main_type = self.main_type.replace('Bonus', '%')

        # if Vice_type1_match == 'none':
        #     print(self.Vice_type1)
        # if Vice_type2_match == 'none':
        #     print(self.Vice_type2)
        # if Vice_type3_match == 'none':
        #     print(self.Vice_type3)
        # if Vice_type4_match == 'none':
        #     print(self.Vice_type4)

    def simple_judge(self):
        base = 0
        if self.level == 20:
            self.general_life_num = self.life_num + self.cr_num + self.cd_num
            self.general_atk_num = self.atk_num + self.cr_num + self.cd_num
            self.general_num_em = max(self.life_num, self.atk_num) + self.em_num / 2 + self.cr_num + self.cd_num
            self.general_num_er = max(self.life_num, self.atk_num) + self.er_num / 2 + self.cr_num + self.cd_num

            self.general_react_num = max(self.life_num, self.atk_num) + self.em_num + self.cr_num + self.cd_num

            if self.position == 1 or self.position == 2:
                base = 6.5
            elif self.position == 3:
                base = 5.5
            else:
                base = 5

            if self.general_life_num >= base and self.general_atk_num >= base:
                return 'all_all'
            elif self.general_life_num > self.general_atk_num:
                if self.general_life_num >= base:  # life > base > atk
                    return 'life_all'
                elif self.general_num_em >= base and self.general_num_er >= base:  # em/er > base > life > atk
                    return 'life_em/er'
                elif self.general_num_em >= base:  # em > base > er > life > atk
                    return 'life_em'
                elif self.general_num_er >= base:  # er > base > em > life > atk
                    return 'life_er'
                else:  # base > em/er > life > atk
                    return 'none'
            elif self.general_atk_num > self.general_life_num:
                if self.general_atk_num >= base:  # atk > base > life
                    return 'atk_all'
                elif self.general_num_em >= base and self.general_num_er >= base:  # em/er > base > atk > life
                    return 'atk_em/er'
                elif self.general_num_em >= base:  # em > base > er > atk > life
                    return 'atk_em'
                elif self.general_num_er >= base:  # er > base > em > atk > life
                    return 'atk_er'
                else:  # base > em/er > atk > life
                    return 'none'
            else:  # base > life/atk
                if self.general_num_em >= base and self.general_num_er >= base:  # em/er > base > atk/life
                    return 'all_em/er'
                elif self.general_num_em >= base:  # em > base > er > atk/life
                    return 'all_em'
                elif self.general_num_er >= base:  # er > base > em > atk/life
                    return 'all_er'
                else:  # base > em/er > atk/life
                    return 'none'
        elif self.level == 0:
            if self.position == 1 or self.position == 2:
                if self.vice_type4 == 'none':
                    if self.cr_num > 0 or self.cd_num > 0:
                        return 'yes'
                    else:
                        return 'no'
                else:
                    if (self.cr_num > 0 and self.cd_num > 0) or (self.cr_num > 0 and self.life_num > 0.5) or (self.cr_num > 0 and self.atk_num > 0.5) or (
                            self.life_num > 0.5 and self.cd_num > 0) or (self.atk_num > 0.5 and self.cd_num > 0):
                        return 'yes'
                    else:
                        return 'no'
            elif self.position == 3:
                if self.main_type == 'def%':
                    return 'no'
                else:
                    if self.cr_num > 0 or self.cd_num > 0:
                        return 'yes'
                    else:
                        return 'no'
            elif self.position == 4:
                if self.main_type == 'life%' or self.main_type == 'atk%' or self.main_type == 'def%':
                    return 'no'
                else:
                    if self.cr_num > 0 or self.cd_num > 0:
                        return 'yes'
                    else:
                        return 'no'
            else:
                if self.main_type == 'life%' or self.main_type == 'atk%' or self.main_type == 'def%':
                    return 'no'
                elif self.main_type == 'em':
                    if self.er_num > 0:
                        return 'yes'
                    else:
                        return 'no'
                elif self.main_type == 'cure%':
                    if self.atk_num > 0.5 or self.life_num > 0.5:
                        return 'yes'
                    else:
                        return 'no'
                else:
                    if self.cr_num > 0 or self.cd_num > 0 or self.atk_num > 0.5 or self.life_num > 0.5:
                        return 'yes'
                    else:
                        return 'no'
        else:
            return 'no'


def deal_json_mona():
    with open(r"C:\Users\Maxwell\Desktop\Genshin\Data\artifacts.genshinart.json", 'r', encoding='utf-8') as mona:
        x = json.load(mona)

    position_list = ['flower', 'feather', 'sand', 'cup', 'head']
    for index in range(5):
        things = x[position_list[index]]
        for thing in things:
            name = thing['setName']
            position = index + 1
            main_type = thing['mainTag']['name']
            main_value = thing['mainTag']['value']
            vice_type1 = thing['normalTags'][0]['name']
            vice_value1 = thing['normalTags'][0]['value']
            vice_type2 = thing['normalTags'][1]['name']
            vice_value2 = thing['normalTags'][1]['value']
            vice_type3 = thing['normalTags'][2]['name']
            vice_value3 = thing['normalTags'][2]['value']
            if len(thing['normalTags']) > 3:
                vice_type4 = thing['normalTags'][3]['name']
                vice_value4 = thing['normalTags'][3]['value']
            else:
                vice_type4 = 'none'
                vice_value4 = 0
            level = thing['level']

            data.append(
                Artifact(name, position, main_type, main_value, vice_type1, vice_value1, vice_type2, vice_value2,
                         vice_type3, vice_value3, vice_type4, vice_value4, level))


def output():
    f1 = open(r"C:\Users\Maxwell\Desktop\Genshin\Data\artifacts.csv", 'w')
    f2 = open(r"C:\Users\Maxwell\Desktop\Genshin\GenshinCalculator\cmake-build-debug\artifacts.txt", 'w')
    print('name,position,main_type,main_value,vice_type1,vice_value1,vice_type2,vice_value2,vice_type3,vice_value3,vice_type4,vice_value4,life_num,atk_num,def_num,em_num,er_num,'
          'cr_num,cd_num,general_life_num,general_atk_num,general_num_em,general_num_er,useful_type,general_react_num', file=f1)
    for d in data:
        print('%s,%s,%s,%.3f,%s,%.3f,%s,%.3f,%s,%.3f,%s,%.3f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%s,%.1f'
              % (d.name, d.position, d.main_type, d.main_value, d.vice_type1, d.vice_value1, d.vice_type2, d.vice_value2, d.vice_type3, d.vice_value3, d.vice_type4, d.vice_value4,
                 d.life_num, d.atk_num, d.def_num, d.em_num, d.er_num, d.cr_num, d.cd_num, d.general_life_num, d.general_atk_num, d.general_num_em, d.general_num_er,
                 d.useful_type, d.general_react_num), file=f1)
        if d.level == 20:
            print('%s %s %s %.3f %s %.3f %s %.3f %s %.3f %s %.3f' % (d.name, d.position, d.main_type, d.main_value, d.vice_type1, d.vice_value1, d.vice_type2, d.vice_value2,
                                                                     d.vice_type3, d.vice_value3, d.vice_type4, d.vice_value4), file=f2)


if __name__ == "__main__":
    deal_json_mona()
    output()