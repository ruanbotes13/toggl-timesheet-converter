class TimesheetEntry:
    def __init__(self, project, description, billable, startDate, duration, tags) -> None:
        self.project = project
        self.description = description
        self.billable = billable
        self.startDate = startDate
        self.duration = duration
        self.tags = tags.strip()

        self.category = ""
        self.hours = 0
        self.minutes = 0
        self.sentiment = "Happy"
        self.location = ""

    def processProjectAndCategory(self, mappingsDict):
        projectLookup = mappingsDict[self.project]
        self.project = projectLookup.project
        self.category = projectLookup.category
        self.billable = projectLookup.billable

    def processTiming(self):
        timeParts = self.duration.split(':')
        self.hours = int(timeParts[0])
        self.minutes = int(timeParts[1])

    def processWorkLocation(self):
        if len(self.tags) == 0:
            self.location = "Home"
        else:
            if self.tags == "Entelect Office":
                self.location = "Entelect"
            else:
                self.location = "Client"
    
    def boolToString(self, booleanValue):
        if booleanValue == True:
            return "True"
        else:
            return "False"
    
    def valuesToArray(self):
        values = [
            self.startDate,
            self.project,
            self.category,
            self.hours,
            self.minutes,
            self.getYesNoFromBool(self.billable),
            self.description,
            "",
            self.sentiment,
            self.location
        ]

        return values

    def getYesNoFromBool(self, booleanValue):
        if (booleanValue == True):
            return "Yes"
        else:
            return "No"