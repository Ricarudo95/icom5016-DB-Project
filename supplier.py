from flask import jsonify
from supplierdao import SupplierDAO


class SupplierHandler:
    
    #------Building Dictionary for Suppliers query results

    def build_supplier_dict(self, row):
        result = {}
        result['Suplier id'] = row[0]
        result['Suplier Name'] = row[1]
        result['Password'] = row[2]
        result['Location'] = row[3]
        result['Address'] = row[4]
       
        return result

    #------Building Dictionary for Resources query results

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['s_id'] = row[1]
        result['rname'] = row[2]
        result['category'] = row[3]
        result['quantity'] = row[4]
        result['price'] = row[5]
        result['adminitrator'] = row[6]
        result['transaction'] = row[7]

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

