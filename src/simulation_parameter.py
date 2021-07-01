import pandas as pd



def get_simulation_parameter(nominal_energy, 
                             Cell_chemistry="NMC", 
                             timeresolution=60,
                             repetition =365,  
                             initial_SoC=1, SoC_max=1, SoC_min=0):
    
    parameter=pd.DataFrame()
    
    parameter.Cell_chemistry=Cell_chemistry
    parameter.timeresolution=timeresolution      #seconds per step
    parameter.repetition = repetition            #how many times the input is repeated
    parameter.fraction_size=10000
    parameter.initial_SoC=initial_SoC
    parameter.SoC_max=SoC_max
    parameter.SoC_min=SoC_min        
    parameter.initial_SoR=1
    parameter.initial_SoH=1
    parameter.nominal_energy=nominal_energy  #Wh
    parameter.lim_Mode=1             #select between one and two 
    parameter.cyc_count_alg=1 #1= Rainflow, 2=Peakt to Peak
          
 

    
    
    
    
    
    
    
    return parameter