from datetime import datetime


class RetirementCalculator:

    def yearsleft(self, currentage, retirementage):
        return retirementage - currentage

    def retirementyear(self, yearsLeft):
        return self.currentyear() + yearsLeft

    def currentyear(self):
        return datetime.now().year


if __name__ == "__main__":
    currentage = input("What is your current age? ")
    retirementage = input("At what age would you like to retire? ")
    retirementCalculator = RetirementCalculator()
    yearsleft = retirementCalculator.yearsleft(int(currentage), int(retirementage))
    print("You have " + str(yearsleft) + " years left until you can retire.")
    print("It's " + str(retirementCalculator.currentyear()) + ", so you can retire in " + str(
        retirementCalculator.retirementyear(yearsleft)))
