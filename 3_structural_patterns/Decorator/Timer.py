import time

def timer(fn: callable) -> callable:
    def wrapper(*args, **kwargs):
        timer_start = time.time()
        result = fn(*args, **kwargs)
        timer_end = time.time()

        timer_result = timer_end - timer_start
        print(f"The operation took {timer_result} seconds")

        return result
    return wrapper

class Database:
    @timer
    def get_from_db(self) -> str:
        time.sleep(2)
        return "Some data from db"


db = Database()
print(db.get_from_db())