# 1_oop exercises <https://github.com/betacord/ZPO/blob/main/1_oop.ipynb>

"1. Przygotować klasę Employee, która będzie przechowywać atrybuty: first_name, last_name i salary. Dodać metodę get_full_name(), zwracającą pełne imię i nazwisko. Następnie utworzyć klasę Manager, dziedziczącą po Employee, dodającą department oraz metodę get_department_info(), zwracającą informację o zarządzanym dziale.",\
"2.  Utworzyć klasę Transaction jako namedtuple zawierającą transaction_id, amount oraz currency. Następnie zdefiniować klasę BankAccount, która będzie miała atrybut balance oraz metodę apply_transaction(), przyjmującą obiekt Transaction i modyfikującą saldo.",\
"3. Napisać klasę Book używając dataclass, która zawiera title, author, year, price. Dodaj metodę apply_discount(), która obniży cenę książki o podany procent.",\
"4. Stworzyć klasę Product jako dataclass zawierającą name, price, category, a następnie rozszerz ją o walidację ceny (powinna być większa od zera) oraz domyślną wartość category="General".",\
"5. Utworzyć klasę Car z atrybutami brand, model i year. Następnie dodać metodę is_classic(), która zwróci True, jeśli samochód ma ponad 25 lat.",\
"6. Stworzyć klasy ElectricVehicle oraz GasolineVehicle, które mają metodę fuel_type(), zwracającą odpowiednio "electric" i "gasoline". Następnie utworzyć klasę HybridCar, która dziedziczy po obu i nadpisuje metodę fuel_type(), aby zwracała "hybrid".",\
"7. Utworzyć klasę Person z metodą introduce(), zwracającą "I am a person". Następnie stworzyć klasy Worker i Student, które dziedziczą po Person i zmieniają tę metodę na "I am a worker" oraz "I am a student". Następnie utworzyć klasę WorkingStudent, która dziedziczy zarówno po Worker, jak i Student, i sprawdź, jak Python rozwiąże konflikt metod.",\
"8. Utworzyć klasy Animal i Pet. Klasa Animal powinna mieć metodę make_sound(), zwracającą "Some sound", a Pet powinna mieć metodę is_domestic(), zwracającą True. Następnie utworzyć klasę Dog, dziedziczącą po obu, i dostosować metody tak, aby pasowały do psa.",\
"9. Zaimplementować klasy FlyingVehicle i WaterVehicle, które mają metody move(), zwracające odpowiednio "I fly" oraz "I sail". Następnie stworzyć klasę AmphibiousVehicle, która łączy obie i pozwala na wybór trybu działania.",\
"10. Utworzyć klasę Robot z metodą operate(), zwracającą "Performing task", oraz AI z metodą think(), zwracającą "Processing data". Następnie utworzyć klasę Android, która dziedziczy po obu i dodaje własną metodę self_learn().",\
"11. Stworzyć klasę TemperatureConverter, która będzie zawierać metody statyczne celsius_to_fahrenheit() oraz fahrenheit_to_celsius().",
"12. Przygotować klasę IDGenerator z metodą klasową generate_id(), która automatycznie generuje unikalne identyfikatory dla obiektów. Każdy nowo utworzony obiekt powinien otrzymać kolejny numer ID.",\
"13. Utworzyć klasę Store z atrybutem klasowym total_customers oraz metodą add_customer(), zwiększającą wartość tego atrybutu. Dodać metodę klasową get_total_customers(), która zwróci liczbę klientów.",\
"14. Stworzyć klasę MathOperations zawierającą zarówno metody statyczne (add(), multiply()) jak i metody klasowe (identity_matrix(cls, size), tworzącą macierz jednostkową [size x size]).",\
"15. Utworzyć klasę GameCharacter, która ma atrybut klasowy default_health=100 oraz metodę restore_health(), ustawiającą zdrowie obiektu na wartość domyślną. Dodać metodę klasową set_default_health(cls, new_value), pozwalającą na zmianę domyślnego zdrowia dla wszystkich postaci.",\
"16. Stworzyć klasę abstrakcyjną Shape z metodą abstrakcyjną area(). Następnie utworzyć klasy Circle i Rectangle, implementujące metodę area().",\
"17. Zaimplementować klasę abstrakcyjną PaymentProcessor z metodami authorize_payment() i capture_payment(). Następnie utworzyć klasy CreditCardPayment i PayPalPayment, implementujące te metody na różne sposoby.",\
"18. Utworzyć klasę abstrakcyjną Vehicle z metodą max_speed(), a następnie stworzyć klasy Car i Bicycle, definiującą ich maksymalną prędkość.",\
"19. Przygotować klasę abstrakcyjną DatabaseConnection z metodami connect() i execute_query(). Utworzyć klasy MySQLConnection oraz PostgreSQLConnection, implementujące te metody na różne sposoby.",\
"20. Utworzyć klasę abstrakcyjną Instrument z metodą play(), a następnie zaimplementować klasy Piano i Guitar, które będą miały różne wersje tej metody."
