import numpy as np

class Plane:
    def __init__(self, normal, d):
        self.d = d
        n_hat = np.linalg.norm(normal)
        self.normal = np.array(normal)/n_hat

    def distance(self, point):
        return np.dot(self.normal, point) - self.d

class CompositePlanes:
    def __init__(self, planes):
        self.planes = np.array(planes)

    def inside(self, point):
        is_inside = True
        for plane in self.planes:
            #print(plane.distance(point))
            is_inside = is_inside and plane.distance(point) < 0

        return is_inside

    def on_surface(self, point):
        for plane in self.planes:
            if plane.distance(point) == 0:
                return True

        return False

    def closest_surface(self, point):
        # Returns array ID of plane which is closest
        if self.inside(point):
            print("Getting the closest surface form the inside not supported yet!")
            return None

        epsilon = 1e-8

        distances = []
        point = np.array(point)

        plane_id = -1
        for plane in self.planes:
            plane_id += 1
            #print((plane.distance(point) - epsilon)*plane.normal)
            #print(self.inside(point - (plane.distance(point) + epsilon)*plane.normal))
            if self.inside(point - (plane.distance(point) + epsilon)*plane.normal):
                #print("!!!")
                distances.append([plane_id, np.abs(plane.distance(point))])

        distances = np.array(distances)

        minimal_distance_plane_id = int(distances[np.argmin(distances[:][0])][0])

        return minimal_distance_plane_id

    def distance(self, point):
        return self.planes[self.closest_surface(point)].distance(point)


def main():
    plane0 = Plane([1,0,0], 1)
    plane1 = Plane([0,1,0], 1)
    plane2 = Plane([0,0,1], 1)
    plane3 = Plane([-1,0,0], 1)
    plane4 = Plane([0,-1,0], 1)
    plane5 = Plane([0,0,-1], 1)

    cube = CompositePlanes([plane0, plane1, plane2, plane3, plane4, plane5])

    print(plane1.distance([0,2,0]))

    print(cube.on_surface([1,0,0]))
    print(cube.inside([0,0,0]))
    print(cube.inside([3,4,5]))

    print(cube.closest_surface([0,2.5,0]))
    print(cube.distance([0,2.5,0]))

if __name__ == "__main__":
    main()