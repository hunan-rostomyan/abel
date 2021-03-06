import math

from typing import List


class Vector:
    def __init__(self, contents: List[float]):
        self._contents = contents
        self.shape = (1, len(self._contents))

    def __str__(self):
        return '<Vector: {}>'.format(self._contents)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._contents == other._contents

    def __neg__(self):
        return self * -1

    def __add__(self, B):
        """Vector addition."""
        xs, ys = self._contents, B._contents
        return Vector([x + ys[i] for i, x in enumerate(xs)])

    def __sub__(self, B):
        """Vector subtraction."""
        return self + -B

    def __mul__(self, k):
        """Scalar multiplication."""
        return Vector([x * k for x in self._contents])

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, k):
        """Scalar division."""
        return self * (1 / k)

    def __matmul__(self, B):
        """Dot product."""
        xs, ys = self._contents, B._contents
        return sum(x * y for x, y in zip(xs, ys))

    def norm(self) -> float:
        """Norm or length."""
        return math.sqrt(self @ self)

    @staticmethod
    def angle(A, B):
        """The angle between vectors A and B."""
        return math.acos(A @ B / (A.norm() * B.norm()))

    @staticmethod
    def proj(A, B):
        """The projection of A onto B."""
        return ((A @ B) / (B @ B)) * B

    @staticmethod
    def scalproj(A, B):
        """The scalar projection of vector A onto B."""
        return ((A @ B) / A.norm())

    @staticmethod
    def cross(A, B):
        """The cross product between two 3D vectors."""
        A_x, A_y, A_z = A._contents
        B_x, B_y, B_z = B._contents
        return Vector([
            A_y * B_z - A_z * B_y,
            A_z * B_x - A_x * B_z,
            A_x * B_y - A_y * B_x
        ])

    @staticmethod
    def average(A, B):
        """The average or arithmetic mean of A and B."""
        return (A + B) / A.shape[1]

    @staticmethod
    def collinear(A, B):
        """Whether two vectors are collinear."""
        def find_n(A_cont, B_cont):
            for a, b in zip(A_cont, B_cont):
                if a != 0:
                    return b / a
                if b != 0:
                    return a / b
        n = find_n(A._contents, B._contents)
        return (n * A == B) or (n * B == A)

    @staticmethod
    def linindep(*vs):
        for i, v in enumerate(vs):
            for j in range(i + 1, len(vs)):
                if Vector.collinear(vs[i], vs[j]):
                    return False
        return True
