from itertools import permutations

class Solution:
    def __init__(self):
        self.combos = {5: [[2, 1, 1, 1]], 6: [[3, 1, 1, 1], [2, 2, 1, 1]], 7: [[2, 2, 2, 1], [3, 2, 1, 1]], 8: [[3, 2, 2, 1], [2, 2, 2, 2], [3, 3, 1, 1]], 9: [[3, 3, 2, 1], [3, 2, 2, 2]], 10: [[3, 3, 2, 2], [3, 3, 3, 1]], 11: [[3, 3, 3, 2]]}
    def is_valid_octet(self , octet):
        if len(octet) != 1 and octet[0] == "0":
            return False

        return int(octet) <= 255

    def valid_octets(self, octets):
        for octet in octets:
            if not self.is_valid_octet(octet):
                return False

        return True

    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        if len(A) == 12:
            return ["{}.{}.{}.{}".format(*[A[i:i + 3] for i in range(0, 12, 3)])]
        if len(A) == 4:
            return [".".join(list(A))]

        perms = []
        for perm in self.combos[len(A)]:
            perms.extend(list(set(permutations(perm, 4))))

        valid_addresses = []
        for perm in perms:
            a, b, c, d = perm
            address = [A[:a], A[a:a + b], A[a + b:a + b + c], A[a + b + c:]]
            if self.valid_octets(address):
                valid_addresses.append(".".join(map(str, address)))

        return valid_addresses
