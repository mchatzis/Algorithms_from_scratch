import json
import pprint
import random

with open('test_data.json') as file:
    data = json.load(file)


"""
    len(data) =~ 20,000
    data format:
        {
            'id': int, (unique)
            'end_time': int,
            'piece_id': int,
            'start_time': int,
            'status': int,
            'user_id': int
        }
"""

# 1
# statuses = [item['status'] for item in data]
# status_population = len(set(statuses))

# Check for duplicates - No duplicates found
# ids = [item['id'] for item in data]
# ids_population = len(set(ids))

# 2
# users_list = [item['user_id'] for item in data]
# from collections import Counter
# users_dict = Counter(users_list)


# users_tuples = users_dict.items()
# users_tuples_sorted = sorted(users_tuples, key=lambda x: x[1], reverse=True)
# first_five_users = users_tuples_sorted[:5]

# for user, freq in first_five_users:
#     print(f"user{user}:{freq}")


# 3
import time
# status = 8951
# entries = [item for item in data if item['status'] == status]
# now = int(time.time())
# times = [(item['end_time'] if item['end_time'] is not None else now) - item['start_time'] for item in entries]
# print(sum(times)/len(times)/3600)

status = 8951
entries = [item for item in data if item['status'] == status]

print(sum(times)/len(times)/3600)

