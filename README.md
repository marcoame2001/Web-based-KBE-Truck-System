Project for NTNU- Knowledge Based Engineering TMM4270

In this project we focused on generating a parameterized automated solution in which users input data through a web application. Our truck server reads the input data such as dimensions, colors and types of the trucks and generates a customized CAD model using Siemens NX Knowledge Fusion. On the other hand, the trucks were stored in OWL database that is connected to a Jena Fuseki server. Using SPARQL queries our truck server checks if the input truck already exists and inserts it in the OWL database, otherwise the truck is not stored:

Examples of the queries and the generated trucks:

<img width="551" alt="image" src="https://github.com/marcoame2001/Web-based-KBE-Truck-System/assets/143449334/2fc9b49f-d367-4b5c-92a3-e94237a703a9">

<img width="558" alt="image" src="https://github.com/marcoame2001/Web-based-KBE-Truck-System/assets/143449334/2c22c04d-b9ff-4d97-92ef-75c681c8c96f">

<img width="573" alt="image" src="https://github.com/marcoame2001/Web-based-KBE-Truck-System/assets/143449334/13dd8e60-c776-4647-a2ea-f21a3d824b7a">
