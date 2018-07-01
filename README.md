# Vector

```python
from abel.linalg.vector import Vector

a, b = Vector([1, 2]), Vector([3, 4])
c, d = Vector([1, 2, 3]), Vector([4, 5, 6])

assert a.shape == b.shape == (1, 2)
assert c.shape == d.shape == (1, 3)
```

#### Addition

```python
assert a + a == Vector([2, 4])
assert a + b == Vector([4, 6])
assert b + b == Vector([6, 8])
```

#### Subtraction

```python
assert a - b == Vector([-2, -2])
assert b - a == Vector([2, 2])
```

#### Scaling

```python
assert a * 5 == Vector([5, 10])
assert 5 * a == Vector([5, 10])
```

#### Dot (inner) product

```python
assert a @ b == 11
assert a @ a == 5
```

#### Norm (length)

```python
assert a.norm() - 2.236 < 0.001
assert b.norm() - 5 < 0.001
```

#### Angle

```python
assert Vector.angle(a, a) < 0.001
assert Vector.angle(a, b) - 0.1799 < 0.001
assert Vector.angle(a, b) == Vector.angle(b, a)
```

#### Vector projection

```python
assert Vector.proj(a, a) == a
assert Vector.proj(a, b) == Vector([1.32, 1.76])
assert Vector.proj(b, a) == Vector([2.2, 4.4])
```

#### Scalar projection

```python
assert Vector.scalproj(a, b) - 4.919 < 0.01
assert Vector.scalproj(b, a) - 2.2 < 0.01
assert Vector.scalproj(a, a) - 2.236 < 0.01
assert Vector.scalproj(b, b) - 5 < 0.1
```

#### Cross product

```python
assert Vector.cross(c, d) == Vector([-3, 6, -3])
```