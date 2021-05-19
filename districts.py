import data
import statistics


class Districts:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        """
        leaving only districts starting with chars from the letters set
        :param letters: set of chars
        :return: none
        """
        all_districts_list = self.dataset.get_all_districts()
        relevant_districts_list = []
        for name in all_districts_list:
            if name[0] in letters:
                relevant_districts_list.append(name)

        self.dataset.set_districts_data(districts=relevant_districts_list)

    def print_details(self, features, statistic_functions):
        """
        printing stats
        :param features: list of features
        :param statistic_functions: list of statistic functions
        :return: none
        """
        for i in features:
            mean = statistic_functions[0](self.dataset.data[i])
            meadian = statistic_functions[1](self.dataset.data[i])
            print(i + ": " + str(mean) + ", " + str(meadian))
        print()

    def determine_day_type(self):
        """
        determining if a day is green
        :return: none
        """
        self.dataset.data["day_type"] = []
        for i in range(len(self.dataset.data["resigned_healed"])):
            if (self.dataset.data["resigned_healed"][i] - self.dataset.data["new_positives"][i]) > 0:
                self.dataset.data["day_type"].append(1)
            else:
                self.dataset.data["day_type"].append(0)

    def get_districts_class(self):
        """
        :return: dict with keys all different districts and values green/not green
        """
        all_names = self.dataset.get_all_districts()
        day_type_dict = {all_names[i]: 0 for i in range(len(all_names))}

        for i in range(len(self.dataset.data["day_type"])):
            if self.dataset.data["day_type"][i] == 1:
                day_type_dict[self.dataset.data["denominazione_region"][i]] += 1

        for i in day_type_dict:
            if day_type_dict[i] > 340:
                day_type_dict[i] = "green"
            else:
                day_type_dict[i] = "not green"

        return day_type_dict
