from statistics import mean, pstdev

def avg(aLijst):
    average = mean(aLijst)
    return average

def std_dev(sLijst):
    st_dev = pstdev(sLijst)
    return st_dev

def rendement_toets(tLijst):
    n = len(tLijst)
    rToets = [i for i in tLijst if i >= 5.5]
    return len(rToets)/n*100

def pas_toetsresultaten_aan(fLijst, gr): # de f van fraude, de gr van gewenst rendement
    rfToets = 0 #aanname dat het rendement te laag is
    argument = (max(fLijst) < 10.0) and rfToets < gr
    while argument == True:
        print('adding one more')
        fLijst = [x+0.1 for x in fLijst]
        roundResult = [float('%.2f' % elem) for elem in fLijst]
        rfToets = rendement_toets(roundResult)
    return roundResult, rfToets        
    

toetsresultaten = [1.2, 3.6, 9.2, 8.2, 3.5, 5.5, 6.0, 7.4, 5.9, 6.0, 5.4, 5.2, 4.3, 7.4, 1.2, 1.0]
print(pas_toetsresultaten_aan(toetsresultaten, 70))