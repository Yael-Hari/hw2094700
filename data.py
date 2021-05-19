import pandas


class Data:
    def __init__(self, path):
        self.data = load_data(path)

    def get_all_districts(self):
        """
        make a list of districts names
        :return: list of districts names
        """
        region_names = []
        for name in self.data["denominazione_region"]:
            if name not in region_names:
                region_names.append(name)
        return region_names

    def set_districts_data(self, districts):
        """

        :param districts: list of districts
        :return:none
        """
        result_dict = dict()
        for key in self.data.keys():
            result_dict[key] = []
        for index, district_name in enumerate(self.data["denominazione_region"]):
            if district_name in districts:
                add_to_dict(self.data, result_dict, index)
        self.data = result_dict


def add_to_dict(main_dict, second_dict, i):
    """
    this func adding record from main dict to the second dict
    :param main_dict: dict from which to add the record
    :param second_dict: dict to which to add the record
    :param i: int: number of record in main dict to add
    :return: none
    """
    for key in main_dict.keys():
        second_dict[key].append((main_dict[key])[i])


def load_data(path):
    """

    :param path: path of file to load
    :return: dict
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient='list')
    return data

