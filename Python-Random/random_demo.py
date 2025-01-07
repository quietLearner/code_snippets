import random


print(random.uniform(1, 10))

# Return random integer in range [a, b], including both end points.
value = random.randint(1, 6)
print(value)


print(random.choice(["red", "black", "green"]))


colors = ["red", "black", "green"]
# Return a k length list of unique elements chosen from the population sequence or set.
print(random.choices(colors, k=10))

# total weight of the colors is 38, red has 18 out of 38 chance to be picked
print(random.choices(colors, k=10, weights=[18, 18, 2]))

# playing cards, 52 cards in a deck
deck = list(range(1, 53))
print(deck)

random.shuffle(deck)

print(deck)

# take 5 cards from the deck, choice might take the same card multiple times, sample take unique cards
hand = random.sample(deck, k=5)
print(hand)
