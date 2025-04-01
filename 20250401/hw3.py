from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import html

# 設定瀏覽器選項
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 啟用無頭模式（不顯示瀏覽器介面）

# 啟動瀏覽器
driver = webdriver.Chrome(options=options)

# 開啟目標網頁
url = "file:///c:/Users/User/Desktop/CYCU_OOP_11041318/bus_route_10417.html"
driver.get(url)

# 等待 JavaScript 加載完成
time.sleep(5)  # 根據網頁的加載速度調整等待時間

# 找到所有站點的行 (tr)
rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'ttego') or contains(@class, 'tteback')]")

# 輸出站點名稱和到站時間
print("站點資訊：")
for row in rows:
    # 提取站點名稱
    stop_name_element = row.find_element(By.TAG_NAME, "td")
    stop_name = html.unescape(stop_name_element.text.strip()) if stop_name_element else "未知站點"

    # 提取到站時間
    try:
        stop_time_element = row.find_element(By.XPATH, ".//td[@align='center' and @nowrap]")
        stop_time = stop_time_element.text.strip() if stop_time_element else "無資料"
    except:
        stop_time = "無資料"

    # 輸出結果
    print(f"站點名稱: {stop_name}, 到站時間: {stop_time}")

# 關閉瀏