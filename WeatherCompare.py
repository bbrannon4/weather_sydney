import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

###############################################################################

def ReadEPW(file):
    data = pd.read_csv(file, skiprows=8, header=None)
    data.columns = ['Year','Month','Day','Hour','Minute','Datasource',
                       'DryBulb {C}','DewPoint {C}','RelHum {%}',
                       'Atmos Pressure {Pa}',
                       'ExtHorzRad {Wh/m2}','ExtDirRad {Wh/m2}','HorzIRSky {Wh/m2}',
                       'GloHorzRad {Wh/m2}','DirNormRad {Wh/m2}','DifHorzRad {Wh/m2}',
                       'GloHorzIllum {lux}','DirNormIllum {lux}','DifHorzIllum {lux}',
                       'ZenLum {Cd/m2}',
                       'WindDir {deg}','WindSpd {m/s}',
                       'TotSkyCvr {.1}','OpaqSkyCvr {.1}',
                       'Visibility {km}','Ceiling Hgt {m}',
                       'PresWeathObs','PresWeathCodes',
                       'Precip Wtr {mm}','Aerosol Opt Depth {.001}',
                       'SnowDepth {cm}','Days Last Snow','Albedo {.01}',
                       'Rain {mm}','Rain Quantity {hr}']
    data['Year_Real'] = data['Year']
    data['Year'] = 2000
    data['datetime'] = pd.to_datetime(data[['Year','Month','Day','Hour']])
    data.set_index(pd.DatetimeIndex(data['datetime']), inplace=True, drop=True)

    return data

def ReadBOMStat(file):
    data = pd.read_csv(file, skiprows=0, header=0)
    data['datetime'] = pd.to_datetime(data[['Year','Month','Day']])
    data.set_index(pd.DatetimeIndex(data['datetime']), inplace=True, drop=True)
    
    return data

###############################################################################

data_RMY = ReadEPW(r'AUS_NSW.Sydney.947680_RMY.epw')
data_IWEC = ReadEPW(r'AUS_NSW.Sydney.947670_IWEC.epw')

data_BOMMin = ReadBOMStat(r'IDCJAC0011_066062_1800_Data.csv')
data_BOMMax = ReadBOMStat(r'IDCJAC0010_066062_1800_Data.csv')
BOMYears = data_BOMMin['Year'].drop_duplicates()
BOMData = pd.DataFrame(columns=BOMYears)
BOMDates = pd.to_datetime(data_BOMMin[['Year','Month','Day']])
BOMDates = BOMDates.apply(lambda dt: dt.replace(year=2000)).drop_duplicates()
BOMData['datetime'] = BOMDates
BOMData.set_index(BOMData['datetime'], inplace=True, drop=True)



hotdays = []
for year in BOMYears:
    
    
###############################################################################

data_RMY['DryBulb {C}'].plot()
data_IWEC['DryBulb {C}'].plot()

data_BOMMin['Minimum temperature (Degree C)'].plot(legend=True)
data_BOMMax['Maximum temperature (Degree C)'].plot(legend=True)