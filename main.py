from suppliers.avtonova import Avtonova
from suppliers.intercars import InterCars
from suppliers.kiaparts import KiaParts
from suppliers.master_service import MasterService
from suppliers.vladislav import Vladislav
from suppliers.vesna import Vesna
from suppliers.uniks import Uniks
from suppliers.fords import Fords
from suppliers.tehnomir import Tehnomir
from suppliers.centr_gaz import CentrGaz
from suppliers.elit import Elit
from suppliers.scars import Scar
from suppliers.omega import Omega
from suppliers.solly_plus import SollyPlus
from suppliers.max_parts import MaxParts
from suppliers.zenit import Zenit
from suppliers.elit_oem import ElitOem
from suppliers.busmarket import BusMarket
from suppliers.bastion import Bastion
from suppliers.avtotechnics import AvtoTechnics
from suppliers.avdtrade import AvdTrade
from suppliers.brovacars import BrovaCar
from multiprocessing import Process
import time

def runInParallel(*fns):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


if __name__ == '__main__':
    time1 = time.time()
    runInParallel(Avtonova().run,InterCars().run,KiaParts().run,Vladislav().run,MasterService().run,Vesna().run,
                  Uniks().run,Fords().run,Tehnomir().run,CentrGaz().run,Elit().run,Scar().run,Omega().run,SollyPlus().run,
                  MaxParts().run,Zenit().run,ElitOem().run,BusMarket().run,Bastion().run,AvtoTechnics().run,AvdTrade().run,BrovaCar().run)
    print(time.time() - time1)


