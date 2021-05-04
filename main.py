import sys
import data
import districts

def main (argv):
    Q1(data)

def Q1(path):
    my_data = data(path=path)
    my_districts = Districts(dataset=my_data)
    d_letters_set = {'S', 'L'}
    my_districts.filter_districts(d_letters_set)
    features = ['hospitalized_with_symptoms',
                'intensive_care',
                'total_hospitalized',
                'home_insulation']
    print ("question 1:")
    my_districts.print_details(features, statistics.statistic_functions)

def Q2(path):
    my_data = data(path=path)
    my_districts = Districts(dataset=my_data)
    my_districts.determine_day_type()
    dict = my_districts.get_districts_class()
    not_green = 0
    for i in len(dict['names']):
        if dict[i]['status'] == "not green":
            not_green += 1
    print ("Question2: ")
    print("Nubmber of districts: "+ len(dict['names']))
    print("Nubmber of not green districts: " + not_green)
    if not_green > 10:
        indicator = "yes"
    else:
        indicator = "no"
    print("Will a lockdown be forced on whole of italy?: " + indicator)


if __name__ == '__main__':
    main(sys.argv)

