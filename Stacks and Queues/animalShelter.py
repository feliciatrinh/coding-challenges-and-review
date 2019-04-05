class Animal(): 
    def __init__(self, position, kind, next=None): 
        self.position = position
        self.kind = kind
        self.next = next
        
class Linkedlst(): 
    def __init__(self, first=None, last=None): 
        self.first = first
        self.last = last
        
    def isEmpty(self): 
        return self.first is None
        
class Shelter(): 
    def __init__(self): 
        self.position = 0
        self.dogs = Linkedlst()
        self.cats = Linkedlst()
        
    def enqueue(self, kind): 
        animal = Animal(self.position+1, kind)
        self.position += 1
        if kind == "dog": 
            animalQueue = self.dogs
        else: 
            animalQueue = self.cats
        if animalQueue.first: 
            animalQueue.last.next = animal
            animalQueue.last = animal
        else: 
            animalQueue.first, animalQueue.last = animal, animal
    
    def dequeueDog(self): 
        animalQueue = self.dogs
        if animalQueue.isEmpty(): 
            return
        adopted = animalQueue.first
        animalQueue.first = animalQueue.first.next
        return adopted
        
    def dequeueCat(self): 
        animalQueue = self.cats
        if animalQueue.isEmpty(): 
            return
        adopted = animalQueue.first
        animalQueue.first = animalQueue.first.next
        return adopted     
        
     def dequeueAny(self): 
        dogs, cats = self.dogs, self.cats
        if dogs.isEmpty(): 
            return self.dequeueCat()
        elif cats.isEmpty(): 
            return self.dequeueDog()
        dog, cat = dogs.first.position, cats.first.position
        if dog < cat: 
            return self.dequeueDog()
        return self.dequeueCat()
        
/* Finish writing tests later
shelter = Shelter()
shelter.enqueue("dog")
shelter.enqueue("dog")
shelter.enqueue("cat")
shelter.dequeueAny()
*/
