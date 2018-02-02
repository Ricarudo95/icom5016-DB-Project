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
    
    

    def getResourceSupplier(self, args):
        name = args.get("Name")
        cat = args.get("Category")
        loc = args.get("Location")
        dao = ResourceDAO()
        supplier_list = []

        if len(args) == 2 and name and loc:
            supplier_list = dao.supplierByNameAndLoc(name,loc)
        elif len(args) == 2 and cat and loc:
            supplier_list = dao.supplierByCatAndLoc(cat,loc)
        elif len(args) == 1 and name:
            supplier_list = dao.supplierByName(name)
        elif len(args) == 1 and cat:
            supplier_list = dao.supplierByCat(name)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

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

    def update(self, r_id, form):
        dao = ResourceDAO()
        if not dao.getResourceById(r_id):
            return jsonify(Error = "Resource not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                s_id= form['s_id']
                rname = form['rname']
                category = form['category']
                quantity = form['quantity']
                price = form['price']
                if rname and category and quantity and price:
                    dao = ResourceDAO()
                    dao.update(r_id, s_id, rname, category, quantity, price)
                    row = [r_id, s_id, rname, category, quantity, price]
                    result = self.build_resource_dict(row)
                    return jsonify(Resource=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
    
    def searchResource(self, args):
        name = args.get("Name")
        cat = args.get("Category")
        status = args.get("Status")
        dao = ResourceDAO()
        resource_list = []
        if len(args) == 2 and name and status == "Any":
            resource_list = dao.searchByName(name)
        elif len(args) == 2 and name and status ==  "Requested":
            resource_list = dao.searchByNameRequested(name)
        elif len(args) == 2 and name and status ==  "Available":
            resource_list = dao.searchByNameAvailable(name)
        elif len(args) == 2 and cat and status == "Any":
            resource_list = dao.searchByCat(name)
        elif len(args) == 2 and cat and status ==  "Requested":
            resource_list = dao.searchByCatRequested(cat)
        elif len(args) == 2 and cat and status ==  "Available":
            resource_list = dao.searchByCatAvailable(cat)
        elif len(args) == 1 and name:
            resource_list = dao.searchByName(name)
        elif len(args) == 1 and cat:
            resource_list = dao.searchByCat(cat)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

        
            