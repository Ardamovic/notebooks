from ROOT import TGraph
from array import array
from timestamp import unix_time
from timestamp import date_time

class EnvironmentSensor:
    __observables = ("time","temperature","humidity","pressure") # attribute of the class
    
    # constructor
    def __init__(self, filename):    # filename is a parameter passed to the constructor
        self.__filename = filename   # self.__filename is an instance variable
        self.__data = []             # self.__data is an attribute of the instance
        self.__readData()            # methods of the class can be called from the constructor
    
    # methods
    @property                        # decorator that allows to use the method as if it were an attribute
    def data(self):
        return self.__data
    
    @property
    def filename(self):
        return self.__filename
    
    @property
    def observables(self):
        return EnvironmentSensor.__observables
    
    def __readData(self):# private method, cannot be used outside the class
        doc = open(self.__filename, 'r')
        data = doc.read().splitlines()
        
        for line in data:
            column = line.split()
    
            time = unix_time(column[0], column[1])
    
            temperature = float(column[2])
            humidity = float(column[3])
            pressure = float(column[4])
            
            tup = (time,temperature,humidity,pressure)
            self.__data.append(tup)
            
            # return print(self.__data)
            
    def getPlot(self,xvar,yvar,Date1 = None,Time1 = None,Date2 = None,Time2 = None):
            if not xvar in self.observables or not yvar in self.observables:
                raise Exception('Check your parameters. Possible observables: {}'.format(self.observables))           
            self.__xvar = xvar
            self.__yvar = yvar

            x, y = array( 'd' ), array( 'd' )
            for data in self.__data:
                data_dict = dict(zip(self.observables,data))
                if not (Date1 and  Date2 and Time1 and Time2):
                    x.append(data_dict[self.__xvar])
                    y.append(data_dict[self.__yvar])
                else:
                    timestamp1 = unix_time(Date1, Time1)
                    timestamp2 = unix_time(Date2, Time2)
                    xmin = timestamp1
                    xmax = timestamp2
                    if data_dict["time"] >=xmin and data_dict["time"] <=xmax:
                        x.append(data_dict[self.__xvar])
                        y.append(data_dict[self.__yvar])
            n = len(x)
            gr = TGraph( n, x, y )
            gr.SetLineWidth(2)
            gr.SetMarkerColor(2)
            gr.SetMarkerStyle(10)
            gr.SetMarkerSize(0.8)
            gr.SetTitle(self.__yvar + " versus " + self.__xvar)
            gr.GetXaxis().SetTitle(self.__xvar)
            gr.GetYaxis().SetTitle(self.__yvar)
            gr.GetXaxis().SetTimeDisplay(1)
            gr.GetXaxis().SetTimeFormat("%Y/%m/%d %H:%M:%S %F1970-01-01 00:00:00");
            gr.GetXaxis().SetNdivisions(404)

            return gr 
 