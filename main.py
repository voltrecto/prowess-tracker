class Tracker():
    def __init__(self):
        self.initialize()

    def _initialize(self, permanents=None):
        self.spell_log = [] # List to hold all spells cast or copied in one turn
        self.permanents = permanents if permanents is not None else [] # List of permanents in play that affect bonuses

        # Spell counters
        self.instant = 0
        self.sorcery = 0
        self.enchantment = 0
        self.artifact = 0
        self.planeswalker = 0
        self.creature = 0

        # Counters for temporary buffs
        self.prowess_counter = self.instant + self.sorcery + self.enchantment + self.artifact + self.planeswalker
        self.power_buff = 0
        self.toughness_buff = 0

    def new_game(self):
        self._initialize()

    def reset(self):
        self._initialize(permanents=self.permanents)
    




def main():
    print("Prowess Tracker")
    print("Select option:")
    print("1. New game (reset everything)")
    print("2. New turn (reset spells only)")
    print("3. Cast instant")
    print("4. Cast sorcery")
    print("5. Cast enchantment")
    print("6. Cast artifact")
    print("7. Cast planeswalker")
    print("8. Cast creature")
    print("9. Remove permanent")
    print("10. Undo last action")


if __name__ == "__main__":
    main()