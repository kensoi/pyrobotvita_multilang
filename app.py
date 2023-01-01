from classes import Robot
from methods.check import check_skills
from methods.build import learn_build_barn, learn_build_home
from methods.floor_count import learn_add_floor, learn_remove_floor
from language_switcher import LanguageSwitcher

def main():
    language_db = LanguageSwitcher(input("Выберите язык [rus]/Select language [eng] >> "))
    # print("Создаём робота...\n")
    print(language_db.get_string("ROBOT_CREATE"))

    # Первичное создание робота и проверка его способностей
    
    robot = Robot("АА001221-56", language_db.get_string("ROBOT_NAME_V1")) 

    check_skills(robot, language_db) # проверка способностей

    # Первое обучение робота

    # print("Обучаем робота...\n")
    print(language_db.get_string("ROBOT_STUDY"))

    learn_build_home(robot, language_db) # робот учится строить дома
    learn_build_barn(robot, language_db) # робот учится строить сараи

    robot.name = language_db.get_string("ROBOT_NAME_V2")

    check_skills(robot, language_db) # проверка способностей

    # Второе обучение робота
    
    # print("Отправка робота на промышленное предприятие \"ООО Кошмарик\"...\n")
    print(language_db.get_string("ROBOT_PRACTICE"))

    learn_add_floor(robot, language_db) # робот учится строить дополнительный этаж к дому
    learn_remove_floor(robot, language_db) # робот учится сносить 1 этаж у дома

    robot.name = language_db.get_string("ROBOT_NAME_V3")

    check_skills(robot, language_db) # проверка способностей


if __name__ == "__main__":
    main()