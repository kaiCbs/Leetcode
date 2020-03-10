SELECT Person.FirstName, Person.Lastname, Address.City, Address.State 
From Person Left Join Address On 
Person.PersonId = Address.PersonId
