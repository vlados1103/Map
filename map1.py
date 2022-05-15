import random
import math
import folium
from folium import vector_layers
from folium import plugins
from folium.plugins.measure_control import MeasureControl

# Начальные координаты:

crd = [56.0062089408958, 37.447499115253876]
# crd = [0.004761, 28.317992] # экватор
# crd = [83.639441, -33.989031] # север
# crd = [0.1, 0.1]
# crd = [42.5, 90]
# crd = [77.519502, 104.001929] # север России
R = 6370000  # Радиус Земли в метрах

opa = 0.5  # float(input("Введите прозрачность заливки от 0 до 1: "))
wd_w = 1000  # float(input("Введите ширину сетки"))
ht_w = 1000  # float(input("Введите высоту сетки"))
wd1 = 20  # float(input("Введите ширину одной клетки"))
ht1 = 20  # float(input("Введите высоту одной клетки"))


ct_w = int(wd_w/wd1)+1  # Вообще, тут не инт, а окрегление в бОльшую сторону.
ct_h = int(ht_w/ht1)+1  # Тут тоже.
i = 0
j = 0
print("ct_w= ", ct_w)
print("ct_h= ", ct_h)

# Можно сделать прогу, которая бы в качестве начальных координат
# брала бы координаты текущего местоположения дрона, или же просто их ввести

m = folium.Map(location=crd, zoom_start=15)
# for crd in [[56.003747, 37.444308],[56.006169, 37.446539]]:

folium.plugins.MousePosition().add_to(m)  # Координаты мыши

folium.plugins.Fullscreen(  # Кнопка полного экрана
    position="bottomright",
    # title="Во весь экран",
    # title_cancel="Выход из полноэкранного режима"
).add_to(m)

folium.plugins.LocateControl(auto_start="True").add_to(m)  # Координаты щелчка мыши
plugins.Geocoder().add_to(m)  # Поиск объектов
MC = MeasureControl(color = "red")
MC.add_to(m)

"""
folium.plugins.Search(
    layer="GeoJson",
    # position=",
    placeholder="Что Вы хотите найти?",
    collapsed="True"
).add_to(m)
"""

folium.Marker(  # Маркер
    location=crd,
    tooltip="Дрон",
    icon=folium.Icon(icon="drone")).add_to(m)

'''folium.vector_layers.path_options(
    weight=1
    #opacity=0
)'''

c1 = 1.2/10**5/1.333*ht1
c2 = 1.2/10**5/1.335*wd1

while i < ct_h*2:
    while j < ct_w*2:
        col = 0  # random.randrange(0, 4)
        if col == 0:
            folium.Rectangle(
                bounds=[[crd[0]+(ct_h-i)*c1, crd[1]-(ct_w-j)*c2/math.cos(crd[0]*3.14/180)],
                        [crd[0]+(ct_h-i-1)*c1, crd[1]-(ct_w-j-1)*c2/math.cos(crd[0]*3.14/180)]],
                tooltip=f"Концентрация = {col}",
                fill=True,
                # fill_opacity=opa,
                # fill_color="green"
            ).add_to(m)
        elif col == 1:
            folium.Rectangle(
                bounds=[[crd[0] + (ct_h - i) * 1.2 / 10 ** 5 * ht1 / 1.333,
                         crd[1] - (ct_w - j) * 1.2 / 10 ** 5 * wd1 / math.cos(crd[0] * 3.14 / 180) / 1.335],
                        [crd[0] + (ct_h - i - 1) * 1.2 / 10 ** 5 * ht1 / 1.333,
                         crd[1] - (ct_w - j - 1) * 1.2 / 10 ** 5 * wd1 / math.cos(crd[0] * 3.14 / 180) / 1.335]],
                tooltip=f"Концентрация = {col}",
                fill=True,
                fill_opacity=opa,
                fill_color="green"

            ).add_to(m)
        elif col == 2:
            folium.Rectangle(
                bounds=[[crd[0] + (ct_h - i) * 1.2 / 10 ** 5 * ht1 / 1.333,
                         crd[1] - (ct_w - j) * 1.2 / 10 ** 5 * wd1 / math.cos(crd[0] * 3.14 / 180) / 1.335],
                        [crd[0] + (ct_h - i - 1) * 1.2 / 10 ** 5 * ht1 / 1.333,
                         crd[1] - (ct_w - j - 1) * 1.2 / 10 ** 5 * wd1 / math.cos(crd[0] * 3.14 / 180) / 1.335]],
                tooltip=f"Концентрация = {col}",
                fill=True,
                fill_opacity=opa,
                fill_color="yellow"
            ).add_to(m)
        elif col == 3:
            folium.Rectangle(
                bounds=[[crd[0] + (ct_h - i) * 1.2 / 10 ** 5 * ht1 / 1.333,
                         crd[1] - (ct_w - j) * 1.2 / 10 ** 5 * wd1 / math.cos(crd[0] * 3.14 / 180) / 1.335],
                        [crd[0] + (ct_h - i - 1) * 1.2 / 10 ** 5 * ht1 / 1.333,
                         crd[1] - (ct_w - j - 1) * 1.2 / 10 ** 5 * wd1 / math.cos(crd[0] * 3.14 / 180) / 1.335]],
                tooltip=f"Концентрация = {col}",
                fill=True,
                fill_opacity=opa,
                fill_color="red"
            ).add_to(m)

        j += 1
        # print("j = ", j)
    j = 0
    i += 1
    # print("i = ", i)

folium.PolyLine(
    locations=[[56.003800988500636, 37.44459603609126],
               [56.00397110020597, 37.444623694265985],
               [56.00440926327093, 37.4442456992114],
               [56.004512359740616, 37.44374785206634],
               [56.004945361909485, 37.44355424484325]],
    popup="Траектория"
).add_to(m)

m.add_child(folium.LatLngPopup())
m.save('map.html')



# Сюда я всякий хлам скопировал, т.е. дальше идёт только нерабочий код.

#wd_w = 0.005# wd_w_/R  # float(input("Введите ширину сетки"))
#ht_w = 0.005# ht_w_/R  # float(input("Введите высоту сетки"))
#wd1 = 0.001# wd1_/R  # float(input("Введите ширину одной клетки"))
#ht1 = 0.001# ht1_/R  # float(input("Введите высоту одной клетки"))


# bounds=[[crd[0]+(ct_h-i)*ht1*180/3.14*math.cos(crd[0]*3.14/180),
                #         crd[1]-(ct_w-j)*wd1*180/3.14*math.sin(crd[0]*3.14/180)],
                #        [crd[0]+(ct_h-i-1)*ht1*180/3.14*math.cos(crd[0]*3.14/180),
                #         crd[1]-(ct_w-j-1)*wd1*180/3.14*math.sin(crd[0]*3.14/180)]],
                # bounds=[[math.atan(math.sinh(R*math.sin(crd[0]*3.14/180+(ct_h-i)*ht1)))*180/3.14,
                #        crd[1]-(ct_w-j)*wd1*180/3.14],
                #        [math.atan(math.sinh(R*math.sin(crd[0]*3.14/180+(ct_h-i-1)*ht1)))*180/3.14,
                #        crd[1]-(ct_w-j-1)*wd1*180/3.14]],