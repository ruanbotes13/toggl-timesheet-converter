from timesheet.timsheet_entry import TimesheetEntry
import csv
import pandas as pd
import openpyxl

class Timesheet:

    timesheetEntry = []

    def __init__(self) -> None:
        pass

    def processTimesheet(self, filePath): 
        with open(filePath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.timesheetEntry.append(self.processRow(row))
                    line_count += 1

    def processRow(self, row) -> TimesheetEntry:
        timesheetEntry = TimesheetEntry(row[3], row[5], row[6], row[7], row[11], row[12])
        return timesheetEntry
    
    def processEntries(self, mappingsDict):
        mappingDict2 = mappingsDict
        for entry in self.timesheetEntry:
            entry.processProjectAndCategory(mappingDict2)
            entry.processTiming()
            entry.processWorkLocation()

    def createExcel(self, outputPath, outputFileName):
        columns = ['Date', 'Project','Category', 'Hours', 'Minutes', 'Billable', 'Description', 'Ticket Number', 'Sentiment', 'Worked From']
        index = []
        entries = []
        for entry in self.timesheetEntry:
            entryArray = entry.valuesToArray()
            entries.append(entryArray)
            index.append("")
        df = pd.DataFrame(entries,
                  index, columns)
        df.to_excel(outputPath + outputFileName, sheet_name='new_sheet_name', index=False)
