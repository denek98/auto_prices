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
import tkinter as tk
from tkinter.ttk import Checkbutton


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
    runInParallel(
        Avtonova().run,
        AvdTrade().run,
        InterCars().run,
        KiaParts().run,
        Vladislav().run,
        MasterService().run,
        Vesna().run,
        Uniks().run,
        Fords().run,
        Tehnomir().run,
        CentrGaz().run,
        Elit().run,
        Scar().run,
        Omega().run,
        SollyPlus().run,
        MaxParts().run,
        Zenit().run,
        ElitOem().run,
        BusMarket().run,
        Bastion().run,
        AvtoTechnics().run,
        BrovaCar().run
    )
    print(time.time() - time1)

    # supplier_checkbox = {
    # 'Автонова': 0,
    # 'АвдТрейд':0,
    # 'ИнтерКарс':0,
    # 'КиаПартс': 0,
    # 'Владислав': 0,
    # 'МастерСервис': 0,
    # 'Весна': 0,
    # 'Юникс': 0,
    # 'Фордс': 0,
    # 'Техномир': 0,
    # 'ЦентрГаз': 0,
    # 'Елит': 0,
    # 'Скар': 0,
    # 'Омега': 0,
    # 'СоллиПлюс': 0,
    # 'МаксПартс': 0,
    # 'Зенит': 0,
    # 'ЕлитОем': 0,
    # 'БасМаркет': 0,
    # 'Бастион': 0,
    # 'АвтоТехникс': 0,
    # 'БроваКар': 0,
    # }
    # window = tk.Tk()
    # window.title("Система обновления потавщиков")
    # window.geometry('800x500')
    # lbl = tk.Label(
    #     text="Выберите поставщиков которые хотите обновить",
    #     height=1,
    #     font=("Arial", 20)
    # )

    # chk_state = tk.BooleanVar()
    # for machine in supplier_checkbox:
    #     supplier_checkbox[machine] = Variable()
    #     l = Checkbutton(text=machine, variable=supplier_checkbox[machine])
    #     l.pack()
    # lbl.pack()
    # window.mainloop()

