from awakening.service import repo


class AwakeningList:
    def __init__(self):
        self.awakening_list = {}
        self.total_page = 0

    def get_list(self):
        if len(self.awakening_list) == 0:
            temp = repo.get_all_awakenings()
            self.awakening_list = sorted(temp, key=lambda x: x['name'])

        if self.total_page == 0:
            self.total_page = (len(self.awakening_list) - 1) // 5 + 1

        return self.awakening_list

    def get_page(self, start, end, awakening_list):
        awakening_name = ""
        rotation = ""
        for i in range(start, end):
            awakening_name += f"{i + 1}. {awakening_list[i]['name']}\n"
            if awakening_list[i]['rotation'] == b'\x01':
                rotation += "- In\n"
            else:
                rotation += " - Out\n"

        return awakening_name, rotation
