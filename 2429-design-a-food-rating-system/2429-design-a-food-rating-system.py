from collections import defaultdict
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_foods = defaultdict(SortedList)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            
            self.cuisine_to_foods[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        old_rating = self.food_to_rating[food]
     
        self.cuisine_to_foods[cuisine].remove((-old_rating, food))
       
        self.cuisine_to_foods[cuisine].add((-newRating, food))
        self.food_to_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        
        return self.cuisine_to_foods[cuisine][0][1]
