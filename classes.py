from collections import namedtuple

# namedtuple for order to have easy access to its time and revenue
Order = namedtuple('Order', ['revenue', 'time'])


class App:
    """
    Class for app.

    Attributes:
        name – name of the program
        e.g. Dotyk.Application.AirHockey --> name = AirHockey
        total_time - total time, while this app was launched
        total_revenue - total revenue, that this app yielded

    Methods:
         calc_eff - calculates the efficiency of this app by simple formula
         e.g. efficiency = (total revenue)/(total working time)
    """
    def __init__(self, name, total_time, total_revenue):
        self.name = name.rsplit('.', 1)[1]
        self.total_time = total_time
        self.total_revenue = total_revenue
        self.efficiency = 0

    def calc_eff(self):
        if self.total_time.seconds:
            self.efficiency = self.total_revenue / self.total_time.seconds

    def __repr__(self):
        return "T:{}, R:{}, E: {}".format(self.total_time, self.total_revenue, self.efficiency)
