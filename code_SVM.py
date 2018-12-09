import numpy as np
from sklearn.svm import SVC
cars = np.array([[0.25, 0.762], [0.17, 0.77], [0.3, 0.665], [0.2, 0.567]])
show_class = np.array([1, 0, 1, 0])
clf = SVC(kernel='linear')
clf = SVC.fit(cars, show_class)


def jeep_or_not(vis_space, wheel_d):
    vis_space = int(input("Введите обзорное пространство Вашего автомобиля в метрах"))
    wheel_d = int(input("Введите диаметр колеса Вашего автомобиля в метрах"))
    prediction = clf.predict([[vis_space, wheel_d]])
    if prediction == 1:
       print("Ваш автомобиль - внедорожник")
    else:
       print("У Вас легковушка, паркетник или кроссовер")


jeep_or_not(vis_space, wheel_d)
