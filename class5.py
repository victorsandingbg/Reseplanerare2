from human.Personal import *


class BussDriverCollection:
    def __init__(self):
        with open("busschaffis.txt", "r") as f:

            obs = f.readlines()
            self.drivers = []

            for d in obs:
                first, last = d.split()
                driver = Bussdriver(first, last)
                self.drivers.append(driver)

    def get_driver_by_id(self, id):
            return self.drivers[id]


class Report:
    def __init__(self):
        pass

    def report_on_site(self, driver1):
        report = input("Bekräfta om förare är på plats.""\n""Inte i tid: tryck någon tangent: ")
        if report == "1":
            report = "på plats"
            print(driver1, "är på plats.""\n")
            Report.report_buss_condition(self, driver1, report)
        else:
            report = "inte på plats"
            print(driver1, ": Föraren är inte på plats""\n")
            Report.report_buss_condition(self, driver1, report)
        # Rapporterar vilket skick bussen är i.

    def report_buss_condition(self, driver1, report):
        status = input("Bekräfta om bussen behöver något fixat?""\n"
                       "1. Bussen är i perfekt skick.""\n"
                       "2. Behöver en mekaniker.""\n"
                       "3. Behöver en städare.""\n"
                       "Ange ett alternativ [1-3]: ")

        if status == "1":
            status = "Perfekt skick."
            print("Bussen är i perfekt skick.")
            Buss().Traffic_addstuff(driver1, report, status)
        elif status == "2":
            status = "Need a mechanic"
            Mechanic("Ringaren", "iNottredam").call_mechanic(driver1, report, status)
        elif status == "3":
            status = "Need a cleaner"
            Cleaner("Shitface", "Mctrotter").call_cleaner(driver1, report, status)
        else:
            print("fel värden")

        # Rapporterar tidspåslag
    def report_accident(self, valdavg):
        print(valdavg)
        rtype = input("Ange varför det är försenat: ")
        time = input("Ange hur länge förseningen är i minuter: ")
        newtime = valdavg.avg +" - " + valdavg.ank +" + " + time
        print(f"""Försenat pga {rtype}: Avångstid {newtime} min""")

class BussLinesCollection:
    def __init__(self):
        with open("busslinje.txt", "r") as f:
            obs = f.readlines()

            self.linje = []
            for d in obs:
                self.linje.append(d)

    def get_bussline_by_id(self, id):
            return self.linje[id]

        # läs in en linje från filen
        # skapa alla hållplatser för denna linje
        # för varje hållplats anropa add_stop för denna linje
        # När linjen är färdigskapad anropa add_line och skicka med denna linje
        # stäng filen när klar


class Buss:
    def __init__(self):
        self.valdavglist = []

    def samla_info(self, driver1, report, status, valdlinje, valdavg):
      #  allt_list = []
       # allt_list.append(valdavg.avg + valdavg.ank + driver1 + report + status + valdlinje)
        #print(alltlist)
        print(driver1, report, status, valdlinje, valdavg)
        TrafficMenu().run(valdavg)

    def Traffic_addstuff(self, driver1, report, status):
        print("****************************************************")
        print(f"""1.{BussLinesCollection().get_bussline_by_id(0)}""")
        print(f"""2.{BussLinesCollection().get_bussline_by_id(1)}""")
        print(f"""3.{BussLinesCollection().get_bussline_by_id(2)}""")
        linje = input("Välj en linje du vill åka.")

        if linje == "1":
            valdlinje = BussLinesCollection().get_bussline_by_id(0)
            print(f"""Välj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable1_spec(0)}""")
            print(f"""2.{Timetable().get_timetable1_spec(1)}""")
            print(f"""3.{Timetable().get_timetable1_spec(2)}""")
            print(f"""4.{Timetable().get_timetable1_spec(3)}""")
            print(f"""5.{Timetable().get_timetable1_spec(4)}""")
            print(f"""6.{Timetable().get_timetable1_spec(5)}""")
            timetable1 = input("Välj specifik avgång:")
            if timetable1 == "1":
                valdavg = Timetable().get_timetable1_spec(0)
                print(f"""{Timetable().get_timetable1_spec(0)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "2":
                valdavg = Timetable().get_timetable1_spec(1)
                print(f"""{Timetable().get_timetable1_spec(1)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "3":
                valdavg = Timetable().get_timetable1_spec(2)
                print(f"""{Timetable().get_timetable1_spec(2)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "4":
                valdavg = Timetable().get_timetable1_spec(3)
                print(f"""{Timetable().get_timetable1_spec(3)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "5":
                valdavg = Timetable().get_timetable1_spec(4)
                print(f"""{Timetable().get_timetable1_spec(4)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable1 == "6":
                valdavg = Timetable().get_timetable1_spec(5)
                print(f"""{Timetable().get_timetable1_spec(5)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            else:
                print("Tyvärr, vänligen försök igen.")

        elif linje == "2":
            valdlinje = BussLinesCollection().get_bussline_by_id(1)
            print(f"""Välj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable2_spec(0)}""")
            print(f"""2.{Timetable().get_timetable2_spec(1)}""")
            print(f"""3.{Timetable().get_timetable2_spec(2)}""")
            print(f"""4.{Timetable().get_timetable2_spec(3)}""")
            print(f"""5.{Timetable().get_timetable2_spec(4)}""")
            print(f"""6.{Timetable().get_timetable2_spec(5)}""")
            timetable2 = input("Välj specifik avgång:")
            if timetable2 == "1":
                valdavg = Timetable().get_timetable2_spec(0)
                print(f"""{Timetable().get_timetable2_spec(0)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "2":
                valdavg = Timetable().get_timetable2_spec(1)
                print(f"""{Timetable().get_timetable2_spec(1)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "3":
                valdavg = Timetable().get_timetable2_spec(2)
                print(f"""{Timetable().get_timetable2_spec(2)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "4":
                valdavg = Timetable().get_timetable2_spec(3)
                print(f"""{Timetable().get_timetable2_spec(3)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "5":
                valdavg = Timetable().get_timetable2_spec(4)
                print(f"""{Timetable().get_timetable2_spec(4)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable2 == "6":
                valdavg = Timetable().get_timetable2_spec(5)
                print(f"""{Timetable().get_timetable2_spec(5)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            else:
                print("Tyvärr, vänligen försök igen.")

        elif linje == "3":
            valdlinje = BussLinesCollection().get_bussline_by_id(2)
            print(f"""Välj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable3_spec(0)}""")
            print(f"""2.{Timetable().get_timetable3_spec(1)}""")
            print(f"""3.{Timetable().get_timetable3_spec(2)}""")
            print(f"""4.{Timetable().get_timetable3_spec(3)}""")
            print(f"""5.{Timetable().get_timetable3_spec(4)}""")
            print(f"""6.{Timetable().get_timetable3_spec(5)}""")
            timetable3 = input("Välj specifik avgång:")
            if timetable3 == "1":
                valdavg = Timetable().get_timetable3_spec(0)
                print(f"""{Timetable().get_timetable3_spec(0)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "2":
                valdavg = Timetable().get_timetable3_spec(1)
                print(f"""{Timetable().get_timetable3_spec(1)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "3":
                valdavg = Timetable().get_timetable3_spec(2)
                print(f"""{Timetable().get_timetable3_spec(2)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "4":
                valdavg = Timetable().get_timetable3_spec(3)
                print(f"""{Timetable().get_timetable3_spec(3)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "5":
                valdavg = Timetable().get_timetable3_spec(4)
                print(f"""{Timetable().get_timetable3_spec(4)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            elif timetable3 == "6":
                valdavg = Timetable().get_timetable3_spec(5)
                print(f"""{Timetable().get_timetable3_spec(5)}""")
                Buss().samla_info(driver1, report, status, valdlinje, valdavg)
            else:
                print("Tyvärr, vänligen försök igen.")
        else:
            print("Välj ett annat alternativ:")
        # Meny för själva linjerna till bussarna


class Linjemenu:
    def __init__(self):
        self.choices = {
            "1": BussLinesCollection().get_bussline_by_id(0),
            "2": BussLinesCollection().get_bussline_by_id(1),
            "3": BussLinesCollection().get_bussline_by_id(2),
        }

    def display_linjemenu(self):
        print(f"""
--------------Busslinjer--------------

1.{BussLinesCollection().get_bussline_by_id(0)}
2.{BussLinesCollection().get_bussline_by_id(1)}
3.{BussLinesCollection().get_bussline_by_id(2)}
--------------------------------------
        """)

    def run(self):
        while True:
            self.display_linjemenu()
            choice = input("Välj linje för att se tidtabell: ")
            action = choice
            if action == "1":
                print("""\nGöteborg Centralstationen - Uddevalla Kampenhof\n** ** ** ** ** ** ** ** ** ** ** **""")
                Timetable().get_timetable1()
            elif action == "2":
                print("""\nPartille Centrum - Nordstan\n** ** ** ** ** ** ** ** ** ** ** **""")
                Timetable().get_timetable2()

            elif action == "3":
                print("""\nKungsbacka Station - Göteborg Centralstation\n** ** ** ** ** ** ** ** ** ** ** **""")
                Timetable().get_timetable3()

            else:
                print("är inte ett alternativ".format(choice))


class TrafficMenu:
    def __init__(self):
        self.choices = {
            "1": self.send_accident,
            "2": self.send_idontknow,
            "3": self.send_cleaner,
                }

    def send_accident(self, valdavg):
        Report().report_accident(valdavg)


    def send_idontknow(self):
        # Report().show_late_arrivals()
        pass

    def send_cleaner(self):
        # Report().show_damage_buss()
        pass

    def display_traffic(self):
        print(f"""
Meny Trafikcentral
************************
1. Rapportera försening.
2. Se pågående förseningar.
3. Bussåtgärder.
""")

    def run(self, valdavg):
        while True:
            self.display_traffic()
            choice = input("Ange ett alternativ: ")
            action = self.choices.get(choice)
            if action:
                action(valdavg)
            else:
                print("är inte ett alternativ".format(choice))


class Drivermenu:
    def __init__(self):
        self.choices = {
            "1": BussDriverCollection().get_driver_by_id(0),
            "2": BussDriverCollection().get_driver_by_id(1),
            "3": BussDriverCollection().get_driver_by_id(2),
            "4": BussDriverCollection().get_driver_by_id(3),
            "5": BussDriverCollection().get_driver_by_id(4)
        }
    def display_driver(self):
        print(f"""
--------------Busschaffisar--------------
1.{BussDriverCollection().get_driver_by_id(0)}
2.{BussDriverCollection().get_driver_by_id(1)}
3.{BussDriverCollection().get_driver_by_id(2)}
4.{BussDriverCollection().get_driver_by_id(3)}
5.{BussDriverCollection().get_driver_by_id(4)}
------------------------------------------
""")

    def run(self):
        while True:
            self.display_driver()
            choice = input("Ange ett alternativ: ")
            action = self.choices.get(choice)
            if action:
                print(f"""Val av förare: {Bussdriver.printname(action)}""")
                driver1 = Bussdriver.printname(action)
                print(driver1)
                Report().report_on_site(driver1)
            else:
                print("är inte ett alternativ".format(choice))


class Menu:
    def __init__(self):
        self.choices = {
            "1": self.company,
            "2": self.consumer,
        }

    def display_menu(self):
        print("""
        --------------Huvudmeny--------------
        1.Företag
        2.Konsument
        -------------------------------------
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Ange ett alternativ [1-2]: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} är inte ett giltigt val".format(choice))

    def company(self):
        password = input("Vänligen skriv in lösenordet: ")
        if password == "dog":
            Drivermenu().run()
        else:
            print("Fel lösenord")

    def consumer(self):
        Linjemenu().run()


class Get_time:
    def __init__(self, avg, ank):
        self.avg = avg
        self.ank = ank

    def __str__(self):
        return f"{self.avg},{self.ank}"


class Timetable:
    def __init__(self):
        with open("tables_linje541.txt", "r") as f:

            obs = f.readlines()
            self.table1 = []

            for d in obs:
                avg, ank = d.split(";")
                string = Get_time(avg, ank)
                self.table1.append(string)

        with open("tables_linje121.txt", "r") as f:

            obs = f.readlines()
            self.table2 = []

            for d in obs:
                avg, ank = d.split(";")
                string = Get_time(avg, ank)
                self.table2.append(string)

        with open("tables_linje95.txt", "r") as f:

            obs = f.readlines()
            self.table3 = []

            for d in obs:
                avg, ank = d.split(";")
                string = Get_time(avg, ank)
                self.table3.append(string)

    def get_timetable1_spec(self, id):
        return self.table1[id]

    def get_timetable2_spec(self, id):
        return self.table2[id]

    def get_timetable3_spec(self, id):
        return self.table3[id]

    def get_timetable1(self):
        for all in self.table1:
            print(all)

    def get_timetable2(self):
        for all in self.table2:
            print(all)

    def get_timetable3(self):
        for all in self.table3:
            print(all)
            

def main():
    Menu().run()


if __name__ == "__main__":
    main()