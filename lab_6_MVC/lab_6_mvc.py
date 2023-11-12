class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def dot_product(self, other):
        return sum(a*b for a, b in zip(self.coordinates, other.coordinates))

    def cross_product(self, other):
        x = self.coordinates[1]*other.coordinates[2] - self.coordinates[2]*other.coordinates[1]
        y = self.coordinates[2]*other.coordinates[0] - self.coordinates[0]*other.coordinates[2]
        z = self.coordinates[0]*other.coordinates[1] - self.coordinates[1]*other.coordinates[0]
        return Vector([x, y, z])

class VectorView:
    @staticmethod
    def get_vector_coordinates():
        return list(map(float, input("Enter vector coordinates: ").split()))

    @staticmethod
    def show_dot_product(dot_product):
        print(f"Dot product is: {dot_product}")

    @staticmethod
    def show_cross_product(vector):
        print(f"Cross product is: {vector.coordinates}")

class VectorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_data_and_calculate_result(self):
        vector1_coordinates = self.view.get_vector_coordinates()
        vector1 = self.model(vector1_coordinates)

        vector2_coordinates = self.view.get_vector_coordinates()
        vector2 = self.model(vector2_coordinates)

        dot_product = vector1.dot_product(vector2)
        self.view.show_dot_product(dot_product)

        cross_product = vector1.cross_product(vector2)
        self.view.show_cross_product(cross_product)

if __name__ == "__main__":
    model = Vector
    view = VectorView
    controller = VectorController(model, view)

    controller.get_data_and_calculate_result()
