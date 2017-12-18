from flask import jsonify


class UserHandler:
    
    
    def build_user_dict(self, row):
        result = {}
        result['User Id'] = row[0]
        result['First Name'] = row[1]
        result['SurName'] = row[2]
        result['Password'] = row[3]
        result['Location'] = row[4]
        result['Address'] = row[5]
       
        return result


    def getAllUser(self):
        resources_list = [ [ 1, 'Eduardo', 'Vega','Elpapichulo98', 'Maya', 34]  , [2, 'Michelle', 'Santiago','TresTristesTigres', 'Maya', 456 ] ]
        result_list = []
        for row in resources_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserById(self, uid):
	users_list = [ [ 1, 'Eduardo', 'Vega','Elpapichulo98', 'Maya', 34]  , [2, 'Michelle', 'Santiago','TresTristesTigres', 'Maya', 456 ] ]
        
	row = users_list[uid-1]
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user)
