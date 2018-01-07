from flask import  Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def index():
	return 'Disaster Site!'

#--------------------- Routes for Resouces -----------------------------

#Basic Route that returns list of total resources. Sorted by resource name.
@app.route('/show/resource')
def showResources():
    	return RHandle().getAllResources();

#--------ID

#Route used to get a resouce via its id
@app.route('/show/resource/id/<int:rid>')
def getResourceById(rid):
	return 'Resouce ' + str(rid) + ' Is a thingie'	

#Route check if specific id is available.
@app.route('/show/resource/id/<int:rid>/available')
def checkAvailable(rid):
	return 'Resouce ' + str(rid) + ' Is not here'	

#--------Supplier

#Route used to get list of aupplier of specific resource.
@app.route('/show/resource/supplier/<int:rid>')
def getResourceSupplierById(rid):
	return 'Resouce ' + str(rid) + ' Is made by Hasbro'	


#--------Available

#Route used to get all available resouces
@app.route('/show/resource/available')
def getAvailableResource():
	return 'All Elemenets available'


#Route used to search available resources via keyword
@app.route('/show/resource/available/search/<keyword>')
def searchAvailable(keyword):
	return 'Resouce ' + keyword + ' Is Available'

#--------Requested

#Route used to get all requested resouces
@app.route('/show/resource/requested')
def getRequestedResource():
	return 'All Elemenets requested'

#Route used to search available resources via keyword. Sorted by Resouce name
@app.route('/show/resource/requested/search/<keyword>')
def searchRequested(keyword):
	return 'Resouce ' + keyword + ' Is Available'

#-----------------------------------------------------------------------

#--------------------- Routes for Suppliers ----------------------------

#Basic Route that returns list of total Suppliers.
@app.route('/show/supplier')
def showSupplier():
    	return 'these are the suppliers';

#--------ID

#Basic Route that returns specific Suppliers.
@app.route('/show/supplier/id/<int:sid>')
def getSupplier(sid):
    	return 'Here is supplier ' + str(sid);

#Basic Route that returns then list of resources specific supplier supplies.
@app.route('/show/supplier/id/<int:sid>/resource')
def getSupplierResources(sid):
    	return 'these are all the things supplier ' + str(sid) + ' has. ';

#Basic Route that returns then list of resources specific supplier has sold.
@app.route('/show/supplier/id/<int:sid>/receipt')
def getSupplierReceipts(sid):
    	return 'these are all the things supplier ' + str(sid) + ' has sold. ';

#-----------------------------------------------------------------------

#--------------------- Routes for User ---------------------------------

#Basic Route that returns list of total Users.
@app.route('/show/user')
def showUsers():
    	return 'these are the user';

#--------ID

#Basic Route that returns specific Suppliers.
@app.route('/show/supplier/id/<int:uid>')
def getUser(sid):
    	return 'Here is user ' + str(uid);

#Basic Route that returns then list of resources specific user has bought or aquired.
@app.route('/show/supplier/id/<int:uid>/receipt')
def getUserReceipts(sid):
    	return 'these are all the things user ' + str(uid) + ' has bought. ';

#-----------------------------------------------------------------------


if __name__ ==  "__main__":
	app.run(debug = True)
