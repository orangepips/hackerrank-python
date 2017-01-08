import artificialintelligence.botbuilding.bot_saves_princess as bot_saves_princess
import os
from tests.BaseTest import BaseTest


class TestParent(BaseTest):
    def setUp(self):
        self.fname = os.path.basename(__file__).split('.')[0]

    def call_main(self):
        bot_saves_princess.main()

    def test_1000(self):
        self.execute(1000)

    def test_2000(self):
        self.execute(2000)
