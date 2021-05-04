import data
import statistics
class Districts:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        # todo docstring
        all_districts_list = self.dataset.get_all_districts()
        relevant_districts_list = []
        for name in all_districts_list:
            if name[0] in letters:
                relevant_districts_list.append(name)

        self.dataset.set_districts_data(districts=relevant_districts_list)

    def print_details (self, features, statistic_functions):
        for i in features:
            mean = statistic_functions[0](self.dataset.data[i])
            meadian = statistic_functions[1](self.dataset.data[i])
            print (i + ":" + mean + "," + meadian)


    def determine_day_type (self):
        dayindicator = 0
        for i in self.dataset.data:
            if ((self.dataset.data["resigned_healed"][i]-self.dataset.data["new_positives"][i]) > 0):
                dayindicator += 1
            else:
                dayindicator += -1
            if dayindicator > 0:
                self.dataset.data["day_type"] = 1
            else:
                self.dataset.data["day_type"] = 0
            dayindicator =0

    def get_districts_class (self):
        dict = {'name': self.data.get_all_districts,
                'status': [0]*len(self.data.get_all_districts)}
        for i in self.dataset.data:
            if self.dataset.data["day_type"][i] == 1:
                dict[self.dataset.data["name"][i]]["status"] += 1
        for i in len["name"]:
            if dict[i]['status'] > 340:
                dict[i]['status'] = "green"
            else:
                dict[i]['status'] = "not green"
        return dict





