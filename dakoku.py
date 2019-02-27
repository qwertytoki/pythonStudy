import time
import datetime
import random
import myholiday
from selenium import webdriver
# <済> sleep_random_time()
# <済>毎日10時～12時の間のランダムな時間に打刻バッチを起動する
# ↓
# <済>can_dakoku()
# <済>打刻していいかチェックする
#   <済>is_week_day() 
# 	<済>・平日であること
#   <済>is_work_day()
# 	<済>・自分が有休orフレックスではないこと
#   is_usual()
# 	・自分が緊急で休みではないこと
# ↓
# <済>dakoku()
# <済>ログインする
# ↓
# <済>dakoku()
# <済>打刻する
# ↓
# send_LINE()
# 打刻したら教えてほしい、失敗しても教えてほしい

def sleep_random_time():
    time.sleep(random.randint(1, 7200))

def can_dakoku():
    if is_week_day()== True and is_work_day() == True and is_usual() ==True:
        return True
    return False
def is_week_day():
    weekday = datetime.date.today().weekday()
    if weekday == 5 or weekday ==6 :
        return False
    else :
        return True

def is_work_day():
    today = str(datetime.date.today())
    for holiday in myholiday.holidays:
        if today == holiday:
            return False
    return True

def is_usual():
    # see https://tanuhack.com/python/operate-spreadsheet/
    return True

def dakoku():

    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get("URL")
    user_id = driver.find_element_by_name("user_id")
    user_id.send_keys("YOUR_ID")
    password = driver.find_element_by_name("password")
    password.send_keys("YOUR_PASSWORD")
    dakoku_button  = driver.find_element_by_class_name("login-syussya-button")
    dakoku_button.click()
    dakoku_done = driver.find_elements_by_class_name("recorded-time")
    if len(dakoku_done) ==1:
        return True
    else:
        return False

def send_LINE(result):
    # see https://qiita.com/analytics-hiro/items/e42f857bd6b40bc178a3
    print(result)

if __name__ == "__main__":
    # sleep_random_time()
    dakokuResult = False
    if  can_dakoku() ==True:
        dakokuResult = dakoku()
    send_LINE(dakokuResult)