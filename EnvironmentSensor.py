from ROOT import TCanvas, TGraph
from array import array

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
    
    def __readData(self):            # private method, cannot be used outside the class
        self.__data.append((1578672498,20.0,80.3,1000))
        self.__data.append((1578672598,21.1,81.0,1010))
        self.__data.append((1578672658,20.5,80.6,1005))
               
    def getPlot(self,xvar,yvar):
        if not xvar in self.observables or not yvar in self.observables:
            raise Exception('Check your parameters. Possible observables: {}'.format(self.observables))           
        self.__xvar = xvar
        self.__yvar = yvar
        
        x, y = array( 'd' ), array( 'd' )
        for reading in self.__data:
            data = dict(zip(self.observables,reading))
            x.append(data[self.__xvar])
            y.append(data[self.__yvar])
        
        n = len(x)
        gr = TGraph( n, x, y )
        gr.SetLineWidth(2)
        gr.SetMarkerColor(2)
        gr.SetMarkerStyle(10)
        gr.SetMarkerSize(0.8)
        gr.SetTitle(self.__yvar + " versus " + self.__xvar)
        gr.GetXaxis().SetTitle(self.__xvar)
        gr.GetYaxis().SetTitle(self.__yvar)
        
        return gr
