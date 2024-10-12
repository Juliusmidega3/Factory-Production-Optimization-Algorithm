import time
from factory import Factory

class Game:
    def __init__(self, materials_required, base_production_rates):
        self.factories = []
        self.materials_required = materials_required
        self.materials_collected = {material: 0 for material in materials_required}
        self.base_production_rates = base_production_rates
        self.max_factories = 12
        self.action_queue = []  # Keeps track of ongoing actions (building/upgrading)
        self.time_elapsed = 0

    def build_factory(self, material_type):
        if len(self.factories) < self.max_factories:
            new_factory = Factory(material_type, self.base_production_rates[material_type])
            self.factories.append(new_factory)
            # Simulate 2 minutes build time
            self.add_action(2, f"Build {material_type} factory")
            return new_factory
        return None

    def add_action(self, duration, description):
        self.action_queue.append({
            'duration': duration,
            'remaining_time': duration,
            'description': description
        })

    def upgrade_factory(self, factory, upgrade_type):
        if upgrade_type == 'production':
            factory.upgrade_production()
            self.add_action(30 * factory.production_level, f"Upgrade production of {factory.material_type} to level {factory.production_level}")
        elif upgrade_type == 'capacity':
            factory.upgrade_capacity()
            self.add_action(15 * factory.capacity_level, f"Upgrade capacity of {factory.material_type} to level {factory.capacity_level}")

    def collect_materials(self):
        for factory in self.factories:
            collected = factory.collect_materials()
            self.materials_collected[factory.material_type] += collected
            print(f"Collected {collected} units of {factory.material_type}")

    def simulate(self, total_minutes):
        while self.time_elapsed < total_minutes:
            # Process action queue
            if len(self.action_queue) > 0:
                current_action = self.action_queue[0]
                current_action['remaining_time'] -= 1
                if current_action['remaining_time'] <= 0:
                    print(f"Action complete: {current_action['description']}")
                    self.action_queue.pop(0)

            # Produce materials in each factory for 1 minute
            for factory in self.factories:
                factory.produce(1)

            # Every 10 minutes, collect materials
            if self.time_elapsed % 10 == 0:
                self.collect_materials()

            # Increment time
            self.time_elapsed += 1
            time.sleep(0.1)  # Speed up simulation by pausing for a fraction of a second per minute

            # Check if goal is reached
            if all(self.materials_collected[mat] >= self.materials_required[mat] for mat in self.materials_required):
                print("All materials collected! Simulation complete.")
                break

    def show_status(self):
        print(f"Time Elapsed: {self.time_elapsed} minutes")
        print(f"Factories: {len(self.factories)}")
        print(f"Materials Collected: {self.materials_collected}")
        print(f"Actions in Queue: {len(self.action_queue)}")


if __name__ == "__main__":
    materials_required = {
        "wheat": 75700,
        "fruit": 219000,
        "iron": 206000,
        "water": 164000,
        "silver": 86300
    }

    base_production_rates = {
        "wheat": 14.017,
        "fruit": 42.733,
        "iron": 40.217,
        "water": 31.733,
        "silver": 16.133
    }

    game = Game(materials_required, base_production_rates)

    # Example: Build factories at the start
    game.build_factory("wheat")
    game.build_factory("fruit")

    # Run the simulation for 1000 minutes
    game.simulate(1000)

    # Show the final status
    game.show_status()
