from coding_exercise.domain.model.cable import Cable
import math

class Splitter:

    def __validate(self, valid = True):
        if not valid:
            raise ValueError

    def split(self, cable: Cable, times: int) -> list[Cable]:
        max_length = math.floor(cable.length / (times + 1))
        self.__validate(max_length > 0)
        remainder = cable.length % (times+1)

        return [Cable(max_length, "coconuts-" + "{:02d}".format(i)) for i in range(0,times + 1)] + \
               [Cable(remainder, "coconuts-" + "{:02d}".format(times+1))]
