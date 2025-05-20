class SpellTracker():
    def __init__(self):
        self.initialize()

    def _initialize(self, permanents=None):
        self.spell_log = [] # List to hold all spells cast or copied in one turn
        self.permanents = permanents if permanents is not None else [] # List of user permanents in play that affect bonuses

        # Counters for spell cast
        self.cast_instant_sorcery = 0
        self.cast_other_noncreature = 0
        self.cast_creature = 0

        # Counters for spell copied (for purposes of magecraft)
        self.copied_instant_sorcery = 0
        self.copied_other_noncreature = 0
        self.copied_creature = 0

        # Counters for spells an opponent played (for purposes of storm)
        self.cast_by_opponent = 0 # Count of spells an opponent played for purposes of storm

        # Counters and trackers for temporary buffs
        self.power_buff = 0
        self.toughness_buff = 0
    
    def reset(self):
        self._initialize(permanents=self.permanents)
    
    


def main():
    print("Prowess Tracker")
    print("Select option:")
    print("1. New turn/reset all")
    print("2. Undo last action")
    print("3. You cast a noncreature spell (instant or sorcery)")
    print("4. You cast a noncreature spell (other)")
    print("5. You cast a creature spell")
    print("6. You copied a noncreature spell (instant or sorcery)")
    print("7. You copied a noncreature spell (other)")
    print("8. You copied a creature spell")
    print("9. Opponent cast (any) spell")
    
if __name__ == "__main__":
    main()