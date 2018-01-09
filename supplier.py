from flask import jsonify


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
        dao = SupplierDao()
        supplier_list = dao.getAllSupplier()
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers = result_list)

    #------Recieves an Supplier Id and the Retuns info of that supplier

    def getSupplierbyId(self, sid):
        dao = SupplierDao()
        row = dao.getSupplierbyId(uid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            supplier = self.build_Supplier_dict(row)
            return jsonify(Supplier = supplier);

    def getSuppierResources(self, sid):
    dao = SupplierDao()
    resource_list = dao.getSupplierResource()
    result_list = []
    for row in resource_list:
        result = self.build_resource_dict(row)
        result_list.append(result)
    return jsonify(Suppliers_Resources = result_list)

    def getSuppierResourceSold(self, sid):
    dao = SupplierDao()
    resource_list = dao.getSupplierResourceSold()
    result_list = []
    for row in resource_list:
        result = self.build_resource_dict(row)
        result_list.append(result)
    return jsonify(Suppliers_Resources = result_list)

