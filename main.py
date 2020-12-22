class Underscore:
    def map(self, iterable, callback):
        for x in range (len(iterable)):
            iterable[x]=callback(iterable[x])
        print(iterable)
        return iterable

    def find(self, iterable, callback):
        for x in range (len(iterable)):
            if callback(iterable[x])==True:
                print(iterable[x])
                return iterable[x]

    def filter(self, iterable, callback):
        ouput=[];
        for x in range (len(iterable)):
            if callback(iterable[x])==True:
                ouput.append(iterable[x])
        print(ouput)
        return ouput


    def reject(self, iterable, callback):
        ouput = [];
        for x in range(len(iterable)):
            if callback(iterable[x]) == False:
                ouput.append(iterable[x])
        print(ouput)
        return ouput

# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above

evens = _.map([1, 2, 3, 4, 5, 6], lambda x: x*2)


evens = _.find([1, 2, 3, 4, 5, 6], lambda x: x>4)

evens = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)