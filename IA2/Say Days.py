#SayDays.py

class SaysDays:
    def _init_(self, year: int, month: int, day:int):
        self.year = year
        self.month = month
        self.day = day
        
    def is_leap(self)-> bool:
        y = self.year
        return(
            (y % 4==0  and y % 100!=0) or
            (y % 400 == 0)
            )
    
    def days (self)->int:
        days_in_month =[
            31, 29 if self.is_leap() else 28 , 31, 30,
            31, 30, 31, 31,
            30, 31, 30, 31
            ]
        total = 0
        m= 0
        while m< self.month -1:
            total += days_in_month[m]
            m += 1
            
        total += self.day
        return total
    
        
    def days_left(self)->int:
        
        total_days = 366 if self.is_leap() else 365
        return total_days - self.days()
    
        
    def weekday(self)->int:
        
        y = self.year
        m = self.month
        d = self.day
        
        if m < 3:
            m+=12
            y-=1
            
        k = y % 100
        j = y // 100
        
        h = (d+(13*(m+1))//
             5+k+k//4+j//4+5*j)%7
        
        return h
        
    def weekday_name(self)->str:
        names = [
            "Saturday", "Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday"]
        return names[self.weekday()]
    
#runit
while True:
    year =  int(input("what year is it?"))
    month = int(input("What month is it?"))
    day = int(input("What day is it?"))
    
    date =  SayDays(year, month,  day)
    
    print("Days after January1: ", date.days())
    print("Days until Dec31:    ", date.days_left())
    print("Nuemric day of the week", date.weekdays())
    print("English day of the week", date.weekday_name())