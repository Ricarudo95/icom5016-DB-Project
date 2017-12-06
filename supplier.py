from flask import jsonify


class SupplierHandler:
    
    
    def build_supplier_dict(self, row):
        result = {}
        result['Suplier id'] = row[0]
        result['Suplier Name'] = row[1]
        result['Password'] = row[2]
        result['Location'] = row[3]
        result['Address'] = row[4]
       
        return result


    def getAllSupplier(self):
        resources_list = [[24, 'Pollo_Inc', 'Pollosricos', 'Maya', 34] ,[26, 'Lechon_Inc', 'Navidad', 'Maya', 456 ] , [25, 'Gatos_Inc', 'Enamorado', 'Maya', 345 ]]
        result_list = []
        for row in resources_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)
