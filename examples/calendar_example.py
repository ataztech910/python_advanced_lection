import calendar

class CustomHTMLCal(calendar.HTMLCalendar):
    cssclasses = [style + " text-nowrap" for style in
                  calendar.HTMLCalendar.cssclasses]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"

calendarGenerated = CustomHTMLCal()

with open('calendar.html', 'w') as g:
    print(calendarGenerated.formatyear(2021, width=4), file=g)