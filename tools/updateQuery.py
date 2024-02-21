#DELETING / UPDATE query in Python
import requests 
URL = "http://127.0.0.1:3030/kbe/update"
theQuery = """
PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
DELETE
{
kbe:cube3 a kbe:Cube.
kbe:cube3 kbe:hasSIde "5.0"^^<http://www.w3.org/2001/XMLSchema#float>.
}
WHERE
{
kbe:cube3 a kbe:Cube.
kbe:cube3 kbe:hasSIde "5.0"^^<http://www.w3.org/2001/XMLSchema#float>.
}
""" 

# sending get request and saving the response as response object 
r = requests.post(URL, theQuery) 
