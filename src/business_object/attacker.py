from business_object.pokemon.pokemon import AbstarctPokemon


class Attacker(AbstarctPokemon):
    def get_pokemon_attack_coef(self):
        return 1 + (self.speed_current + self.attack_current)/200