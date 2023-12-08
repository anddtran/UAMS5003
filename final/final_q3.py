'''
Consider the Bayesian belief network that classify ﬁsh (see Figure 1). The node A represents the time of the
year and has four values: a1 =Spring, a2 =Summer, a3 =Fall, and a4 =Winter. The node B represents the
location where the ﬁsh was caught and has values b1 =North Atlantic, and b2 = South Atlantic. The node
X represents the type of ﬁsh and has values x1 =Salmon, and x2 =Sea bass. The node C represents the
”lightness” of the ﬁsh and has values c1 =light, c2 =medium, and c3 =dark. Finally, the node D represents
the thickness and has values d1 =wide, and d2 =thin.

(a) Calculate the join probability of the event that the ﬁsh was caught in the Spring, in the South Atlantic,
and the ﬁsh was salmon and was light and thin.
(b) Write a Python program that provides allows the user to give any event as in (a) and returns the joint
probability for that event.

Figure 1: The figure shows a and b go into x and x goes into c and d.
'''

import re
import sys
