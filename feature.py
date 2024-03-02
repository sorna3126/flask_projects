from flask import Flask 
FAI=Flask(__name__)

@FAI.route('/stringResponse')
def stringResponse():
    return 'Hai this is our first view of flask'



if __name__ =='__main__':
    FAI.run(debug=True)