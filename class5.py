from human.Personal import *

class BussDriverCollection:
    def __init__(self):
        with open("busschaffis.txt", "r", encoding="utf-8") as f:

            obs = f.readlines()
            self.drivers = []

            for d in obs:
                first, last = d.split(" ")
                driver = Bussdriver(first, last)
                self.drivers.append(driver)
            f.close()

    def get_driver_by_id(self, id):
            return self.drivers[id]


class Report:
    def __init__(self):
        pass

    def report_on_site(self, driver1):
        report = input("-----Förare på plats-----\nVänligen ange [j/n]: ")
        if report == "ja" or report == "j":
            report = "På plats"
            Report.report_buss_condition(self, driver1, report)
        elif report == "n" or report == "nej":
            report = "Inte på plats"
            Report.report_buss_condition(self, driver1, report)
        else:
            print("Fel värde")

    # Rapporterar vilket skick bussen är i.
    def report_buss_condition(self, driver1, report):
        status = input("\n-----Bekräfta om bussen behöver något fixat-----""\n"
                       "1. Bussen är i bra skick.""\n"
                       "2. Behöver en mekaniker.""\n"
                       "3. Behöver en städare.""\n"
                       "\nAnge ett alternativ [1-3]: ")

        if status == "1":
            status = "Bussen är i bra skick."
            Buss().Traffic_addstuff(driver1, report, status)
        elif status == "2":
            status = "Bussen behöver en mekaniker."
            Buss().Traffic_addstuff(driver1, report, status)

        elif status == "3":
            status = "Bussen behöver en städare."
            Buss().Traffic_addstuff(driver1, report, status)
        else:
            print("Fel värde")

        # Rapporterar tidspåslag
    def report_accident(self, valdavg, allinfo, delayreport, valdlinje):
        rtype = input("Ange varför det är försenat: ")
        time = input("Ange hur länge förseningen är i minuter: ")
        newtime = valdavg.avg + " - " + valdavg.ank + "+ " + time
        reason = f"""Avgång: {newtime} min
Anledning till försening: {rtype}"""
        consumerdelay = [valdlinje, "Avgång:",newtime]
        delayreport.append(reason)
        Report().create(delayreport)
        Report().create_consumerdelay(consumerdelay)
        Menu().run()

    def create(self, delayreport):
        with open("ongoing_delays.txt", "a") as f:
            f.write("-----------------\n")
            for i in delayreport:
                f.write("{}\n".format(i))

    def create_condition(self, condition):
        with open("busscondition.txt", "a") as f:
            f.write("-----------------\n")
            for i in condition:
                f.write("{}\n".format(i))

    def create_ontime(self, ontime):
        with open("ontime.txt", "a") as f:
            f.write("-----------------\n")
            for i in ontime:
                f.write("{}\n".format(i))

    def create_consumerdelay(self, consumerdelay):
        with open("consumerdelay.txt", "a") as f:
            f.write("-----------------\n")
            for i in consumerdelay:
                f.write("{}\n".format(i))

                
class BussLinesCollection:
    def __init__(self):
        with open("busslinje.txt", "r", encoding="utf-8") as f:
            obs = f.readlines()

            self.linje = []
            for d in obs:
                self.linje.append(d)

    def get_bussline_by_id(self, id):
            return self.linje[id]


class Buss:
    def __init__(self):
        pass

    def samla_info(self, driver1, report, status, valdlinje, valdavg):
        allinfo = [driver1, report, status, valdlinje, valdavg]
        delayreport = [valdlinje]
        condition = [valdlinje, "Avgång: ", valdavg, "Rapport: ", status]
        Report().create_condition(condition)
        ontime = [valdlinje, "Avgång: ", valdavg, "Förare: ", driver1, "Rapport: ", report]
        Report().create_ontime(ontime)
        TrafficMenu().run(valdavg, allinfo, delayreport, valdlinje)


    def Traffic_addstuff(self, driver1, report, status):
        print("****************************************************")
        print(f"""1.{BussLinesCollection().get_bussline_by_id(0)}""")
        print(f"""2.{BussLinesCollection().get_bussline_by_id(1)}""")
        print(f"""3.{BussLinesCollection().get_bussline_by_id(2)}""")
        linje = input("Ange linje [1-3]: ")

        if linje == "1":
            valdlinje = BussLinesCollection().get_bussline_by_id(0)
            print(f"""\nVälj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable1_spec(0)}""")
            print(f"""2.{Timetable().get_timetable1_spec(1)}""")
            print(f"""3.{Timetable().get_timetable1_spec(2)}""")
            print(f"""4.{Timetable().get_timetable1_spec(3)}""")
            print(f"""5.{Timetable().get_timetable1_spec(4)}""")
            print(f"""6.{Timetable().get_timetable1_spec(5)}""")
            timetable1 = input("\nAnge specifik avgång: ")
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
            print(f"""\nVälj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable2_spec(0)}""")
            print(f"""2.{Timetable().get_timetable2_spec(1)}""")
            print(f"""3.{Timetable().get_timetable2_spec(2)}""")
            print(f"""4.{Timetable().get_timetable2_spec(3)}""")
            print(f"""5.{Timetable().get_timetable2_spec(4)}""")
            print(f"""6.{Timetable().get_timetable2_spec(5)}""")
            timetable2 = input("\nVälj specifik avgång:")
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
            print(f"""\nVälj avgång för busslinjen:""")
            print("*********************************")
            print(f"""1.{Timetable().get_timetable3_spec(0)}""")
            print(f"""2.{Timetable().get_timetable3_spec(1)}""")
            print(f"""3.{Timetable().get_timetable3_spec(2)}""")
            print(f"""4.{Timetable().get_timetable3_spec(3)}""")
            print(f"""5.{Timetable().get_timetable3_spec(4)}""")
            print(f"""6.{Timetable().get_timetable3_spec(5)}""")
            timetable3 = input("\nVälj specifik avgång:")
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


class Get_time:
    def __init__(self, avg, ank):
        self.avg = avg
        self.ank = ank

    def __str__(self):
        return f"{self.avg}-{self.ank}"


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
4.Se pågående förseningar i trafiken
--------------------------------------
        """)

    def run(self):
        displayMenu = True
        while displayMenu:
            self.display_linjemenu()
            choice = input("Välj linje för att se tidtabell: \n"
                            "Välj 0 för att avsluta.")
            action = choice
            if action == "0":
                displayMenu = False
            if action == "1":
                print("""\nGöteborg Centralstationen - Uddevalla Kampenhof\n** ** ** ** ** ** ** ** ** ** ** **""")
                Timetable().get_timetable1()
                with open("ongoing_delays.txt","r") as f:
                    lines = f.readlines()
                    for i in lines:
                        print(i, end="")

            elif action == "2":
                print("""\nPartille Centrum - Nordstan\n** ** ** ** ** ** ** ** ** ** ** **""")
                Timetable().get_timetable2()

            elif action == "3":
                print("""\nKungsbacka Station - Göteborg Centralstation\n** ** ** ** ** ** ** ** ** ** ** **""")
                Timetable().get_timetable3()

            elif action == "4":
                TrafficMenu().send_consumerdelay()

            else:
                print("är inte ett alternativ".format(choice))


class TrafficMenu:
    def send_accident(self, valdavg, allinfo, delayreport):
        Report().report_accident(valdavg, allinfo, delayreport)

    def send_currentreport(self):
        with open("ongoing_delays.txt.", "r") as f:
            lines = f.readlines()
            for i in lines:
                print(i, end="")

    def send_condition(self):
        with open("busscondition.txt.", "r") as f:
            lines = f.readlines()
            for i in lines:
                print(i, end="")

    def send_ontime(self):
        with open("ontime.txt.", "r") as f:
            lines = f.readlines()
            for i in lines:
                print(i, end="")

    def send_consumerdelay(self):
        with open("consumerdelay.txt", "r") as f:
            lines = f.readlines()
            for i in lines:
                print(i, end="")

    def display_traffic(self):
        print(f"""
--------------Trafikcentral--------------
1. Rapportera försening.
2. Se pågående förseningar.
3. Bussåtgärder.
4. Tidsrapportering.
5. Avräknare för busschaufför
-----------------------------------------
""")


    def run(self, valdavg, allinfo, delayreport, valdlinje):
        passenger = []
        displayMenu = True
        while displayMenu:
            self.display_traffic()
            choice = input("Ange ett alternativ: \n"
                           "Välj 0 för att avsluta:")
            if choice == "0":
                Menu().run()
            elif choice == "1":
                if allinfo == None:
                    print("Du har inte valt linje, Välj linje.")
                else:
                    Report().report_accident(valdavg, allinfo, delayreport, valdlinje)
            elif choice == "2":
                TrafficMenu().send_currentreport()

            elif choice == "3":
                TrafficMenu().send_condition()

            elif choice == "4":
                TrafficMenu().send_ontime()

            elif choice == "5":
                count_passenger().add_passenger(passenger)
                newlist = 0
                for x in passenger:
                    newlist += x
                print("Antal resenärer som har åkt:", newlist)

            else:
                print("är inte ett alternativ".format(choice))


class count_passenger:
    def add_passenger(self, passenger):
        number = int(input("Rapportera hur många passagerare som åkt buss idag:"))
        passenger.append(number)
        return passenger

class Drivermenu:
    def __init__(self):
        self.choices = {
            "1": BussDriverCollection().get_driver_by_id(0),
            "2": BussDriverCollection().get_driver_by_id(1),
            "3": BussDriverCollection().get_driver_by_id(2),
            "4": BussDriverCollection().get_driver_by_id(3),
            "5": BussDriverCollection().get_driver_by_id(4),
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
        displaymenu = True
        while displaymenu:
            self.display_driver()
            choice = input("Ange ett alternativ: \n"
                           "Välj 0 för att avsluta:")
            action = self.choices.get(choice)
            if action:
                driver1 = action
                Report().report_on_site(driver1)
            elif choice == "0":
                displaymenu = False
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
            choice = input("Ange ett alternativ [1-2] \n")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} är inte ett giltigt val".format(choice))

    def company(self):
        password = input("Vänligen skriv in lösenordet: ")
        if password == "dog":
            companyMenu().run()
        else:
            print("Fel lösenord")

    def consumer(self):
        Linjemenu().run()


class companyMenu:
    def __init__(self):
        self.choices = {
            "1": self.busschaffisar,
            "2": self.trafikgenvag,
        }

    def display_menu(self):
        print("""
--------------Företagsmeny--------------
1.Bussförare
2.Trafikledning
-------------------------------------
""")

    def run(self):
        displaymenu = True
        while displaymenu:
            self.display_menu()
            choice = input("Ange ett alternativ [1-2] \n"
                           "Välj 0 för Startmenyn:")
            action = self.choices.get(choice)
            if action:
                action()

            elif choice == "0":
                displaymenu = False
            else:
                print(f"""{choice} är inte ett giltigt""")

    def busschaffisar(self):
        Drivermenu().run()

    def trafikgenvag(self):

        TrafficMenu().run(valdavg=None,allinfo=None,delayreport=None, valdlinje=None)


def main():
    Menu().run()


if __name__ == "__main__":
    main()