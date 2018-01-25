from flask import jsonify
from resourcedao import ResourceDAO


class ResourceHandler:
    
     #------Building Dictionary for Resources query results

    def build_resource_dict(self, row):
        result = {}
        result['Resource ID'] = row[0]
        result['Supplier ID'] = row[1]
        result['Resource Name'] = row[2]
        result['Category'] = row[3]
        result['Quantity'] = row[4]
        result['Price'] = row[5]

        return result

    #------Building Dictionary for Suppliers query results

    def build_supplier_dict(self, row):
        result = {}
        result['Suplier ID'] = row[0]
        result['Suplier Name'] = row[1]
        result['Password'] = row[2]
        result['Location'] = row[3]
        result['Address'] = row[4]
       
        return result

    #------Returns all Users in the Database

    def getAllResources(self):
        dao = ResourceDAO()
        resource_list = dao.getAllResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    #------Recieves an Resource Id and the Returns info of that Resource

    def getResourceById(self, rid):
        dao = ResourceDAO()
        row = dao.getResourceById(rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource = resource)

    #------Recieves an Resource Id and Location and returns appropriate suppliers

    def fromLocation(self, rid, location):
        dao = ResourceDAO()
        supplier_list = dao.getResourcesSuppplierFrom(rid,location)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Resource_Suppliers = result_list)

    #-------Check if Resource is avaiable.

    def isAvailable(self, rid):
        dao = ResourceDAO()
        status = dao.checkAvailableByID(rid)
        if not status:
            return 'False'
        else:
            return 'True'
    
    #------Recieves an Resource Id and the Returns list of Suppliers that have that resource.

    def getResourceSupplier(self, rid):
        dao = ResourceDAO()
        supplier_list = dao.getResourceSupplierById(rid)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Resource_Suppliers = result_list)

    #------Returns all Available resources in the Database

    def getAvailableResources(self):
        dao = ResourceDAO()
        resource_list = dao.getAvailableResource()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    #------Returns all Requested resources in the Database

    def getRequestedResources(self):
        dao = ResourceDAO()
        resource_list = dao.getRequestedResource()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    #------Search resourceses available witha specific keyword - INCOMPLETE

    def searchAvailable(self, args):
        dao = ResourceDAO()
        row = dao.searchAvailable(args)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource = resource)

    
    #------Search Requested resources with specific keyword - INCOMPLETE

    def searchRequested(self, args):
        dao = ResourceDAO()
        row = dao.searchRequested(args)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource = resource)

    def insert(self, form):
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            s_id= form['s_id']
            rname = form['rname']
            category = form['category']
            quantity = form['quantity']
            price = form['price']
            if rname and category and quantity and price:
                dao = ResourceDAO()
                rid = dao.insert(s_id, rname, category, quantity, price)
                row = [rid, s_id, rname, category, quantity, price]
                result = self.build_resource_dict(row) 
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
