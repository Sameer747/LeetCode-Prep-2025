course = "Pyython is great"
indices = []
index = 0

# while True:
#     index = course.find('Pyython', index)  # Find 'Pyython' starting from the current position
#     if index == -1:
#         break  # Stop if 'Pyython' is not found
#     # Append the index of each character in the word 'Pyython'
#     for i in range(len('Pyython')):
#         indices.append(index + i)
#     index += 1  # Move to the next character for the next search

# print(indices)

res = course.split(' ')

print('res:', res[0])
while True:
    index = course.find('Pyython', index)  # Find 'Pyython' starting from the current position
    if index == -1:
        break  # Stop if 'Pyython' is not found
    # Append the index of each character in the word 'Pyython'
    for i in range(len(res[0])):
        indices.append(index + i)
    index += 1  # Move to the next character for the next search

print(indices)


