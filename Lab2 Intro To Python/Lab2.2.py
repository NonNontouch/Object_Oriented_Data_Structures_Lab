class Bus:
    def __init__(self, people, fare):
        self.people = people
        self.fare = fare

    def __str__(self):
        return 'this bus has ' + str(self.people) + ' people with fare = ' + str(self.fare)

    def __lt__(self, rhs):
        return self.people*self.fare < rhs.people*rhs.fare

    def people_in(self, k):
        self.people += k

    def people_out(self, k):
        self.people -= k
        if self.people < 0:
            self.people = 0

    def change_fare(self, new_fare):
        self.fare = new_fare


B1P, B2P, B1F, B2F = input(
    "Enter people in Bus1, Bus2, fare Bus1, Bus2 : ").split()
B1P = Bus(int(B1P), int(B1F))
B2P = Bus(int(B2P), int(B2F))
if B1P < B2P:
    print(B1P)
else:
    print(B2P)
B1P.people_in(3)
B1P.people_out(6)
B1P.change_fare(12)
print(B1P)
