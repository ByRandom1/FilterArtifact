import json

data = []
atk_base = 950
life_base = 15000
def_base = 800

filepath_mode = "MAC"


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

        self.result_life, self.result_atk = self.simple_judge()

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
        elif name == 'huskOfOpulentDreams':
            new_name = '华馆梦醒形骸记'
        elif name == 'oceanHuedClam':
            new_name = '海染砗磲'
        elif name == 'VermillionHereafter':
            new_name = '辰砂往生录'
        elif name == 'EchoesOfAnOffering':
            new_name = '来歆余响'
        elif name == 'DeepwoodMemories':
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
            self.main_type = '生命值'
        if self.vice_type1 == 'lifeStatic':
            self.life_num += (self.vice_value1 / life_base) / 0.05
            self.vice_type1 = '生命值'
            # Vice_type1_match = 'lifeStatic'
        if self.vice_type2 == 'lifeStatic':
            self.life_num += (self.vice_value2 / life_base) / 0.05
            self.vice_type2 = '生命值'
            # Vice_type2_match = 'lifeStatic'
        if self.vice_type3 == 'lifeStatic':
            self.life_num += (self.vice_value3 / life_base) / 0.05
            self.vice_type3 = '生命值'
            # Vice_type3_match = 'lifeStatic'
        if self.vice_type4 == 'lifeStatic':
            self.life_num += (self.vice_value4 / life_base) / 0.05
            self.vice_type4 = '生命值'
            # Vice_type4_match = 'lifeStatic'

        if self.main_type == 'lifePercentage':
            self.main_type = '生命值'
        if self.vice_type1 == 'lifePercentage':
            self.life_num += self.vice_value1 / 0.05
            self.vice_type1 = '生命值%'
            # Vice_type1_match = 'lifePercentage'
        if self.vice_type2 == 'lifePercentage':
            self.life_num += self.vice_value2 / 0.05
            self.vice_type2 = '生命值%'
            # Vice_type2_match = 'lifePercentage'
        if self.vice_type3 == 'lifePercentage':
            self.life_num += self.vice_value3 / 0.05
            self.vice_type3 = '生命值%'
            # Vice_type3_match = 'lifePercentage'
        if self.vice_type4 == 'lifePercentage':
            self.life_num += self.vice_value4 / 0.05
            self.vice_type4 = '生命值%'
            # Vice_type4_match = 'lifePercentage'

        if self.main_type == 'attackStatic':
            self.main_type = '攻击力'
        if self.vice_type1 == 'attackStatic':
            self.atk_num += (self.vice_value1 / atk_base) / 0.05
            self.vice_type1 = '攻击力'
            # Vice_type1_match = 'attackStatic'
        if self.vice_type2 == 'attackStatic':
            self.atk_num += (self.vice_value2 / atk_base) / 0.05
            self.vice_type2 = '攻击力'
            # Vice_type2_match = 'attackStatic'
        if self.vice_type3 == 'attackStatic':
            self.atk_num += (self.vice_value3 / atk_base) / 0.05
            self.vice_type3 = '攻击力'
            # Vice_type3_match = 'attackStatic'
        if self.vice_type4 == 'attackStatic':
            self.atk_num += (self.vice_value4 / atk_base) / 0.05
            self.vice_type4 = '攻击力'
            # Vice_type4_match = 'attackStatic'

        if self.main_type == 'attackPercentage':
            self.main_type = '攻击力'
        if self.vice_type1 == 'attackPercentage':
            self.atk_num += self.vice_value1 / 0.05
            self.vice_type1 = '攻击力%'
            # Vice_type1_match = 'attackPercentage'
        if self.vice_type2 == 'attackPercentage':
            self.atk_num += self.vice_value2 / 0.05
            self.vice_type2 = '攻击力%'
            # Vice_type2_match = 'attackPercentage'
        if self.vice_type3 == 'attackPercentage':
            self.atk_num += self.vice_value3 / 0.05
            self.vice_type3 = '攻击力%'
            # Vice_type3_match = 'attackPercentage'
        if self.vice_type4 == 'attackPercentage':
            self.atk_num += self.vice_value4 / 0.05
            self.vice_type4 = '攻击力%'
            # Vice_type4_match = 'attackPercentage'

        if self.main_type == 'defendStatic':
            self.main_type = '防御力'
        if self.vice_type1 == 'defendStatic':
            self.def_num += (self.vice_value1 / def_base) / 0.062
            self.vice_type1 = '防御力'
            # Vice_type1_match = 'defendStatic'
        if self.vice_type2 == 'defendStatic':
            self.def_num += (self.vice_value2 / def_base) / 0.062
            self.vice_type2 = '防御力'
            # Vice_type2_match = 'defendStatic'
        if self.vice_type3 == 'defendStatic':
            self.def_num += (self.vice_value3 / def_base) / 0.062
            self.vice_type3 = '防御力'
            # Vice_type3_match = 'defendStatic'
        if self.vice_type4 == 'defendStatic':
            self.def_num += (self.vice_value4 / def_base) / 0.062
            self.vice_type4 = '防御力'
            # Vice_type4_match = 'defendStatic'

        if self.main_type == 'defendPercentage':
            self.main_type = '防御力'
        if self.vice_type1 == 'defendPercentage':
            self.def_num += self.vice_value1 / 0.062
            self.vice_type1 = '防御力%'
            # Vice_type1_match = 'defendPercentage'
        if self.vice_type2 == 'defendPercentage':
            self.def_num += self.vice_value2 / 0.062
            self.vice_type2 = '防御力%'
            # Vice_type2_match = 'defendPercentage'
        if self.vice_type3 == 'defendPercentage':
            self.def_num += self.vice_value3 / 0.062
            self.vice_type3 = '防御力%'
            # Vice_type3_match = 'defendPercentage'
        if self.vice_type4 == 'defendPercentage':
            self.def_num += self.vice_value4 / 0.062
            self.vice_type4 = '防御力%'
            # Vice_type4_match = 'defendPercentage'

        if self.main_type == 'elementalMastery':
            self.main_type = '元素精通'
        if self.vice_type1 == 'elementalMastery':
            self.em_num += self.vice_value1 / 20
            self.vice_type1 = '元素精通'
            # Vice_type1_match = 'elementalMastery'
        if self.vice_type2 == 'elementalMastery':
            self.em_num += self.vice_value2 / 20
            self.vice_type2 = '元素精通'
            # Vice_type2_match = 'elementalMastery'
        if self.vice_type3 == 'elementalMastery':
            self.em_num += self.vice_value3 / 20
            self.vice_type3 = '元素精通'
            # Vice_type3_match = 'elementalMastery'
        if self.vice_type4 == 'elementalMastery':
            self.em_num += self.vice_value4 / 20
            self.vice_type4 = '元素精通'
            # Vice_type4_match = 'elementalMastery'

        if self.main_type == 'recharge':
            self.main_type = '元素充能效率'
        if self.vice_type1 == 'recharge':
            self.er_num += self.vice_value1 / 0.055
            self.vice_type1 = '元素充能效率'
            # Vice_type1_match = 'recharge'
        if self.vice_type2 == 'recharge':
            self.er_num += self.vice_value2 / 0.055
            self.vice_type2 = '元素充能效率'
            # Vice_type2_match = 'recharge'
        if self.vice_type3 == 'recharge':
            self.er_num += self.vice_value3 / 0.055
            self.vice_type3 = '元素充能效率'
            # Vice_type3_match = 'recharge'
        if self.vice_type4 == 'recharge':
            self.er_num += self.vice_value4 / 0.055
            self.vice_type4 = '元素充能效率'
            # Vice_type4_match = 'recharge'

        if self.main_type == 'critical':
            self.main_type = '暴击率'
        if self.vice_type1 == 'critical':
            self.cr_num += self.vice_value1 / 0.033
            self.vice_type1 = '暴击率'
            # Vice_type1_match = 'critical'
        if self.vice_type2 == 'critical':
            self.cr_num += self.vice_value2 / 0.033
            self.vice_type2 = '暴击率'
            # Vice_type2_match = 'critical'
        if self.vice_type3 == 'critical':
            self.cr_num += self.vice_value3 / 0.033
            self.vice_type3 = '暴击率'
            # Vice_type3_match = 'critical'
        if self.vice_type4 == 'critical':
            self.cr_num += self.vice_value4 / 0.033
            self.vice_type4 = '暴击率'
            # Vice_type4_match = 'critical'

        if self.main_type == 'criticalDamage':
            self.main_type = '暴击伤害'
        if self.vice_type1 == 'criticalDamage':
            self.cd_num += self.vice_value1 / 0.066
            self.vice_type1 = '暴击伤害'
            # Vice_type1_match = 'criticalDamage'
        if self.vice_type2 == 'criticalDamage':
            self.cd_num += self.vice_value2 / 0.066
            self.vice_type2 = '暴击伤害'
            # Vice_type2_match = 'criticalDamage'
        if self.vice_type3 == 'criticalDamage':
            self.cd_num += self.vice_value3 / 0.066
            self.vice_type3 = '暴击伤害'
            # Vice_type3_match = 'criticalDamage'
        if self.vice_type4 == 'criticalDamage':
            self.cd_num += self.vice_value4 / 0.066
            self.vice_type4 = '暴击伤害'
            # Vice_type4_match = 'criticalDamage'

        if self.main_type == "waterBonus":
            self.main_type == "水伤害加成"
        elif self.main_type == "iceBonus":
            self.main_type == "冰伤害加成"
        elif self.main_type == "fireBonus":
            self.main_type == "火伤害加成"
        elif self.main_type == "thunderBonus":
            self.main_type == "雷伤害加成"
        elif self.main_type == "windBonus":
            self.main_type == "风伤害加成"
        elif self.main_type == "rockBonus":
            self.main_type == "岩伤害加成"
        elif self.main_type == "dendroBonus":
            self.main_type == "草伤害加成"
        elif self.main_type == "physicalBonus":  # ?
            self.main_type == "物理伤害加成"

        if self.main_type == 'cureEffect':
            self.main_type = '治疗加成'

        # if Vice_type1_match == 'none':
        #     print(self.Vice_type1)
        # if Vice_type2_match == 'none':
        #     print(self.Vice_type2)
        # if Vice_type3_match == 'none':
        #     print(self.Vice_type3)
        # if Vice_type4_match == 'none':
        #     print(self.Vice_type4)

    def simple_judge(self):
        if self.level == 20:
            life_num = self.life_num + self.cr_num + self.cd_num
            life_em_num = self.life_num + self.em_num / 2 + self.cr_num + self.cd_num
            life_er_num = self.life_num + self.er_num / 2 + self.cr_num + self.cd_num
            life_react_num = self.life_num + self.em_num + self.cr_num + self.cd_num

            atk_num = self.atk_num + self.cr_num + self.cd_num
            atk_em_num = self.atk_num + self.em_num / 2 + self.cr_num + self.cd_num
            atk_er_num = self.atk_num + self.er_num / 2 + self.cr_num + self.cd_num
            atk_react_num = self.atk_num + self.em_num + self.cr_num + self.cd_num

            if self.position == 1 or self.position == 2:
                base = 6.5
            elif self.position == 3:
                base = 5.5
            else:
                base = 5

            result_life = 'life'
            if life_em_num >= base:
                result_life += '_em'
            if life_er_num >= base:
                result_life += '_er'
            if life_react_num >= base:
                result_life += '_react'
            if life_num >= base:
                result_life = 'life_all'
            if result_life == 'life':
                result_life = 'none'

            result_atk = 'atk'
            if atk_em_num >= base:
                result_atk += '_em'
            elif atk_er_num >= base:
                result_atk += '_er'
            elif atk_react_num >= base:
                result_atk += '_react'
            if atk_num >= base:
                result_atk = 'atk_all'
            if result_atk == 'atk':
                result_atk = 'none'

            return result_life, result_atk

        # elif self.level == 0:
        #     if self.position == 1 or self.position == 2:
        #         if self.vice_type4 == 'none':
        #             if self.cr_num > 0 or self.cd_num > 0:
        #                 return 'yes'
        #             else:
        #                 return 'no'
        #         else:
        #             if (self.cr_num > 0 and self.cd_num > 0) or (self.cr_num > 0 and self.life_num > 0.5) or (self.cr_num > 0 and self.atk_num > 0.5) or (
        #                     self.life_num > 0.5 and self.cd_num > 0) or (self.atk_num > 0.5 and self.cd_num > 0):
        #                 return 'yes'
        #             else:
        #                 return 'no'
        #     elif self.position == 3:
        #         if self.main_type == '防御力':
        #             return 'no'
        #         else:
        #             if self.cr_num > 0 or self.cd_num > 0:
        #                 return 'yes'
        #             else:
        #                 return 'no'
        #     elif self.position == 4:
        #         if self.main_type == '生命值' or self.main_type == '攻击力' or self.main_type == '防御力':
        #             return 'no'
        #         else:
        #             if self.cr_num > 0 or self.cd_num > 0:
        #                 return 'yes'
        #             else:
        #                 return 'no'
        #     else:
        #         if self.main_type == '生命值' or self.main_type == '攻击力' or self.main_type == '防御力':
        #             return 'no'
        #         elif self.main_type == '元素精通':
        #             if self.er_num > 0:
        #                 return 'yes'
        #             else:
        #                 return 'no'
        #         elif self.main_type == '治疗加成':
        #             if self.atk_num > 0.5 or self.life_num > 0.5:
        #                 return 'yes'
        #             else:
        #                 return 'no'
        #         else:
        #             if self.cr_num > 0 or self.cd_num > 0 or self.atk_num > 0.5 or self.life_num > 0.5:
        #                 return 'yes'
        #             else:
        #                 return 'no'
        # else:
        #     return 'no'


def deal_json_mona():
    if filepath_mode == "WIN":
        with open(r"C:\Users\Maxwell\Desktop\Genshin\GenshinData\artifacts.genshinart.json", 'r', encoding='utf-8') as mona:
            x = json.load(mona)
    elif filepath_mode == "MAC":
        with open(r"/Users/maxwell/Downloads/资料/游戏资料/Genshin/Data/artifacts.genshinart.json", 'r', encoding='utf-8') as mona:
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
    if filepath_mode == "WIN":
        f1 = open(r"C:\Users\Maxwell\Desktop\Genshin\GenshinData\artifacts.csv", 'w')
        f2 = open(r"C:\Users\Maxwell\Desktop\Genshin\GenshinCalculator\cmake-build-debug\artifacts.txt", 'w')
    elif filepath_mode == "MAC":
        f1 = open(r"/Users/maxwell/Downloads/资料/游戏资料/Genshin/Data/artifacts.csv", 'w')
        f2 = open(r"/Users/maxwell/Downloads/资料/游戏资料/Genshin/GenshinCalculator/cmake-build-debug/artifacts.txt", 'w')
    print('name,position,main_type,main_value,vice_type1,vice_value1,vice_type2,vice_value2,vice_type3,vice_value3,vice_type4,vice_value4,life_num,atk_num,def_num,em_num,er_num,'
          'cr_num,cd_num,result_life,result_atk', file=f1)
    for d in data:
        print('%s,%s,%s,%.3f,%s,%.3f,%s,%.3f,%s,%.3f,%s,%.3f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%s,%s'
              % (d.name, d.position, d.main_type, d.main_value, d.vice_type1, d.vice_value1, d.vice_type2, d.vice_value2, d.vice_type3, d.vice_value3, d.vice_type4, d.vice_value4,
                 d.life_num, d.atk_num, d.def_num, d.em_num, d.er_num, d.cr_num, d.cd_num, d.result_life, d.result_atk), file=f1)
        if d.level == 20:
            print('%d %s %s %s %.3f %s %.3f %s %.3f %s %.3f none' % (d.position, d.name, d.main_type, d.vice_type1, d.vice_value1, d.vice_type2,
                                                                     d.vice_value2, d.vice_type3, d.vice_value3, d.vice_type4, d.vice_value4), file=f2)


if __name__ == "__main__":
    deal_json_mona()
    output()
