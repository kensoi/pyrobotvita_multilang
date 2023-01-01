"""
Обучения технологии постройки этажей зданий
"""

from classes import Robot, Building


def learn_add_floor(robot: Robot, language_db)->None:
    """
    Научить робота увеличивать количество этажей
    """

    def add_floor(self, building: Building)->None:
        """
        Построить 1 этаж у постройки
        """

        building.floor += 1
        # print(f"{self.name} только что увеличил количество этажей на 1!")
        print(language_db.get_string("ROBOT_FLOOR_ADD").format(robot_name = robot.name))
    robot.add_floor = add_floor
    

def learn_remove_floor(robot: Robot, language_db)->None:
    """
    Научить робота увеличивать количество этажей
    """

    def remove_floor(self, building: Building)->None:
        """
        Построить 1 этаж у постройки
        """
        
        if building.floor == 1:
            # print(f"{self.name} не может уменьшить количество этажей у одноэтажки!")
            print(language_db.get_string("ROBOT_FLOOR_REMOVE_FAIL").format(robot_name = robot.name))
        
        else:
            building.floor -= 1
            # print(f"{self.name} только что уменьшил количество этажей на 1!")
            print(language_db.get_string("ROBOT_FLOOR_REMOVE").format(robot_name = robot.name))

    robot.remove_floor = remove_floor