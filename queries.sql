USE `BarnesAndIgnoble`;

-- Question 7.1 - Books per author
SELECT A.*, COUNT(DISTINCT(BA.ISBN)) AS `Total Books Written`
FROM   Authors A
JOIN BookAuthors BA
	ON A.AuthorID = BA.AuthorID
GROUP BY BA.AuthorID;

-- Question 7.2 - Authors per book
SELECT B.*, COUNT(DISTINCT(BA.AuthorID)) AS `Number of Authors`
FROM   Books B
JOIN BookAuthors BA 
	ON B.ISBN = BA.ISBN
GROUP BY B.ISBN;

-- Question 7.3 - Author roylaties on a book
SELECT B.ISBN, B.Title, SUM(BA.Royalty) AS `Total Royalties`
FROM   Books B
JOIN BookAuthors BA
	ON B.ISBN = BA.ISBN
GROUP BY B.ISBN;

-- Question 7.3 - Book royalties per author
SELECT A.*, SUM(BA.Royalty) AS `Total Royalties`
FROM   Authors A
JOIN BookAuthors BA
	ON A.AuthorID = BA.AuthorID
GROUP BY A.AuthorID;

-- Question 7.5 - Books in a genre
SELECT B.Genre, COUNT(B.Genre) AS `Books per Genre`
FROM   Books B
GROUP BY B.Genre;

-- Question 7.6 - Books published by a publisher
SELECT P.PublisherID, P.Name, COUNT(DISTINCT(B.ISBN)) AS `Books Published`
FROM   Publishers P
JOIN Books B
	ON B.PublisherID = P.PublisherID
GROUP BY B.PublisherID;

-- Question 7.7 - Editors per book
SELECT B.*, COUNT(DISTINCT(BE.EditorID)) AS `Editors`
FROM   Books B
JOIN BookEditors BE
	ON B.ISBN = BE.ISBN
GROUP BY B.ISBN;

-- Question 7.8 - Books per editor
SELECT E.EditorID, E.Name, COUNT(DISTINCT(BE.ISBN)) AS `Books Edited`
FROM   Editors E
JOIN BookEditors BE
	ON E.EditorID = BE.EditorID
GROUP BY E.EditorID;

-- Question 7.9 - Books in an order
SELECT O.*, COUNT(DISTINCT(S.ISBN)) AS `Books per Order`
FROM   Orders O
JOIN Shipments S
	ON O.OrderID = S.OrderID
GROUP BY O.OrderID;

-- Question 7.10 - Orders for a book
SELECT B.*, COUNT(DISTINCT(S.OrderID)) AS `Copies Ordered`
FROM   Books B
JOIN Shipments S
	ON B.ISBN = S.ISBN
GROUP BY B.ISBN;

-- Question 7.11 - Customer Orders
SELECT O.*, O.Total, O.CustomerID
FROM   Orders O
GROUP BY O.OrderID;

-- Question 7.12 - Orders per customer
SELECT C.*, COUNT(DISTINCT(O.OrderID)) AS `Orders Placed`
FROM   Customers C
JOIN Orders O
	ON C.CustomerID = O.OrderID
GROUP BY C.CustomerID;