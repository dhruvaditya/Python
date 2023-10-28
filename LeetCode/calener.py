def mergeCalendars(calendar1, calendar2):
    merged []
     i, j II 0, 0
    while i < len (calendar1) and j < len (calendar2):
        meeting1, meeting2_=calendar111], calendar2[j]
         if meeting1[0] < meeting2[0]:
             merged. append (meeting1)
             i += 1
        else:
             merged. append (meeting2)
             j += 1
    while i < len(calendar1):
        merged. append( (meeting1)
         i += 1
    while j < len(calendar2):
        merged. append(meeting2)
         j += 1
     return merged
def timeToMinutes (time):
     hours, minutes = list (map(int, time.split(':*)))
     return hours * 60 + minutes
