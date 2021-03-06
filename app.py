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
            return ResourceHandler().searchResource(request.args)

#Route used to get a resouce via its id and update an existing resource
@app.route('/show/resource/id/<int:r_id>', methods=['GET', 'PUT'])
def getResourceById(r_id):
    if request.method == 'GET':
        return ResourceHandler().getResourceById(r_id)
    elif request.method == 'PUT':
        return ResourceHandler().update(r_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


#Route check if specific id is available.
@app.route('/show/resource/id/<int:rid>/available')
def checkAvailable(rid):
	return ResourceHandler().isAvailable(rid)

#Route used to get list of supplier of specific resource.
@app.route('/show/resource/supplier', methods=['GET'])
def getResourceSupplierById():
	return ResourceHandler().getResourceSupplier(request.args)

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
@app.route('/show/supplier',  methods=['GET','POST'])
def showSupplier():
        if request.method == 'POST':
                return SupplierHandler().addSupplier(request.form)
        else:
                return SupplierHandler().getAllSupplier()
               
#--------ID

#Basic Route that returns specific Suppliers.
@app.route('/show/supplier/id/<int:sid>')
def getSupplier(sid):
        return SupplierHandler().getSupplierbyId(sid);

#Basic Route that returns then list of resources specific supplier supplies.
@app.route('/show/supplier/resource/id/<int:s_id>')
def getSupplierResources(s_id):
        return SupplierHandler().getSupplierResources(s_id);

@app.route('/show/supplier/transactions/id/<int:sid>')
def getSupplierTransactions(sid):
        return SupplierHandler().getSupplierTransactions(sid);

#Basic Route that returns then list of resources specific supplier has sold.
@app.route('/show/supplier/sold/id/<int:sid>')
def getSupplierReceipts(sid):
        return SupplierHandler().getSupplierSold(sid);

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
                        return UserHandler().userSearch(request.args)
                
#Basic Route that returns specific User.
@app.route('/show/user/id/<int:uid>')
def getUser(uid):
    return UserHandler().getUserbyId(uid);

#Basic Route that returns list of total Users.
@app.route('/show/user/card' , methods=['POST'])
def userCards():
        return UserHandler().updateUserCreditCard(request.form)

@app.route('/show/user/card/id/<int:uid>')
def getUserCards(uid):
        return UserHandler().getCardbyID(uid)

@app.route('/show/user/request', methods = ['POST'])
def userRequests():
                return UserHandler().createRequest(request.form)

@app.route('/show/user/request/pay' , methods=['POST'])
def userPay():
        return UserHandler().userPay(request.form)

@app.route('/show/user/request/id/<int:uid>')
def getUserTransacactions(uid):
        return UserHandler().getUserTransaction(uid)

@app.route('/show/user/resource/acquired/id/<int:uid>')
def getUserBought(uid):
        return UserHandler().getResourceBought(uid)

@app.route('/show/user/resource/requested/id/<int:uid>')
def getUserRequested(uid):
        return UserHandler().getResourceRequest(uid)


#-----------------------------------------------------------------------


if __name__ ==  "__main__":
	app.run(debug = True)
