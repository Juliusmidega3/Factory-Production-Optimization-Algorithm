class Factory:
    def __init__(self, material_type, base_production_rate):
        self.material_type = material_type
        self.base_production_rate = base_production_rate  # Base production rate per minute
        self.production_level = 1
        self.capacity_level = 1
        self.current_production = 0
        self.total_collected = 0

    def get_production_rate(self):
        # Production rate multiplier based on level
        multipliers = [1.0, 1.6, 2.198, 2.788, 3.374, 3.98]
        return self.base_production_rate * multipliers[self.production_level - 1]

    def get_capacity(self):
        # Capacity multiplier based on level
        multipliers = [4.0, 7.16, 12.67, 22.56, 40.18, 100.45]
        return self.get_production_rate() * multipliers[self.capacity_level - 1]

    def produce(self, minutes):
        # Produce materials based on production rate and time
        production = self.get_production_rate() * minutes
        self.current_production = min(self.get_capacity(), self.current_production + production)

    def collect_materials(self):
        # Collect all materials that have been produced
        collected = self.current_production
        self.total_collected += collected
        self.current_production = 0
        return collected

    def upgrade_production(self):
        if self.production_level < 6:
            self.production_level += 1

    def upgrade_capacity(self):
        if self.capacity_level < 6:
            self.capacity_level += 1
