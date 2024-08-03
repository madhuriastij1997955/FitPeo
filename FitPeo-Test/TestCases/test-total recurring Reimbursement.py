import time

from PageObjects.totalRecurring import FitPeo


class Test_001:

    def test_total_reimbusement(self):
        f = FitPeo(self.driver)
        f.calculate_revenue(95)
