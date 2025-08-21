import sys
from utils import assert_equals
from analysis import accuracy, majority_count, assign_labels


# ----------------------------------------------------------
# HELPER FUNCTIONS
def setup_for_tests():
    """Creates are returns data for testing analysis methods.

    Returns: data, a list of data points
             labels, numeric labels for each data point
             centroids_dict1, three 4D centroids
             centroids_dict2, three non-random 4D centroids
                with poor starting values
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    list_of_points = [
        [-1.01714716,  0.95954521,  1.20493919,  0.34804443],
        [-1.36639346, -0.38664658, -1.02232584, -1.05902604],
        [1.13659605, -2.47109085, -0.83996912, -0.24579457],
        [-1.48090019, -1.47491857, -0.6221167,  1.79055006],
        [-0.31237952,  0.73762417,  0.39042814, -1.1308523],
        [-0.83095884, -1.73002213, -0.01361636, -0.32652741],
        [-0.78645408,  1.98342914,  0.31944446, -0.41656898],
        [-1.06190687,  0.34481172, -0.70359847, -0.27828666],
        [-2.01157677,  2.93965872,  0.32334723, -0.1659333],
        [-0.56669023, -0.06943413,  1.46053764,  0.01723844]
    ]
    labels = [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]
    centroids_dict1 = {
        "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
        "centroid2": [-0.71767545, 1.2309971, -1.00348728, -0.38204247],
        "centroid3": [-1.71767545, 0.29971, 0.00328728, -0.38204247],
    }
    centroids_dict2 = {
        "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
        "centroid2": [10, 10, 10, 10],
        "centroid3": [-10, 1, -10, 10],
    }
    return list_of_points, labels, centroids_dict1, centroids_dict2


# ----------------------------------------------------------
# TESTS
def test_assign_labels():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    try:
        r = assign_labels([[0]], [0], {"centroid1": [0]})
        if r is None:
            sys.tracebacklimit = 0
            raise Exception(
                "assign_labels() returned None; have you implemented it yet?")
    finally:
        pass

    # set up
    (list_of_points, labels,
     centroids_dict1, centroids_dict2) = setup_for_tests()

    # test with centroids_dict1
    answer = {'centroid3': [0, 1, 2, 1, 2, 2, 0], 'centroid1': [0],
              'centroid2': [1, 0]}

    assert_equals(answer,
                  assign_labels(list_of_points, labels, centroids_dict1))

    # test with centroids_dict2
    answer = {'centroid1': [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]}
    assert_equals(answer,
                  assign_labels(list_of_points, labels, centroids_dict2))

    # test to make sure parameters remains unchanged
    # If you're failing this test,
    # make sure your code doesn't modify the parameters passed in
    (list_of_points_copy, labels_copy,
     centroids_dict1_copy, centroids_dict2_copy) = setup_for_tests()
    assert_equals(list_of_points_copy, list_of_points)
    assert_equals(labels_copy, labels)
    assert_equals(centroids_dict1_copy, centroids_dict1)
    assert_equals(centroids_dict2_copy, centroids_dict2)

    print("test_assign_labels passed")


def test_majority_count():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    try:
        r = majority_count([0])
        if r is None:
            sys.tracebacklimit = 0
            raise Exception(
                "majority_count() returned None; have you implemented it yet?")
    finally:
        pass

    # single
    assert_equals(6, majority_count([0, 0, 0, 0, 0, 0]))
    assert_equals(5, majority_count([1, 0, 0, 0, 0, 0]))
    assert_equals(5, majority_count([0, 1, 1, 1, 1, 1]))

    # mixed
    assert_equals(4, majority_count([0, 0, 1, 1, 0, 0]))
    assert_equals(4, majority_count([0, 2, 2, 2, 3, 3, 0, 1, 1, 0, 0]))

    # tied max count
    assert_equals(4, majority_count([0, 2, 2, 2, 0, 2, 0, 0]))

    # test with labels outside of 1-10
    assert_equals(6,
                  majority_count(["cat", "cat", "cat", "cat", "cat", "cat"]))

    print("test_majority_count passed")


def test_accuracy():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    try:
        r = accuracy([[0]], [0], {"centroid1": [0]})
        if r is None:
            sys.tracebacklimit = 0
            raise Exception(
                "accuracy() returned None; have you implemented it yet?")
    finally:
        pass

    # set up
    (list_of_points, labels,
     centroids_dict1, centroids_dict2) = setup_for_tests()

    # test with centroids_dict1
    expected = 0.5
    received = accuracy(list_of_points, labels, centroids_dict1)
    assert_equals(expected, received)

    # test with centroids_dict2
    expected = 0.4
    received = accuracy(list_of_points, labels, centroids_dict2)
    assert_equals(expected, received)

    # test to make sure parameters remains unchanged
    # If you're failing this test,
    # make sure your code doesn't modify the parameters passed in
    (list_of_points_copy, labels_copy,
     centroids_dict1_copy, centroids_dict2_copy) = setup_for_tests()
    assert_equals(list_of_points_copy, list_of_points)
    assert_equals(labels_copy, labels)
    assert_equals(centroids_dict1_copy, centroids_dict1)
    assert_equals(centroids_dict2_copy, centroids_dict2)

    print("test_accuracy passed")


def main_test():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    test_assign_labels()
    test_majority_count()
    test_accuracy()
    print("all tests passed.")


if __name__ == "__main__":
    main_test()
