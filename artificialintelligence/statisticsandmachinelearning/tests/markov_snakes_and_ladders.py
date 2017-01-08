import artificialintelligence.statisticsandmachinelearning.markov_snakes_and_ladders as markov_snakes_and_ladders
import os
from tests.BaseTest import BaseTest


class TestParent(BaseTest):
    def setUp(self):
        self.fname = os.path.join(os.path.dirname(__file__), os.path.basename(__file__).split('.')[0])

    def call_main(self):
        markov_snakes_and_ladders.main()

    def test_2(self):
        self.execute(2)

    def test_1000(self):
        self.execute(1000)