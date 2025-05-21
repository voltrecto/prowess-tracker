class Tracker():
    def __init__(self):
        self._initialize()

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
        self.update_prowess()

    def new_game(self):
        self._initialize()

    def reset(self):
        self._initialize(permanents=self.permanents)

    def add_instant(self):
        self.instant += 1
        self.update_prowess()
    
    def add_sorcery(self):
        self.sorcery += 1
        self.update_prowess()

    def add_creature(self):
        self.creature += 1

    def update_prowess(self):
        self.prowess_counter = self.instant + self.sorcery + self.enchantment + self.artifact + self.planeswalker
        self.power_buff = 0
        self.toughness_buff = 0


    def show_status(self):
        print(f"Number of instants cast: {tracker.instant}")
        print(f"Number of sorceries cast: {tracker.sorcery}")
        print(f"Number of creatures cast: {tracker.creature}")
        print(f"Number of prowess triggers: {tracker.prowess_counter}")


tracker = Tracker()

tracker.show_status()
tracker.add_instant()
tracker.show_status()
tracker.add_creature()
tracker.show_status()
tracker.add_sorcery()
tracker.show_status()