class Vector():
    def __init__(self,*args):
        self.vector = []
        if len(args) > 0:
            for number in args:
                try:
                    value = int(number)
                    if value > 0:
                        self.vector.append(value)
                    else:
                        raise Exception(f'The value of {number} is not a natural number. Please enter a valid value')
                except ValueError:
                    print(f'The value of {number} is not a natural number. Please enter a valid value')
                    exit()
    
    def same_length(self,vector):
        if len(vector.vector) == len(self.vector):
            return True
        raise Exception("The length of two vectors does not match")

    def __add__(self,vector):
        if self.same_length(vector):
           return Vector(*[x + y for x, y in zip(self.vector,vector.vector)])
      
            

    def __subtract__(self,vector):
        if self.same_length(vector):
           return Vector(*[x - y for x, y in zip(self.vector,vector.vector)])

    def __mul__(self,vector):
        if self.same_length(vector):
            return sum( [self.vector[i]*vector.vector[i] for i in range(len(self.vector))] )

    def __str__(self):
        text = ''
        for number in self.vector:
            text += f'[{number}] \n'
        return text

# Instantiated lists of numbers
v1Numbers = list(range(1,31))
v2Numbers = list(range(31,61))

# Intialize the vectors
v1 = Vector(*v1Numbers)
v2 = Vector(*v2Numbers)

# Print the vectors
print(v1*v2)
