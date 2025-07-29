class Superhero:
    def __init__(self, name, power, strength, secret_identity):
        self._name = name  # Public attribute
        self._power = power  # Public attribute
        self._strength = strength  # Public attribute
        self.__secret_identity = secret_identity  # Private attribute (encapsulation)

    # Method to display superhero details
    def show_info(self):
        return f"Hero: {self._name}, Power: {self._power}, Strength: {self._strength}"

    # Method to use power
    def use_power(self):
        return f"{self._name} uses {self._power}!"

    # Getter for secret identity (encapsulation)
    def get_secret_identity(self):
        return self.__secret_identity

    # Method to be overridden by child class (for polymorphism)
    def special_ability(self):
        return f"{self._name} performs a basic heroic act!"

# Derived class inheriting from Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength, secret_identity, flight_speed):
        super().__init__(name, power, strength, secret_identity)  # Call parent constructor
        self._flight_speed = flight_speed  # Additional attribute

    # Override special_ability method (polymorphism)
    def special_ability(self):
        return f"{self._name} soars through the sky at {self._flight_speed} mph!"

    # Additional method specific to FlyingSuperhero
    def fly(self):
        return f"{self._name} is flying at {self._flight_speed} mph!"

# Create instances
hero1 = Superhero("Thunderbolt", "Lightning Control", 80, "Alex Storm")
hero2 = FlyingSuperhero("Sky Guardian", "Wind Manipulation", 90, "Sam Breeze", 300)

# Test the classes
print(hero1.show_info())  # Output: Hero: Thunderbolt, Power: Lightning Control, Strength: 80
print(hero1.use_power())  # Output: Thunderbolt uses Lightning Control!
print(hero1.special_ability())  # Output: Thunderbolt performs a basic heroic act!
print(hero1.get_secret_identity())  # Output: Alex Storm

print(hero2.show_info())  # Output: Hero: Sky Guardian, Power: Wind Manipulation, Strength: 90
print(hero2.use_power())  # Output: Sky Guardian uses Wind Manipulation!
print(hero2.special_ability())  # Output: Sky Guardian soars through the sky at 300 mph!
print(hero2.fly())  # Output: Sky Guardian is flying at 300 mph!
print(hero2.get_secret_identity())  # Output: Sam Breeze
