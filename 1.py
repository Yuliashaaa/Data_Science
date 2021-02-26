users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}]
    
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# friends contains friends of user
for user in users:
    user["friends"] = []

for i, j in friendships:
    user[i]["friends"].append(users[j]) # add j as friend for i
    user[j]["friends"].append(isers[i]) # add i as friend for j
    
# number of friends
def number_of_friends(user):
    return len(user["friends"]) 

total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

# amount of friends for every user id
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

sorted(num_friends_by_id, key = Lambda(user_id, num_friends): num_friends, reverse = True)
