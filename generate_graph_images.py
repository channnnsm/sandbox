import japanize_matplotlib
import numpy as np
import matplotlib.pyplot as plt

def plot_exponential():
    """
    エクスポネンシャル関数のグラフ (例: y = 2^x)
    """
    x = np.linspace(-5, 5, 400)
    y = 2 ** x
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label=r"$y=2^x$", color="blue")
    plt.title("エクスポネンシャル関数のグラフ: $y=2^x$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # plt.show() もしくは画像として保存する場合
    plt.savefig("exp_graph.png")
    plt.close()

def plot_sigmoid():
    """
    シグモイド関数のグラフ (σ(x)=1/(1+e^(-x)))
    """
    x = np.linspace(-10, 10, 400)
    y = 1 / (1 + np.exp(-x))
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label=r"$\sigma(x)=\frac{1}{1+e^{-x}}$", color="green")
    plt.title("シグモイド関数のグラフ")
    plt.xlabel("x")
    plt.ylabel("σ(x)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # plt.show() もしくは画像として保存する
    plt.savefig("sigmoid_graph.png")
    plt.close()

if __name__ == "__main__":
    plot_exponential()
    plot_sigmoid()