class IDGenerator:
    def __init__(self, start_id=1):
        self.current_id = start_id

    def get_next_id(self):
        next_id = self.current_id
        self.current_id += 1
        return next_id

id_generator = IDGenerator(start_id=4)  # Assuming 3 books already exist
