class Animal:
    def __init__(self, position, kind, next=None): 
        self.position = position
        self.kind = kind
        self.next = next
        
class Linkedlst:
    def __init__(self, first=None, last=None): 
        self.first = first
        self.last = last
        
    def is_empty(self):
        return self.first is None
        
class Shelter:
    def __init__(self): 
        self.position = 0
        self.dogs = Linkedlst()
        self.cats = Linkedlst()
        
    def enqueue(self, kind): 
        animal = Animal(self.position+1, kind)
        self.position += 1
        if kind == "dog":
            animal_queue = self.dogs
        else: 
            animal_queue = self.cats
        if animal_queue.first:
            animal_queue.last.next = animal
            animal_queue.last = animal
        else: 
            animal_queue.first, animal_queue.last = animal, animal
    
    def dequeue_dog(self):
        animal_queue = self.dogs
        if animal_queue.is_empty():
            return
        adopted = animal_queue.first
        animal_queue.first = animal_queue.first.next
        return adopted
        
    def dequeue_cat(self):
        animal_queue = self.cats
        if animal_queue.is_empty():
            return
        adopted = animal_queue.first
        animal_queue.first = animal_queue.first.next
        return adopted
        
     def dequeue_any(self):
        dogs, cats = self.dogs, self.cats
        if dogs.is_empty():
            return self.dequeue_cat()
        elif cats.is_empty():
            return self.dequeue_dog()
        dog, cat = dogs.first.position, cats.first.position
        if dog < cat: 
            return self.dequeue_dog()
        return self.dequeue_cat()


# Finish writing tests later
# shelter = Shelter()
# shelter.enqueue("dog")
# shelter.enqueue("dog")
# shelter.enqueue("cat")
# shelter.dequeueAny()
