import pandas as pd
import matplotlib.pyplot as plt

try:
    # 讀取 Excel 檔案
    df = pd.read_excel(r'311.xlsx')

    # 檢查是否存在 'x' 和 'y' 欄位
    if 'x' in df.columns and 'y' in df.columns:
        # 計算 'x' 和 'y' 的和
        df['sum'] = df['x'] + df['y']
        
        # 印出相加結果
        print(df['sum'])

        # 繪製散佈圖
        plt.scatter(df['x'], df['y'])
        plt.xlabel('X 軸')
        plt.ylabel('Y 軸')
        plt.title('X 和 Y 的散佈圖')
        plt.show()
    else:
        print("Excel 檔案中缺少 'x' 或 'y' 欄位")
except FileNotFoundError:
    print("找不到指定的 Excel 檔案")
except Exception as e:
    print(f"發生錯誤: {e}")