from flask import  Flask, jsonify, request
from user import UserHandler
from supplier import SupplierHandler
from resource import ResourceHandler
app = Flask(__name__)


@app.route('/')
def index():
	return 'Disaster Site!'

#--------------------- Routes for Resouces -----------------------------

# Route that returns list of total resources or insert new resources
@app.route('/show/resource', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        return ResourceHandler().insert(request.form)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchRequested(request.args)


#--------ID

#Route used to get a resouce via its id
@app.route('/show/resource/id/<int:rid>')
def getResourceById(rid):
	return ResourceHandler().getResourceById(rid)

#Route check if specific id is available.
@app.route('/show/resource/id/<int:rid>/available')
def checkAvailable(rid):
	return ResourceHandler().isAvailable(rid)

#Route used to get list of supplier of specific resource.
@app.route('/show/resource/id/<int:rid>/supplier')
def getResourceSupplierById(rid):
	return ResourceHandler().getResourceSupplier(rid)

#Routes used to get suppliers of items in a specific location
@app.route('/show/resource/id/<int:rid>/locate/<location>')
def getResourcesSuppplierFrom(rid,location):
	return ResourceHandler().fromLocation(rid,location)

#--------Available

#Route used to get all available resouces
@app.route('/show/resource/available')
def getAvailableResource():
	return ResourceHandler().getAvailableResources()


#Route used to search available resources via keyword
@app.route('/show/resource/available/search/<keyword>')
def searchAvailable(keyword):
	return ResourceHandler().searchAvailable(keyword)

#--------Requested

#Route used to get all requested resouces
@app.route('/show/resource/requested')
def getRequestedResource():
	return ResourceHandler().getRequestedResources()

#Route used to search available resources via keyword. Sorted by Resouce name
@app.route('/show/resource/requested/search/<keyword>')
def searchRequested(keyword):
	return ResourceHandler().searchRequested(keyword)

#-----------------------------------------------------------------------

#--------------------- Routes for Suppliers ----------------------------

#Basic Route that returns list of total Suppliers.
@app.route('/show/supplier')
def showSupplier():
        return SupplierHandler().getAllSupplier();

#--------ID

#Basic Route that returns specific Suppliers.
@app.route('/show/supplier/id/<int:sid>')
def getSupplier(sid):
        return SupplierHandler().getSupplierbyId(sid);

#Basic Route that returns then list of resources specific supplier supplies.
@app.route('/show/supplier/id/<int:sid>/resource')
def getSupplierResources(sid):
        return SupplierHandler.getSupplierResources(sid);

#Basic Route that returns then list of resources specific supplier has sold.
@app.route('/show/supplier/id/<int:sid>/sold')
def getSupplierReceipts(sid):
        return SupplierHandler().getSupplierResorceSold(sid);

#-----------------------------------------------------------------------

#--------------------- Routes for User ---------------------------------

#Basic Route that returns list of total Users.
@app.route('/show/user' , methods=['GET','POST'])

def showUsers():
        if request.method == 'POST':
                return UserHandler().addUser(request.form)
        else:
                if not request.args:
                        return UserHandler().getAllUser()
                else:
                        return 'work for fucking gods sake'
    		



    # if request.method == 'POST':
    # 	print(request.form)
    # 	return UserHandler().addUser(request.form)
	# elif not request.args:
    # 	return UserHandler.getAllUser()
	# else:
    # 	return 'for fucks sake'
	

#-----------------------------------------------------------------------


if __name__ ==  "__main__":
	app.run(debug = True)
