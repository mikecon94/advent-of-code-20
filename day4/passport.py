import re

class Passport:
    
    issueYear = None
    expirationYear = None
    height = None
    hairColour = None
    eyeColour = None
    id = None
    birthYear = None
    countryId = None

    def __init__(self):
        pass

    def isSchemaValid(self):
        valid = True
        if self.birthYear < 1920 or self.birthYear > 2002:
            valid = False
        if self.issueYear < 2010 or self.issueYear > 2020:
            valid = False
        if self.expirationYear < 2020 or self.expirationYear > 2030:
            valid = False
        if not self.heightValid():
            valid = False
        if not self.hairColourValid():
            valid = False
        if not self.eyeColourValid():
            valid = False
        if not self.idValid():
            valid = False
        return valid

    def idValid(self):
        pattern = re.compile("^[0-9]{9}$")
        return pattern.match(self.id)

    def eyeColourValid(self):
        validColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if self.eyeColour in validColours:
            return True
        else:
            return False

    def hairColourValid(self):
        pattern = re.compile("#[0-9a-f]{6}")
        return pattern.match(self.hairColour)

    def heightValid(self):
        valid = True
        if self.height.endswith("cm"):
            heightNum = int(self.height[:-2])
            if heightNum < 150 or heightNum > 193:
                valid = False
        elif self.height.endswith("in"):
            heightNum = int(self.height[:-2])
            if heightNum < 59 or heightNum > 76:
                valid = False
        else:
            valid = False
        return valid

    def isValid(self):
        valid = True
        if self.birthYear == None:
            valid = False
        if self.issueYear == None:
            valid = False
        if self.expirationYear == None:
            valid = False
        if self.height == None:
            valid = False
        if self.hairColour == None:
            valid = False
        if self.eyeColour == None:
            valid = False
        if self.id == None:
            valid = False
        #if self.countryId == None:
        #    valid = False
        return valid

    def setProperty(self, key, value):
        if key == 'byr':
            self.setBirthYear(value)
        elif key == 'iyr':
            self.setIssueYear(value)
        elif key == 'eyr':
            self.setExpirationYear(value)
        elif key == 'hgt':
            self.setHeight(value)
        elif key == 'hcl':
            self.setHairColour(value)
        elif key == 'ecl':
            self.setEyeColour(value)
        elif key == 'pid':
            self.setId(value)
        elif key == 'cid':
            self.setCountryId(value)

    def setBirthYear(self, year):
        self.birthYear = int(year)
    
    def setIssueYear(self, year):
        self.issueYear = int(year)
    
    def setExpirationYear(self, year):
        self.expirationYear = int(year)

    def setHeight(self, height):
        self.height = height

    def setHairColour(self, colour):
        self.hairColour = colour

    def setEyeColour(self, colour):
        self.eyeColour = colour

    def setId(self, id):
        self.id = id

    def setCountryId(self, cid):
        self.countryId = cid