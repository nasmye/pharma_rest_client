from odoo import http
from odoo.http import request
import logging as log
import json

class RestClient(http.Controller):
    

    @http.route('/api/v1/db14/products', type='json', auth='none', methods=['POST'], csrf=False)
    def post_product_data(self, **post):

        body = request.httprequest.get_data()
        json_body = json.loads(body.decode('utf-8'))
        data = json_body['data']

  

        # Get the token from the request header
        auth_token = request.httprequest.headers.get('Authorization')

        my_token = request.env['res.company'].search([('token','=',auth_token)],limit=1).token
        # Check if the token is valid
        if not auth_token:
            return json.dumps({'error': 'Authorization token is missing'})

        
        # Validate the token (you may need to implement your own validation logic)
        # For example, you can check if the token matches a user's API token
        if not my_token or auth_token != my_token:
            return json.dumps({'error': 'Invalid authorization token'})

        # Retrieve data from the request body
        log.warning(data)
        
   
        # Update product quantity
        product = request.env['product.product'].sudo().search([],limit=1)
        product.with_context(from_controller=True).update_product_from_controller(data)
       
        # Return success response
        return json.dumps({'success': True})

    @http.route('/api/v1/db14/product_categories', type='json', auth='none', methods=['POST'], csrf=False)
    def post_product_category_data(self, **post):

        body = request.httprequest.get_data()
        json_body = json.loads(body.decode('utf-8'))
        data = json_body['data']


        # Get the token from the request header
        auth_token = request.httprequest.headers.get('Authorization')

        my_token = request.env['res.company'].search([('token','=',auth_token)],limit=1).token
        # Check if the token is valid
        if not auth_token:
            return json.dumps({'error': 'Authorization token is missing'})

        
        # Validate the token (you may need to implement your own validation logic)
        # For example, you can check if the token matches a user's API token
        if not my_token or auth_token != my_token:
            return json.dumps({'error': 'Invalid authorization token'})

        # Retrieve data from the request body
        log.warning(data)


        
        # Update product quantity
        category = request.env['product.category'].sudo().search([],limit=1)
        log.warning('category')
        log.warning(category)

        category.with_context(from_controller=True).update_category_from_controller(data)
       
        # Return success response
        return json.dumps({'success': True})