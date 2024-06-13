class Weather():
    '''
    The Weather class takes a string for the description
    and a floating point number or integer for the temperature
    '''
    def __init__(self, city, desc, temp):
        self.city = city
        self.desc = desc
        self.temp = temp
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new_city):
        if type(new_city) == str and len(new_city)>2:
            self.__city = new_city
        else:
            self.__city = 'Athlone'
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, new_desc):
        if type(new_desc) == str:
            self.__desc = new_desc
        else:
            self.__desc = '' # default to an empty string
    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self, new_temp):
        if type(new_temp) in (int, float):
            self.__temp = new_temp
        else:
            self.__temp = 12 # a reasonable default
    def showWeatherReport(self):
        # output a nicely formatted weather report
        report  = f'The weather in {self.city} is {self.desc} at {self.temp}C'
        return report

def writeWeatherFile(report):
    '''commit the report string to a text file'''
    with(open ('weather_reports.txt', 'at')) as fout:
        fout.write(f'{report.showWeatherReport()}\n')

def readWeatherFile():
    '''retrieve all the reports from a text file'''
    with(open ('weather_reports.txt', 'rt')) as fin:
        reports = fin.read()
    return reports

if __name__ == '__main__':
    # exercise this module
    w_dub = Weather('Dublin', 'rainy', 19.04)
    w_gal = Weather('Galway', 'windy', 16.70)
    w_lk  = Weather('Letterkenny', 'sunny', 27.98)
   
    print(w_dub.showWeatherReport())
    print(w_gal.showWeatherReport())
    print(w_lk.showWeatherReport())

    w_default = Weather(False, [], ()) # wrong data types so should fall back to the defaults
    print(w_default.showWeatherReport())

    # commit the reports to a text file
    writeWeatherFile(w_dub)
    writeWeatherFile(w_gal)
    writeWeatherFile(w_lk)
    writeWeatherFile(w_default)
    # retrieve and print the weather reports
    print( readWeatherFile() )
