from flask import jsonify


class ResourceHandler:
    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['s_id'] = row[1]
        result['rname'] = row[2]
        result['category'] = row[3]
        result['quantity'] = row[4]
        result['price'] = row[5]
        return result


    def getAllResources(self):
        resources_list = [[1, 1, 'R1', 'Water-Small bottles', 5, 1 ], 
			  [2, 2,'R2', 'Medications', 10, 11], 
			  [3, 3,'R3', 'Baby Food', 4, 6]]
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self, rid):
        resources_list = [[1, 1, 'R1', 'Water-Small bottles', 5, 1] , [2, 2,'R2', 'Medications', 10, 11] , [3, 3,'R3', 'Baby Food', 4, 6]]
        row = resources_list[rid][0]
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource = resource)

    def searchResources(self, args):
        cartegory= args.get("category")
        resources_list = []

        if (len(args) == 1) and category:
            resources_list = []
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    
