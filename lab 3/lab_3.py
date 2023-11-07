class Runway:
    __instance = None

    @staticmethod
    def getInstance():
        if Runway.__instance == None:
            Runway()
        return Runway.__instance

    def __init__(self):
        if Runway.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Runway.__instance = self
            self._plane_on_runway = None

    def is_available(self):
        return self._plane_on_runway is None

    def land_plane(self, plane):
        if self.is_available():
            self._plane_on_runway = plane
            print(f"Plane {plane} has landed.")
        else:
            print("Runway is not available.")

    def clear_runway(self):
        if not self.is_available():
            print(f"Plane {self._plane_on_runway} has cleared the runway.")
            self._plane_on_runway = None
        else:
            print("Runway is already clear.")

runway = Runway.getInstance()
runway.land_plane("Flight 101")
runway.clear_runway()
runway.land_plane("Flight 102")
