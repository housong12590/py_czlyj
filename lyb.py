# -*- coding: utf-8 -*-

import requests
import random
import json
from urllib import parse
import time
import base64
import os

api = r'http://www.lyb520.com/api/login_api/'

ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')


def makeNew():
    u''' 随机生成新的18为身份证号码 '''
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                          random.randint(1, 99),
                                          random.randint(1, 99),
                                          random.randint(t - 80, t - 18),
                                          random.randint(1, 12),
                                          random.randint(1, 28),
                                          random.randint(1, 999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    return '%s%s' % (x, LAST[y % 11])


def get_constellation(month, date):
    dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    constellations = ("摩羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子", "处女", "天秤", "天蝎", "射手", "摩羯")
    if date < dates[month - 1]:
        return constellations[month - 1]
    else:
        return constellations[month]


def chinese_zodiac(year):
    return u'猴鸡狗猪鼠牛虎兔龙蛇马羊'[year % 12]


def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150",
               "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


def createQQ():
    return "".join(random.choice("0123456789") for i in range(9))


class script:
    def __init__(self, account, name):
        self.account = account
        self.info = {}
        self.index = 2
        self.name = name

    # 注册
    def register(self, ):
        print("register")
        params = {
            'action': 'adduserinfo',
            'account': self.name,
            'email': self.account,
            'password': '111111'
        }
        self.info[
            "01"] = "---------------------------------账号信息----------------------------------------"
        self.info['账号'] = self.account
        self.info['姓名'] = self.name
        result = requests.post(api, params)
        self.resp_check(result)

    # 性别
    def gender(self):
        print("gender")
        self.g = random.randint(1, 2)
        params = {
            'action': 'gender',
            'username': self.account,
            'gender': self.g
        }

        if self.g == 1:
            temp = '男'
        else:
            temp = '女'
        self.info['性别'] = temp
        result = requests.post(api, params)
        self.resp_check(result)

    # 婚姻状态
    def marital(self):
        print("marital")
        status = random.randint(1, 3)
        params = {
            'action': 'marital',
            'username': self.account,
            'marital': status,
        }
        if status == 1:
            temp = '未婚'
        elif status == 2:
            temp = '离婚'
        elif status == 3:
            temp = '丧偶'
        else:
            temp = '分居'
        self.info['婚姻状态'] = temp
        result = requests.post(api, params)
        self.resp_check(result)

    # 个人基本资料
    def profile(self):
        print("profile")
        self.info[
            "02"] = "---------------------------------个人资料----------------------------------------"
        self.age = random.randint(18, 32)
        # 是否有小孩
        # child = random.randint(1, 2)
        child = 1
        if child == 1:
            child_follow = random.randint(0, 1)
            if child_follow == 0:
                childText = '有小孩-跟我'
            else:
                childText = '有小孩-跟对方'
        else:
            child_follow = ''
            childText = '没有小孩'

        if self.g == 1:  # 男
            self.height = random.randint(160, 185)
        else:
            self.height = random.randint(155, 175)
        self.info['是否有小孩'] = childText
        # 住房情况
        housingList = ['', '有房', '购房按揭中', '和家人同住', '单位宿舍', '租房']
        housing = random.randint(1, 5)

        # 职位
        jobList = ['', '单位负责人', '高管', '中层管理', '单位职员', '工人', '务农', '自由职业', '其他']
        job = random.randint(3, 6)

        # 宗教信仰
        religionList = ['', '无宗教信仰', '佛教', '基督教', '天主教', '伊斯兰教', '其他宗教']
        religion = random.randint(1, 5)

        # 作息时间
        scheduleList = ['', '正常作息', '经常加班', '经常出差', '应酬较多', '轮班制']
        schedule = random.randint(1, 4)

        # 体重
        if self.g == 1:
            weight = random.randint(50, 90)
        else:
            weight = random.randint(40, 65)

        # 是否愿意去对方城市
        willingtocityList = ['', '不愿意', '视情况而定', '愿意']
        willingtocity = random.randint(1, 3)

        # 教育学历
        educationalList = ['', '博士(及以上)', '硕士', '本科', '大专', '高中(中专)', '初中(及以下)']
        educational = random.randint(1, 6)

        income = random.randint(3000, 20000)

        familyList = ['', "独生子女", '2个', '3个', '4个及以上']
        family = random.randint(1, 4)
        params = {
            'action': 'profile',
            'username': self.account,
            'address_city': '南京',
            'address_province': '江苏',
            'age': str(self.age),
            'child': str(child),
            'child_follow': str(child_follow),
            'height': str(self.height),
            'hometown_city': '南京',
            'hometown_province': '江苏',
            'housing': str(housing),
            'job': str(job),
            'religion': str(religion),
            'schedule': str(schedule),
            'weight': str(weight),
            'willingtocity': str(willingtocity),
            'educational': str(educational),
            'income': str(income),
            'family': family

        }
        result = requests.post(api, params)
        self.info['年龄'] = self.age
        self.info['体重'] = weight
        self.info['身高'] = self.height
        self.info['月收入'] = income
        self.info['住房情况'] = housingList[housing]
        self.info['职位'] = jobList[job]
        self.info['宗教信仰'] = religionList[religion]
        self.info['作息时间'] = scheduleList[schedule]
        self.info['是否愿意去对方城市'] = willingtocityList[willingtocity]
        self.info['教育学历'] = educationalList[educational]
        self.info['家乡'] = '江苏 南京'
        self.info['现居住地'] = '江苏 南京'
        self.info['兄弟姐妹几人'] = familyList[family]
        self.resp_check(result)

    def spouseInformation(self):
        print("spouseInformation")
        self.info[
            "03"] = "---------------------------------择偶要求----------------------------------------"
        if self.g == 1:
            if self.age - 10 < 18:
                min_age = 18
            else:
                min_age = self.age - 10

            if self.age - 3 < 18:
                max_age = 18
            else:
                max_age = self.age - 3
            ta_age = '%d,%d' % (min_age, max_age)
            ta_height = '%d,%d' % (self.height - 17, self.height - 7)
        else:
            ta_age = '%d,%d' % (self.age + 3, self.age + 10)
            ta_height = '%d,%d' % (self.height + 7, self.height + 17)

        # 教育程度
        ta_educationList = ["", "不限", "博士(及以上)", "硕士", "本科", "大专", "高中(中专)", "初中(及以下)"]
        # ta_education = random.randint(1, 7)
        ta_education = 1

        # 住房情况
        ta_housingList = ["", "不限", "有房", "购房按揭中", "和家人同住", "单位宿舍", "租房"]
        # ta_housing = random.randint(1, 6)
        ta_housing = 1

        # 地理位置
        ta_locationList = ["不限", "同城", "同乡", "同省", "国内"]
        # ta_location = random.randint(0, 4)
        ta_location = 0

        # 婚姻状况
        ta_maritalList = ["不限", "未婚", "离异", "丧偶"]
        # ta_marital = random.randint(0, 3)
        ta_marital = 0

        # 信仰范围
        ta_religionList = ["", "不限", "无宗教信仰", "佛教", "基督教", "天主教", "伊斯兰教", "其他宗教"]
        # ta_religion = random.randint(1, 7)
        ta_religion = 1

        # 是否接受他有小孩
        ta_childList = ["", "是", "否", "视情况而定"]
        ta_child = random.randint(1, 3)

        ta_income = random.randint(2000, 5000)
        params = {
            'action': 'spouseInformation',
            'username': self.account,
            'ta_age': ta_age,
            'ta_height': ta_height,
            'ta_education': ta_education,
            'ta_housing': ta_housing,
            'ta_location': ta_location,
            'ta_marital': ta_marital,
            'ta_religion': ta_religion,
            'ta_child': ta_child,
            'ta_income': ta_income
        }
        self.info['年龄范围'] = ta_age
        self.info['身高范围'] = ta_height
        self.info['对方教育程度'] = ta_educationList[ta_education]
        self.info['对方住房情况'] = ta_housingList[ta_housing]
        self.info['对方地理位置'] = ta_locationList[ta_location]
        self.info['对方婚姻状况'] = ta_maritalList[ta_marital]
        self.info['对方信仰范围'] = ta_religionList[ta_religion]
        self.info['是否接受他有小孩'] = ta_childList[ta_child]
        self.info['对方收入'] = ta_income
        result = requests.post(api, params)
        self.resp_check(result)

    def first_answer(self):
        print("first_answer")
        self.info[
            "04"] = "---------------------------------性格特点----------------------------------------"
        with open('answer_first.json', 'r', encoding='utf-8') as f:
            file_list = json.load(f)
            for i in file_list:
                h_answer = random.randint(1, 7)
                i_answer = random.randint(1, 7)
                params = {
                    'action': 'uploadquestion',
                    'username': self.account,
                    'h_answer': h_answer,
                    'i_answer': i_answer,
                    'number': self.index
                }
                self.index = self.index + 1
                self.info['.%s' % i[1]] = "%d , %d " % (i_answer, h_answer)
                result = requests.post(api, params)
                self.resp_check(result)
            select = random.randint(1, len(file_list) - 1)

            self.importantQuestion(1, str(select))

    def second_answer(self):
        print("second_answer")
        self.info[
            "05"] = "---------------------------------关系互动----------------------------------------"
        with open('answer_second.json', 'r', encoding='utf-8') as f:
            file_list = json.load(f)
            for i in file_list:
                # h_answer = random.randint(1, 7)
                i_answer = random.randint(1, 7)
                params = {
                    'action': 'uploadquestion',
                    'username': self.account,
                    'h_answer': '',
                    'i_answer': i_answer,
                    'number': self.index
                }
                self.index = self.index + 1
                self.info[',%s' % i[1]] = "%d  " % (i_answer)
                result = requests.post(api, params)
                self.resp_check(result)
            select = random.randint(1, len(file_list) - 1)

            self.importantQuestion(2, str(select))

    def third_answer(self):
        print("third_answer")
        self.info[
            "06"] = "---------------------------------人生价值观一----------------------------------------"
        with open('answer_third.json', 'r', encoding='utf-8') as f:
            file_list = json.load(f)
            for i in file_list:
                # h_answer = random.randint(1, 7)
                i_answer = random.randint(1, 7)
                params = {
                    'action': 'uploadquestion',
                    'username': self.account,
                    'h_answer': '',
                    'i_answer': i_answer,
                    'number': self.index
                }
                self.index = self.index + 1
                self.info['`%s' % i[1]] = "%d  " % (i_answer)
                result = requests.post(api, params)
                self.resp_check(result)
            select = random.randint(1, len(file_list) - 1)

            self.importantQuestion(3, str(select))

    def four_answer(self):
        print("four_answer")
        with open('answer_four.json', 'r', encoding='utf-8') as f:
            file_list = json.load(f)
            self.info[
                '07'] = "---------------------------------人生价值观二----------------------------------------"
            for i in file_list:
                # h_answer = random.randint(1, 7)
                i_answer = random.randint(1, 7)
                params = {
                    'action': 'uploadquestion',
                    'username': self.account,
                    'h_answer': '',
                    'i_answer': i_answer,
                    'number': self.index
                }
                self.index = self.index + 1
                self.info['!%s' % i[1]] = "%d  " % (i_answer)
                result = requests.post(api, params)
                self.resp_check(result)
            select = random.randint(1, len(file_list) - 1)

            self.importantQuestion(4, str(select))

    def importantQuestion(self, type, select):
        # self.info[
        #     select] = "---------------------------------重点题----------------------------------------"
        print("importantQuestion")
        params = {
            'action': 'importantQuestion',
            'username': self.account,
            'type': type,
            'selected': select
        }
        result = requests.post(api, params)
        self.resp_check(result)

    def hobby(self):
        print("hobby")

        anjingList = ["读书", "听音乐", "看报", "品茶", "乐器", "烹饪", "手工制作", "游戏", "收藏", "看电视", "网络分享", "咖啡",
                      "写作", "书法绘画"]
        anjing = self.content(anjingList)

        foodList = ["清淡", "偏咸", "偏辣", "素食", "鱼", "不忌口", "偏甜", "偏麻", "偏酸", "肉食", "海鲜", "都行",
                    # "网上购物"
                    ]
        food = self.content(foodList)

        zuoxishijianList = ["早睡早起", "夜猫子", "睡得较晚", "没规律"]
        zuoxishijian = zuoxishijianList[random.randint(0, 3)]

        xiuxianList = ["园艺", "跳舞", "朋友聚会", "下棋", "听音乐会", "看球赛", "动物园", "图书馆", "展会", "钓鱼", "志愿者活动",
                       "美食", "唱歌KTV", "打牌", "逛街购物", "看演出", "散步", "游乐场", "博物馆", "教堂", "摄影"]
        xiuxian = self.content(xiuxianList)

        sportsList = ["瑜伽", "健身/跑步", "赛车", "兵乓球", "健美操", "排球", "保龄球", "滑雪/溜冰", "游泳", "单车", "羽毛球",
                      "网球", "足球", "篮球", "高尔夫", "极限运动"]
        sports = self.content(sportsList)

        travelList = ["自驾游", "繁华都市", "古迹", "崇山峻岭", "沙漠", "田园风光", "特色小镇", "海边岛屿", "草原"]
        trave = self.content(travelList)

        petList = ["狗", "鸟", "乌龟", "兔", "猫", "鱼", "鼠"]
        pet = self.content(petList)

        params = {
            'action': 'hobby',
            'username': self.account,
            'anjing': anjing,
            'xiuxian': xiuxian,
            'sports': sports,
            'travel': trave,
            'pet': pet,
            'food': food,
            'zuoxishijian': zuoxishijian
        }
        self.info[
            '08'] = "---------------------------------兴趣爱好----------------------------------------"
        self.info["喜欢安静"] = anjing
        self.info["户外休闲"] = xiuxian
        self.info["体育运动"] = sports
        self.info["喜欢旅游"] = trave
        self.info["喜欢宠物"] = pet
        self.info["饮食习惯"] = food
        self.info["作息时间"] = zuoxishijian
        result = requests.post(api, params)
        self.resp_check(result)

    def familychooselist(self):
        print('familychooselist')
        self.info[
            '09'] = "---------------------------------家庭背景----------------------------------------"

        childhoodList = ["", "农村", "乡镇", "县城", "地级市", "大都市", "一线城市"]

        jobList = ["", "无固定职业", "务农", "工人", "单位职员", "中层管理", "高管", "单位负责人"]

        economyList = ["", "贫困", "低收入", "工薪", "小资", "中产", "富裕", "富豪"]

        guardianList = ["", "父母", "祖辈", "单亲", "单亲和长辈", "其他"]

        childhood = random.randint(1, 6)
        economy = random.randint(1, 7)
        fatherjob = random.randint(1, 7)
        motherjob = random.randint(1, 7)
        guardian = random.randint(1, 5)
        params = {
            'action': 'familychooselist',
            'username': self.account,
            'childhood': childhood,
            'economy': economy,
            'fatherjob': fatherjob,
            'motherjob': motherjob,
            'guardian': guardian
        }
        self.info['自幼生活在'] = childhoodList[childhood]
        self.info['父亲职业'] = jobList[fatherjob]
        self.info['母亲职业'] = jobList[motherjob]
        self.info['经济状况'] = economyList[economy]
        self.info['主要监护人'] = guardianList[guardian]
        result = requests.post(api, params)
        self.resp_check(result)

    def familychoose(self):
        self.info[
            '10'] = "---------------------------------成长环境----------------------------------------"
        print('familychoose')
        with open('answer_final.json', 'r', encoding='utf-8') as f:
            file_list = json.load(f)
            for i in file_list:
                affection = ''
                communicate = ''
                upbringing = ''
                houswork = ''
                if i == '父母感情':
                    affection = random.randint(1, 7)
                    self.info[i] = affection
                elif i == '和监护人的沟通':
                    communicate = random.randint(1, 7)
                    self.info[i] = communicate
                elif i == '家教家规':
                    upbringing = random.randint(1, 7)
                    self.info[i] = upbringing
                elif i == '家务劳动':
                    houswork = random.randint(1, 7)
                    self.info[i] = houswork
                params = {
                    'action': 'familychoose',
                    'username': self.account,
                    'affection': affection,
                    'communicate': communicate,
                    'upbringing': upbringing,
                    'houswork': houswork
                }
                result = requests.post(api, params)
                self.resp_check(result)

    def updatephoto(self):
        self.info[
            '11'] = "---------------------------------上传照片----------------------------------------"
        print('updatephoto')
        number = random.randint(3, 9)
        image_base64 = self.image_to_base64(number)
        params = {
            'action': 'updatephoto',
            'username': self.account,
            'base64_image_content': image_base64
        }
        result = requests.post(api, params)
        self.resp_check(result)

    def personalData(self):
        self.info[
            '12'] = "---------------------------------联系方式----------------------------------------"
        print('personalData')
        image_base64 = self.idcrad_ptoto()
        idcard = makeNew()
        year = idcard[6:10]
        month = idcard[10:12]
        day = idcard[12:14]
        birthday = '%s-%s-%s' % (year, month, day)
        xinzuo = get_constellation(int(month), int(day))
        shuxiang = chinese_zodiac(int(year))
        telephone = createPhone()
        qq = createQQ()
        params = {
            'action': 'personalData',
            'username': self.account,
            'idphoto': image_base64,
            'birthday': birthday,
            'email': str(self.account),
            'qq': str(qq),
            'mobile': str(telephone),
            'telephone': str(telephone),
            'xinzuo': xinzuo,
            'shuxiang': shuxiang,
            'idcardnr': str(idcard),
            'name': self.name,
        }
        self.info['身份证号'] = idcard
        self.info['生日'] = birthday
        self.info['邮箱'] = self.account
        self.info['QQ'] = qq
        self.info['电话号码'] = telephone
        self.info['星座'] = xinzuo
        self.info['名字'] = self.account
        self.info['属相'] = shuxiang
        result = requests.post(api, params)
        self.resp_check(result)

    def date(self):
        params = {
            'action': 'date',
            'username': self.account
        }
        result = requests.post(api, params)
        self.resp_check(result)

    def idcrad_ptoto(self):
        image_path = r'%s\image\idcard_photo.jpg' % os.getcwd()
        with open(image_path, 'rb') as f:
            image_base64 = '%s' % str(base64.b64encode(f.read()), encoding='utf-8')
        self.info['身份证照片'] = image_path
        return image_base64

    def image_to_base64(self, number):
        image_path = r'%s\image' % os.getcwd()
        image_base64 = ''
        image_list = os.listdir(image_path)
        for i in [random.randint(0, len(image_list) - 1) for _ in range(number)]:
            p = os.path.join(image_path, image_list[i])
            print(p)
            self.info[p] = ' ~'
            with open(p, 'rb') as f:
                image_base64 += '%s&' % str(base64.b64encode(f.read()), encoding='utf-8')
        return image_base64[:len(image_base64) - 1]

    def resp_check(self, result):
        print(parse.unquote(result.request.body))
        print(result.text)
        if result.json()['res'] == 0:
            return True
        else:
            raise Exception('请求失败')

            # try:
            #     j = result.json()
            #     if j['res'] == 0:
            #         return True
            #     else:
            #         print(result.url, "-------------------请求重试-------------------------")
            #         result = requests.post(api, result.request.body)
            #         self.resp_check(result)
            #         return False
            # except Exception as e:
            #     print(e)

            # raise Exception(result.url)

    def content(self, list):
        r = random.randint(1, 5)
        anjing = ''
        for i in set(random.randint(0, len(list) - 1) for _ in range(r)):
            anjing += '%s,' % list[i]
        return anjing[0: len(anjing) - 1]

    def main(self):

        self.register()

        self.gender()

        self.marital()

        self.profile()

        self.spouseInformation()

        self.first_answer()

        self.second_answer()

        self.third_answer()

        self.four_answer()

        self.hobby()

        self.familychooselist()

        self.familychoose()

        # self.updatephoto()
        #
        # self.personalData()
        #
        # self.date()

        with open('account/%s.txt' % self.account, 'w', encoding='utf-8') as f:
            for key in self.info:
                f.write('%s  %s \n' % (key, self.info[key]))


# print(register('20171142@qq.com'))


if __name__ == '__main__':
    with open('name.json', 'r', encoding='utf-8') as f:
        for item in enumerate(json.load(f)):
            account = '0%03d@qq.com' % item[0]
            name = item[1]
            if item[0] == 23:
                s = script(account, name)
                s.main()
            elif item[0] > 23:
                break
    print('注册完成')
