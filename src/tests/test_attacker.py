from business_object.pokemon.attacker import Attacker
from business_object.statistic import Statistics


class TestAttacker:
    def test_get_coeff_damage_type(self):
        snorlax = Attacker(stat_current=Statistics(attack=100, defense =100))

        multiplier = snorlax.get_pokemon_attack_coef()

        assert multiplier == 1.5