import datetime
import calendar

class Solution:
    def run(self, birthday_date):
        self.future_dates = []
        dd, mm = (int(x) for x in birthday_date.split('-'))
        yy = 2016
        for i in range(50):
            b_date = datetime.date(yy, mm, dd)
            b_day = calendar.day_abbr[b_date.weekday()]

            if b_day == 'Fri':
                self.future_dates.append(f"{b_day}-{yy} ")
            elif b_day == 'Sat':
                self.future_dates.append(f"{b_day}-{yy} ")
            elif b_day == 'Sun':
                self.future_dates.append(f"{b_day}-{yy} ")
            
            yy += 1
        
        return self.list_to_string(self.future_dates)
    
    def list_to_string(self, a):
        """ Convert a list into a string """

        res = ''.join(a)

        return res

def main():
    test = Solution()
    ans = test.run("23-10")
    print(ans)

if __name__ == "__main__":
    main()