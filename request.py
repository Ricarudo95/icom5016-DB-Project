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
        return jsonify(Requests=result_list)
    
        def getRequestById(self, reqid):
	    req_list = [[1, 346, 436, 10] ,[2, 647,445, 1] , [3, 345,3434, 23]]
        row = req_list[reqid-1]
        if not row:
            return jsonify(Error = "Request Not Found"), 404
        else:
            request = self.build_resource_dict(row)
            return jsonify(Resquest = request)

    

    
