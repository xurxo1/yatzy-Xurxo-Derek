from src.pips import Pips

class Yatzy:
    # Class constants
    ZERO = 0
    FIFTY = 50

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice) -> int:
        return sum(dice)

    @staticmethod
    def yatzy(*dice) -> int:
        return Yatzy.FIFTY if len(set(dice)) == 1 else Yatzy.ZERO

    @staticmethod
    def ones(*dice) -> int:
        ONE = Pips.ONE.value
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice) -> int:
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice) -> int:
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE

    def fours(self) -> int:
        return self.__sum_dice_equals(Pips.FOUR.value)

    def fives(self) -> int:
        return self.__sum_dice_equals(Pips.FIVE.value)

    def sixes(self) -> int:
        return self.__sum_dice_equals(Pips.SIX.value)

    def __sum_dice_equals(self, pip: int) -> int:
        return self.dice.count(pip) * pip

    @classmethod
    def pair(cls, *dice) -> int:
        return cls.__get_pip_repeated(dice, Pips.TWO.value)

    @classmethod
    def two_pairs(cls, *dice) -> int:
        pairs = cls.__get_repeated_pips(dice, Pips.TWO.value)
        return sum(pairs) * Pips.TWO.value if len(pairs) == 2 else Yatzy.ZERO

    @classmethod
    def three_of_a_kind(cls, *dice) -> int:
        return cls.__get_pip_repeated(dice, Pips.THREE.value)

    @classmethod
    def four_of_a_kind(cls, *dice) -> int:
        return cls.__get_pip_repeated(dice, Pips.FOUR.value)

    @classmethod
    def __get_pip_repeated(cls, dice, times: int) -> int:
        pips = cls.__get_repeated_pips(dice, times)
        return pips[0] * times if pips else Yatzy.ZERO

    @classmethod
    def __get_repeated_pips(cls, dice, times: int) -> list:
        return [pip for pip in Pips.reversedValues() if dice.count(pip) >= times]

    @classmethod
    def small_straight(cls, *dice) -> int:
        return cls.chance(*dice) if not Pips.minus(Pips.SIX) - set(dice) else Yatzy.ZERO

    @classmethod
    def large_straight(cls, *dice) -> int:
        return cls.chance(*dice) if not Pips.minus(Pips.ONE) - set(dice) else Yatzy.ZERO

    @classmethod
    def full_house(cls, *dice) -> int:
        two_of_a_kind = cls.__two_of_a_kind(*dice)
        three_of_a_kind = cls.three_of_a_kind(*dice)
        return two_of_a_kind + three_of_a_kind if two_of_a_kind and three_of_a_kind else Yatzy.ZERO

    @classmethod
    def __two_of_a_kind(cls, *dice) -> int:
        pips = cls.__get_repeated_pips(dice, Pips.TWO.value)
        return pips[0] * Pips.TWO.value if pips else Yatzy.ZERO