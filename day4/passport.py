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
        self.birthYear = year
    
    def setIssueYear(self, year):
        self.issueYear = year
    
    def setExpirationYear(self, year):
        self.expirationYear = year

    def setHeight(self, height):
        self.height = height

    def setHairColour(self, colour):
        self.hairColour = colour

    def setEyeColour(self, colour):
        self.eyeColour = colour

    def setId(self, id):
        self.id = id

    def setCountryId(self, countryId):
        self.countryId = countryId