import streamlit as st
import base64
import mysql.connector
import pandas as pd

st.sidebar.header("configuration")
#tab1, tab2, tab3 = st.tabs(["About", "Contact_Us", "Help"])
choice=st.sidebar.selectbox("My Menu", ("Home", "Employee", "Admin"))
if (choice == "Home"):
    tab1, tab2, tab3 = st.tabs(["About", "Contact_Us", "Help"])
    @st.experimental_memo
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    #img=get_img_as_base64("image.jpg")

    page_bg_img =f"""
    <style>[data-testid="stAppViewContainer"]
    {{
    background-image: url("https://images.unsplash.com/photo-1510851896000-498520af2236?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8ZGFyayUyMG9mZmljZXxlbnwwfHwwfHx8MA%3D%3D&w=1000&q=80");
    background-size: 100%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
   }}
    [data-testid="stSidebar"]{{
    background-image:url("https://img.freepik.com/free-photo/desk-office_23-2148110207.jpg?w=2000");
    background-size:cover;
   }}
    </style>
    """


    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title(":blue[HUMAN RESOURCE MANAGEMENT SYSTEM!]")
                      #if st.button('Say hello'):
 
    st.header(":red[About]")
    container = st.container()
    container.write("What is human resource management?")
    container.write("Employee management is the process by which employers ensure workers perform their jobs to the best of their abilities so as to achieve business goals. It typically entails building and maintaining healthy relationships with employees, as well as monitoring their daily labor and measuring progress. In this way, employers can identify opportunities for improvement and recognize achievements.")
    st.image("https://www.adp.com/-/media/adp/resourcehub/rh2/images/insight/img/employee-mgmt-800px.jpg?rev=6f652eff6dc54eac8c47e0fb640d3c8b&hash=3F9E8450E5C987255EA81E3C1DB97EFE")
    st.write("What responsibilities does human resource management include?")
    st.write("""Helping employees reach their full potential requires managers and supervisors to fulfill several of the following key responsibilities:

    Acquire talent:
    Filling open positions with the right people can make employee management easier from the start.
    That’s why many hiring managers are diligent about writing detailed job descriptions, sourcing and
    interviewing qualified applicants, and running background checks.

    Manage performance:
    Employees tend to do their jobs better and are more engaged when they are given opportunities to
    learn new skills or grow with the organization. To this end, employers may provide training and
    upskilling programs, encourage attendance at conferences and trade shows, or permit employees to
    adjust their roles according to their strengths and interests.

    Support two-way communication:
    Managers who want to make their employees feel included generally have open door policies and
    share important information about the business with them. They also provide a forum for individuals
    to express their ideas, opinions and complaints. This feedback is then used to address any issues 
    that may be negatively affecting the workforce, improve processes and keep employees engaged.""")

    st.write("Why is an employee management system important?")
    st.write("""Employee management systems are important because a business’s workforce is its greatest
    asset. Yet, despite this intrinsic value, employee engagement is sometimes overlooked because HR
    professionals are either too busy with administrative work or lack the integrations necessary to 
    use their people data effectively. Technology can alleviate such burdens and afford employers more
    time to connect with workers and create strategic initiatives that will attract and retain talent.""")

    st.write("Benefits of an employee management system")
    st.write("""Employers rely on employee management systems to help them not only maintain day-to-day
    workflows, but also solve complex challenges and achieve long-term business objectives. Some more
    specific benefits include:

    Increased productivity:
    The automation and machine learning capabilities that are common with most employee management
    systems can help HR departments accomplish more with less effort,

    Richer employee experiences:
    Mobile self-service features, online training and upskilling programs and flexible pay options 
    are just a few of the ways technology can enrich the employee experience,

    Actionable insights:
    With predictive analytics and benchmark data at their disposal, employers may be able to make more 
    informed workforce decisions and improve their profitability,

    Secure information:
    To deter hackers and prevent security breaches, employee management systems typically use
    multi-factor authentication, data encryption and fraud detection,

    Compliance support:
    Some employee management system providers offer global and/or local regulatory monitoring services
    that can help decrease the risk of fines or penalties for inadvertent non-compliance.""")
    st.write("What are employee management services?")
    st.write("""When employers choose to outsource their responsibilities to a third party, it’s sometimes referred to as employee management services. This arrangement is often beneficial for small and midsized businesses who have limited HR
    departments, lack compliance expertise or want to offer employee benefits comparable to those commonly available at larger organizations. Reducing the amount of time and resources spent on employee management also affords business owners the ability to focus more attention on growing their operations.""")
         # Now insert some more in the container
            #container.write("This is inside too")

                  #st.header(":red[About]")
                     #st.sidebar.header("configuration")
                       #choice=st.sidebar.selectbox("My Menu", ("Home", "Employee", "Admin"))

elif (choice == 'Employee'):
   
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    #img=get_img_as_base64("image.jpg")

    page_bg_img1 =f"""
    <style>[data-testid="stAppViewContainer"]
    {{
    background-image: url("https://c0.wallpaperflare.com/preview/918/958/450/adult-blond-hair-blurred-background-businesspeople.jpg");
    background-size: cover;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
   }}
    [data-testid="stSidebar"]{{
    background-image:url("https://img.freepik.com/free-photo/desk-office_23-2148110207.jpg?w=2000");
    background-size:cover;
   }}
    </style>
    """
    
    st.markdown(page_bg_img1, unsafe_allow_html=True)

    if 'login' not in st.session_state:
        st.session_state['login'] = False
    id = st.text_input("Enter Employee ID")
    paswrd = st.text_input("Enter Password")
    btn = st.button("login")
    if btn:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345", database="employee")
        c = mydb.cursor()
        c.execute("select * from users")
        for r in c:
            if (r[0] == id and r[1] == paswrd):
                st.session_state['login'] = True
                break
        if (st.session_state['login'] == False):
            st.subheader("Incorrect ID or Password")
    if (st.session_state['login'] == True):
        st.subheader("Login Successful")
        choice2=st.selectbox("Features",("None","View Details","Track Leave Request","Payroll Information","Training and Development","Timesheet and Attendance"))
        if(choice2=="View Details"):
            user=st.text_input("Enter Your Id")
            mydb=mysql.connector.connect(host="localhost",user="root",password="Dipika@12345",database="employee")
            c=mydb.cursor()
            query="SELECT first_name, email, address FROM employee_table WHERE employee_id=%s"
            c.execute(query,(user,))
            result=c.fetchone()
            l=[]
            if result is not None:
                """st.header("Employee Information")
                st.write(f"first_name: {result[0]}")
                st.write(f"email: {result[1]}")
                st.write(f"address: {result[2]}")"""
                l.append(result)
                df=pd.DataFrame(data=l,columns=['first_name','email','address'])
                st.dataframe(df)
            else:
                print("Employee Not found")
        elif(choice2=="Payroll Information"):
            user=st.text_input("Enter Your Id")
            mydb=mysql.connector.connect(host="localhost",user="root",password="Dipika@12345",database="employee")
            c=mydb.cursor()
            query="SELECT payroll_info FROM employee_table WHERE employee_id=%s"
            c.execute(query,(user,))
            result=c.fetchone()
            if result is not None:
                st.header("Salary Information")
                st.write(f"Status: {result[0]}")
            else:
                print("Not paid yet")
        elif(choice2=="Track Leave Request"):
            user=st.text_input("Enter Your ID")
            mydb=mysql.connector.connect(host="localhost",user="root",password="Dipika@12345",database="employee")
            c=mydb.cursor()
            query="SELECT Leave_Request FROM employee.employee_table WHERE employee_id=%s"
            c.execute(query,(user,))
            result=c.fetchone()
            if result is not None:
                st.header("Leave Request")
                st.write(f"Status: {result[0]}")
            else:
                print("Not paid yet")
elif (choice == 'Admin'):
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    #img=get_img_as_base64("image.jpg")

    page_bg_img1 =f"""
    <style>[data-testid="stAppViewContainer"]
    {{
    background-image: url("https://img.freepik.com/premium-photo/boardroom-is-where-success-is-brought-into-focus-cropped-shot-group-business-colleagues-meeting-boardroom_590464-18809.jpg");
    background-size: 100%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
   }}
    [data-testid="stSidebar"]{{
    background-image:url("https://img.freepik.com/free-photo/desk-office_23-2148110207.jpg?w=2000");
    background-size:cover;
   }}
    </style>
    """
    
    st.markdown(page_bg_img1, unsafe_allow_html=True)
    if 'login' not in st.session_state:
        st.session_state['login'] = False
    admin_id = st.text_input("Enter Admin ID")
    admin_password = st.text_input("Enter Password")
    btn1 = st.button("login")
    btn2 = st.button("ADD NEW")
    if btn1:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345", database="employee")
        c = mydb.cursor()
        c.execute("select * from employee.admins")
        for r in c:
            if (r[0] == admin_id and r[1] == admin_password):
                st.session_state['login'] = True
                break
        if (st.session_state['login'] == False):
            st.subheader("Incorrect ID or Password")
    if (st.session_state['login'] == True):
        st.subheader("Login Successful")
        choice3 = st.selectbox("Features", ("Select",
                                            "Master Data", "Transactions", "HRD", "Training and Development", "Report",
                                            "Utility", "Help", "Quit"))
        if choice3 == "Master Data":
            choice4 = st.selectbox("Select",
                                   ("Select", "Check Employee Details", "Add Employee", "Update Employee Detaiils","Remove Employee",
                                    "Loan", "BankLoan",
                                    "SalaryAdvance", "Department", "PayMode"))
            if choice4 == "Check Employee Details":
                st.header("Check Employee Details")
                e1 = st.text_input("Enter Employee Id")
                mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                               database="employee")
                c = mydb.cursor()
                query = "SELECT first_name,last_name,dob, email, address,contact_no FROM employee_table WHERE employee_id=%s"
                c.execute(query, (e1,))
                result = c.fetchone()
                l1 = []
                if result is not None:
                    l1.append(result)
                    df = pd.DataFrame(data=l1,
                                      columns=['first_name', 'last_name', 'dob', 'email', 'address', 'contact_no'])
                    st.dataframe(df)
                    c.close()
                    mydb.close()
                else:
                    print("Employee Not found")
                    c.close()
                    mydb.close()
            elif choice4 == "Add Employee":
                st.title("ADD EMPLOYEE")
                employee_id = st.text_input("Create Employee ID")
                first_name = st.text_input("Enter First Name")
                last_name = st.text_input("Enter Last Name")
                dob = st.date_input("Enter your DOB")
                gender = st.text_input("Enter Your Gender")
                email = st.text_input("Enter Mail ID")
                address=st.text_input("Add Address")
                contact_no = st.text_input("Enter contact no")
                payroll_info = st.text_input("Enter empoyee's payroll information")
                department_id= st.text_input("ENter depatment id of employee")
                # Function to add data to the database
                def add_employee_to_database(employee_id, first_name, last_name, dob, gender, email,address, contact_no,
                                             payroll_info,department_id):
                    try:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                       database="employee")
                        c = mydb.cursor()
                        sql = "INSERT INTO employee_table (employee_id, first_name, last_name,dob,gender,email,address,contact_no,payroll_info,department_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
                        values = (employee_id, first_name, last_name, dob, gender, email,address, contact_no, payroll_info,department_id)
                        c.execute(sql, values)
                        mydb.commit()
                        st.subheader("Added new employee successfully!")
                    except mysql.connector.Error as err:
                        st.error(f"Error: {err}")
                    finally:
                        c.close()
                        mydb.close()


                btn = st.button("ADD EMP")
                # Check if the "ADD EMP" button is clicked
                if btn:
                    # Check if the required fields are not empty
                    if employee_id and first_name and last_name and dob and gender and email and address and contact_no and payroll_info and department_id:
                        # Call the function to add employee data to the database
                        add_employee_to_database(employee_id, first_name, last_name, dob, gender, email,address, contact_no,
                                                 payroll_info,department_id)
                    else:
                        st.warning("Please fill in all the required fields.")
                    # btnn=st.button("Add Employee")
            elif choice4=="Update Employee Detaiils":
                employee_id = st.text_input("ENTER Employee ID", key="employee_id")
                first_name = st.text_input("Enter First Name", key="first_name")
                last_name = st.text_input("Enter Last Name", key="last_name")
                dob = st.text_input("Enter your DOB", key="dob")
                gender = st.text_input("Enter Your Gender", key="gender")
                email = st.text_input("Enter Mail ID", key="email")
                contact_no = st.text_input("Enter contact no", key="contact_no")
                payroll_info = st.text_input("Enter empoyee's payroll information", key="payroll_info")
                btnn = st.button("Update")
                if btnn:
                    def update_data(employee_id, first_name, last_name, dob, gender, email, contact_no, payroll_info):
                        global c, mydb
                        try:
                            mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                           database="employee")
                            c = mydb.cursor()
                            sql = "UPDATE employee_table SET first_name=%s, last_name=%s,dob=%s,gender=%s,email=%s,contact_no=%s,payroll_info=%s WHERE employee_id=%s"
                            data1 = (employee_id, first_name, last_name, dob, gender, email, contact_no, payroll_info)
                            c.execute(sql, data1)
                            mydb.commit()

                            st.subheader("Update employee successfully!")
                        except mysql.connector.Error as err:
                            st.error(f"Error: {err}")
                        finally:

                            c.close()
                            mydb.close()
                             # Check if the required fields are not empty and the button is clicked
                    if btnn and employee_id and first_name and last_name and dob and gender and email and contact_no and payroll_info:
                                # Call the function to update employee data in the database
                        update_data(employee_id, first_name, last_name, dob, gender, email, contact_no,
                                            payroll_info)
            elif choice4=="Remove Employee":
                emp_id=st.text_input("Enter employee id")
                btn3=st.button("Delete")
                if btn3:
                    def delete_employee_data(employee_id):
                        global mydb, c
                        try:
                            mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                           database="employee")
                            c = mydb.cursor()
                            sql = "DELETE FROM employee.employee_table WHERE employee_id = %s"
                            c.execute(sql, (employee_id,))
                            mydb.commit()

                            st.subheader("Employee successfully deleted!")
                        except mysql.connector.Error as err:
                            st.error(f"Error: {err}")
                        finally:
                            c.close()
                            mydb.close()


                    if emp_id == " ":
                        print("Error, First select the member")
                    else:
                        delete_employee_data(emp_id)
            elif choice4 == "SalaryAdvance":
                emp_id = st.text_input("Enter Employee_id")
                payroll_info = st.number_input("Enter new salary: ")
                btn4 = st.button("Proceed")
                if btn4:
                    def update_salary(employee_id, payroll_info):
                        #global mydb, c
                        #global mydb, c
                        try:
                            mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                           database="employee")
                            c = mydb.cursor()

                            sql = "UPDATE employee.employee_table SET payroll_info = %s WHERE employee_id = %s"
                            data = (payroll_info, employee_id)

                            c.execute(sql, data)
                            mydb.commit()

                            print("Salary updated successfully!")
                        except mysql.connector.Error as err:
                            print(f"Error: {err}")
                        """finally:
                            c.close()
                            mydb.close()"""


                    if emp_id.strip() == "":
                        st.error("Error, First select the member")
                    else:
                        update_salary(emp_id, payroll_info)
                        st.success("Salary updated successfully!")
                    # update_salary(emp_id, new_salary)        

            elif choice4=="Department":
                  
                department_id = st.text_input("Enter Department ID: ")
                department_name = st.text_input("Enter Department Name: ")
                btn5=st.button("ADD")
                if btn5:

                    def add_into_department_table(department_id,department_name):
                        try:    
                            mydb = mysql.connector.connect(host="localhost",user="root",password="Dipika@12345",database="employee")

                             # Create a cursor to execute SQL queries
                            cursor = mydb.cursor()
                           
                          # Insert user input into the 'department' table
                            insert_query = "INSERT INTO employee.department_table (department_id, department_name) VALUES (%s, %s)"
                           
                            department_data = (department_id, department_name)

                            cursor.execute(insert_query, department_data)
                            mydb.commit()
                            print("Department added successfully!")
                        except mysql.connector.Error as err:
                            print(f"Error: {err}")
                        finally:
                            cursor.close()
                            mydb.close()
                    if btn5:
                        if department_id.strip() and department_name.strip():
                         # Call the function to add department data to the database
                            add_into_department_table(department_id, department_name)
                            st.success("Department added successfully!")
                        else:
                            st.warning("Please fill in all the required fields.")
            elif choice4=="PayMode":

                emp_id = st.text_input("Enter Employee_id")
                paymode = st.text_input("Enter PayMode: ")
                btn4 = st.button("Update")
                if btn4:
                    def update_PayMode(employee_id,PayMode ):
                        #global mydb, c
                        #global mydb, c
                        try:
                            mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                           database="employee")
                            c = mydb.cursor()

                            sql = "UPDATE employee.employee_table SET PayMode = %s WHERE employee_id = %s"
                            data = (PayMode, employee_id)

                            c.execute(sql, data)
                            mydb.commit()

                            print("PayMode updated successfully!")
                        except mysql.connector.Error as err:
                            print(f"Error: {err}")
                        """finally:
                            c.close()
                            mydb.close()"""


                    if emp_id.strip() == "":
                        st.error("Error, First select the member")
                    else:
                        update_PayMode(emp_id, paymode)
                        st.success("Payment mode updated successfully!")
                    # update_salary(emp_id, paymode)             
            elif choice4=="Loan":

                emp_id = st.text_input("Enter Employee_id")
                loan = st.text_input("Enter Loan: ")
                btn4 = st.button("Update")
                if btn4:
                    def update_Loan(employee_id,Loan ):
                        #global mydb, c
                        #global mydb, c
                        try:
                            mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                           database="employee")
                            c = mydb.cursor()

                            sql = "UPDATE employee.employee_table SET Loan = %s WHERE employee_id = %s"
                            data = (Loan, employee_id)

                            c.execute(sql, data)
                            mydb.commit()

                            print("Loan updated successfully!")
                        except mysql.connector.Error as err:
                            print(f"Error: {err}")
                        """finally:
                            c.close()
                            mydb.close()"""


                    if emp_id.strip() == "":
                        st.error("Error, First select the member")
                    else:
                        update_Loan(emp_id, loan)
                        st.success("Lone status updated successfully!")
            elif choice4=="BankLoan":
                emp_id = st.text_input("Enter Employee_id")
                bank_loan = st.text_input("Enter Loan detail: ")
                btn7 = st.button("Update")
                if btn7:
                    def update_Loan(employee_id,BankLoan ):
                        #global mydb, c
                        #global mydb, c
                        try:
                            mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                           database="employee")
                            c = mydb.cursor()

                            sql = "UPDATE employee.employee_table SET BankLoan = %s WHERE employee_id = %s"
                            data = (BankLoan, employee_id)

                            c.execute(sql, data)
                            mydb.commit()

                            print("BankLoan updated successfully!")
                        except mysql.connector.Error as err:
                            print(f"Error: {err}")
                        """finally:
                            c.close()
                            mydb.close()"""


                    if emp_id.strip() == "":
                        st.error("Error, First select the member")
                    else:
                        update_Loan(emp_id, bank_loan)
                        st.success("Bank_Loan status updated successfully!")                         
        elif choice3 == "Transactions":
            ch1 = st.selectbox("Select", ("Attendance", "Deductions", "Pay Calculation", "Bonus Calculation"))
            if ch1=="Attendance":
                attendanceid=st.text_input("Enter Employee's AttendanceID")
                attendance_status=st.text_input("Enter Employee's attendance Status")
                #emp_id = st.text_input("Enter Employee_id")
                btn7 = st.button("Update")
                if btn7:
                    def update_Attendance(Attendance_id,Attendance_status ):
                        #global mydb, c
                        #global mydb, c
                        try:
                            mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                           database="employee")
                            c = mydb.cursor()

                            sql = "UPDATE employee.attendance SET Attendance_id = %s ,Attendance_status = %s WHERE Attendance_id = %s"
                            data = (Attendance_id,Attendance_status)

                            c.execute(sql, data)
                            mydb.commit()

                            print("Attendance updated successfully!")
                        except mysql.connector.Error as err:
                            print(f"Error: {err}")
                        """finally:
                              c.close()
                            mydb.close()"""
                    if attendanceid.strip() == "":
                        st.error("Error, First select the member")
                    else:
                        update_Attendance( attendanceid,attendance_status)
                        st.success("Attendance status updated successfully!")        
        elif choice3 == "HRD":
            ch2 = st.selectbox("Select", (
                "Employee Dependent", "Training", "Promotion/Increment", "Reports", "Attendance Analysis"))
            if ch2=="Employee Dependent":
                emp_id = st.text_input("Enter Employee_id")
                e_dependent = st.text_input("Enter Employee_Dependent Name ")
                btn4 = st.button("Update")
                if btn4:
                    def update_Loan(employee_id,Employee_Dependent ):
                        #global mydb, c
                        #global mydb, c
                        try:
                            mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                           database="employee")
                            c = mydb.cursor()

                            sql = "UPDATE employee.employee_table SET Employee_Dependent = %s WHERE employee_id = %s"
                            data = (Employee_Dependent, employee_id)

                            c.execute(sql, data)
                            mydb.commit()

                            print("Employee Dependent updated successfully!")
                        except mysql.connector.Error as err:
                            print(f"Error: {err}")
                        """finally:
                            c.close()
                            mydb.close()"""


                    if emp_id.strip() == "":
                        st.error("Error, First select the member")
                    else:
                        update_Loan(emp_id, e_dependent)
                        st.success("Employee_Dependent updated successfully!")
        elif choice3 == "Training and Development":
            ch3 = st.selectbox("Select", (
                "Training Programs", "Employee Training Records", "Training Evaluation", "Training Resources",
                "Training Budget", "Training Reports", "Certification Tracking"))
            if ch3=="Training Programs":
                training_id = st.text_input("Enter training_id")
                training_name = st.text_input("Enter Employee_Training Name ")
                btn8 = st.button("Update")
                if btn8:
                    def update_Training(Training_id,Training_name ):
                        #global mydb, c
                        #global mydb, c
                        try:
                            mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                           database="employee")
                            c = mydb.cursor()

                            sql = "UPDATE employee.training_programs SET Training_name = %s WHERE Training_id = %s"
                            data = (Training_id, Training_name)

                            c.execute(sql, data)
                            mydb.commit()

                            print("Employee training updated successfully!")
                        except mysql.connector.Error as err:
                            print(f"Error: {err}")
                        """finally:
                            c.close()
                            mydb.close()"""


                    if training_id.strip() == "":
                        st.error("Error, First select the member")
                    else:
                        update_Training(training_id, training_name)
                        st.success("Employe Training Program updated successfully!")
        elif choice3 == "Report":
            ch4 = st.selectbox("Select", (
                 "PaySlip", "Control Statement", "Loan Statement", "PF Statement", "Deduction", "Undeductions",
                "Bank Statements", "Goverment PF", "Prof Tax Analysis", "Total Advance", "Fest advance",
                "Attendance Statement", "Costing Statement", "QT Statement", "Bonus"))
            if ch4=="PaySlip":
                st.title("ADD EMPLOYEE in PAYSLIP")
                payslip_id = st.text_input("Create payslip ID")
                emp_name = st.text_input("Enter employee Name")
                Month_year = st.date_input("Enter Month and year")
                basic_salary = st.text_input("Enter basic_salary")
                allowances = st.text_input("Enter Allowances")
                Deductions=st.text_input("Add deductions")
                gross_salary = st.text_input("Enter gross salary information")
                net_salary = st.text_input("Enter empoyee's net salary information")
                payment_date= st.text_input("ENter payment date of employee")
                tax_info=st.text_input("Enter Tax information")
                # Function to add data to the database
                def add_employee_to_database(Payslip_id,Emp_name,Month_and_Year,basic_salary,Allowances,Deductions,Gross_Salary,Net_salary,payment_date,Tax_info):
                    try:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="Dipika@12345",
                                                       database="employee")
                        c = mydb.cursor()
                        sql = "INSERT INTO employee.payslip (Payslip_id,Emp_name,Month_and_Year,basic_salary,Allowances,Deductions,Gross_Salary,Net_salary,payment_date,Tax_info) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
                        values = (Payslip_id,Emp_name,Month_and_Year,basic_salary,Allowances,Deductions,Gross_Salary,Net_salary,payment_date,Tax_info)
                        mydb.commit()
                        st.subheader("Added into payslip successfully!")
                    except mysql.connector.Error as err:
                        st.error(f"Error: {err}")
                    finally:
                        c.close()
                        mydb.close()


                btn = st.button("ADD Payslip")
                # Check if the "ADD EMP" button is clicked
                if btn:
                    # Check if the required fields are not empty
                    if Payslip_id and Emp_name and Month_and_Year and basic_salary and Allowances and Deductions and Gross_Salary and Net_salary and payment_date and Tax_info:
                        # Call the function to add employee data to the database
                        add_employee_to_database(payslip_id,emp_name,Month_year,basic_salary,allowances,Deductions,gross_salary,net_salary,payment_date,tax_info)
                    else:
                        st.warning("Please fill in all the required fields.")
                    # btnn=st.button("Add Employee")   
        elif choice3 == "Utility":
            ch5 = st.selectbox("Select", (
                "User Management", "Reset Passwords", "Backup and Restore", "Audit Logs", "System Settings",
                "Data Cleanup",
                "System Logs", "User Roles and Permissions", "Database Maintenance"))
        elif choice3 == "Help":
            ch6 = st.selectbox("Select", (
                "FAQs", "Contact Support", "Video Tutorials", "Feedback and Suggestions", "Report a Bug",
                "Terms of Service and Privacy Policy"))
        else:
            ch7 = st.selectbox("Select", ("Exit", "Quit"))
