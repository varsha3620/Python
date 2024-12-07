def compare(S1, S2, n):
        return S1[:n] == S2[:n]

S1 = input("Enter First String: ")
S2 = input("Enter Second String: ")
n = int(input("Enter the position upto which the comparison should take place: ")) 
print("Comparison result:", compare(S1, S2, n))




