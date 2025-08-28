import random
import time

class FortuneWheel:
    def printSpin():
        userinput = input("Введите экземпляры (разделенно запятой) >>> ").split(',')
        print("Колесо крутится...")
        time.sleep(random.randint(1, 5))
        print("Выпало: {}".format(random.choice(userinput)))
    def spin(objects: list) -> str:
        return random.choice(objects)

if __name__ == "__main__":
    pass # скоро будет