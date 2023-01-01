"""
Обучения технологии постройки зданий
"""

from classes import Robot, House, Barn


def learn_build_home(robot: Robot, language_db)->Robot:
    """
    Научить робота строить дом
    """

    def build_home(self)->None:
        """
        Построить дом
        """
        # print(f"{self.name} только что построил дом!")
        print(language_db.get_string('ROBOT_BUILD_HOME_COMPLETE').format(robot_name = robot.name))
        return House()

    robot.build_home = build_home


def learn_build_barn(robot: Robot, language_db)->None:
    """
    Научить робота строить сарай
    """
    
    def build_barn(self)->None:
        """
        Построить сарай
        """
        # print(f"{self.name} только что построил сарай!")
        print(language_db.get_string('ROBOT_BUILD_BARN_COMPLETE').format(robot_name = robot.name))
        return Barn()

    robot.build_barn = build_barn