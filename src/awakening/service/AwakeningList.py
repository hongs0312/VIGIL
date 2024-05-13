from src.awakening.service import repo


class AwakeningList:
    def __init__(self):
        self.rotation_list = []
        self.total_page = 0

    def get_list(self):
        if len(self.rotation_list) == 0:
            temp = []
            for i in repo.get_all_awakenings():
                if i['rotation'] == b'\x01':
                    temp.append(i)

            self.rotation_list = sorted(temp, key=lambda x: x['name'])

        if self.total_page == 0:
            self.total_page = (len(self.rotation_list) - 1) // 5 + 1

        return self.rotation_list

    def get_rotation_msg(self, start, end, rotation_list):
        msg = ""
        for i in range(start, end):
            msg += f"{i + 1}. {rotation_list[i]['name']}\n"

        return msg
