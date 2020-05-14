from util import Queue, Stack


class Player:
    def __init__(self, starting_room, num_rooms):
        self.current_room = starting_room
        self.seen = {starting_room.id}
        self.num_rooms = num_rooms
        self.traversal_path = []
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            self.traversal_path.append(direction)
            self.seen.add(self.current_room.id)
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")
    def find_new_room(self):
        q = Queue()
        q.enqueue((self.current_room, []))

        visited = set()

        while q.size() > 0:
            room, path = q.dequeue()

            if room.id not in self.seen:
                return path
            
            elif room.id not in visited:
                visited.add(room.id)

                for exit in room.get_exits():
                    path_copy = path.copy()
                    path_copy.append(exit)
                    q.enqueue((room.get_room_in_direction(exit), path_copy))

        raise ValueError('Room not found')

    def run_maze(self):
        while len(self.seen) < self.num_rooms:
            if len(self.seen) % 10 == 0:
                print('Rooms seen: ', len(self.seen))
            path = self.find_new_room()
            for direction in path:
                print('Direction: ', direction)
                self.travel(direction)
                print(self.current_room.id)
        print('DONE')