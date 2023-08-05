from Menu import Pizza, Burger, Drinks, Menu
from restaurant import Restaurant
from user import chef, Customer, Server, Manager
from Order import Order

def main ():
    menu = Menu()
    Pizza_1 = Pizza('Shutki pizza', 600, 'large', ['oil', 'shutki'])
    menu.add_menu_item('pizza', Pizza_1)
    pizza_2 = Pizza('Alur Vorta pizza', 400, 'large', ['potato', 'onion'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Dal Pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)


    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)

    burger_2 = Burger('Beef Burger', 1000, 'chicken', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)


    coke = Drinks('Coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Coffee', 30, False)
    menu.add_menu_item('drinks', coffee)

    menu.show_menu()

    restaurant = Restaurant('Sai Baba Restaurant', 1000, menu)

    manager = Manager('Kala Chan Manager', 5, 'kala@chan.com', 'kaliapur', 1500, 'Jan 1 2020', 'core')
    restaurant.add_employee('manager', manager)
    Chef = chef('Rustom Baburchi', 6, 'chupa@rustom.com', 'rustomNagar', 3500, 'Feb 1, 2020', 'Chef', 'everything')
    restaurant.add_employee('chef', Chef)
    server = Server('Chotu server', 6, 'nai@jai.com', 'restaurant', 200, 'March 1, 2020', 'server', 2000)
    restaurant.add_employee('server', server)

    restaurant.show_employees()

    customer_1 = Customer('sakib khan', 525, 'sakib@khan.com', '125 banani', 1000000)
    order_1 = Order(customer_1, [pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)
    restaurant.receive_payment(order_1, 1000, customer_1)

    print(restaurant.revenue, restaurant.balance)


    

if __name__ == '__main__':
    main()
