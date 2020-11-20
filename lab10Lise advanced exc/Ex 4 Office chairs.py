num_rooms = int(input())

free_chairs = 0
room_counter = 0
needed_chairs = 0
for _ in range(num_rooms):
    room_data = input().split()
    room_counter += 1
    if len(room_data[0]) > int(room_data[1]):
        free_chairs += (len(room_data[0]) - int(room_data[1]))
    elif len(room_data[0]) < int(room_data[1]):
        needed_chairs_in_room = int(room_data[1]) - len(room_data[0])
        needed_chairs += needed_chairs_in_room
        print(f"{needed_chairs_in_room} more chairs needed in room {room_counter}")

if free_chairs > needed_chairs:
    free_chairs -= needed_chairs
    print(f"Game On, {free_chairs} free chairs left")