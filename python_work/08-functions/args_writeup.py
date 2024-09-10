"""
# FORMAL PARAMETERS (FPs)
def foo(a, b): <-- these are FPs, aliases for APs
    ...

# ACTUAL PARAMETERS (APs)
foo(4, 3) <-- these are APs

# DEFAULT PARAMETERS (DPs)
def foo(a, b=15, c=27): <-- b and c are DEFAULT PARAMETERS (DPs)
    print(a, b, c)

foo(4) # prints 4, 15, 27

# POLYMORPHISM = functions support more than one calling signature
foo(8, 20) # prints 8, 20, 27
foo(4, 2, 6) # prints 4, 2, 6 <-- DPs are overriden by APs

def bar(a, b=15, c) <-- ILLEGAL << declaring one DP
                        implies all subsequent Ps must
                        have a default value

# KEYWORD PARAMETERS (KPs)
def foo(a=10, b=20, c=30): <-- POSITIONAL PARAMETERS (PPs)
    ...

foo(5) # indicates a = 5, while b and c have default values (20, 30)

foo(c=5) <-- KP << invokes the function with a=10, b=20, c=5

"""