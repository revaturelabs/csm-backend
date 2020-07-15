''' TODO : docstring '''

from flask import request, make_response, jsonify, Blueprint
import src.data as db


associates = Blueprint('associates', __name__)

@associates.route('/employees/<int:userId>')
class 
def put_employees_userId(userId):
    if request.method == 'PUT':
        bod = request.body
        swot_dict = {'Strengths': bod.Strengths,
                     'Weaknesses': bod.Weaknesses,
                     'Opportunities': bod.Opportunities,
                     'Threats': bod.Threats, 
                     'Notes': bod.Notes}
        
        return {}, 204
        