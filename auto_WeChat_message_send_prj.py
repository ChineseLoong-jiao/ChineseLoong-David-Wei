import csv
import random
from datetime import datetime, timedelta

# 生肖列表，按照顺序排列
zodiac_animals = [
    "鼠", "牛", "虎", "兔", "龙", "蛇",
    "马", "羊", "猴", "鸡", "狗", "猪"
]

def get_zodiac(year):
    """
    根据年份计算生肖
    """
    return zodiac_animals[(year - 4) % 12]

def generate_detailed_greeting(contact, zodiac):
    """
    根据详细的联系人信息生成约 500 字的新年祝福语
    """
    name = contact["name"]
    age = contact["age"]
    gender = contact["gender"]
    phone = contact["phone"]
    email = contact["email"]
    address = contact["address"]
    wechat = contact["wechat"]
    qq = contact["qq"]
    birthday = contact["birthday"]
    hobby = contact["hobby"]
    interest = contact["interest"]
    education = contact["education"]
    occupation = contact["occupation"]
    marital_status = contact["marital_status"]
    children = contact["children"]
    relationship = contact["relationship"]
    description = contact["description"]

    greeting = f"亲爱的{name}，在这辞旧迎新的{zodiac}年，祝您新春快乐！作为{relationship}，我由衷地感谢您在过去一年的陪伴与支持。"

    if gender == "女":
        greeting += f"作为一位杰出的{occupation}，您的智慧和魅力令人折服，"
    elif gender == "男":
        greeting += f"作为一位优秀的{occupation}，您的努力和成就令人钦佩，"

    current_year = datetime.now().year
    age_at_next_birthday = current_year - birthday.year + 1
    greeting += f"马上就要迎来您的{age_at_next_birthday}岁生日，愿这一年您身体健康、岁岁平安。"

    if hobby or interest:
        greeting += f"愿您继续在{hobby or interest}方面找到更多乐趣，生活更加多姿多彩。"

    if education:
        greeting += f"以您{education}的学识，我相信您一定能在事业上蒸蒸日上！"

    if marital_status == "已婚":
        greeting += "愿您和家人幸福美满，"
        if children:
            greeting += "您的子女也能茁壮成长，前途无量。"
    else:
        greeting += "愿您早日找到人生伴侣，拥有属于自己的幸福家庭。"

    greeting += (
        f"您平日的{description}深受大家喜爱，愿这样的美好品质继续发扬光大！"
        f"无论何时，您都可以通过电话（{phone}）、邮箱（{email}）、"
        f"地址（{address}）、微信（{wechat})或QQ({qq}）找到我。"
    )

    greeting += f"在{zodiac}年里，愿您事事顺心，财源滚滚，家庭和睦，事业辉煌！"
    return greeting

def generate_random_contacts(file_path, num_contacts=100):
    """
    随机生成通讯录 CSV 文件
    """
    
    num_contacts = int(input("请输入需要生成的联系人数量(默认100个): "))
    
    while not isinstance(num_contacts, int) or num_contacts <= 0:
        print("请输入一个正整数！")
        num_contacts = int(input("请输入需要生成的联系人数量(默认100个): "))

    if num_contacts > 10000:
        print("警告：生成大量联系人可能会导致文件过大，建议分批生成。\n")
        confirm = input("是否继续生成？(y/n): ").lower()
        if confirm!= "y":
            return -1# 退出程序

    print("正在生成联系人信息...\n\n")
    
    first_names = ["张", "李", "王", "赵", "刘", "陈", "杨", "黄", "周", "吴", "徐", "孙", "陈", "许", "何", "吕", "施", "张", "孔", "曹", "许", "孙", "马", "邓", "钟", "江", "郑", "谢", "余", "蒋", "潘", "杜", "魏", "程", "蔡", "彭", "袁", "董", "夏", "沈", "叶", "谭", "廖", "萧", "姜", "崔", "汪", "范", "金", "石", "熊", "孟", "秦", "白", "任", "袁", "宋", "卢", "邹", "高", "林", "罗", "戴", "阎", "梁", "方", "易", "胡", "郭", "董", "贾", "路", "娄", "陶", "常", "傅", "戚", "裘", "鲁", "倪", "汤", "殷", "卞", "危", "解", "康", "欧阳", "田", "文", "明", "华", "顾", "毛", "方", "申", "赖", "龚", "钱", "陆", "姬", "缪", "柯", "诸葛", "佟", "贺", "房", "兰", "席", "武", "柳", "颜", "韦", "章", "唐", "费", "岑", "薛", "雷", "贺", "倪", "汤", "韩", "凌", "程", "靳", "麦", "惠", "龚", "邵", "洪", "包", "温", "矫", "喻", "辛", "凌", "蓝", "柴", "史", "陶", "顾", "蒙", "黄", "梅", "盛", "鲍", "郝", "邱", "楼", "酆", "鲍", "史", "巩", "聂", "印", "伏", "蔺","虞", "万", "支", "柯", "昝", "段", "侯", "赖", "漆", "干", "冷", "尚", "富"]
    last_names = ["伟", "芳", "娜", "敏", "静", "丽", "强", "磊", "军", "洋", "勇", "刚", "涛", "超", "秀英", "霞", "艳红", "玉珍", "莉莉", "玲", "婕", "丹", "丽娅", "燕子", "雪莲", "小花", "小红", "小翠", "小丽", "小凤", "小琴", "小雨", "小芳","基霸","玉坤","小飞","小亮", "文皓","小宇"]
    genders = ["男", "女"]
    marital_statuses = ["已婚", "未婚"]
    educations = ["高中", "本科", "硕士", "博士","博士后", "其他"]
    occupations = ["工程师", "医生", "教师", "程序员", "设计师"]

    with open(file_path, mode="w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "姓名", "年龄", "性别", "备注", "手机号", "邮箱", "地址",
            "微信", "QQ", "生日", "爱好", "兴趣", "学历", "职业",
            "婚姻状况", "子女情况", "与本人关系", "个人描述"
        ])

        for _ in range(num_contacts):
            name = random.choice(first_names) + random.choice(last_names)
            age = random.randint(1, 100)
            gender = random.choice(genders)
            marital_status = random.choice(marital_statuses)
            birthday = datetime.now() - timedelta(days=random.randint(7000, 20000))
            writer.writerow([
                name, age, gender, "努力工作", f"1{random.randint(3000000000, 9999999999)}",
                f"{name.lower()}@example.com", f"某城市某小区{random.randint(1, 20)}号",
                f"{name.lower()}_wx", random.randint(10000000, 99999999),
                birthday.strftime("%Y-%m-%d"), "阅读", "旅行",
                random.choice(educations), random.choice(occupations),
                marital_status, "有一个孩子" if marital_status == "已婚" else "无子女",
                "好友", "热情友善，工作积极"
            ])

def read_contacts(file_path):
    """
    读取CSV格式的通讯录
    """
    contacts = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                contacts.append({
                    "name": row["姓名"],
                    "age": int(row["年龄"]),
                    "gender": row["性别"],
                    "remark": row["备注"],
                    "phone": row["手机号"],
                    "email": row["邮箱"],
                    "address": row["地址"],
                    "wechat": row["微信"],
                    "qq": row["QQ"],
                    "birthday": datetime.strptime(row["生日"], "%Y-%m-%d").date(),
                    "hobby": row["爱好"],
                    "interest": row["兴趣"],
                    "education": row["学历"],
                    "occupation": row["职业"],
                    "marital_status": row["婚姻状况"],
                    "children": row["子女情况"],
                    "relationship": row["与本人关系"],
                    "description": row["个人描述"],
                })
            except ValueError:
                print(f"无效数据：{row}，跳过。")
    return contacts

def main():
    """_summary_: Main function.

    Returns:
        _type_: None.
    """
    current_year = datetime.now().year
    zodiac = get_zodiac(current_year)
    print(f"当前年份: {current_year}年，生肖: {zodiac}\n")

    csv_file = "contacts.csv"
    if generate_random_contacts(csv_file) == -1:
        print("程序退出。")
        return 0

    contacts = read_contacts(csv_file)
    output_file = "greetings_output.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for contact in contacts:
            greeting = generate_detailed_greeting(contact, zodiac)
            print(greeting)  # 打印到屏幕
            f.write(greeting + "\n")  # 写入文件

    print(f"\n祝福语已保存到 {output_file}")

if __name__ == "__main__":
    main()
