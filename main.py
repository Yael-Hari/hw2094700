def Q1(path):
    my_data = Data(path=path)
    my_districts = Districts(dataset=my_data)
    d_letters_set = {'S', 'L'}
    my_districts.filter_districts(d_letters_set)
    features = ['hospitalized_with_symptoms',
                'intensive_care',
                'total_hospitalized',
                'home_insulation']

    my_districts.print_details(features, statistics.stats_list)

