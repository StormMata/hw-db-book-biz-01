import mysql.connector
from faker import Faker
import random
fake = Faker()

# #  connection string
# cnx = mysql.connector.connect(
#     user        ='root',
#     password    ='13500586',
#     host        ='127.0.0.1',
#     database    ='ps3',
#     auth_plugin ='mysql_native_password')

# # query
# cursor = cnx.cursor()

# NumData = 25

genre_list = ['Action','adventure','Autobiography','Anthology','Biography','Crafts/hobbies',
'Classic','Cookbook','Diary','Dictionary','Crime','Encyclopedia','Drama','Fairytale','Health/fitness',
'Fantasy','History','Graphic novel' ]

# isbn_list = ['1-942652-80-1','1-77925-566-7','0-8468-4877-5','1-81712-997-X','0-7451-2778-9',
# '1-5228-6187-4','0-8053-4436-5','1-348-60060-8','0-241-41547-0','1-08-178914-X','1-65289-274-5',
# '0-87860-927-X','0-7613-1837-2','0-8295-0938-0','1-924056-80-1','1-81250-000-9','0-461-88452-6',
# '1-397-97211-4','1-254-35307-0','0-03-585233-X','0-373-78388-4','1-123-86083-1','1-337-40078-5',
# '0-10-553601-6','0-13-391590-5','0-302-76711-8','1-874618-83-6','1-188-69671-8','0-9628936-5-X',
# '1-392-22775-5','1-79458-254-1','0-09-435867-2','1-72135-884-6','1-387-40207-2','1-4367-4895-X',
# '1-371-64702-X','1-340-78919-1','1-65081-704-5','0-448-67309-6','1-67329-936-9','0-906963-71-0',
# '1-4566-9852-4','1-76279-395-4','1-170-15924-9','0-85173-872-9','0-522-85473-7','0-587-16753-X',
# '1-287-61104-4','1-05-311311-0','0-475-51315-0']

# people_list = ['Christopher Holt','David Davis','Michelle Williamson','William Norman','Jamie Benton',
# 'Michael Simpson DVM','Eric Tucker','Melissa Ross','Brian Sanchez','David Smith','Kenneth Buck',
# 'Lisa Brennan','Kimberly Bell','Kayla Lopez','Ruth Ford','Sandra Young PhD','Sandra Alvarado',
# 'Mr. Ricky Russell Jr.','Christopher Coffey','Austin Reilly','Michael Adams','Brandy Collins PhD',
# 'Vicki Green','Kent Barber','Janet Harris','Barry Torres','Heidi Kerr','Joshua Snyder','Peter Bennett',
# 'Shaun Cox','Emily Frey','James Ruiz','Jeremy James','Michael Duncan','Rhonda Alvarado','Alexis Weaver',
# 'Brandy Rogers','Kevin Fletcher','Dylan Small','Erica Cook','Michele Mueller','Rachel Turner','Edward Roberts',
# 'Mr. David Jennings','David Perry','Eric Bradley','Emily West','Jorge Lamb','Sheila Wilkinson','Norma Gonzalez']

# # Customers

# AddCustomers = "INSERT INTO Customers (Name) VALUES (%(Name)s)"

# for x in range(NumData):
#     DataCustomers = {
#     'Name': fake.name(),
#     }

#     cursor.execute(AddCustomers,DataCustomers)

# # Orders

# AddOrders = "INSERT INTO Orders (Date, Total, CustomerID) VALUES (%(Date)s, %(Total)s, %(CustomerID)s)"

# for x in range(NumData):
#     DataOrders = {
#     'Date': fake.date(),
#     'Total': round(random.uniform(1, 1000),2),
#     'CustomerID': random.randint(1, NumData)
#     }

#     cursor.execute(AddOrders,DataOrders)

# # Authors

# AddAuthors = "INSERT INTO Authors (Name) VALUES (%(Name)s)"

# for x in range(NumData):
#     DataAuthors = {
#     'Name': random.choice(people_list),
#     }

#     cursor.execute(AddAuthors,DataAuthors)

# # Publishers

# AddPublishers = "INSERT INTO Publishers ( Name, City) VALUES ( %(Name)s, %(City)s)"

# for x in range(NumData):
#     DataPublishers = {
#     'Name': fake.company(),
#     'City': fake.city(),
#     }

#     cursor.execute(AddPublishers,DataPublishers)

# # Books

# AddBooks = "INSERT INTO Books (ISBN, PublisherID, Title, Genre, PubDate, Price) VALUES (%(ISBN)s, %(PublisherID)s, %(Title)s, %(Genre)s, %(PubDate)s, %(Price)s)"

# for x in range(NumData):
#     DataBooks = {
#     'ISBN': isbn_list[x],
#     'PublisherID': random.randint(1, NumData),
#     'Title': fake.sentence(),
#     'Genre': random.choice(genre_list),
#     'PubDate': fake.date(),
#     'Price': round(random.uniform(1, 500),2)
#     }

#     cursor.execute(AddBooks,DataBooks)

# # Editors

# AddEditors = "INSERT INTO Editors (PublisherID,Name) VALUES (%(PublisherID)s,%(Name)s)"

# for x in range(NumData):
#     DataEditors = {
#     'PublisherID': random.randint(1, NumData),
#     'Name': random.choice(people_list)
#     }

#     cursor.execute(AddEditors,DataEditors)

# # Shipments

# AddShipments = "INSERT INTO Shipments (ISBN,AuthorID,PublisherID,Royalty) VALUES (%(ISBN)s,%(AuthorID)s,%(PublisherID)s,%(Royalty)s)"

# for x in range(NumData):
#     DataShipments = {
#     'ISBN': random.choice(isbn_list[0:NumData-5]),
#     'AuthorID': random.randint(1, NumData-10),
#     'PublisherID': random.randint(1, NumData-10),
#     'Royalty': round(random.uniform(1, 5000),2)
#     }

#     cursor.execute(AddShipments,DataShipments)

# # Book Authors

# AddBookAuthors = "INSERT INTO BookAuthors (AuthorID,ISBN) VALUES (%(AuthorID)s,%(ISBN)s)"

# for x in range(NumData):
#     DataBookAuthors = {
#     'AuthorID': random.randint(1, NumData-10),
#     'ISBN': random.choice(isbn_list[0:NumData-20]),
#     }

#     cursor.execute(AddBookAuthors,DataBookAuthors)

# # Book Orders

# AddBookOrders = "INSERT INTO BookOrders (OrderID,ISBN) VALUES (%(OrderID)s,%(ISBN)s)"

# for x in range(NumData):
#     DataBookOrders = {
#     'OrderID': random.randint(1, NumData-10),
#     'ISBN': random.choice(isbn_list[0:NumData-20]),
#     }

#     cursor.execute(AddBookOrders,DataBookOrders)

# # Book Editors

# AddBookEditors = "INSERT INTO BookEditors (EditorID, ISBN) VALUES (%(EditorID)s,%(ISBN)s)"

# for x in range(NumData):
#     DataBookEditors = {
#     'EditorID': random.randint(1, NumData-10),
#     'ISBN': random.choice(isbn_list[0:NumData-10])
#     }

#     cursor.execute(AddBookEditors,DataBookEditors)

# ------------------ Publishers ------------------
NumData = 8
ID = 1

with open('/Users/stormmata/Desktop/Publishers.txt', 'w') as f:

    for x in range(NumData):

        string = (f"INSERT INTO `Publishers` VALUES({ID},'{fake.company()}','{fake.city()}');")

        ID = ID + 1

        f.write(string)
        f.write('\n')
f.close()

# ------------------ Editors ------------------
NumData = 15
ID = 1

with open('/Users/stormmata/Desktop/Editors.txt', 'w') as f:

    for x in range(NumData):

        string = (f"INSERT INTO `Editors` VALUES({ID},{random.randint(1, NumData-10)},'{fake.name()}');")
        ID = ID + 1

        f.write(string)
        f.write('\n')
f.close()

# ------------------ Authors ------------------
NumData = 20
ID = 1

with open('/Users/stormmata/Desktop/Authors.txt', 'w') as f:

    for x in range(NumData):

        string = (f"INSERT INTO `Authors` VALUES({ID},'{fake.name()}');")
        ID = ID + 1

        f.write(string)
        f.write('\n')
f.close()

# ------------------ Customers ------------------
NumData = 50
ID = 1

with open('/Users/stormmata/Desktop/Customers.txt', 'w') as f:

    for x in range(NumData):

        string = (f"INSERT INTO `Customers` VALUES({ID},'{fake.name()}');")
        ID = ID + 1

        f.write(string)
        f.write('\n')
f.close()

# ------------------ Orders ------------------
NumData = 100

ID = 1

with open('/Users/stormmata/Desktop/Orders.txt', 'w') as f:

    for x in range(NumData):

        string = (f"INSERT INTO `Orders` VALUES({ID},{fake.year()},'{round(random.uniform(15.99, 500),2)}',{random.randint(1, 50)});")
        ID = ID + 1

        f.write(string)
        f.write('\n')
f.close()

# ------------------ Books ------------------
NumData = 200

ISBNs = []

with open('/Users/stormmata/Desktop/Books.txt', 'w') as f:

    for x in range(NumData):

        ISBNs.append(fake.isbn10())

        # print(f"INSERT INTO `Books` VALUES('{ISBNs[x]}','{fake.sentence()}','{random.choice(genre_list)}',{fake.year()},{round(random.uniform(15.99, 125.99),2)},{random.randint(1, 8)});")
        string = (f"INSERT INTO `Books` VALUES('{ISBNs[x]}','{fake.sentence()}','{random.choice(genre_list)}',{fake.year()},{round(random.uniform(15.99, 125.99),2)},{random.randint(1, 8)});")

        f.write(string)
        f.write('\n')
f.close()

# ------------------ BookEditors ------------------
NumData = 200

with open('/Users/stormmata/Desktop/BookEditors.txt', 'w') as f:

    for x in range(NumData):

        # print(f"INSERT INTO `Editors` VALUES({ID},{random.randint(1, NumData-10)},'{fake.name()}');")
        string = (f"INSERT INTO `BookEditors` VALUES({random.randint(1, 15)},'{ISBNs[x]}');")

        f.write(string)
        f.write('\n')
f.close()

# ------------------ BookAuthors ------------------
NumData = 200

with open('/Users/stormmata/Desktop/BookAuthors.txt', 'w') as f:

    for x in range(NumData):

        string = (f"INSERT INTO `BookAuthors` VALUES({random.randint(1, 15)},'{ISBNs[x]}',{round(random.uniform(15.99, 10000),2)});")

        f.write(string)
        f.write('\n')
f.close()

# ------------------ Shipments ------------------
NumData = 100

ID = 1

with open('/Users/stormmata/Desktop/Shipments.txt', 'w') as f:

    for x in range(NumData):

        string = (f"INSERT INTO `Shipments` VALUES({ID},'{random.choice(ISBNs)}');")

        ID = ID + 1

        f.write(string)
        f.write('\n')
f.close()


# for x in range(5):
#     print(x)

# clean up
# cnx.commit()
# cursor.close()
# cnx.close()