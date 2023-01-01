"""
Проверка способностей робота
"""

from classes import Robot


def check_skills(robot:Robot, language_db)->None:
    """
    Проверка способностей робота
    """

    # print(f"Проверка способностей у робота \"{robot.name}\":")
    # print(f"build_home: {hasattr(robot, 'build_home')}")
    # print(f"build_barn: {hasattr(robot, 'build_barn')}")
    # print(f"add_floor: {hasattr(robot, 'add_floor')}")
    # print(f"remove_floor: {hasattr(robot, 'remove_floor')}")
    # print()

    print(language_db.get_string("ROBOT_CHECK_SKILLS").format(robot_name = robot.name))
    print(language_db.get_string("ROBOT_CHECK_HOME_SKILL"), hasattr(robot, 'build_home'))
    print(language_db.get_string("ROBOT_CHECK_BARN_SKILL"), hasattr(robot, 'build_barn'))
    print(language_db.get_string("ROBOT_CHECK_FLOOR_ADD_SKILL"), hasattr(robot, 'add_floor'))
    print(language_db.get_string("ROBOT_CHECK_FLOOR_REMOVE_SKILL"), hasattr(robot, 'remove_floor'))
    print()