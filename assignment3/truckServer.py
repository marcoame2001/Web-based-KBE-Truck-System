# Length / Width / Height – Remember to update the template to work for <LENGTH>, <WIDTH> and <HEIGHT>

#paramServer.py
#HTTP Server template / One parameter
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests


HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234 # Maybe set this to 1234
#file path of this python file
filePath = 'C:\\Users\\alvaroor\\assignment3\\DFAS' #A folder where you store your DFAs

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        
        # Check what is the path
        path = s.path
        if path.find("/") != -1 and len(path) == 1:
            s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))
        elif path.find("/setParameters") != -1:
            s.wfile.write(bytes('<html><body><h2>TRUCK</h2>', 'utf-8'))
            s.wfile.write(bytes('<form action="/setParameters" method="post">', 'utf-8'))
            #ELEMENT
            s.wfile.write(bytes('<label for="selement">Set element (BoxElement, PlatformElement, TankElement):</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="selement" name="selement" value="BoxElement"><br><br>', 'utf-8'))
            #TRUCK_LENGTH
            s.wfile.write(bytes('<label for="strucklength">Set truck length:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="strucklength" name="strucklength" value="190"><br><br>', 'utf-8'))
            #TRUCK_WIDTH
            s.wfile.write(bytes('<label for="struckwidth">Set truck width:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="struckwidth" name="struckwidth" value="50"><br><br>', 'utf-8'))
            #ELEMENT_HEIGHT
            s.wfile.write(bytes('<label for="selementheight">Set element height/diameter:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="selementheight" name="selementheight" value="50"><br><br>', 'utf-8'))
            #ELEMENT_LENGTH
            s.wfile.write(bytes('<label for="selementlength">Set element length:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="selementlength" name="selementlength" value="150"><br><br>', 'utf-8'))
            #CABINE_HEIGHT
            s.wfile.write(bytes('<label for="scabineheight">Set cabine height:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="scabineheight" name="scabineheight" value="40"><br><br>', 'utf-8'))
            #DETAILS_COLOR
            s.wfile.write(bytes('<label for="sdetailscolor">Set details color:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="sdetailscolor" name="sdetailscolor" value="BLACK"><br><br>', 'utf-8'))
            #ELEMENT_COLOR
            s.wfile.write(bytes('<label for="selementcolor">Set element color:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="selementcolor" name="selementcolor" value="DARK_DULL_GREEN"><br><br>', 'utf-8'))
            #TRUCK_COLOR
            s.wfile.write(bytes('<label for="struckcolor">Set truck color:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="struckcolor" name="struckcolor" value="RED"><br><br>', 'utf-8'))
            #SUBMIT
            s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
            s.wfile.write(bytes('</form></body></html>', 'utf-8'))
        else:
            s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
            s.wfile.write(bytes("<body><p>The path: " + path + "</p>", "utf-8"))
            s.wfile.write(bytes('</body></html>', "utf-8"))
            
    def do_POST(s):

        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        
        # Check what is the path
        path = s.path
        print("Path: ", path)
        if path.find("/setParameters") != -1:
            content_len = int(s.headers.get('Content-Length'))
            post_body = s.rfile.read(content_len)
            param_line = post_body.decode()
            print("Body: ", param_line)
            
            #Get the param value
            pairs = param_line.split("&")
            rpairs = [] #ready pairs
            for pair in pairs:
                p = pair.split("=")
                rpairs.append(p)
            
            print(rpairs)
            
            #Open the template file
            f = open(filePath + "\\templates\\Box_Truck.dfa", "r")
            txt = f.read()

            
            s.wfile.write(bytes('<form action="/setParameters" method="post">', 'utf-8'))
            #ELEMENT
            s.wfile.write(bytes('<label for="selement">Set element (BoxElement, PlatformElement, TankElement):</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="selement" name="selement" value="BoxElement"><br><br>', 'utf-8'))
            #TRUCK_LENGTH
            s.wfile.write(bytes('<label for="strucklength">Set truck length:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="strucklength" name="strucklength" value="190"><br><br>', 'utf-8'))
            #TRUCK_WIDTH
            s.wfile.write(bytes('<label for="struckwidth">Set truck width:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="struckwidth" name="struckwidth" value="50"><br><br>', 'utf-8'))
            #ELEMENT_HEIGHT
            s.wfile.write(bytes('<label for="selementheight">Set element height/diameter:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="selementheight" name="selementheight" value="50"><br><br>', 'utf-8'))
            #ELEMENT_LENGTH
            s.wfile.write(bytes('<label for="selementlength">Set element length:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="selementlength" name="selementlength" value="150"><br><br>', 'utf-8'))
            #CABINE_HEIGHT
            s.wfile.write(bytes('<label for="scabineheight">Set cabine height:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="scabineheight" name="scabineheight" value="40"><br><br>', 'utf-8'))
            #DETAILS_COLOR
            s.wfile.write(bytes('<label for="sdetailscolor">Set details color:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="sdetailscolor" name="sdetailscolor" value="BLACK"><br><br>', 'utf-8'))
            #ELEMENT_COLOR
            s.wfile.write(bytes('<label for="selementcolor">Set element color:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="selementcolor" name="selementcolor" value="DARK_DULL_GREEN"><br><br>', 'utf-8'))
            #TRUCK_COLOR
            s.wfile.write(bytes('<label for="struckcolor">Set truck color:</label><br>', 'utf-8'))
            s.wfile.write(bytes('<input type="text" id="struckcolor" name="struckcolor" value="RED"><br><br>', 'utf-8'))
            #SUBMIT
            s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))

            s.wfile.write(bytes('<p>The value of the sides were set to ' + str(rpairs) + '</p>', 'utf-8'))
            
            s.wfile.write(bytes('</form></body></html>', 'utf-8'))
            
            txt = txt.replace("<ELEMENT>", rpairs[0][1])
            
            
            file2a = open(filePath + "\\Box_Truck.dfa", "w")
            file2a.write(txt)
            file2a.close()

            "We open the cabine file to write"            
            cabinefile = open(filePath + "\\templates\\cabine.dfa", "r")
            txt = cabinefile.read()
            txt = txt.replace("<ELEMENT>", rpairs[0][1])
            txt = txt.replace("<TRUCK_LENGTH>", rpairs[1][1])
            txt = txt.replace("<TRUCK_WIDTH>", rpairs[2][1])
            txt = txt.replace("<ELEMENT_HEIGHT>", rpairs[3][1])
            txt = txt.replace("<ELEMENT_LENGTH>", rpairs[4][1])
            txt = txt.replace("<CABINE_HEIGHT>", rpairs[5][1])
            txt = txt.replace("<DETAILS_COLOR>", rpairs[6][1]) 
            txt = txt.replace("<ELEMENT_COLOR>", rpairs[7][1]) 
            txt = txt.replace("<TRUCK_COLOR>", rpairs[8][1])
            
            f = open(filePath + "\\cabine.dfa", "w")
            f.write(txt)
            f.close()
            
            "We open the structure file to write"            
            structurefile = open(filePath + "\\templates\\structure.dfa", "r")
            txt = structurefile.read()
            txt = txt.replace("<ELEMENT>", rpairs[0][1])
            txt = txt.replace("<TRUCK_LENGTH>", rpairs[1][1])
            txt = txt.replace("<TRUCK_WIDTH>", rpairs[2][1])
            txt = txt.replace("<ELEMENT_HEIGHT>", rpairs[3][1])
            txt = txt.replace("<ELEMENT_LENGTH>", rpairs[4][1])
            txt = txt.replace("<CABINE_HEIGHT>", rpairs[5][1])
            txt = txt.replace("<DETAILS_COLOR>", rpairs[6][1]) 
            txt = txt.replace("<ELEMENT_COLOR>", rpairs[7][1]) 
            txt = txt.replace("<TRUCK_COLOR>", rpairs[8][1])
            
            file3 = open(filePath + "\\structure.dfa", "w")
            file3.write(txt)
            file3.close()
            
            "CHANGE CHOZEN DFA"
            
            if rpairs[0][1] =='BoxElement':
                "We open the boxelem to write"            
                boxfile = open(filePath + "\\templates\\Box.dfa", "r")
                txt = boxfile.read()
                txt = txt.replace("<ELEMENT>", rpairs[0][1])
                txt = txt.replace("<TRUCK_LENGTH>", rpairs[1][1])
                txt = txt.replace("<TRUCK_WIDTH>", rpairs[2][1])
                txt = txt.replace("<ELEMENT_HEIGHT>", rpairs[3][1])
                txt = txt.replace("<ELEMENT_LENGTH>", rpairs[4][1])
                txt = txt.replace("<CABINE_HEIGHT>", rpairs[5][1])
                txt = txt.replace("<DETAILS_COLOR>", rpairs[6][1]) 
                txt = txt.replace("<ELEMENT_COLOR>", rpairs[7][1]) 
                txt = txt.replace("<TRUCK_COLOR>", rpairs[8][1])
                
                file4 = open(filePath + "\\Box.dfa", "w")
                file4.write(txt)
                file4.close()
                
            elif rpairs[0][1] =='PlatformElement':
                "We open the platform to write"
                
           
                platfile = open(filePath + "\\templates\\Platform.dfa", "r")
                txt = platfile.read()
                txt = txt.replace("<ELEMENT>", rpairs[0][1])
                txt = txt.replace("<TRUCK_LENGTH>", rpairs[1][1])
                txt = txt.replace("<TRUCK_WIDTH>", rpairs[2][1])
                txt = txt.replace("<ELEMENT_HEIGHT>", rpairs[3][1])
                txt = txt.replace("<ELEMENT_LENGTH>", rpairs[4][1])
                txt = txt.replace("<CABINE_HEIGHT>", rpairs[5][1])
                txt = txt.replace("<DETAILS_COLOR>", rpairs[6][1]) 
                txt = txt.replace("<ELEMENT_COLOR>", rpairs[7][1]) 
                txt = txt.replace("<TRUCK_COLOR>", rpairs[8][1])
                
                file5 = open(filePath + "\\Platform.dfa", "w")
                file5.write(txt)
                file5.close() 
                
            elif rpairs[0][1] =='TankElement':

                tankfile = open(filePath + "\\templates\\Tank.dfa", "r")
                txt = tankfile.read()
                txt = txt.replace("<ELEMENT>", rpairs[0][1])
                txt = txt.replace("<TRUCK_LENGTH>", rpairs[1][1])
                txt = txt.replace("<TRUCK_WIDTH>", rpairs[2][1])
                txt = txt.replace("<ELEMENT_HEIGHT>", rpairs[3][1])
                txt = txt.replace("<ELEMENT_LENGTH>", rpairs[4][1])
                txt = txt.replace("<CABINE_HEIGHT>", rpairs[5][1])
                txt = txt.replace("<DETAILS_COLOR>", rpairs[6][1]) 
                txt = txt.replace("<ELEMENT_COLOR>", rpairs[7][1]) 
                txt = txt.replace("<TRUCK_COLOR>", rpairs[8][1])
                
                file6 = open(filePath + "\\Tank.dfa", "w")
                file6.write(txt)
                file6.close() 
                
            #GET
            theQuery = '''
            PREFIX kbe:<http://www.my-kbe.com/truck.owl#>
            SELECT ?truck ?element ?truckLength ?truckWidth ?elementLength ?elementHeight ?cabineHeight ?detailsColor ?elementColor ?truckColor
            WHERE
            {
                ?truck a kbe:Truck.
                ?truck kbe:hasElement ?element.
                ?truck kbe:hasTruckLength ?truckLength.
                ?truck kbe:hasTruckWidth ?truckWidth.
                ?truck kbe:hasElementHeight ?elementHeight.
                ?truck kbe:hasElementLength ?elementLength.
                ?truck kbe:hasCabineHeight ?cabineHeight.
                ?truck kbe:hasDetailsColor ?detailsColor.
                ?truck kbe:hasElementColor ?elementColor.
                ?truck kbe:hasTruckColor ?truckColor.
                } 
            '''
            URL = "http://127.0.0.1:3030/kbe/query"
            
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
                print("Truck:", res['truck']['value'])
                print("Element:", res['element']['value'])
                print("Truck Length:", res['truckLength']['value'])
                print("Truck Width:", res['truckWidth']['value'])
                print("Element Height:", res['elementHeight']['value'])
                print("Element Length:", res['elementLength']['value'])
                print("Cabine Height:", res['cabineHeight']['value'])
                print("Details Color:", res['detailsColor']['value'])
                print("Element Color:", res['elementColor']['value'])
                print("Truck Color:", res['truckColor']['value'])
            print("************************")
            #sino printeo de tipos aqui
            
            #CHECK
            h = False
            for res in iResults:
                if str(res['element']['value'])== str(rpairs[0][1]) and str(res['truckLength']['value'])==str(float(rpairs[1][1])) and  str(res['truckWidth']['value'])==str(float(rpairs[2][1])) and str(res['elementHeight']['value'])==str(float(rpairs[3][1])) and str(res['elementLength']['value'])== str(float(rpairs[4][1])) and str(res['cabineHeight']['value'])==str(float(rpairs[5][1])) and str(res['detailsColor']['value'])==str(rpairs[6][1]) and str(res['elementColor']['value'])==str(rpairs[7][1]) and str(res['truckColor']['value'])==str(rpairs[8][1]):
                    print("TRUE")
                    h = True
                else:
                    print("FALSE")
            if h == False:
                print("************************")
                print("UPLOAD WITH:")
                print("Element:", str(rpairs[0][1]))
                print("Truck Length:", str(float(rpairs[1][1])))
                print("Truck Width:", str(float(rpairs[2][1])))
                print("Element Height:", str(float(rpairs[3][1])))
                print("Element Length:", str(float(rpairs[4][1])))
                print("Cabine Height:", str(float(rpairs[5][1])))
                print("Details Color:", str(rpairs[6][1]))
                print("Element Color:", str(rpairs[7][1]))
                print("Truck Color:", str(rpairs[8][1]))
                print("************************")
                
                if str(rpairs[0][1]) == "TankElement":
                    URL = "http://127.0.0.1:3030/kbe/update"
                    theQuery = '''
                    PREFIX kbe:<http://www.my-kbe.com/truck.owl#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
                    INSERT
                    {
                    kbe:truck a kbe:Truck.
                    kbe:truck kbe:hasElement "TankElement"^^<http://www.w3.org/2001/XMLSchema#string>.
                    kbe:truck kbe:hasTruckLength "'''+str(float(rpairs[1][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasTruckWidth "'''+str(float(rpairs[2][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasElementHeight "'''+str(float(rpairs[3][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasElementLength "'''+str(float(rpairs[4][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasCabineHeight "'''+str(float(rpairs[5][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasDetailsColor "'''+str(rpairs[6][1])+'''"^^<http://www.w3.org/2001/XMLSchema#string>.
                    kbe:truck kbe:hasElementColor "'''+str(rpairs[7][1])+'''"^^<http://www.w3.org/2001/XMLSchema#string>.
                    kbe:truck kbe:hasTruckColor "'''+str(rpairs[8][1])+'''"^^<http://www.w3.org/2001/XMLSchema#string>.
                    }
                    WHERE
                    {}
                    '''
                    # sending get request and saving the response as response object 
                    r = requests.post(URL, theQuery)   
                    
                elif str(rpairs[0][1]) == "BoxElement":
                    URL = "http://127.0.0.1:3030/kbe/update"
                    theQuery = '''
                    PREFIX kbe:<http://www.my-kbe.com/truck.owl#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
                    INSERT
                    {
                    kbe:truck a kbe:Truck.
                    kbe:truck kbe:hasElement "BoxElement"^^<http://www.w3.org/2001/XMLSchema#string>.
                    kbe:truck kbe:hasTruckLength "'''+str(float(rpairs[1][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasTruckWidth "'''+str(float(rpairs[2][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasElementHeight "'''+str(float(rpairs[3][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasElementLength "'''+str(float(rpairs[4][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasCabineHeight "'''+str(float(rpairs[5][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasDetailsColor "'''+str(rpairs[6][1])+'''"^^<http://www.w3.org/2001/XMLSchema#string>.
                    kbe:truck kbe:hasElementColor "'''+str(rpairs[7][1])+'''"^^<http://www.w3.org/2001/XMLSchema#string>.
                    kbe:truck kbe:hasTruckColor "'''+str(rpairs[8][1])+'''"^^<http://www.w3.org/2001/XMLSchema#string>.
                    }
                    WHERE
                    {}
                    '''
                    # sending get request and saving the response as response object 
                    r = requests.post(URL, theQuery)
                
                if str(rpairs[0][1]) == "PlatformElement":
                    URL = "http://127.0.0.1:3030/kbe/update"
                    theQuery = '''
                    PREFIX kbe:<http://www.my-kbe.com/truck.owl#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
                    INSERT
                    {
                    kbe:truck a kbe:Truck.
                    kbe:truck kbe:hasElement "PlatformElement"^^<http://www.w3.org/2001/XMLSchema#string>.
                    kbe:truck kbe:hasTruckLength "'''+str(float(rpairs[1][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasTruckWidth "'''+str(float(rpairs[2][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasElementHeight "'''+str(float(rpairs[3][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasElementLength "'''+str(float(rpairs[4][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasCabineHeight "'''+str(float(rpairs[5][1]))+'''"^^<http://www.w3.org/2001/XMLSchema#float>.
                    kbe:truck kbe:hasDetailsColor "'''+str(rpairs[6][1])+'''"^^<http://www.w3.org/2001/XMLSchema#string>.
                    kbe:truck kbe:hasElementColor "'''+str(rpairs[7][1])+'''"^^<http://www.w3.org/2001/XMLSchema#string>.
                    kbe:truck kbe:hasTruckColor "'''+str(rpairs[8][1])+'''"^^<http://www.w3.org/2001/XMLSchema#string>.
                    }
                    WHERE
                    {}
                    '''
                    # sending get request and saving the response as response object 
                    r = requests.post(URL, theQuery)     



            
            
 
if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))

