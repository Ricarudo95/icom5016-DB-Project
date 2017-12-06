from flask import jsonify


class RequestHandler:
    
    
    def build_request_dict(self, row):
        result = {}
        result['rq_id'] = row[0]
        result['u_id'] = row[1]
        result['r_id'] = row[2]
        result['qty_requested'] = row[3]
       
        return result


    def getAllRequest(self):
        resources_list = [[1, 346, 436, 10] ,[2, 647,445, 1] , [3, 345,3434, 23]]
        result_list = []
        for row in resources_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getRequestById(self, rid):
        resources_list = [[1, 1, 'R1', 'Water-Small bottles', 5, 1] , [2, 2,'R2', 'Medications', 10, 11] , [3, 3,'R3', 'Baby Food', 4, 6]]
        row = resources_list[rid][0]
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource = resource)

    # def searchResources(self, args):
    #     cartegory= args.get("category")
    #     resources_list = []

    #     if (len(args) == 1) and category:
    #         resources_list = []
    #     else:
    #         return jsonify(Error = "Malformed query string"), 400
    #     result_list = []
    #     for row in resources_list:
    #         result = self.build_resource_dict(row)
    #         result_list.append(result)
    #     return jsonify(Resources=result_list)

    
