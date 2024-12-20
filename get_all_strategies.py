from strategies.cooperator_strategy import CooperatorStrategy
from strategies.defector_strategy import DefectorStrategy
from strategies.random_strategy import RandomStrategy
from strategies.randomp_strategy import RandomPStrategy
from strategies.tit_for_tat_strategy import TitForTatStrategy
from strategies.tit_for_twotat_strategy import TitForTwoTatStrategy
from strategies.twotit_for_tat_strategy import TwoTitForTatStrategy


def get_all_strategies() -> list:
    return [
        CooperatorStrategy,
        DefectorStrategy,
        RandomPStrategy,
        RandomStrategy,
        TitForTatStrategy,
        TitForTwoTatStrategy,
        TwoTitForTatStrategy,
    ]
