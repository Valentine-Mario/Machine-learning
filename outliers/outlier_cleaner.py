#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    from sklearn.linear_model import LinearRegression


    cleaned_data = []

    ### your code goes here
    reg = LinearRegression().fit(ages, net_worths)


    error_diff=   predictions - net_worths
    #create list of tuple
    zipped = zip(ages, net_worths, error_diff)
    #remove 10% of the lowest values
    new_sorted=sorted(zipped, key=lambda tup: tup[2])[:81]
    cleaned_data=new_sorted
    return cleaned_data

