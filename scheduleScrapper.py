from bs4 import BeautifulSoup as bs
from requests import Session
from selenium import webdriver
import re
import mongoDBConnector

collections = mongoDBConnector.connect_mongo()
schedule_test = collections[1]
union_test = collections[2]

login_url = "https://www.improveonline.jp/"


def login():
    with Session() as s:
        login_data = {"loginid": "in0928", "password": "54hanghang"}
        s.post(login_url, login_data)
    return s


def get_unions():
    """This uses Selenium because Session does not work well with dynamic contents"""
    driver = webdriver.Chrome(executable_path="C:\\Users\\Ko.In\\Desktop\\chromdriver75\\chromedriver.exe")
    driver.implicitly_wait(20)
    driver.get(login_url)
    print("Reach here")
    # Try to login
    username = driver.find_element_by_xpath("//input[@name='loginid']")
    username.send_keys('in0928')
    pw = driver.find_element_by_xpath("//input[@name='password']")
    pw.send_keys('54hanghang')
    login_btn = driver.find_element_by_xpath("//a[@class='login-btn']")
    driver.implicitly_wait(10)
    login_btn.click()

    # unions
    driver.implicitly_wait(10)
    union_icon = driver.find_element_by_xpath("//a[@href='union/group_select.php?category=8']/div")
    union_icon.click()

    # tokyo
    driver.implicitly_wait(10)
    tokyo = driver.find_element_by_xpath("//a[contains(text(),'東京')]")
    tokyo.click()
    driver.implicitly_wait(10)

    # Beautifulsoup
    html = driver.page_source
    soup = bs(html, features="lxml")

    driver.quit()

    all_id = soup.find_all("a", attrs={"href": re.compile("^list")})

    unions = {}
    for a in all_id:
        link = a.get("href")
        group_id = link[9:]
        name = a.text
        unions[name] = group_id
        union_test.insert_one({
            "union-name": name,
            "group-id": unions[name]
        })
    return unions


def get_table_data(SessionObj, url):
    """Given any union url, returns the html with all tr tags"""
    schedule = SessionObj.get(url)
    schedule_content = bs(schedule.content, "html.parser")
    schedule_table = schedule_content.find_all("tr")  # get the full table in list
    return schedule_table

def get_row_data(table, union_name):
    # Need to initialize the DB
    schedule_test.delete_many({})
    for row in table:
        row_date = row.find("th")
        row_data = row.find_all("td")
        row_dic_keys = ["date", "union_name", "content", "time", "SP", "MC_AC", "venue"]
        row_list = [row_date, union_name]
        row_data_dic = {}
        # iterate through every cell
        for item in row_data:
            val = item.text
            row_list.append(val) # a list with 5 values from 5 cells in the same row

        # Create a dic to send to MongoDB
        for i in range(len(row_dic_keys)):
            row_data_dic[row_dic_keys[i]] = row_list[i]

        schedule_test.insert_one(row_data_dic)


def all_data():
    s = login()
    union_urls = map_union_url()

    for item in union_urls: # item is union_name
        url = union_urls.get(item)
        schedule_table = get_table_data(s, url)
        get_row_data(schedule_table, item)


def map_union_url():
    base = "https://www.improveonline.jp/mypage/union/schedule_detail.php?"
    month = "date=2019-08&" # notice & is attached
    suffix = "&mc=8" # notice & is at the beginning
    groups = get_unions()
    union_urls = {}
    for group in groups:
        group_id = groups.get(group)
        url = base + month + group_id + suffix
        union_urls[group] = url
    return union_urls




