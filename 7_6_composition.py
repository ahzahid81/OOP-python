class Engine:
    def __init__(self) -> None:
        pass

    def start(self):
        return "Engine Started"

class Driver:
    def __init__(self) -> None:
        pass

# Char "has a"   
class car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()
    