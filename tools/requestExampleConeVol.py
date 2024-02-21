# importing the requests library - MAKING REQUEST TO FUSEKI example - Cone Volumes.
import requests 

URL = "http://127.0.0.1:3030/kbe/query"

theQuery = """
PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>
SELECT ?block ?l ?w ?h
WHERE
{
?block a kbe:Block.
?block kbe:hasLength ?l.
?block kbe:hasWidth ?w.
?block kbe:hasHeight ?h.
} 
"""
  
# defining a query params 
PARAMS = {'query':theQuery} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

#Checking the result
print("Result:", r.text)
data = r.json()
print("JSON:", data)

#Checking the value of the parameter
iResults = data['results']['bindings'] #Iteratable results.
print("Results", iResults)
for res in iResults:
    print("************************")
    print("Block:", res['block']['value'])
    print("Length:", res['l']['value'])
    print("Width:", res['w']['value'])
    print("Height:", res['h']['value'])
print("************************")
