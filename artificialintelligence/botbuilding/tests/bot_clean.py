import artificialintelligence.botbuilding.bot_clean as bot_clean
import os
from tests.BaseTest import BaseTest


class TestParent(BaseTest):
    def setUp(self):
        self.fname = os.path.basename(__file__).split('.')[0]

    def call_main(self):
        bot_clean.main()

    def test_1000(self):
        self.execute(1000)

    def test_1001(self):
        self.execute(1001)

    def test_1002(self):
        self.execute(1001)