Project for NTNU- Knowledge Based Engineering TMM4270

In this project we focused on generating a parameterized solution in which users input data through a web application. Our truck server reads the input data such 
as dimensions, colors and types of the trucks and generates a customized CAD model using Siemens NX. On the other hand, the trucks were stored in OWL database that 
is connected to a Jena Fuseki server. Using SPARQL queries our truck server checks if the input truck already exists and inserts it in the OWL database, otherwise 
the truck is not stored:

