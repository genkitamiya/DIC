#【問題１】べき乗の算術演算子を使用して作成

t_0 = 0.00008           #折る前の紙の厚さ（m）
t_exp = t_0 * 2 ** 43   #43回折った紙の厚さ（m）
print("厚さ： {}メートル".format(t_exp))


#【問題2】単位の変換

print("厚さ： {:.2f}万キロメートル".format(t_exp/(1000*10000)))


#【問題3】for文を使用して作成

t_for = t_0             #t_forを0回折ったt_0と定義

for i in range(43):     #t_for掛ける2を43回繰り返す
  t_for *= 2

print("厚さ： {}メートル".format(t_for))


#【問題4】計算時間の比較

t_for = t_0

import time
start = time.time()
t_exp = t_0 * 2 ** 43
elapsed_time = time.time() - start
print("time : {}[s]".format(elapsed_time))

start = time.time()
for i in range(10000):
  t_for *= 2
elapsed_time = time.time() - start
print("time : {}[s]".format(elapsed_time))

    #計算方法の計算時間の違いについては、べき乗の場合、計算が１度のみであり（t^43またはt^n）、
    #for文の場合は43回（またはn回）繰り返されるため、計算時間はfor文の方が長い。
    #43回では計算時間に大きな違いは見られないが、nが大きくなるにつれ、その差は顕著になる。
    #ただしべき乗計算はn値が大きすぎるとfloat変換できず、overflow errorを起こすため、
    #その場合はfor文計算を使用すべきと考えられる。


#【問題5】リストへの保存

t_for = t_0
thickness = [t_0]

for i in range(43):
  t_for *= 2
  thickness.append(t_for)
print(len(thickness))


#【問題6】折れ線グラフの表示

import matplotlib.pyplot as plt

#%matplotlib inline
plt.title("Thickness of folded paper")
plt.xlabel("Number of folds")
plt.ylabel("Thickness[m]")
plt.plot(thickness)
plt.show()


#【問題7】グラフのカスタマイズ

#マーカーの追加
#%matplotlib inline
plt.title("Thickness of folded paper")
plt.xlabel("Number of folds")
plt.ylabel("Thickness[m]")
plt.plot(thickness,marker='o',markersize='5')
plt.show()

#点線に変更（マーカーと線を区別するため）
#%matplotlib inline
plt.title("Thickness of folded paper")
plt.xlabel("Number of folds")
plt.ylabel("Thickness[m]")
plt.plot(thickness,marker='o',markersize='5',ls='--',c ='gray',mfc='b',mec='b')
plt.show()

#グリッド線追加＋軸ラベルのフォント拡大
#%matplotlib inline
plt.title("Thickness of folded paper",fontsize=16)
plt.xlabel("Number of folds",fontsize=14)
plt.ylabel("Thickness[m]",fontsize=14)
plt.plot(thickness,marker='o',markersize='5',ls='--',c ='gray',mfc='b',mec='b')
plt.tick_params(labelsize=12,direction = 'in')
plt.grid(ls='--',alpha=0.5)
plt.show()
