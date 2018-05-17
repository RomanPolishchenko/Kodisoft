from collections import namedtuple

Order = namedtuple('Order', ['revenue', 'time'])


class App:
    def __init__(self, total_time, total_revenue, efficiency):
        self.total_time = total_time
        self.total_revenue = total_revenue
        self.efficiency = efficiency

    def calc_eff(self):
        self.efficiency = self.total_revenue / self.total_time

    def __repr__(self):
        return str(self.total_time)
