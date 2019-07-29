from bs4 import BeautifulSoup as bs
from requests import Session

def get_row_data():
    with Session() as s:
        # To login
        site = s.get("https://www.improveonline.jp/")
        login_data = {"loginid": "in0928", "password": "54hanghang"}
        s.post("https://www.improveonline.jp/", login_data)

        # Create a list of IDs for all groups

        # Test with IDEA August schedule
        idea_aug = s.get("https://www.improveonline.jp/mypage/union/schedule_detail.php?date=2019-08&group=20&mc=8")
        idea_aug_content = bs(idea_aug.content, "html.parser")
        schedule = idea_aug_content.find_all("tr")  # get the full schedule
        #     print(schedule)
        aug3 = schedule_data[3]
        #     print(aug3)
        row_data = aug3.find_all("td")
        print(row_data)
        row_list = []
        for item in row_data:
            val = item.text
            row_list.append(val)
        print(row_list)