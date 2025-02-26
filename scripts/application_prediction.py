import gradio as gr
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# ダミーデータを作成
# サンプル数
n_samples = 100
np.random.seed(42)

# 特徴量の生成
#  最寄り駅までの時間：0～30分
#  専有面積：10～200㎡
#  築年数：0～60年
dummy_time = np.random.uniform(0, 30, n_samples)
dummy_space = np.random.uniform(10, 200, n_samples)
dummy_age = np.random.uniform(0, 60, n_samples)

# ダミーの目的変数(取引価格)は、専有面積の影響を大きくしつつ、時間と築年数で調整
dummy_price = (dummy_space * 500) - (dummy_time * 10) - (dummy_age * 5) + np.random.normal(0, 50, n_samples)

# DataFrame作成
df_dummy = pd.DataFrame({
    "最寄り駅までの時間": dummy_time,
    "専有面積": dummy_space,
    "築年数": dummy_age,
    "取引価格（総額）": dummy_price
})

# 学習に必要なカラムを抽出
x = df_dummy[["最寄り駅までの時間", "専有面積", "築年数"]]
y = df_dummy["取引価格（総額）"]

# モデルの初期化と学習
model = RandomForestRegressor(random_state=42)
model.fit(x, y)

# 不動産価格を予測する関数
def predict_price(time, space, age):
    values = np.array([time, space, age]).reshape(1, -1)  # 入力を2次元配列に変換
    prediction = model.predict(values)
    return round(prediction[0], 2)

# Gradioインターフェースのレイアウト作成
with gr.Blocks() as iface:
    gr.Markdown(
        """
        # 新宿区不動産価格予測アプリ（ダミーデータ版）
        このデモはダミーデータを用いて学習したモデルで予測を行います。
        """
    )
    with gr.Row():
        time_input = gr.Slider(0, 30, value=5, step=1, label="最寄り駅までの時間（分）")
        space_input = gr.Slider(10, 200, value=50, step=1, label="専有面積（㎡）")
        age_input = gr.Slider(0, 60, value=20, step=1, label="築年数")
    value_output = gr.Number(label="予測取引価格（万円）")
    
    predict_btn = gr.Button("予測")
    predict_btn.click(predict_price, inputs=[time_input, space_input, age_input], outputs=value_output)

# インターフェースを起動（シェア用設定も含む）
iface.launch(share=True)