from monlen import month_length

def test_month_length():
    
    month_day_dict = {
        "January": 31,
        "February": {"leap": 29, "not_leap": 28},
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    error_msg_month = "Month not matching day!"
    error_msg_february = "Month not matching day, and " + \
                         "check leap year status!"
    error_msg_sthelse = "If input is not the name of a " + \
                        "month, then should return None!"

    for key, value in month_day_dict.items():
        if key == "February":
            assert month_length(key, True) == \
                   month_day_dict[key]["leap"], error_msg_february
            assert month_length(key, False) == \
                   month_day_dict[key]["not_leap"], error_msg_february
        else:
            assert month_length(key) == \
                   month_day_dict[key]
    assert month_length("Something_Else") == None, error_msg_sthelse
