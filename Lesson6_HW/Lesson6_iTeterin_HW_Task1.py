# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы:
# красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться
# только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        from time import sleep
        from itertools import cycle

        for color in cycle(TrafficLight.__color):
            if color == 'красный':
                print(f'Горит {color} свет. Подождите 7 секунд.')
                sleep(7)
            elif color == 'жёлтый':
                print(f'Горит {color} свет. Подождите 2 секунды.')
                sleep(2)
            elif color == 'зелёный':
                print(f'Горит {color} свет. Подождите 3 секунды.')
                sleep(3)


def main():
    light_signal = TrafficLight()
    light_signal.running()


if __name__ == '__main__':
    print("Задание №1")
    main()
