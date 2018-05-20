from collections import namedtuple

Order = namedtuple('Order', ['revenue', 'time'])


class App:
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
