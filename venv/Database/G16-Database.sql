drop database if exists g16_db;
create database g16_db;
use g16_db;

create table users(
	user_id varchar(10) primary key, 
	user_name varchar(50),
    dob varchar(20),
	phone_num varchar(20), 
	email varchar(30)
);

create table books(
	book_id varchar(10) primary key, 
    book_title varchar(50),
    author_id varchar(10),
    available_copies int
);

create table authors(
	author_id varchar(10) primary key, 
    author_name varchar(50) 
);

create table lent_books(
	book_id varchar(10),
    lent_copies int,
    user_id varchar(10),
    borrowed_date varchar(20),
    deadline varchar(20)
);

ALTER TABLE lent_books ADD FOREIGN KEY(user_id) REFERENCES users(user_id);
ALTER TABLE lent_books ADD FOREIGN KEY(book_id) REFERENCES books(book_id) on delete cascade;
ALTER TABLE books ADD FOREIGN KEY(author_id) REFERENCES authors(author_id);

-- Chinh sua tu dong nay tro xuong
INSERT INTO authors values
('Au1', 'Conan Doyle'),
('Au2', 'J. K. Rowling'),
('Au3', 'Nguyen Du'),
('Au4', 'James Dashner'),
('Au5', 'Rick Riordan'),
('Au6', 'Fujiko Fujio'),
('Au7', 'Nam Cao'),
('Au8', 'Stan Lee'),
('Au9', 'Zed Shaw'),
('Au10', 'Chi Dau')
;

INSERT INTO books values 
('B01', 'Learn Python the Hard 	Way', 'Au9', '8' ),
('B02', 'Chi Dau', 'Au10', '9' ),
('B03', 'Doraemon', 'Au6', '6' ),
('B04', 'Harry Potter', 'Au2', '2' ),
('B05', 'Percy Jackson', 'Au5', '5' ),
('B06', 'The maze runner', 'Au4', '4' ),
('B07', 'Lao Hac', 'Au7', '9' ),
('B08', 'The Avengers', 'Au8', '7' ),
('B09', 'Truyen Kieu', 'Au3', '3' ),
('B010', 'Sherlock Holmes', 'Au1', '1' )
;



INSERT INTO users values
('U01', 'Alex', '2001-12-03', '0980113114', 'alex@gmail.com'),
('U02', 'Peter', '2000-11-04', '0363646423', 'peter@gmail.com'),
('U03', 'Wong', '2001-07-31', '0923523665', 'wong@gmail.com'),
('U04', 'Son', '2000-01-03', '0923535345', 'son@gmail.com'),
('U05', 'LiLy', '1998-11-02', '0983426654', 'lily@gmail.com'),
('U06', 'Rosé', '1993-10-15', '0983466734', 'rose@gmail.com'),
('U07', 'Mixi', '1997-05-27', '0982345352', 'mixi@gmail.com'),
('U08', 'Tony', '1990-03-30', '0980132454', 'tony@gmail.com');

INSERT INTO lent_books values
('B01', 1, 'U01', '2021-05-18', '2021-06-18'),
('B03', 4, 'U08', '2020-06-10', '2020-07-10'),
('B04', 1, 'U06', '2021-04-18', '2021-05-18'),
('B05', 1, 'U02', '2020-04-16', '2020-05-16'),
('B07', 3, 'U05', '2021-03-02', '2021-04-02'),
('B02', 5, 'U03', '2021-02-28', '2021-03-28');


/* Insert Authors And Books */
-- drop procedure if exists InsertAuthorsAndBooks;
delimiter //
CREATE PROCEDURE InsertAuthorsAndBooks(in author_id varchar(10), author_name varchar(30), book_id varchar(10), book_title varchar(50), copies int)
BEGIN
	INSERT INTO authors values (author_id, author_name);
	INSERT INTO books values (book_id, book_title, author_id, copies);
END //
delimiter ;


/* Delete Book By ID (onlywhen no ones lent it)*/
-- drop procedure if exists DeleteBookByID;
delimiter //
CREATE PROCEDURE DeleteBookByID(IN id varchar(10))
BEGIN
	DELETE FROM books WHERE book_id = id;
END //
delimiter ;


/* Delete Users By ID*/
-- drop procedure if exists DeleteUserByID;
-- users insert the userID
delimiter //
CREATE PROCEDURE DeleteUserByID(IN id varchar(10))
BEGIN
	DELETE FROM users WHERE user_id = id;
END //
delimiter ;


/* Add Users */
-- drop procedure if exists AddUsers;
-- insert the user's info
delimiter //
CREATE PROCEDURE AddUser(in user_id varchar(10), user_name varchar(30), dob varchar(20), phone_num varchar(20), email varchar(30))
BEGIN
	INSERT INTO users values (user_id, user_name, dob, phone_num, email);
END //
delimiter ;


/* View All Users */
-- drop procedure if exists ViewAllUsers;
-- users insert the userID
delimiter //
CREATE PROCEDURE ViewAllUsers()
BEGIN
	SELECT * FROM users WHERE user_id = id;
END //
delimiter ;


/* Update User */
-- drop procedure if exists UpdateUser;
-- insert the user's new info
delimiter //
CREATE PROCEDURE UpdateUser(IN id varchar(10), newUserName varchar(30), newDob varchar(20), newPhoneNum varchar(20), newEmail varchar(30))
BEGIN
	UPDATE users
    SET user_name = newUserName, 
		dob = newDob, 
		phone_num = newPhoneNum, 
        email = newEmail
    WHERE user_id = id;	
END //
delimiter ;


/* Update Book */
-- drop procedure if exists UpdateBook;
delimiter //
CREATE PROCEDURE UpdateBook(IN id varchar(10), newBookTitle varchar(30), newAvailableCopies int,  newAuthorID varchar(10))
BEGIN
	UPDATE books
    SET book_title = newBookTitle, 
		available_copies = newAvailableCopies, 
        author_id = newAuthorID
    WHERE book_id = id;	
END //
delimiter ;


/* Lend Book */
-- drop procedure if exists LendBook;
delimiter //
-- users insert the bookID, copies, userID, borrowDate and deadline
CREATE PROCEDURE LendBook(IN newBookID varchar(10), newLentCopies int, newUserID varchar(10),  newBorrowedDate varchar(20), newDeadline varchar(20) )
BEGIN
    INSERT INTO lent_books values (newBookID, newLentCopies, newUserID,  newBorrowedDate, newDeadline);
    UPDATE books
    SET available_copies = available_copies - newLentCopies
    WHERE book_id = newBookID;
END //
delimiter ;


/* Return Book */
-- drop procedure if exists Returnbook;
delimiter //
-- users insert the bookID, userID and copies had lent
-- !users have to return all copies.
CREATE PROCEDURE ReturnBook(IN newBookID varchar(10), newUserID varchar(10), newLentCopies int)
BEGIN
    UPDATE books
    SET available_copies = available_copies + newLentCopies
    WHERE book_id = newBookID;
    
    DELETE FROM lent_books WHERE book_id = newBookID AND user_id = newUserID;
END //
delimiter ;

-- find which user borrows which book
delimiter //
CREATE PROCEDURE FindBorrowerByName(in u_name varchar(50)) 
begin
    select users.user_id, user_name, dob, books.book_id, book_title, lent_copies 
    from users inner join lent_books 
    on (users.user_id=lent_books.user_id and users.user_name=u_name)
    join books 
    on (lent_books.book_id=books.book_id)
    ;
end //
delimiter ;

delimiter //
CREATE PROCEDURE ShowBorrowersByBookName(in b_name varchar(50)) 
begin
    select users.user_id, users.user_name, users.dob, books.book_id, books.book_title, lent_books.lent_copies 
    from users inner join lent_books 
    on (users.user_id=lent_books.user_id)
    join books 
    on (books.book_title=b_name)
    ;
end //
delimiter ;

-- show all borrowers
delimiter //
CREATE PROCEDURE ShowAllBorrowers() 
begin
    select users.user_id, user_name, dob, books.book_id, book_title, lent_copies, borrowed_date, deadline 
    from users inner join lent_books 
    on (users.user_id=lent_books.user_id)
    inner join books 
    on (lent_books.book_id=books.book_id)
    ;
end //
delimiter ;

delimiter //
CREATE PROCEDURE DeleteBookByName(IN book_name varchar(10))
BEGIN
-- 	delete books, lent_books
--     from lent_books inner join books 
--     on books.book_id=lent_books.book_id
--     where books.book_title=book_name
--     ;
	delete from books where books.book_title=book_name;
END //
delimiter ;

delimiter //
CREATE PROCEDURE ShowAllBooksByBorrowerName(IN borrower_name varchar(10))
BEGIN
	select users.user_id, users.user_name, lent_books.book_id, books.book_title, lent_books.lent_copies 
    from lent_books inner join users
    on users.user_name = borrower_name and users.user_id = lent_books.user_id
    inner join books
    on books.book_id = lent_books.book_id
    ;
END //
delimiter ;

delimiter //
CREATE PROCEDURE ShowAllBooksByBorrowerID(IN id varchar(10))
BEGIN
	select users.user_id, users.user_name, lent_books.book_id, books.book_title, lent_books.lent_copies 
    from lent_books inner join users
    on users.user_id = id and users.user_id = lent_books.user_id
    inner join books
    on books.book_id = lent_books.book_id
    ;
END //
delimiter ;

-- delimiter //
-- CREATE PROCEDURE ShowAllBooksByBorrowerID(IN id varchar(10))
-- BEGIN
-- 	
-- END //
-- delimiter ;

-- call UpdateBook (
-- call ShowAllBooksByBorrowerID('U01');
-- call ShowAllBooksByBorrowerName('Wong');
-- call DeleteBookByID('B02');
-- call FindBorrowerByName('Alex');
-- call DeleteBookByID('B03');
-- call InsertAuthorsAndBooks('23', '4324', '43', '1234', 1);
-- call AddUser('U04', 'Hana', '2000-01-03', '0981393166', 'hana@gmail.com');
-- call ReturnBook ('B05', 'U02', 1);
-- call lendBook ('B05', 1, 'U02', '2020-04-16', '2020-05-16');