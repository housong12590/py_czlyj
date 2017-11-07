import requests
import random
import json
from urllib import parse
import time

api = r'http://www.lyb520.com/api/login_api/'


class script:
    def __init__(self, account):
        self.account = account
        self.info = {}
        self.index = 2

    # 注册
    def register(self, ):
        print("register")
        params = {
            'action': 'adduserinfo',
            'account': self.account,
            'email': self.account,
            'password': '111111'
        }
        self.info['账号'] = self.account
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
        self.age = random.randint(18, 45)
        child = random.randint(1, 2)
        if child == 1:
            child_follow = random.randint(0, 1)
        else:
            child_follow = ''

        if self.g == 1:  # 男
            self.height = random.randint(160, 185)
        else:
            self.height = random.randint(155, 175)

        # 住房情况
        housingList = ['', '有房', '购房按揭中', '和家人同住', '单位宿舍', '租房']
        housing = random.randint(1, 5)

        # 职位
        jobList = ['', '单位负责人', '高管', '中层管理', '单位职员', '工人', '务农', '自由职业', '其他']
        job = random.randint(1, 8)

        # 宗教信仰
        religionList = ['', '无宗教信仰', '佛教', '基督教', '天主教', '伊斯兰教', '其他宗教']
        religion = random.randint(1, 6)

        # 作息时间
        scheduleList = ['', '正常作息', '经常加班', '经常出差', '应酬较多', '轮班制']
        schedule = random.randint(1, 5)

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

        income = random.randint(3000, 30000)

        family = random.randint(1, 4)
        familyList = ['', "独生子女", '2个', '3个', '4个及以上']
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
        self.info['住房情况'] = housingList[housing]
        self.info['职位'] = jobList[job]
        self.info['宗教信仰'] = religionList[religion]
        self.info['作息时间'] = scheduleList[schedule]
        self.info['体重'] = weight
        self.info['是否愿意去对方城市'] = willingtocityList[willingtocity]
        self.info['教育学历'] = educationalList[educational]
        self.info['家乡'] = '江苏 南京'
        self.info['现居住地'] = '江苏 南京'
        self.info['兄弟姐妹几人'] = familyList[family]
        self.resp_check(result)

    def spouseInformation(self):
        print("spouseInformation")
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
        ta_education = random.randint(1, 7)

        # 住房情况
        ta_housingList = ["", "不限", "有房", "购房按揭中", "和家人同住", "单位宿舍", "租房"]
        ta_housing = random.randint(1, 6)

        # 地理位置
        ta_locationList = ["不限", "同城", "同乡", "同省", "国内"]
        ta_location = random.randint(0, 4)

        # 婚姻状况
        ta_maritalList = ["不限", "未婚", "离异", "丧偶"]
        ta_marital = random.randint(0, 3)

        # 信仰范围
        ta_religionList = ["", "不限", "无宗教信仰", "佛教", "基督教", "天主教", "伊斯兰教", "其他宗教"]
        ta_religion = random.randint(1, 7)

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
        with open('answer_first.json', 'r', encoding='utf-8') as f:
            file_list = json.load(f)
            for i in file_list:
                time.sleep(0.5)
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
                self.info[i[1]] = "%d , %d " % (i_answer, h_answer)
                result = requests.post(api, params)
                self.resp_check(result)
            select = random.randint(0, len(file_list) - 1)
            time.sleep(0.5)
            self.importantQuestion(1, str(select))

    def second_answer(self):
        print("second_answer")
        with open('answer_second.json', 'r', encoding='utf-8') as f:
            file_list = json.load(f)
            for i in file_list:
                time.sleep(0.5)
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
                self.info[i[1]] = "%d  " % (i_answer)
                result = requests.post(api, params)
                self.resp_check(result)
            select = random.randint(0, len(file_list) - 1)
            time.sleep(0.5)
            self.importantQuestion(2, str(select))

    def third_answer(self):
        print("third_answer")
        with open('answer_third.json', 'r', encoding='utf-8') as f:
            file_list = json.load(f)
            for i in file_list:
                time.sleep(0.5)
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
                self.info[i[1]] = "%d  " % (i_answer)
                result = requests.post(api, params)
                self.resp_check(result)
            select = random.randint(0, len(file_list) - 1)
            time.sleep(0.5)
            self.importantQuestion(3, str(select))

    def four_answer(self):
        print("four_answer")
        with open('answer_four.json', 'r', encoding='utf-8') as f:
            file_list = json.load(f)
            for i in file_list:
                time.sleep(0.5)
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
                self.info[i[1]] = "%d  " % (i_answer)
                result = requests.post(api, params)
                self.resp_check(result)
            select = random.randint(0, len(file_list) - 1)
            time.sleep(0.5)
            self.importantQuestion(4, str(select))

    def importantQuestion(self, type, select):
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
        params = {
            'action': 'hobby',
            'username': self.account,
            'anjing': '读书,收藏',
            'xiuxian': '园艺,美食',
            'sports': '瑜伽,游泳',
            'travel': '自驾游,田园风光',
            'pet': '狗,猫',
            'food': '清淡,偏甜',
            'zuoxishijian': '早睡早起'
        }
        result = requests.post(api, params)
        self.resp_check(result)

    def familychooselist(self):
        print('familychooselist')
        params = {
            'action': 'familychooselist',
            'username': self.account,
            'childhood': '读书,收藏',
            'economy': '园艺,美食',
            'fatherjob': '瑜伽,游泳',
            'motherjob': '自驾游,田园风光',
            'guardian': '狗,猫'
        }
        result = requests.post(api, params)
        self.resp_check(result)

    def familychoose(self):
        print('familychoose')
        params = {
            'action': 'familychoose',
            'username': self.account,
            'affection': '读书,收藏',
            'communicate': '园艺,美食',
            'upbringing': '瑜伽,游泳',
            'houswork': '自驾游,田园风光'
        }
        result = requests.post(api, params)
        self.resp_check(result)

    def updatephoto(self):
        print('updatephoto')
        params = {
            'action': 'updatephoto',
            'username': self.account,
            'base64_image_content': '读书,收藏'
        }
        result = requests.post(api, params)
        self.resp_check(result)

    def personalData(self):
        print('personalData')
        params = {
            'action': 'personalData',
            'username': self.account,
            'idphoto': '读书,收藏',
            'birthday': '读书,收藏',
            'email': '读书,收藏',
            'qq': '读书,收藏',
            'mobile': '读书,收藏',
            'telephone': '读书,收藏',
            'xinzuo': '读书,收藏',
            'shuxiang': '读书,收藏',
            'idcardnr': '读书,收藏',
            'name': '读书,收藏',
        }
        result = requests.post(api, params)
        self.resp_check(result)

    def resp_check(self, result):
        print(parse.unquote(result.request.body))
        print(result.text)
        if result.json()['res'] == 0:
            return True
        else:
            raise Exception(result.url)

    def main(self):
        time.sleep(0.5)
        self.register()
        time.sleep(0.5)
        self.gender()
        time.sleep(0.5)
        self.marital()
        time.sleep(0.5)
        self.profile()
        time.sleep(0.5)
        self.spouseInformation()
        time.sleep(0.5)
        self.first_answer()
        time.sleep(0.5)
        self.second_answer()
        time.sleep(0.5)
        self.third_answer()
        time.sleep(0.5)
        self.four_answer()


# print(register('20171142@qq.com'))

if __name__ == '__main__':
    s = script('11012@qq.com')
    s.main()
    # print('%d,%d' % (20 - 10, 20 - 3))
    # with open('answer_first.json', 'r', encoding='utf-8') as f:
    #     for i in json.load(f):
    #         print(i[1])
    # pass
