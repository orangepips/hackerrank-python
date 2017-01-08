import artificialintelligence.statisticsandmachinelearning.predicting_house_prices as predicting_housing_prices
import os
from tests.BaseTest import BaseTest


class TestParent(BaseTest):
    def setUp(self):
        self.fname = os.path.join(os.path.dirname(__file__), os.path.basename(__file__).split('.')[0])

    def call_main(self):
        predicting_housing_prices.main()

    def test_1000(self):
        self.execute(1000)