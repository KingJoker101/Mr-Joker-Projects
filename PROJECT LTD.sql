iiCREATE SCHEMA Payment
GO
CREATE SCHEMA ProjectDetails
GO
CREATE SCHEMA CustomerDetails
GO
CREATE SCHEMA HumanResources
GO

CREATE TABLE HumanResources.Employee
(
EMPLOYEEID INT PRIMARY KEY,
NAME VARCHAR(50) NOT NULL,
TITLE NVARCHAR(50) CHECK(TITLE IN ('TRAINEE', 'TEAM MEMBER', 'TEAM LEADER','PROJECT MANAGER', 'SENIOR PROJECT MANAGER')),
PHONE_NO VARCHAR(50) CONSTRAINT CHK_PHONE
CHECK (PHONE_NO LIKE '%[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9]%'),
BILLING_RATE INT
)


CREATE TABLE CustomerDetails.Clients
(
CLIENTID INT PRIMARY KEY,
COMPANY_NAME VARCHAR(30) NOT NULL,
ADDRESS NVARCHAR(30) NOT NULL,
CITY VARCHAR(30) NOT NULL,
STATE VARCHAR(30) NOT NULL,
ZIP CHAR(30) NOT NULL,
COUNTRY VARCHAR NOT NULL,
CONTACT_PERSON NVARCHAR(30),
PHONE_NO VARCHAR NOT NULL
)


CREATE TABLE ProjectDetails.project
(
PROJECTID INT PRIMARY KEY,
PROJECT_NAME VARCHAR(20),
DESCRIPTION NVARCHAR(250),
CLIENTID INT FOREIGN KEY REFERENCES CustomerDetails.clients(clientID),
BILLING_ESTIMATE MONEY CONSTRAINT CK_BE CHECK(BILLING_ESTIMATE > 1000),
EMPLOYEEID INT,
StartDate DATE
)


alter table  ProjectDetails.project add constraint SK_SD CHECK (EndDate > StartDate)

CREATE TABLE ProjectDetails.timecards
(
timecards int primary key,
employeeid int foreign key references HumanResources.Employee(employeeID),
DATE_ISSUED int CONSTRAINT CDI
CHECK (DATE_ISSUED > 0)
)

Update ProjectDetails.timecards set TotalCost = Billable_hours * (select BillingRate HumanResources.Employee)



CREATE TABLE ProjectDetails.WorkCodes
(
WorkCodeID Int Primary Key,
Description Nvarchar(250) Not Null
)


CREATE TABLE projectDetails.TimeCardHours
(
"Time Card Detail ID" Nvarchar,
TimeCardID int primary key,
DateWorked Nvarchar(30),
ProjectID Varchar(30),
Work_Description Nvarchar(250),
Billable_Hours Nvarchar,
Total_Cost Nvarchar,
Work_Code_ID int
)


create table ProjectDetails.TimeCardExpenses
(
TimeCardExpenseID int primary key,
TimeCardID int foreign key references ProjectDetails.TimeCards(timecards),
ExpenseDate Date  Not Null,
ProjectID int foreign key references ProjectDetails.Project(ProjectID),
ExpenseDescription Nvarchar(300),
ExpenseAmount Money Constraint ch_EA check(ExpenseAmount > 0),
ExpenseCodeID varchar(50)
)

Create Trigger trg_P
on ProjectDetails.TimecardExpenses
After insert
AS
Begin
   Declare @ExpenseDate Date
   Declare @EndDate Date
   Select @ExpenseDate=ExpenseDate From inserted
   Select @EndDate = EndDate From ProjectDetails.project
   Begin
    if @ExpenseDate >= @EndDate 
		begin
	rollback transaction
		end
	end
end

Drop Table ProjectDetails.TimeCardExpenses

create table ProjectDetails.ExpenseCode
(
ExpenseCodeID int primary key,
Description Nvarchar(250) Not Null
)


Create Table Payment.Payments
(
PaymentID Int Primary Key,
ProjectID Varchar(30),
PaymentAmount Money Constraint CH_PA Check(PaymentAmount > 0),
PaymentDate Date,
CreditCardNumber INT,
CardHoldersName Nvarchar(30),
CreditCardExpiryDate Varchar(30) Null,
PaymentMethodID int foreign key references Payment.PaymentMethods(PaymentMethodID),
PaymentDue Money Constraint Chk_PD 
Check(PaymentDue < PaymentAmount)
)

Create trigger trg_PP
on Payment.Payments
After insert
As
 Begin
     Declare @PaymentDate Date
	 Declare @EndDate Date
	 Select @PaymentDate=PaymentDate From inserted
	 Select @EndDate=EndDate From ProjectDetails.project
	 Begin
	 if @PaymentDate <= @EndDate
	     Begin
	 RollBack Transaction
	     End
	 End
 End


Create Table payment.paymentMethods
(
PaymentMethodID Int Primary Key identity,
Description Nvarchar(250) Not Null
)

