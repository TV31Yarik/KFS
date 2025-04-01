import json
import os

nakrytka_day = 100
nakrytka_night = 80
tarif_day = 4.32
tarif_night = 1.73
JSON_FILE = "counters_data.json"  

class energy_counter:
    def __init__(self, number, date, day_inf, night_inf):
        self.number = number
        self.date = date
        self.day_inf = day_inf
        self.night_inf = night_inf
        self.old_day = 0
        self.old_night = 0
    
    def change_inf(self, new_date, new_day_inf, new_night_inf):
        if self.date == new_date:
            print(f"Дані для лічильника {self.number} на {new_date} вже оновлено.")
            return
        else:
            self.date = new_date
            self.old_day = self.day_inf
            self.old_night = self.night_inf
            self.day_inf = new_day_inf
            self.night_inf = new_night_inf
            if new_day_inf < self.old_day:
                self.day_inf += nakrytka_day
            if new_night_inf < self.old_night:
                self.night_inf += nakrytka_night
    
    def calculate_bill(self, tarif_day, tarif_night):
        day_usage = abs(self.day_inf - self.old_day)
        night_usage = abs(self.night_inf - self.old_night)
        bill = (day_usage * tarif_day) + (night_usage * tarif_night)
        return bill
    
    def to_dict(self):  
        return {
            'number': self.number,
            'date': self.date,
            'day_inf': self.day_inf,
            'night_inf': self.night_inf,
            'old_day': self.old_day,
            'old_night': self.old_night
        }

class DETEK:
    def __init__(self):
        self.counters = []
        #self.load_from_json()  
    
    def add_or_update_counter(self, number, date, day_inf, night_inf):
        for counter in self.counters:
            if counter.number == number:
                counter.change_inf(date, day_inf, night_inf)
                print(f"Лічильник {number} оновлений.")
                self.save_to_json()  
                return
        new_counter = energy_counter(number, date, day_inf, night_inf)
        self.counters.append(new_counter)
        print(f"Лічильник {number} доданий.")
        self.save_to_json() 
    
    def calculate_all_bills(self, tarif_day, tarif_night):
        total_bill = 0
        print("\nВсі лічильники:")
        for counter in self.counters:
            bill = counter.calculate_bill(tarif_day, tarif_night)
            total_bill += bill
            print(f"Лічильник {counter.number} | Дата: {counter.date}")
            print(f"  Попередні: День {counter.old_day}, Ніч {counter.old_night}")
            print(f"  Поточні: День {counter.day_inf}, Ніч {counter.night_inf}")
            print(f"  Рахунок: {bill:.2f} грн.\n")
        print(f"Загальний рахунок: {total_bill:.2f} грн.")
    
    def save_to_json(self):  
        data = [counter.to_dict() for counter in self.counters]
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    def load_from_json(self):  
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.counters = []
                for item in data:
                    counter = energy_counter(
                        item['number'], 
                        item['date'], 
                        item['day_inf'], 
                        item['night_inf']
                    )
                    counter.old_day = item['old_day']
                    counter.old_night = item['old_night']
                    self.counters.append(counter)
            print("Дані завантажено з файлу.")


manager = DETEK()

manager.add_or_update_counter(1, "2025-05-30", 500, 300)
manager.add_or_update_counter(2, "2025-05-30", 600, 350)
#manager.add_or_update_counter(1, "2025-03-31", 550, 320)

manager.calculate_all_bills(tarif_day, tarif_night)