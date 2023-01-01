"""
Здесь расположен класс для переключения языка UI
"""
from enum import Enum

class LangRu(Enum):
    ROBOT_CREATE = "Создаём робота...\n"
    ROBOT_STUDY = "Обучаем робота...\n"
    ROBOT_PRACTICE = "Отправка робота на промышленное предприятие \"ООО Кошмарик\"...\n"

    ROBOT_BUILD_HOME_COMPLETE = "{robot_name} только что построил дом!"
    ROBOT_BUILD_BARN_COMPLETE = "{robot_name} только что построил сарай!"

    ROBOT_CHECK_SKILLS = "Проверка способностей у робота {robot_name}"
    ROBOT_CHECK_HOME_SKILL = "build_home_rus:"
    ROBOT_CHECK_BARN_SKILL = "build_barn_rus:"
    ROBOT_CHECK_FLOOR_ADD_SKILL = "build_floor_add_rus:"
    ROBOT_CHECK_FLOOR_REMOVE_SKILL = "build_floor_remove_rus:"
    
    ROBOT_FLOOR_ADD = "{robot_name} только что увеличил количество этажей на 1!"
    ROBOT_FLOOR_REMOVE = "{robot_name} только что уменьшил количество этажей на 1!"
    ROBOT_FLOOR_REMOVE_FAIL = "{robot_name} не может уменьшить количество этажей у одноэтажки!"

    ROBOT_NAME_V1 = "В"
    ROBOT_NAME_V2 = "Вита"
    ROBOT_NAME_V3 = "Виталий"


class LangEng(Enum):
    ROBOT_CREATE = "Creating robot...\n"
    ROBOT_STUDY = "Robot studying a skill...\n"
    ROBOT_PRACTICE = "Sending a robot to an industrial plant \"OOO Koshmarik\"...\n"

    ROBOT_BUILD_HOME_COMPLETE = "{robot_name} have just built the home!"
    ROBOT_BUILD_BARN_COMPLETE = "{robot_name} have just built the barn!"

    ROBOT_CHECK_SKILLS = "Checking skill of the robot"
    ROBOT_CHECK_HOME_SKILL = "build_home_eng"
    ROBOT_CHECK_BARN_SKILL = "build_barn_eng"
    ROBOT_CHECK_FLOOR_ADD_SKILL = "build_floor_add_eng"
    ROBOT_CHECK_FLOOR_REMOVE_SKILL = "build_floor_remove_eng"
    
    ROBOT_FLOOR_ADD = "{robot_name} have just added 1 floor to building!"
    ROBOT_FLOOR_REMOVE = "{robot_name} have just remove 1 floor from building"
    ROBOT_FLOOR_REMOVE_FAIL = "{robot_name} can't remove any floor from 1 floor building!"

    ROBOT_NAME_V1 = "v"
    ROBOT_NAME_V2 = "vita"
    ROBOT_NAME_V3 = "vitaly"


class LanguageSwitcher:
    def __init__(self, language) -> None:
        if language == "rus":
            self.__db = LangRu
            
        else:
            self.__db = LangEng


    def get_string(self, string_name:str) -> str:
        try:
            return self.__db._member_map_[string_name].value

        except:
            return ""