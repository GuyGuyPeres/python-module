friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
# print(f"friends group: {friends}")
# print(f"abroad group: {abroad}")

local = friends.difference(abroad)
# print(local)

HutzLaAretz = abroad.difference(friends)
# print(HutzLaAretz)

empty = {}
# print(empty)
local = {"Rolf"}
abroad = {"Bob", "Anne"}

# friends = local.union(abroad)
# print(friends)
# print(friends | abroad)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
print(f"Common Elements: {art.intersection(science)}")
print(art & science)

print("Bob" in art)
print("Anne" in art)

