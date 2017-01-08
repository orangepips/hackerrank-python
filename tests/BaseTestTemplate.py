# import path.to.module as module
import os
from BaseTest import BaseTest


class TestParent(BaseTest):
    def setUp(self):
        self.fname = os.path.basename(__file__).split('.')[0]

    def call_main(self):
        pass
        # module.main()

    def test_1000(self):
        self.execute(1000)