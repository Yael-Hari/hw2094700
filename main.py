import sys
import data
import districts
import statistics

def main(argv):
    Q1(argv[1])
    Q2(argv[1])

def Q1(path):
    my_data = data.Data(path=path)
    my_districts = districts.Districts(dataset=my_data)
    d_letters_set = {'S', 'L'}
    my_districts.filter_districts(d_letters_set)
    features = ['hospitalized_with_symptoms',
                'intensive_care',
                'total_hospitalized',
                'home_insulation']
    print("Question 1:")
    my_districts.print_details(features, statistics.statistic_functions)


def Q2(path):
    my_data = data.Data(path=path)
    my_districts = districts.Districts(dataset=my_data)
    my_districts.determine_day_type()
    green_dict = my_districts.get_districts_class()
    not_green = 0
    for i in green_dict:
        if green_dict[i] == "not green":
            not_green += 1
    print("Question2: ")
    print("Number of districts: " + str(len(green_dict.keys())))
    print("Number of not green districts: " + str(not_green))

    if not_green > 10:
        indicator = "yes"
    else:
        indicator = "no"
    print("Will a lockdown be forced on whole of Italy?: " + indicator)


if __name__ == '__main__':
    main(sys.argv)

