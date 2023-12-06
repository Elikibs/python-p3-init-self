#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed= breed
    
max = Dog("Max")
print(f"{max.name} is of breed {max .breed}")

siba = Dog("Siba", "Bobel")
print(f"{siba.name} is of breed {siba.breed}")