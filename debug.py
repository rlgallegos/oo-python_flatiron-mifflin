from lib.employee import *
from lib.manager import *

# Test your code here

# e.g.
m1 = Manager( 'Mr. Levi', 'HR', 33 )
m2 = Manager( 'Mr. Strauss', 'Sales', 19 )
m3 = Manager( 'Mr. Nike', 'Sales', 63 )
m4 = Manager( 'Mr. Adidas', 'Janitorial', 43 )

e1 = Employee( 'Norris', 50000, m1 )

m2.hire_employee("Sarah", 51000)
m3.hire_employee("Betty", 49500)
m2.hire_employee("Sam", 6000)
m4.hire_employee("Frank", 45000)
m1.hire_employee("Karen", 89000)

paid_list = Employee.paid_over(50000)

the_manager = Employee.find_by_department("Janitorial")

the_list = e1.tax_bracket()

avg = Manager.average_age()



# do not remove
import ipdb; ipdb.set_trace()
