

from time_to_seconds import time_to_seconds


def test_verify_time_to_seconds():
    assert time_to_seconds("01:00:00") == 3600
    assert time_to_seconds("01:00:10") == 3610
    assert time_to_seconds("01:01:01") == 3661
    assert time_to_seconds("24:00:00") == 86400

    print("all tests passed")




test_verify_time_to_seconds()
test1 = "01:00:00" #should return 3600
test2 =  "01:00:10" #should return 3610
test3 = "01:01:01" #should return 3661
test4 = "24:00:00" #should return 86400