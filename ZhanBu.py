import datetime
import time

"""
开发者：喵星君大大
开发日期：2020年3月26日
微信：minglishi2016
微信公众号：喵星君大大
"""

class BaziPaipan(object): #  计算八字排盘

    def __init__(self,y,m,d,h):

        self.stardard_day = datetime.datetime(1970,2,4,23)
        # self.input_data = datetime.datetime(self.year,self.month,self.day_num,self.time)
        self.__Jie = [19700204, 19700306, 19700405, 19700506, 19700606, 19700707, 19700808, 19700908, 19701009,
                 19701108, 19701207, 19710106, 19710204, 19710306, 19710405, 19710506, 19710606, 19710708, 19710808,
                 19710908,
                 19711009, 19711108, 19711208, 19720106, 19720205, 19720305, 19720405, 19720505, 19720605, 19720707,
                 19720807, 19720907, 19721008, 19721107, 19721207, 19730106, 19730204, 19730306, 19730405, 19730505,
                 19730606, 19730707, 19730808, 19730908, 19731008, 19731107, 19731207, 19740105, 19740204, 19740306,
                 19740405, 19740506, 19740606, 19740707, 19740808, 19740908, 19741009, 19741108, 19741207, 19750106,
                 19750204, 19750306, 19750405, 19750506, 19750606, 19750708, 19750808, 19750908, 19751009, 19751108,
                 19751208, 19760106, 19760205, 19760305, 19760404, 19760505, 19760605, 19760707, 19760807, 19760907,
                 19761008, 19761107, 19761207, 19770106, 19770204, 19770306, 19770405, 19770505, 19770606, 19770707,
                 19770807, 19770908, 19771008, 19771107, 19771207, 19780105, 19780204, 19780306, 19780405, 19780506,
                 19780606, 19780707, 19780808, 19780908, 19781008, 19781108, 19781207, 19790106, 19790204, 19790306,
                 19790405, 19790506, 19790606, 19790708, 19790808, 19790908, 19791009, 19791108, 19791208, 19800106,
                 19800205, 19800305, 19800404, 19800505, 19800605, 19800707, 19800807, 19800907, 19801008, 19801107,
                 19801207, 19810106, 19810204, 19810306, 19810405, 19810505, 19810606, 19810707, 19810807, 19810908,
                 19811008, 19811107, 19811207, 19820105, 19820204, 19820306, 19820405, 19820506, 19820606, 19820707,
                 19820808, 19820908, 19821008, 19821108, 19821207, 19830106, 19830204, 19830306, 19830405, 19830506,
                 19830606, 19830708, 19830808, 19830908, 19831009, 19831108, 19831208, 19840106, 19840204, 19840305,
                 19840404, 19840505, 19840605, 19840707, 19840807, 19840907, 19841008, 19841107, 19841207, 19850106,
                 19850204, 19850305, 19850405, 19850505, 19850606, 19850707, 19850807, 19850908, 19851008, 19851107,
                 19851207, 19860105, 19860204, 19860306, 19860405, 19860506, 19860606, 19860707, 19860808, 19860908,
                 19861008, 19861108, 19861207, 19870105, 19870204, 19870306, 19870405, 19870506, 19870606, 19870707,
                 19870808, 19870908, 19871009, 19871108, 19871207, 19880106, 19880204, 19880305, 19880404, 19880505,
                 19880605, 19880707, 19880807, 19880907, 19881008, 19881107, 19881207, 19890106, 19890204, 19890305,
                 19890405, 19890505, 19890606, 19890707, 19890807, 19890907, 19891008, 19891107, 19891207, 19900105,
                 19900204, 19900306, 19900405, 19900506, 19900606, 19900707, 19900808, 19900908, 19901008, 19901108,
                 19901207, 19910105, 19910204, 19910306, 19910405, 19910506, 19910606, 19910707, 19910808, 19910908,
                 19911009, 19911108, 19911207, 19920106, 19920204, 19920305, 19920404, 19920505, 19920605, 19920707,
                 19920807, 19920907, 19921008, 19921107, 19921207, 19930106, 19930204, 19930305, 19930405, 19930505,
                 19930606, 19930707, 19930807, 19930907, 19931008, 19931107, 19931207, 19940105, 19940204, 19940306,
                 19940405, 19940506, 19940606, 19940707, 19940808, 19940908, 19941008, 19941107, 19941207, 19950105,
                 19950204, 19950306, 19950405, 19950506, 19950606, 19950707, 19950808, 19950908, 19951009, 19951108,
                 19951207, 19960106, 19960204, 19960305, 19960404, 19960505, 19960605, 19960707, 19960807, 19960907,
                 19961008, 19961107, 19961207, 19970106, 19970204, 19970305, 19970405, 19970505, 19970605, 19970707,
                 19970807, 19970907, 19971008, 19971107, 19971207, 19980105, 19980204, 19980306, 19980405, 19980506,
                 19980606, 19980707, 19980808, 19980908, 19981008, 19981107, 19981207, 19990105, 19990204, 19990306,
                 19990405, 19990506, 19990606, 19990707, 19990808, 19990908, 19991009, 19991108, 19991207, 20000106,
                 20000204, 20000305, 20000404, 20000505, 20000605, 20000707, 20000807, 20000907, 20001008, 20001107,
                 20001207, 20010106, 20010204, 20010305, 20010405, 20010505, 20010605, 20010707, 20010807, 20010907,
                 20011008, 20011107, 20011207, 20020105, 20020204, 20020306, 20020405, 20020506, 20020606, 20020707,
                 20020808, 20020908, 20021008, 20021107, 20021207, 20030105, 20030204, 20030306, 20030405, 20030506,
                 20030606, 20030707, 20030808, 20030908, 20031009, 20031108, 20031207, 20040106, 20040204, 20040305,
                 20040404, 20040505, 20040605, 20040707, 20040807, 20040907, 20041008, 20041107, 20041207, 20050106,
                 20050204, 20050305, 20050405, 20050505, 20050605, 20050707, 20050807, 20050907, 20051008, 20051107,
                 20051207, 20060105, 20060204, 20060306, 20060405, 20060505, 20060606, 20060707, 20060807, 20060908,
                 20061008, 20061107, 20061207, 20070105, 20070204, 20070306, 20070405, 20070506, 20070606, 20070707,
                 20070808, 20070908, 20071009, 20071108, 20071207, 20080106, 20080204, 20080305, 20080404, 20080505,
                 20080605, 20080707, 20080807, 20080907, 20081008, 20081107, 20081207, 20090106, 20090204, 20090305,
                 20090404, 20090505, 20090605, 20090707, 20090807, 20090907, 20091008, 20091107, 20091207, 20100105,
                 20100204, 20100306, 20100405, 20100505, 20100606, 20100707, 20100807, 20100908, 20101008, 20101107,
                 20101207, 20110105, 20110204, 20110306, 20110405, 20110506, 20110606, 20110707, 20110808, 20110908,
                 20111008, 20111108, 20111207, 20120106, 20120204, 20120305, 20120404, 20120505, 20120605, 20120707,
                 20120807, 20120907, 20121008, 20121107, 20121207, 20130106, 20130204, 20130305, 20130404, 20130505,
                 20130605, 20130707, 20130807, 20130907, 20131008, 20131107, 20131207, 20140105, 20140204, 20140306,
                 20140405, 20140505, 20140606, 20140707, 20140807, 20140908, 20141008, 20141107, 20141207, 20150105,
                 20150204, 20150306, 20150405, 20150506, 20150606, 20150707, 20150808, 20150908, 20151008, 20151108,
                 20151207, 20160106, 20160204, 20160305, 20160404, 20160505, 20160605, 20160707, 20160807, 20160907,
                 20161008, 20161107, 20161207, 20170106, 20170203, 20170305, 20170404, 20170505, 20170605, 20170707,
                 20170807, 20170907, 20171008, 20171107, 20171207, 20180105, 20180204, 20180305, 20180405, 20180505,
                 20180606, 20180707, 20180807, 20180908, 20181008, 20181107, 20181207, 20190105, 20190204, 20190306,
                 20190405, 20190506, 20190606, 20190707, 20190808, 20190908, 20191008, 20191108, 20191207, 20200105,
                 20200204, 20200305, 20200404, 20200505, 20200605, 20200706, 20200807, 20200907, 20201008, 20201107,
                 20201207, 20210106, 20210203, 20210305, 20210404, 20210505, 20210605, 20210707, 20210807, 20210907,
                 20211008, 20211107, 20211207, 20220105, 20220204, 20220305, 20220405, 20220505, 20220606, 20220707,
                 20220807, 20220907, 20221008, 20221107, 20221207, 20230105, 20230204, 20230306, 20230405, 20230506,
                 20230606, 20230707, 20230808, 20230908, 20231008, 20231108, 20231207, 20240105, 20240204, 20240305,
                 20240404, 20240505, 20240605, 20240706, 20240807, 20240907, 20241008, 20241107, 20241206, 20250106,
                 20250203, 20250305, 20250404, 20250505, 20250605, 20250707, 20250807, 20250907, 20251008, 20251107,
                 20251207, 20260105, 20260204, 20260305, 20260405, 20260505, 20260605, 20260707, 20260807, 20260907,
                 20261008, 20261107, 20261207, 20270105, 20270204, 20270306, 20270405, 20270506, 20270606, 20270707,
                 20270808, 20270908, 20271008, 20271107, 20271207, 20280105, 20280204, 20280305, 20280404, 20280505,
                 20280605, 20280706, 20280807, 20280907, 20281008, 20281107, 20281206, 20290106, 20290203, 20290305,
                 20290404, 20290505, 20290605, 20290707, 20290807, 20290907, 20291008, 20291107, 20291207, 20300105,
                 20300204, 20300305, 20300405, 20300505, 20300605, 20300707, 20300807, 20300907, 20301008, 20301107,
                 20301207, 20300105]

        self.__Tian_Gan = {0: '甲', 1: '乙', 2: '丙', 3: '丁', 4: '戊', 5: '己', 6: '庚', 7: '辛', 8: '壬', 9: '癸'}

        self.__Di_Zhi = {0: '寅', 1: '卯', 2: '辰', 3: '巳', 4: '午', 5: '未', 6: '申', 7: '酉', 8: '戌', 9: '亥', 10: '子', 11: '丑', }

        self.__Hour_Dz = {1: '子', 2: '丑',3: '寅', 4: '卯', 5: '辰', 6: '巳', 7: '午', 8: '未', 9: '申', 10: '酉', 11: '戌', 12: '亥'}

        self.__Sex = ['女', '男']

        self.__SixtyJZ = ["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉", "甲戌", "乙亥",
                     "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未", "甲申", "乙酉", "丙戌", "丁亥", "戊子",
                     "己丑", "庚寅", "辛卯", "壬辰", "癸巳", "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑",
                     "壬寅", "癸卯", "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑", "甲寅",
                     "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"]

        self.year = y
        self.month = m
        self.day = d
        self.hour = h
        self.input_day = datetime.datetime(self.year, self.month, self.day, self.hour)
        self.hour_num = self.input_day - self.stardard_day

    def Time(self):  #  八字排盘主程序，元祖序列[0]为八字，排列为年干，年支，月干，月支，日干，日支，时干，时支。元祖序列[1]为空亡
    # def Year(self):

        self.list_num = self.year * 10000 + self.month * 100 + self.day

        if self.list_num in self.__Jie:
            self.mid_num = self.__Jie.index(self.list_num) + 1
        elif self.list_num not in self.__Jie:
            self.__Jie.append(self.list_num)
            self.__Jie.sort()
            self.mid_num = self.__Jie.index(self.list_num)

        if self.mid_num % 12 == 0:
            self.mid_num1 = self.mid_num - 1
            self.year_num = self.mid_num1 // 12

        else:
            self.year_num = self.mid_num // 12

        self.tiangan_y = (self.year_num + 6) % 10
        self.dizhi_y = (self.year_num + 8) % 12
        self.tiangan_year = self.__Tian_Gan[self.tiangan_y]
        self.dizhi_year = self.__Di_Zhi[self.dizhi_y]
        # return self.tiangan_year, self.dizhi_year, self.tiangan_y, self.dizhi_y

    # def Month(self):

        self.month_num = self.mid_num % 12 + 1
        self.dizhi_m = (self.month_num + 10) % 12
        if self.tiangan_y == 0 or self.tiangan_y == 5:
            self.tiangan_mid = 2
        elif self.tiangan_y == 1 or self.tiangan_y == 6:
            self.tiangan_mid = 4
        elif self.tiangan_y == 2 or self.tiangan_y == 7:
            self.tiangan_mid = 6
        elif self.tiangan_y == 3 or self.tiangan_y == 8:
            self.tiangan_mid = 8
        elif self.tiangan_y == 4 or self.tiangan_y == 9:
            self.tiangan_mid = 0
        self.tiangan_m = (self.month_num + self.tiangan_mid - 2) % 10
        self.tiangan_month = self.__Tian_Gan[self.tiangan_m]
        self.dizhi_month = self.__Di_Zhi[self.dizhi_m]
        # return self.tiangan_month,self.dizhi_month, self.tiangan_m, self.dizhi_m

    # def Day(self):

        self.date_num = int((datetime.datetime(self.year, self.month, self.day) - self.stardard_day).days)
        self.day_num = self.date_num % 60
        self.day_tg = (self.day_num + 2) % 10
        self.day_dz = (self.day_num + 2) % 12
        self.tiangan_day = self.__Tian_Gan[self.day_tg]
        self.dizhi_day = self.__Di_Zhi[self.day_dz]
        self.hour_num = (datetime.datetime(self.year, self.month, self.day, self.hour) - self.stardard_day).seconds
        if self.hour_num == 0:
            self.tiangan_day = self.__Tian_Gan[(self.day_tg + 1) % 10]
            self.dizhi_day = self.__Di_Zhi[(self.day_dz + 1) % 12]
        # return self.tiangan_day , self.dizhi_day, self.day_tg, self.day_dz

    # def Hour(self):

        self.hour_num = int((datetime.datetime(self.year, self.month, self.day, self.hour) - self.stardard_day).seconds / 3600)
        if self.hour_num == 0 or self.hour_num == 1:
            self.hour_dz = 0
            if self.day_tg == 0 or self.day_tg == 5:
                self.hour_tg = 0
            elif self.day_tg == 1 or self.day_tg == 6:
                self.hour_tg = 2
            elif self.day_tg== 2 or self.day_tg == 7:
                self.hour_tg = 4
            elif self.day_tg == 3 or self.day_tg == 8:
                self.hour_tg = 6
            elif self.day_tg == 4 or self.day_tg == 9:
                self.hour_tg = 8
        else:

            if self.hour_num % 2 == 0:
                self.hour_dz = self.hour_num // 2
                self.hour_tg = ((self.day_tg + 1) * 2 + self.hour_dz - 2) % 10

            elif self.hour_num % 2 == 1:
                self.hour_dz = (self.hour_num + 1) // 2
                self.hour_tg = ((self.day_tg + 1) * 2 + self.hour_dz - 2) % 10

        self.tiangan_hour = self.__Tian_Gan[self.hour_tg]
        self.dizhi_hour = self.__Hour_Dz[(self.hour_dz + 1) % 12]

        # return self.tiangan_hour, self.dizhi_hour, self.hour_dz, self.hour_tg

    # def KongWang(self):
        if self.day_tg == 0:
            self.day_tg = self.day_tg + 10
        self.kongwang = self.day_dz + 2 - self.day_tg
        if self.kongwang <= 0:
            self.kongwang = self.kongwang + 12

        self.kongwang_previous = (self.kongwang + 11) % 12

        self.kongwang1 = self.__Hour_Dz[self.kongwang_previous]
        self.kongwang2 = self.__Hour_Dz[self.kongwang]
        # return self.kongwang1, self.kongwang2, self.kongwang, self.kongwang_previous   #  空亡

    def QiYun(self,sex):  #  sex:男为1，女为0  此为排大运主程序，输出元祖[0]为字典形式大运，元祖[1]为起运年份
        self.Time()
        self.dayun_dict = {}
        if sex == "男":
            self.sex = 1
        elif sex == "女":
            self.sex = 0

        if (self.sex == 1 and self.tiangan_y % 2 == 0) or (self.sex == 0 and self.tiangan_y % 2 == 1):
            self.jie_year = int(self.__Jie[self.mid_num + 1] // 10000)
            self.jie_month = int((self.__Jie[self.mid_num + 1] - self.jie_year * 10000) // 100)
            self.jie_day = int(self.__Jie[self.mid_num + 1] % 10)
            self.jie_date = datetime.datetime(self.jie_year, self.jie_month, self.jie_day)
            self.jie_day_num = int((self.jie_date - self.input_day).days / 3)
            if self.jie_day_num == 0:
                self.jie_day_num = self.jie_day_num + 1
            self.qiyun_year = str(self.year + self.jie_day_num)

            qiyun = str(self.tiangan_month + self.dizhi_month)
            qiyun_num = self.__SixtyJZ.index(qiyun)
            for i in range(1,8):
                dayun_num = (qiyun_num + i) % 60
                self.dayun = self.__SixtyJZ[dayun_num]
                self.dayun_year = int(self.qiyun_year) + i * 10
                self.dayun_dict[self.dayun] = self.dayun_year
                # print(self.dayun_dict)

        elif (self.sex == 1 and self.tiangan_y % 2 == 1) or (self.sex == 0 and self.tiangan_y % 2 == 0):
            self.jie_year = int(self.__Jie[self.mid_num - 1] // 10000)
            self.jie_month = int((self.__Jie[self.mid_num - 1] - self.jie_year * 10000) // 100)
            self.jie_day = int(self.__Jie[self.mid_num - 1] % 10)
            self.jie_date = datetime.datetime(self.jie_year, self.jie_month, self.jie_day)
            self.jie_day_num = int((self.input_day - self.jie_date).days / 3)
            if self.jie_day_num == 0:
                self.jie_day_num = self.jie_day_num + 1
            self.qiyun_year = str(self.year + self.jie_day_num)
            qiyun = str(self.tiangan_month + self.dizhi_month)
            qiyun_num = self.__SixtyJZ.index(qiyun)
            for i in range(1, 8):
                dayun_num = (qiyun_num - i + 60) % 60
                self.dayun = self.__SixtyJZ[dayun_num]
                self.dayun_year = int(self.qiyun_year) + i * 10
                self.dayun_dict[self.dayun] = self.dayun_year
                # print(self.dayun_dict)
        # print(self.sex, type(self.sex))
        return self.dayun_dict, self.qiyun_year



    def pre_Bazi_words(self):   #  输出文字版八字程序，元祖序列[0]为八字，排列为年干，年支，月干，月支，日干，日支，时
        # 干，时支。元祖序列[1]为空亡
        self.Time()
        res = [self.tiangan_year , self.dizhi_year , self.tiangan_month , self.dizhi_month , self.tiangan_day ,\
              self.dizhi_day , self.tiangan_hour , self.dizhi_hour]
        res_kw = [self.kongwang1 , self.kongwang2]
        # print(type(self.tiangan_year))
        return res , res_kw


class Bazi_Number(BaziPaipan):  #   输出数字版八字程序，元祖序列[0]为八字，排列为年干，年支，月干，月支，日干，日支，时
        # 干，时支。元祖序列[1]为空亡

    __tgdz = ["占","甲","乙","丙","丁","戊","己","庚","辛","壬","癸","子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

    def Bazi_Num(self):   #   输出数字版八字程序
        super().Time()
        super().pre_Bazi_words()
        res = [self.__tgdz.index(self.tiangan_year) , self.__tgdz.index(self.dizhi_year) , self.__tgdz.index(self.tiangan_month) , self.__tgdz.index(self.dizhi_month) , self.__tgdz.index(self.tiangan_day) , \
              self.__tgdz.index(self.dizhi_day) , self.__tgdz.index(self.tiangan_hour) , self.__tgdz.index(self.dizhi_hour)]
        res_kw = [self.__tgdz.index(self.kongwang1) , self.__tgdz.index(self.kongwang2)]

        return res , res_kw


class TenGods(object):   # 输出十神，十神为文字版和数字版，"比肩","劫财","食神","伤官","偏财","正财","偏官","正官","偏印","正印"分别为0-9

    def __init__(self,dayself, *args):

        self.dayself = dayself
        self.args = args
        self.__tengod = [("比肩","劫财"),("食神","伤官"),("偏财","正财"),("偏官","正官"),("偏印","正印")]
        self.__tengod_num = ["比肩","劫财","食神","伤官","偏财","正财","偏官","正官","偏印","正印"]
        # self.__tgdz = ["占","甲","乙","丙","丁","戊","己","庚","辛","壬","癸","子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
        self.__tiangandizhi = {"1":2,"2":2,"13":2,"14":2,"3":3,"4":3,"16":3,"17":3,"7":5,"8":5,"19":5,"20":5,"9":1,"10":1,"22":1,"11":1,"5":4,"6":4,
                      "15":4,"21":4,"12":4,"18":4}
        self.__teng = []
        self.__teng_num = []

    def Status(self): # 元祖输入只支持数字，所以甲-癸由1-10表示，子-亥由11-22表示
        # print(self.args,self.dayself,type(self.args),type(self.dayself))
        for item in self.args:
            shengke = (self.__tiangandizhi[str(item)] - self.__tiangandizhi[str(self.dayself)] + 5) % 5
            # print(shengke)
            if abs(self.dayself - item) % 2 == 0:
                self.tengods = self.__tengod[shengke][0]
            elif abs(self.dayself - item) % 2 == 1:
                self.tengods = self.__tengod[shengke][1]
            self.__teng.append(self.tengods)
            self.__teng_num.append(self.__tengod_num.index(self.tengods))
        # print(self.__teng)
        return self.__teng,self.__teng_num

class WuxingWangshuai(object):  #  输出五行旺衰主程序，列表形式输出，甲-癸为1-10，子-亥为11-22，输出列表前者为旺的天干
    # 地支，后者为衰的天干地支

    def __init__(self,y,m,d):

        self.__Li = [19700204, 19700506, 19700808, 19701108, 19710204, 19710506, 19710808, 19711108, 19720205, 19720505,
                19720807, 19721107, 19730204, 19730505, 19730808, 19731107, 19740204, 19740506, 19740808, 19741108,
                19750204, 19750506, 19750808, 19751108, 19760205, 19760505, 19760807, 19761107, 19770204, 19770505,
                19770807, 19771107, 19780204, 19780506, 19780808, 19781108, 19790204, 19790506, 19790808, 19791108,
                19800205, 19800505, 19800807, 19801107, 19810204, 19810505, 19810807, 19811107, 19820204, 19820506,
                19820808, 19821108, 19830204, 19830506, 19830808, 19831108, 19840204, 19840505, 19840807, 19841107,
                19850204, 19850505, 19850807, 19851107, 19860204, 19860506, 19860808, 19861108, 19870204, 19870506,
                19870808, 19871108, 19880204, 19880505, 19880807, 19881107, 19890204, 19890505, 19890807, 19891107,
                19900204, 19900506, 19900808, 19901108, 19910204, 19910506, 19910808, 19911108, 19920204, 19920505,
                19920807, 19921107, 19930204, 19930505, 19930807, 19931107, 19940204, 19940506, 19940808, 19941107,
                19950204, 19950506, 19950808, 19951108, 19960204, 19960505, 19960807, 19961107, 19970204, 19970505,
                19970807, 19971107, 19980204, 19980506, 19980808, 19981107, 19990204, 19990506, 19990808, 19991108,
                20000204, 20000505, 20000807, 20001107, 20010204, 20010505, 20010807, 20011107, 20020204, 20020506,
                20020808, 20021107, 20030204, 20030506, 20030808, 20031108, 20040204, 20040505, 20040807, 20041107,
                20050204, 20050505, 20050807, 20051107, 20060204, 20060505, 20060807, 20061107, 20070204, 20070506,
                20070808, 20071108, 20080204, 20080505, 20080807, 20081107, 20090204, 20090505, 20090807, 20091107,
                20100204, 20100505, 20100807, 20101107, 20110204, 20110506, 20110808, 20111108, 20120204, 20120505,
                20120807, 20121107, 20130204, 20130505, 20130807, 20131107, 20140204, 20140505, 20140807, 20141107,
                20150204, 20150506, 20150808, 20151108, 20160204, 20160505, 20160807, 20161107, 20170203, 20170505,
                20170807, 20171107, 20180204, 20180505, 20180807, 20181107, 20190204, 20190506, 20190808, 20191108,
                20200204, 20200505, 20200807, 20201107, 20210203, 20210505, 20210807, 20211107, 20220204, 20220505,
                20220807, 20221107, 20230204, 20230506, 20230808, 20231108, 20240204, 20240505, 20240807, 20241107,
                20250203, 20250505, 20250807, 20251107, 20260204, 20260505, 20260807, 20261107, 20270204, 20270506,
                20270808, 20271107, 20280204, 20280505, 20280807, 20281107, 20290203, 20290505, 20290807, 20291107,
                20300204, 20300505, 20300807, 20301107]  # 1960到2030年的立春立夏立冬立秋,一共284个

        self.__Jijie = {1: '春天',2: '夏天',3: '秋天',0: '冬天'}
        self.__Season_GZ = {1:[1,2,13,14],2:[3,4,5,6,12,15,16,17,18,21],3:[7,8,19,20],0:[9,10,11,22]}

        self.year = y
        self.month = m
        self.day = d
        self.wang = []
        self.shuai = []

    def Season(self):  #  求出季节
        self.celander = self.year * 10000 + self.month * 100 + self.day
        if self.celander in self.__Li:
            self.celander = int(self.celander + 1)
            self.result = int(self.__Li.index(self.celander))
        elif self.celander not in self.__Li:
            self.__Li.append(self.celander)
            self.__Li.sort()
            self.result = int(self.__Li.index(self.celander))

        self.final_result = self.result % 4
        self.season_result = self.__Jijie[self.final_result]

        return self.season_result
    def Judge_WangShuai(self, *args):  #  各季节中五行的旺衰
        d.Season()
        self.season = self.__Season_GZ[self.final_result]
        self.args = args
        for item in self.args:
            if item in self.season:
                self.wang.append(item)
            elif item not in self.season:
                self.shuai.append(item)

        # print(self.wang,self.shuai)
        return self.wang,self.shuai

class MeihuaPaipan(object):  #  梅花易数排盘，输出三个列表，列表[0]为本卦，[1]为互卦，[2]为变卦，每一个小列表中，[0]为上卦，[1]为下卦
    #由乾到坤按照先天八卦顺序排列，序号为1-8

    def __init__(self):

        self.bgshang_fianl = []
        self.bgxia_final = []
        self.hgshang_final = []
        self.hgxia_final = []
        self.bg_shang_final = []
        self.bg_xia_final = []
        self.__BaGua = ([1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0])
        self.__ZhongWen = ('乾☰', '兑☱', '离☲', '震☳', '巽☴', '坎☵', '艮☶', '坤☷')
        self.__BaGua1 = ([1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0])

    def Paipan(self, num_one, num_two, num_three):

        self.num_one = (num_one - 1) % 8
        self.num_two = (num_two - 1) % 8
        self.bengua_shang = self.__BaGua[self.num_one]
        self.bengua_xia = self.__BaGua[self.num_two]

        self.hugua_xia = self.bengua_xia + self.bengua_shang
        # print("互卦是： %s" % self.hugua_xia)
        self.hugua_xia = self.hugua_xia[1:4]
        self.hugua_shang = self.bengua_xia + self.bengua_shang
        self.hugua_shang = self.hugua_shang[2:5]
        self.__BenGuaShangGua = self.bengua_shang
        self.__BenGuaXiaGua = self.bengua_xia
        self.__HuGuaShangGua = self.hugua_shang
        self.__HuGuaXiaGua = self.hugua_xia

        if self.bengua_shang in self.__BaGua:
            self.bgshang = int(self.__BaGua.index(self.bengua_shang))
            # print(self.bgshang)
            self.bgshang_final = self.__ZhongWen[self.bgshang]

        if self.bengua_xia in self.__BaGua:
            self.bgxia = int(self.__BaGua.index(self.bengua_xia))
            # print(self.bgxia)
            self.bgxia_final = self.__ZhongWen[self.bgxia]

        if self.hugua_shang in self.__BaGua:
            self.hgshang = int(self.__BaGua.index(self.hugua_shang))
            # print(self.hgshang)
            self.hgshang_final = self.__ZhongWen[self.hgshang]

        if self.hugua_xia in self.__BaGua:
            self.hgxia = int(self.__BaGua.index(self.hugua_xia))
            # print(self.hgxia)
            self.hgxia_final = self.__ZhongWen[self.hgxia]

    # def Num_Three(self, num_three):
        self.num_three = num_three % 6
        self.biangua_shang = self.bengua_shang[:]
        self.biangua_xia = self.bengua_xia[:]
        if 4 <= self.num_three <= 5:
            self.num_three = self.num_three - 4
            if self.biangua_shang[self.num_three] == 0:
                self.biangua_shang[self.num_three] = 1
            else:
                self.biangua_shang[self.num_three] = 0
        elif self.num_three == 0:
            self.num_three = self.num_three + 2
            if self.biangua_shang[self.num_three] == 0:
                self.biangua_shang[self.num_three] = 1
            else:
                self.biangua_shang[self.num_three] = 0
        else:
            self.num_three = self.num_three - 1
            if self.biangua_xia[self.num_three] == 0:
                self.biangua_xia[self.num_three] = 1
            else:
                self.biangua_xia[self.num_three] = 0

        if self.biangua_shang in self.__BaGua1:
            self.bg_shang = int(self.__BaGua1.index(self.biangua_shang))
            # print(self.bg_shang)
            self.bg_shang_final = self.__ZhongWen[self.bg_shang]

        if self.biangua_xia in self.__BaGua1:
            self.bg_xia = int(self.__BaGua1.index(self.biangua_xia))
            # print(self.bg_xia)
            self.bg_xia_final = self.__ZhongWen[self.bg_xia]

        # print(self.bgshang_final,self.bgxia_final,  self.hgshang_final, self.hgxia_final,self.bg_shang_final,  self.bg_xia_final)

        self.bengua_end = [self.__ZhongWen.index(self.bgshang_final) + 1,self.__ZhongWen.index(self.bgxia_final)+1]
        self.hugua_end = [self.__ZhongWen.index(self.hgshang_final)+ 1,self.__ZhongWen.index(self.hgxia_final)+ 1]
        self.biangua_end = [self.__ZhongWen.index(self.bg_shang_final)+ 1,self.__ZhongWen.index(self.bg_xia_final)+ 1]
        #
        return self.bengua_end,self.hugua_end,self.biangua_end


class Gua_Wangshuai(object): # 专门计算八卦的旺衰，由乾到坤按照先天八卦顺序排列，序号为1-8

    def __init__(self):

        self.__Li = [19600205, 19600505, 19600807, 19601107, 19610204, 19610506, 19610808, 19611107, 19620204, 19620506,
                19620808, 19621108, 19630204, 19630506, 19630808, 19631108, 19640205, 19640505, 19640807, 19641107,
                19650204, 19650506, 19650808, 19651107, 19660204, 19660506, 19660808, 19661108, 19670204, 19670506,
                19670808, 19671108, 19680205, 19680505, 19680807, 19681107, 19690204, 19690506, 19690808, 19691107,
                19700204, 19700506, 19700808, 19701108, 19710204, 19710506, 19710808, 19711108, 19720205, 19720505,
                19720807, 19721107, 19730204, 19730505, 19730808, 19731107, 19740204, 19740506, 19740808, 19741108,
                19750204, 19750506, 19750808, 19751108, 19760205, 19760505, 19760807, 19761107, 19770204, 19770505,
                19770807, 19771107, 19780204, 19780506, 19780808, 19781108, 19790204, 19790506, 19790808, 19791108,
                19800205, 19800505, 19800807, 19801107, 19810204, 19810505, 19810807, 19811107, 19820204, 19820506,
                19820808, 19821108, 19830204, 19830506, 19830808, 19831108, 19840204, 19840505, 19840807, 19841107,
                19850204, 19850505, 19850807, 19851107, 19860204, 19860506, 19860808, 19861108, 19870204, 19870506,
                19870808, 19871108, 19880204, 19880505, 19880807, 19881107, 19890204, 19890505, 19890807, 19891107,
                19900204, 19900506, 19900808, 19901108, 19910204, 19910506, 19910808, 19911108, 19920204, 19920505,
                19920807, 19921107, 19930204, 19930505, 19930807, 19931107, 19940204, 19940506, 19940808, 19941107,
                19950204, 19950506, 19950808, 19951108, 19960204, 19960505, 19960807, 19961107, 19970204, 19970505,
                19970807, 19971107, 19980204, 19980506, 19980808, 19981107, 19990204, 19990506, 19990808, 19991108,
                20000204, 20000505, 20000807, 20001107, 20010204, 20010505, 20010807, 20011107, 20020204, 20020506,
                20020808, 20021107, 20030204, 20030506, 20030808, 20031108, 20040204, 20040505, 20040807, 20041107,
                20050204, 20050505, 20050807, 20051107, 20060204, 20060505, 20060807, 20061107, 20070204, 20070506,
                20070808, 20071108, 20080204, 20080505, 20080807, 20081107, 20090204, 20090505, 20090807, 20091107,
                20100204, 20100505, 20100807, 20101107, 20110204, 20110506, 20110808, 20111108, 20120204, 20120505,
                20120807, 20121107, 20130204, 20130505, 20130807, 20131107, 20140204, 20140505, 20140807, 20141107,
                20150204, 20150506, 20150808, 20151108, 20160204, 20160505, 20160807, 20161107, 20170203, 20170505,
                20170807, 20171107, 20180204, 20180505, 20180807, 20181107, 20190204, 20190506, 20190808, 20191108,
                20200204, 20200505, 20200807, 20201107, 20210203, 20210505, 20210807, 20211107, 20220204, 20220505,
                20220807, 20221107, 20230204, 20230506, 20230808, 20231108, 20240204, 20240505, 20240807, 20241107,
                20250203, 20250505, 20250807, 20251107, 20260204, 20260505, 20260807, 20261107, 20270204, 20270506,
                20270808, 20271107, 20280204, 20280505, 20280807, 20281107, 20290203, 20290505, 20290807, 20291107,
                20300204, 20300505, 20300807, 20301107]  # 1960到2030年的立春立夏立冬立秋,一共284个

        self.__Jijie = {1: '春天',
                   2: '夏天',
                   3: '秋天',
                   0: '冬天'}

        self.__LeiXiang = {1: [4, 5, 3], 2: [3, 7, 8], 3: [1, 2, 6], 0: [6, 4, 5]}
        self.today_time = time.time()
        self.final_time = time.strftime('20%y-%m-%d', time.localtime(self.today_time))

        date = self.final_time.split("-")
        self.year = int(date[0])
        self.month = int(date[1])
        self.day = int(date[2])
        self.qiang = []
        self.ruo = []

    def Season(self):  # 求出季节
        self.celander = self.year * 10000 + self.month * 100 + self.day
        if self.celander in self.__Li:
            self.celander = self.celander + 1
        self.int_celander = int(self.celander)
        self.__Li.append(self.int_celander)
        self.__Li.sort()
        self.result = int(self.__Li.index(self.int_celander))
        self.final_result = self.result % 4
        self.__Li.remove(self.int_celander)

        return self.__Jijie[self.final_result]

    def Judge_WangShuai(self, *args):  # 各季节中八卦的旺衰
        self.Season()
        self.season = self.__LeiXiang[self.final_result]
        # print(self.season)
        self.args = args
        for self.item in self.args:
            if self.item in self.season:
                self.qiang.append(self.item)

            else:
                self.ruo.append(self.item)

        return (self.qiang, self.ruo)


if __name__ == '__main__':
    a = Bazi_Number(1988,8,6,9)
    a1 = a.Bazi_Num()
    print(a1)
    b = BaziPaipan(1988,8,6,9)

    b1 = b.pre_Bazi_words()
    print(b1)
    c = TenGods(a1[0][4],a1[0][1],a1[0][2])
    print(c.Status())
    d = WuxingWangshuai(1988,8,6)
    d1 = d.Judge_WangShuai(3,6,4,15,19)
    print(d1)
    e = BaziPaipan(1988,8,6,9)
    e1 = e.QiYun("男")
    print(e1)
    f = Gua_Wangshuai()
    f1 = f.Judge_WangShuai(4,5,6,7)
    print(f1)
    g = MeihuaPaipan()
    g1 = g.Paipan(257,588,634)
    print(g1)
