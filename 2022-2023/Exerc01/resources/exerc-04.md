## a

To prove that the intersection of two convex sets is a convex set, we need to show that any line segment between two points in the intersection is also contained in the intersection.

Let A and B be two points in the intersection of convex sets C1 and C2. Since A and B are in the intersection, they must be in both C1 and C2.

Now let C be any point on the line segment between A and B. We need to show that C is also in the intersection of C1 and C2.

Since C is on the line segment between A and B, we can write C as a convex combination of A and B:

C = λA + (1-λ)B

where λ is a scalar between 0 and 1.

Since A and B are in both C1 and C2, we have:

A ∈ C1, A ∈ C2, B ∈ C1, B ∈ C2

Since C1 and C2 are convex sets, this implies that any convex combination of A and B is also in both C1 and C2. Therefore, we have:

λA + (1-λ)B ∈ C1, λA + (1-λ)B ∈ C2

Since λA + (1-λ)B = C, we have shown that C is in both C1 and C2. Therefore, the intersection of C1 and C2 is a convex set.

Hence, we have proved that the intersection of two convex sets is a convex set.

---

##b

To prove that the set {(x,y) ∈ R^2 : x^2 + y^2 ≤ 1} is a convex set, we need to show that for any two points (x1, y1) and (x2, y2) in the set, the line segment between them lies entirely within the set.

Let (x1, y1) and (x2, y2) be two arbitrary points in the set. We want to show that any point on the line segment connecting these two points also lies in the set.

Consider the line segment connecting these two points, parameterized by t:

(x,y) = (1-t)(x1,y1) + t(x2,y2) = ((1-t)x1 + tx2, (1-t)y1 + ty2), where t ∈ [0,1].

We need to show that for any value of t ∈ [0,1], the point (x,y) lies within the set {(x,y) ∈ R^2 : x^2 + y^2 ≤ 1}.

To do this, we can compute the squared distance of the point (x,y) from the origin:

x^2 + y^2 = [(1-t)x1 + tx2]^2 + [(1-t)y1 + ty2]^2
= (1-t)^2 x1^2 + 2t(1-t)x1x2 + t^2 x2^2 + (1-t)^2 y1^2 + 2t(1-t)y1y2 + t^2 y2^2

Using the fact that x1^2 + y1^2 ≤ 1 and x2^2 + y2^2 ≤ 1, we can bound the expression above as follows:

x^2 + y^2 ≤ (1-t)^2 + 2t(1-t) + t^2 = 1

This shows that for any value of t ∈ [0,1], the point (x,y) lies within the set {(x,y) ∈ R^2 : x^2 + y^2 ≤ 1}, and therefore, the set is convex.

Hence, we have shown that the set {(x,y) ∈ R^2 : x^2 + y^2 ≤ 1} is a convex set.
