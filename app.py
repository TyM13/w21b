from apihelper import check_endpoint_info
import dbhelper
from flask import Flask, request, make_response
import json

app = Flask (__name__)
#get request for the api /api/philosopher
@app.get('/api/philosopher')
def get_all_philosophers():
# runs the run_statment from dbhelper, calls the procedure philosopher_info.
    results = dbhelper.run_statment("CALL philosopher_info")
# checks to see if all items are == to a list
    if(type(results) == list):
# takes all_items and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 201
        return make_response(json.dumps(results, default=str), 201)
# takes all_items and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 400
    else:
        return make_response(json.dumps(results, default=str), 400)


#------------------------------------------------------------------------------------------------------#
# post request for the api /api/philosopher
@app.post('/api/philosopher')
def insert_a_philosopher():
#checks the endpoint for json and stores info as variable invalid, if invalid is not equal to none it will return an error
    invalid = check_endpoint_info(request.json, ['philosopher_name', 'philosopher_bio',
     'philosopher_date_of_birth', 'philosopher_date_of_death', 'philosopher_image'])
    if(invalid != None):
        return make_response(json.dumps(invalid), 400)
# calls the procedure insert_quote and takes in 5 arguements from the user, philosopher_name and philosopher_bio philosopher_date_of_birth
#philosopher_date_of_death philosopher_image
    results = dbhelper.run_statment('CALL insert_philosopher(?,?,?,?,?)',[
    request.json.get('philosopher_name'), request.json.get('philosopher_bio'), request.json.get('philosopher_date_of_birth'),
     request.json.get('philosopher_date_of_death'), request.json.get('philosopher_image')])
# checks to see if all items are == to a list
    if(type(results) == list):
# takes all_items and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 400
        return make_response(json.dumps(results, default=str), 200)
# takes all_items and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 400
    else:
        return make_response(json.dumps(results, default=str), 400)


#------------------------------------------------------------------------------------------------------#

#get request for the api /api/quote
@app.get('/api/quote')
def return_philosopher_quotes():
#checks the endpoint for args and stores info as variable invalid, if invalid is not equal to none it will return an error
    invalid = check_endpoint_info(request.args, ['philosopher_id'])
    if(invalid != None):
        return make_response(json.dumps(invalid), 400)
# calls the procedure insert_quote and takes in  arguements from the user philosopher_id  
    results = dbhelper.run_statment('CALL show_philosopher_quote(?)',
    [request.args.get('philosopher_id')])
# checks to see if all items are == to a list
    if(type(results) == list):
# takes all_items and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 400
        return make_response(json.dumps(results, default=str), 200)
# takes all_items and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 400
    else:
        return make_response(json.dumps(results, default=str), 400)


#------------------------------------------------------------------------------------------------------#

# post request for the api /api/quote
@app.post('/api/quote')
def inset_philosopher_quote():
# #checks the endpoint for json and stores info as variable invalid, if invalid is not equal to none it will return an error
    invalid = check_endpoint_info(request.json, ['quote_content', 'philosopher_id'])
    if(invalid != None):
        return make_response(json.dumps(invalid), 400)
# calls the procedure insert_quote and takes in 2 arguements from the user quote_content and philosopher_id
    results = dbhelper.run_statment('CALL insert_quote(?,?)', 
    [request.json.get('quote_content'), request.json.get('philosopher_id')])
# checks to see if all items are == to a list
    if(type(results) == list):
# takes all_items and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 400
        return make_response(json.dumps(results, default=str), 200)
    else:
# takes all_items and puts it in the format of json and if it can't convert, it will default to a string.
# if the make_respone fails it will send the error code 400
        return make_response(json.dumps(results, default=str), 400)
    



app.run(debug=True)