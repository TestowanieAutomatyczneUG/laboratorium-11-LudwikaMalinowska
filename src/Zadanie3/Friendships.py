
class Friendships:

    fr = {
        "Miotk": ["Kowalski", "Nowak", "Bobkowska"],
        "Kowalski": ["Miotk", "Nowak"],
        "Nowak": ["Miotk", "Kowalski", "Bobkowska"],
        "Bobkowska": ["Miotk", "Nowak"],
    }

    def makeFriends(self, person1, person2):
        id = self.fr[person1].index(person2)
        id2 = self.fr[person2].index(person1)
        if id < 0 and id2 < 0:
            self.fr[person1].append(person2)
            self.fr[person2].append(person1)
        else:
            print(f"{person1} and {person2} are already friends")




    def getFriendsList(self, person):
        return self.fr[person]

    def areFriends(self, person1, person2):
        id = self.fr[person1].index(person2)
        if id >= 0:
            return True
        else:
            return False

    def addFriend(self, person, friend):
        id = self.fr[person].index(friend)
        if id < 0:
            self.fr[person].append(friend)
        else:
            print(f"{friend} is already in {person} friend list")
