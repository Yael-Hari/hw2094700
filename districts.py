

class Districts:
    # __init__

    def filter_districts(self, letters):
        # todo docstring
        all_districts_list = self.dataset.get_all_districts()
        relevant_districts_list = []
        for name in all_districts_list:
            if name[0] in letters:
                relevant_districts_list.append(name)

        self.dataset.set_districts_data(districts=relevant_districts_list)