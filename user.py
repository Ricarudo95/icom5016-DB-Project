
from flask import jsonify
from userdao import UserDAO


class UserHandler:
    
    #------Building Dictionary for user query results

    def build_user_dict(self, row):
        result = {}
        result['User Id'] = row[0]
        result['First Name'] = row[1]
        result['SurName'] = row[2]
        result['Password'] = row[3]
        result['Location'] = row[4]
        result['Address'] = row[5]
       
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

     #------Building Dictionary for Creditcard query results    
    def build_creditcard_dict(self, row):
        result = {}
        result['Credit Card ID'] = row[0]
        result['User ID'] = row[1]
        result['Expiration Date'] = row[2]
        result['CVC Code'] = row[3]
        result['Active'] = row[4]
        result['Card Number'] = row[5]

        return result

    def build_transaction_dict(self, row):
        result = {}
        result['Transaction ID'] = row[0]
        result['Credit Card ID'] = row[1]
        result['Quantity'] = row[2]
        result['Price'] = row[3]
        result['Resource ID'] = row[4]
        result['User ID'] = row[5]
        result['Status'] = row[7]

        return result
    

    #------Returns all Users in the Database

    def getAllUser(self):
        dao = UserDAO()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    #------Recieves an User Id and the Retuns info of that User

    def getUserbyId(self, uid):
        dao = UserDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User = user);

    #------Recieves an User Id an the Retuns Suppliers the user has bought from.

    def getUserResources(self, uid):
        dao = UserDAO()
        resource_list = dao.getUserResources(uid)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(User_Resources = result_list)

    def updateUserCreditCard(self, form):
        if len(form) != 5:
            return jsonify(Error = "Malformed post request") , 400
        else:
            u_id= form.get("u_id")
            ccNumber=form.get("card_number")
            expDate=form.get("expiration_date")
            cvc_code=form.get("cvc_code")
            c_update=form.get("Update")

            if u_id and ccNumber and expDate and cvc_code and c_update:
                dao = UserDAO()
                card_list = dao.updateUserCreditCard(u_id, ccNumber, expDate, cvc_code, c_update)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
            
            
        result_list = []   
        for row in card_list:
            result = self.build_creditcard_dict(row)
            result_list.append(result)
        return jsonify(New_Cards = result_list)

    def addUser(self, form):
        if len(form) != 5:
            return jsonify(Error = "Malformed post request") , 400
        else:
            fname = form.get("uFirstName")
            lname = form.get("uLastName")
            upass = form.get("pass")
            loc = form.get("loc")
            address = form.get("address")
            if fname and lname and upass and loc and address:
                dao = UserDAO()
                u_id = dao.addUser(fname, lname, upass, loc, address)
                return self.getUserbyId(u_id)
                
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
    
    def createRequest(self, form):
        if len(form) !=3:
            return jsonify(Error = "Malformed post request") , 400
        else:
            qty = form.get("Quantity")
            u_id = form.get("User ID")
            r_id = form.get("Resource ID")
            if r_id and u_id and qty:
                dao = UserDAO()
                t_id = dao.createRequest(r_id, u_id, qty)
                transaction = self.build_transaction_dict (dao.getTransactionByID(t_id))
                return jsonify(Transaction=transaction)
            else:
                return jsonify(Error="Unexpected attributes in post request")
    
    def userPay(self,form):
        if len(form) != 3:
            return jsonify(Error = "Malformed post request") , 400
        else:
            t_id = form.get("Transaction ID")
            u_id = form.get("User ID")
            c_id = form.get("Credit Card ID")
            if t_id and u_id and c_id:
                dao = UserDAO()
                t_id = dao.userPay(t_id,u_id,c_id)
                if t_id == 'Error With Payment':
                    return t_id
                else:
                    transaction = self.build_transaction_dict (dao.getTransactionByID(t_id))
                    return jsonify(Transaction=transaction)
                

            else:
                 return jsonify(Error="Unexpected attributes in post request"), 400

    def getCardbyID(self, uid):
        dao = UserDAO()
        resource_list = dao.getUserCards(uid)
        result_list = []
        for row in resource_list:
            result = self.build_creditcard_dict(row)
            result_list.append(result)
        return jsonify(User_Cards = result_list)

    def getResourceBought(self,u_id):
        dao = UserDAO()
        resource_list = dao.getUserResourcesBought(u_id)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(User_Bought_Resources = result_list)

    def getResourceRequest(self,u_id):
        dao = UserDAO()
        resource_list = dao.getUserResourcesRequested(u_id)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(User_Requested_Resources = result_list)
    
    def getUserTransaction(self,u_id):
        dao = UserDAO()
        resource_list = dao.getUserTransaction(u_id)
        result_list = []
        for row in resource_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(User_Transactions = result_list)

    def userSearch(self,args):
        fname = args.get("First_Name")
        lname = args.get("Last_Name")
        loc = args.get("Loc")
        dao = UserDAO()
        user_list =[]
        if len(args) == 3:
            user_list = dao.getUserByFnameLnameLoc(fname,lname,loc)
        elif len(args) == 2 and fname and lname:
            user_list = dao.getUserByFnameLname(fname,lname)
        elif len(args) == 2 and fname and loc:
            user_list = dao.getUserByFnameLoc(fname,loc)
        elif len(args) == 2 and loc and lname:
            user_list = dao.getUserByLnameLoc(lname,loc)
        elif len(args) == 1 and fname:
            user_list = dao.getUserByFname(fname)
        elif len(args) == 1 and lname:
            user_list = dao.getUserByLname(lname)
        elif len(args) == 1 and loc:
            user_list = dao.getUserByLoc(loc)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)
            

           

    