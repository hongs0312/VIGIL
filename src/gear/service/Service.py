from gear.service import repo


def get_all_gear_info(gear_type):
    if gear_type == "forward":
        return repo.get_all_forward_gear()
    elif gear_type == "goalie":
        return repo.get_all_goalie_gear()
