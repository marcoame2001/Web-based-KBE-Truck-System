# Length / Width / Height / Color / Path– Remember to update the template to work for <LENGTH>, <WIDTH> and <HEIGHT>

#desiner.py
#HTTP Server template / One parameter
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234 # Maybe set this to 1234
#file path of this python file
filePath =  'C:\\Users\\andreilo\\Desktop\\Temp\\DFAs' #NOTE! ASCII characters in the path - YOUR PATH HERE

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
		elif path.find("/info") != -1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes("<body><p>Let's change the side of the block</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/setSide") != -1:
			s.wfile.write(bytes('<html><body><h2>Block</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/setSide" method="post">', 'utf-8'))
			s.wfile.write(bytes('<label for="slength">Set Side:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="slength" name="slength" value="100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
		elif path.find("/setLWH") != -1:
			s.wfile.write(bytes('<html><body><h2>Block</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/setLWH" method="post">', 'utf-8'))
			s.wfile.write(bytes('<label for="slength">Set Length:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="slength" name="slength" value="100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="swidth">Set Width:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="swidth" name="swidth" value="100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="sheight">Set Height:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="sheight" name="sheight" value="100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="scolor">Set Color:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="scolor" name="scolor" value="CYAN"><br><br>', 'utf-8'))
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
		if path.find("/setSide") != -1:
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
			
			#Get the param value
			pair = param_line.split("=")
			
			#Open the template file
			f = open(filePath + "\\templates\\Colored_Block_2022_DYN.dfa", "r")
			txt = f.read()

			
			s.wfile.write(bytes('<html><body><h2>Block</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/setSide" method="post">', 'utf-8'))
			s.wfile.write(bytes('<label for="slength">Set Side:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="slength" name="slength" value="' + pair[1] +'"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			
			s.wfile.write(bytes('<p>The value of the side was set to ' + pair[1] + '</p>', 'utf-8'))
			
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
			
			# Replacing and writing the file to correct location
			txt = txt.replace("<SIDE>", pair[1])

			#Writing to the correct location
			f = open(filePath + "\\Colored_Block_2022_DYN.dfa", "w")
			f.write(txt)
			f.close()
			
		elif path.find("/setLWH") != -1:
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
			
			#Check if block is already there [Flag, Name]
			blockExists = s.checkIfBlockExists(rpairs[0][1], rpairs[1][1], rpairs[2][1])

			
			s.wfile.write(bytes('<form action="/setLWH" method="post">', 'utf-8'))
			s.wfile.write(bytes('<label for="slength">Set Length:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="slength" name="slength" value="100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="swidth">Set Width:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="swidth" name="swidth" value="100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="sheight">Set Height:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="sheight" name="sheight" value="100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="scolor">Set Color:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="scolor" name="scolor" value="CYAN"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			
			if blockExists[0]:
				s.wfile.write(bytes('<p>The block named ' + blockExists[1] + ' already exists.</p>', 'utf-8'))
				#Give a reference
			else:
				s.wfile.write(bytes('<p>The value of the sides were set to ' + str(rpairs) + '</p>', 'utf-8'))
				#Generate new one. Give reference.
				# Make new instance in ontology.
				# Define new instance name (= file name).
				import random
				fileName = "block" + str(random.randint(1, 10000))
				s.addBlockToOWL(rpairs, filePath, fileName) # Also a fine name 
				
				# Write new DFA file. 
				s.writeDFATemplate(filePath, rpairs)
			
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))


	def addBlockToOWL(self, pairs, folder, fileName):
		import requests 
		URL = "http://127.0.0.1:3030/kbe/update"
		theQuery = """
		PREFIX kbe:<http://www.my-kbe.com/shapes.owl#>
		PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
		INSERT
		{
		kbe:""" 

		theQuery = theQuery + fileName + " a kbe:Block.\nkbe:" 
		theQuery = theQuery + fileName
		theQuery = theQuery + " kbe:hasLength "
		theQuery = theQuery + "\""  + pairs[0][1] + "\"^^<http://www.w3.org/2001/XMLSchema#float>.\n kbe:"
		theQuery = theQuery	+ fileName
		theQuery = theQuery + "  kbe:hasWidth " + "\""  + pairs[1][1] + "\"^^<http://www.w3.org/2001/XMLSchema#float>.\n kbe:"
		theQuery = theQuery + fileName
		theQuery = theQuery + "  kbe:hasHeight " + "\""  + pairs[2][1] + "\"^^<http://www.w3.org/2001/XMLSchema#float>.\n kbe:"
		theQuery = theQuery + fileName
		theQuery = theQuery + "  kbe:hasColor " + "\""  + pairs[3][1] + "\"^^<http://www.w3.org/2001/XMLSchema#string>.\n kbe:"
		theQuery = theQuery + fileName
		completePath = folder + "\\" + fileName
		completePath = completePath.replace("\\", "/")
		theQuery = theQuery + "  kbe:hasPathToFile " + "\""  + completePath  + "\"^^<http://www.w3.org/2001/XMLSchema#string>.\n"
		theQuery = theQuery + " } WHERE {} "  
		
		print("The UPDATE Query:\n", theQuery)

		# sending get request and saving the response as response object 
		r = requests.post(URL, theQuery) 

	
	def writeDFATemplate(self, path, pairs):
		#Open the template file
		f = open(path + "\\templates\\Colored_Block_2022_DYN.dfa", "r")
		txt = f.read()
			
		# Replacing and writing the file to correct location
		txt = txt.replace("<LENGTH>", pairs[0][1])
		txt = txt.replace("<WIDTH>", pairs[1][1])
		txt = txt.replace("<HEIGHT>", pairs[2][1])
		txt = txt.replace("<COLOR>", pairs[3][1])

		#Writing to the correct location
		f = open(path + "\\Colored_Block_2022_DYN.dfa", "w")
		f.write(txt)
		f.close()
	
	def checkIfBlockExists(self, l, w, h):
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

		flagExists = False 
		blockName = ""

		#Recieved from web form
		inL = l + ".0"
		inW = w + ".0"
		inH = h + ".0"

		for res in iResults:
			print("************************")
			print("Block:", res['block']['value'])
			print("Lenght:", res['l']['value'])
			print("Width:", res['w']['value'])
			print("Height:", res['h']['value'])
			if inL == res['l']['value'] and inW == res['w']['value'] and inH == res['h']['value']:
				flagExists = True
				blockName = res['block']['value']
		print("************************")

		#Check if block exists.
		print("Block found: ", flagExists)
		
		return [flagExists, blockName]
			
 
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
