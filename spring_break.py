"""
Toby Au
"""

from rit_lib import*


class Station(struct):
    _slots = ((int,'distance'), (str, 'location'))



def read_trip(filepath):
    """
    Takes a filename to read, and returns a list of stations
    :param file:
    :return: lst,mpt
    """
    file = open(filepath)
    lst = []
    mpt = int(file.readline().split()[0])
    for line in file:
        words = line.strip().split()
        str = ""
        for word in words[1:]:
            str += word
        dist = int(words[0])
        lst.append(Station(dist, str))
    return lst, mpt



def Findmin(lst):
    """
    Helper function that returns min distance
    :param lst:
    :return:
    """
    min = lst[0]
    min_dist = lst[0].distance
    for x in lst:
        if x.distance > min_dist:
            min = min
        if x.distance < min_dist:
            min = x
    return min



def sort_choices(lst):
    """
    - sorts the stations in place
    :param lst:
    :return: lst
    """

    for i in range(len(lst)):
        smallest = Findmin(lst[i:])
        small_idx = lst[i:].index(smallest)
        lst[i + small_idx] = lst[i]
        lst[i] = smallest
    return lst



def plan_trip(lst,mpt):
    """
    Takes a sorted list of Stations and the car's miles_per_tank value.
    - function decides whether or not it should stop to fill up at the next station
    - if it stops, it adds this station to the plan, and otherwise, it continues to the destination
    - returns the list of stations at which to stop
    :return:
    """
    total, plan = mpt, []
    for i in range(1, len(lst)):
        if lst[i].distance - lst[i - 1].distance <= mpt:
            mpt -= lst[i].distance
        if lst[i - 1].distance > mpt:
            if lst[i] == lst[len(lst) - 1]:
                return plan
            plan.append(lst[i])
            mpt = total



def report_trip(plan):
    """
    takes the results returned by the plan_trip() and prints the plan
    :param plan:
    :return:
    """
    print("Number of stops made:", len(plan), "\nStops List:")
    for stop in plan:
        print(stop.location, stop.distance)



def main():
    """
    - prints out the list of stations from the lowest distance to the greatest distance
    - prints out miles per tank (until it needs to make a stop)
    - prints out the starting position
    - prints out number of stops made
    - prints out locations where it stopped
    :return:
    """
    stations, mpt = read_trip(input("Enter the trip file name: "))
    stations = sort_choices(stations)
    print("\nList of stations: ")
    for station in stations:
        print("   ", station)
    print("\nMiles per tank:", mpt, "\nStart:", stations[0].location, "with 350 mile range.")
    plan = plan_trip(sort_choices(stations), mpt)
    print(report_trip(plan))

main()
