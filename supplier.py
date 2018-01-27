from flask import jsonify
from supplierdao import SupplierDAO


class SupplierHandler:
    
    #------Building Dictionary for Suppliers query results

    def build_supplier_dict(self, row):
        result = {}
        result['Supplier ID'] = row[0]
        result['Supplier Name'] = row[1]
        result['Password'] = row[2]
        result['Location'] = row[3]
        result['Address'] = row[4]
       
        return result

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

    #------Returns all Suppliers in the Database

    def getAllSupplier(self):
        dao = SupplierDAO()
        supplier_list = dao.getAllSuppliers()
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

    #------Recieves an Supplier Id and the Retuns info of that supplier

    def getSupplierbyId(self, sid):
        dao = SupplierDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            supplier = self.build_Supplier_dict(row)
            return jsonify(Supplier = supplier);

    #------Recieves an Supplier Id and the Retuns all reosurces that the supplier has.

    def getSupplierResources(self, sid):
        dao = SupplierDAO()
        resource_list = dao.getResourcesBySupplier(sid)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Suppliers_Resources = result_list)

    #------Recieves an Supplier Id and the Retuns all reosurces that the supplier has Sold.

    def getSupplierResourceSold(self, sid):
        dao = SupplierDAO()
        resource_list = dao.getSupplierResourceSold(sid)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Suppliers_Resources = result_list)

    def addSupplier(self, form):
        if len(form) != 3:
            return jsonify(Error = "Malformed post request") , 400
        sup_name = form.get("Supplier Name")
        sup_pass = form.get("Password")
        sup_loc = form.get("Location")

        if sup_name and sup_pass and sup_loc:
            dao = SupplierDAO()
            s_id = dao.addSupplier(sup_name, sup_pass, sup_loc)
            return self.getSupplierbyId(s_id)
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400



