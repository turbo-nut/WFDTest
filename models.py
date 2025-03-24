from django.db import models


class Car(models.Model):
    CarID = models.IntegerField(primary_key=True, name="Car_ID")
    serialNumber = models.IntegerField(name="Serial Number")
    make = models.TextField(name="Make")
    model = models.TextField(name="Model")
    color = models.TextField(name="Colour")
    year = models.TextField(name="Year")
    forSale = models.BooleanField(name="Car for Sale Y/N")


class Customer(models.Model):
    CustomerID = models.IntegerField(primary_key=True, name="Customer_ID")
    firstName = models.TextField(name="First Name")
    lastName = models.TextField(name="Last Name")
    phoneNum = models.IntegerField(name="Phone Number")
    address = models.TextField(name="Address")
    city = models.TextField(name="City")
    stateProvince = models.TextField(name="State/Province")
    country = models.TextField(name="Country")
    zipCode = models.TextField(name="Postal Code")


class Service(models.Model):
    ServiceID = models.IntegerField(primary_key=True, name="Service_ID")
    serviceName = models.TextField(name="Service Name")
    hourlyRate = models.TextField(name="Hourly Rate")


class Parts(models.Model):
    PartsID = models.IntegerField(primary_key=True, name="Parts_ID")
    partNumber = models.IntegerField(name="Part Number")
    partDesc = models.TextField(name="Description")
    partPrice = models.IntegerField(name="Purchase Price")
    retailPrice = models.IntegerField(name="Retail Price")


class Mechanic(models.Model):
    MechanicID = models.IntegerField(primary_key=True, name="Mechanic_ID")
    firstName = models.TextField(name="First Name")
    lastName = models.TextField(name="Last Name")


class ServiceTicket(models.Model):
    ServiceTicketID = models.IntegerField(
        primary_key=True, name="Service_Ticket_ID")
    serviceTicketNumber = models.IntegerField(name="Service Ticket Number")
    carID = models.ForeignKey(Car, name="Car ID")
    customerID = models.ForeignKey(Customer, name="Customer ID")
    dateRecieved = models.DateField(name="Date Recieved")
    comments = models.TextField(name="Comments")
    dateReturned = models.DateField(name="Date Returned to Customer")


class ServiceMechanic(models.Model):
    ServiceMechanicID = models.IntegerField(
        primary_key=True, name="ServiceMechanic_ID")
    ServiceTicketID = models.ForeignKey(
        ServiceTicket, name="Service Ticket ID")
    ServiceID = models.ForeignKey(Service, name="Service ID")
    MechanicID = models.ForeignKey(Mechanic, name="Mechanic ID")
    hours = models.IntegerField(name="Hours")
    comment = models.TextField(name="Comment")
    rate = models.TextField(name="Rate")


class PartsUsed(models.Model):
    PartsUsedID = models.IntegerField(primary_key=True, name="Parts_Used_ID")
    PartID = models.ForeignKey(Parts, name="Part ID")
    ServiceTicketID = models.ForeignKey(
        ServiceTicket, name="Service Ticket ID")


class Salesperson(models.Model):
    SalespersonID = models.IntegerField(
        primary_key=True, name="Salesperson_ID")
    firstName = models.TextField(name="First Name")
    lastName = models.TextField(name="Last Name")


class SalesInvoice(models.Model):
    InvoiceID = models.IntegerField(primary_key=True, name="Invoice_ID")
    invoiceNum = models.IntegerField(name="Invoice Number")
    date = models.DateField(name="Date")
    CarID = models.ForeignKey(Car, name="Car ID")
    CustomerID = models.ForeignKey(Customer, name="Customer ID")
    SalespersonID = models.ForeignKey(Salesperson, name="Salesperson ID")
