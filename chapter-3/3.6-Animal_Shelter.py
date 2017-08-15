# Could have implemented this data structure simple and easy
class LinkedList:

    class Node:

        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, e):
        node = self.Node(e)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    def remove_head(self):
        if self.head is None:
            return None
        if self.head.next is None:
            old_head = self.head
            self.head = self.tail = None
            self.size -= 1
            return old_head.data
        new_head = self.head.next
        self.head.next = None
        old_head = self.head
        self.head = new_head
        self.size -= 1
        return old_head.data

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        elements = []
        walk = self.head
        while walk is not None:
            elements.append(walk.data[0])
            walk = walk.next
        return " -> ".join(elements)

class AnimalShelter:

    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def enqueue(self, name, arrival_time, is_dog=True):
        if is_dog:
            self.dogs.append((name, arrival_time))
        else:
            self.cats.append((name, arrival_time))

    def dequeueAny(self):
        if self.dogs.is_empty() and self.cats.is_empty():
            return None
        if self.dogs.is_empty():
            return self.cats.remove_head()
        if self.cats.is_empty():
            return self.dogs.remove_head()

        dog_name, dog_arrival_time = self.dogs.peek()
        cat_name, cat_arrival_time = self.cats.peek()

        if dog_arrival_time < cat_arrival_time:
            return self.dogs.remove_head()
        else:
            return self.cats.remove_head()

    def dequeueDog(self):
        if self.dogs.is_empty():
            raise Exception("No dogs!")
        return self.dogs.remove_head()

    def dequeueCat(self):
        if self.cats.is_empty():
            raise Exception("No cats!")
        return self.cats.remove_head()

    def __str__(self):
        return "Dogs: " + self.dogs.__str__() + "\n" + "Cats: " + self.cats.__str__()


if __name__ == "__main__":

    shelter = AnimalShelter()

    shelter.enqueue("dog1", 1)
    shelter.enqueue("dog2", 2)
    shelter.enqueue("cat1", 3, False)

    print(shelter)

    assert shelter.dequeueAny()[0] == "dog1"
    assert shelter.dequeueCat()[0] == "cat1"
    assert shelter.dequeueDog()[0] == "dog2"
    assert shelter.dequeueAny() is None
