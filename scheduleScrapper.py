from bs4 import BeautifulSoup as bs
from requests import Session


def login():
    with Session() as s:
        site = s.get("https://www.improveonline.jp/")
        login_data = {"loginid": "in0928", "password": "54hanghang"}
        s.post("https://www.improveonline.jp/", login_data)
    return s


def get_union_name(SessionObj):
    tokyo_unions = SessionObj.get("https://www.improveonline.jp/mypage/union/group_detail_select.php?pref=13")
    union_content = bs(tokyo_unions.content, "html.parser")
    all_id = union_content.find_all("li")  # get the full schedule


def get_row_data(SessionObj):
    # Test with IDEA August schedule
    idea_aug = SessionObj.get("https://www.improveonline.jp/mypage/union/schedule_detail.php?date=2019-08&group=46&mc=8")
    idea_aug_content = bs(idea_aug.content, "html.parser")
    schedule = idea_aug_content.find_all("tr")  # get the full schedule
    #     print(schedule)
    aug3 = schedule[3]
    #     print(aug3)
    row_data = aug3.find_all("td")
    row_list = []
    for item in row_data:
        val = item.text
        row_list.append(val.strip())
    return row_list
