class Util():

 def validate_num(num) :
    try :
        int ( num )
        return True
    except ValueError :
        print ( "enter valid integer value" )