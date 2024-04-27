from odoo import http
from odoo.http import request
import logging as log
import json

class RestClient(http.Controller):
        

    def _validate_token(self, auth_token):
        """Validate the authorization token."""
        my_token = request.env['res.company'].sudo().search([('token','=',auth_token)], limit=1).token
        if not auth_token:
            return False
        return auth_token == my_token



    @http.route('/api/v1/db14/products', type='json', auth='none', methods=['POST'], csrf=False)
    def post_product_data(self, **post):
        # Get the token from the request header
        auth_token = request.httprequest.headers.get('Authorization')
        if not self._validate_token(auth_token):
            return json.dumps({'error': 'Invalid authorization token'})

        #Get datas
        body = request.httprequest.get_data()
        data = json.loads(body.decode('utf-8'))['data']
       
        # Update product quantity
        product = request.env['product.product'].sudo().search([],limit=1)
        product.with_context(from_controller=True).update_product_from_controller(data)
       
        # Return success response
        return json.dumps({'success': True})

    @http.route('/api/v1/db14/product_categories', type='json', auth='none', methods=['POST'], csrf=False)
    def post_product_category_data(self, **post):

        # Get the token from the request header
        auth_token = request.httprequest.headers.get('Authorization')
        if not self._validate_token(auth_token):
            return json.dumps({'error': 'Invalid authorization token'})

        body = request.httprequest.get_data()
        data = json.loads(body.decode('utf-8'))['data']

        category = request.env['product.category'].sudo().search([],limit=1)
        category.with_context(from_controller=True).update_category_from_controller(data)
       
        # Return success response
        return json.dumps({'success': True})


    @http.route('/api/v1/db14/product_brands', type='json', auth='none', methods=['POST'], csrf=False)
    def post_product_brand_data(self, **post):
        # Get the token from the request header
        auth_token = request.httprequest.headers.get('Authorization')
        if not self._validate_token(auth_token):
            return json.dumps({'error': 'Invalid authorization token'})

        body = request.httprequest.get_data()
        data = json.loads(body.decode('utf-8'))['data']

        
        # Update product quantity
        brand = request.env['product.brand'].sudo().search([],limit=1)
        brand.with_context(from_controller=True).update_brand_from_controller(data)
       
        # Return success response
        return json.dumps({'success': True})

    @http.route('/api/v1/db14/product_families', type='json', auth='none', methods=['POST'], csrf=False)
    def post_product_family_data(self, **post):
        # Get the token from the request header
        auth_token = request.httprequest.headers.get('Authorization')
        if not self._validate_token(auth_token):
            return json.dumps({'error': 'Invalid authorization token'})

        body = request.httprequest.get_data()
        data = json.loads(body.decode('utf-8'))['data']

        
        # Update product quantity
        family = request.env['product.family'].sudo().search([],limit=1)
        family.with_context(from_controller=True).update_family_from_controller(data)
       
        # Return success response
        return json.dumps({'success': True})


    @http.route('/api/v1/db14/product_subfamilies', type='json', auth='none', methods=['POST'], csrf=False)
    def post_product_subfamily_data(self, **post):
        # Get the token from the request header
        auth_token = request.httprequest.headers.get('Authorization')
        if not self._validate_token(auth_token):
            return json.dumps({'error': 'Invalid authorization token'})

        body = request.httprequest.get_data()
        data = json.loads(body.decode('utf-8'))['data']

        
        # Update product quantity
        subfamily = request.env['product.sub.family'].sudo().search([],limit=1)
        subfamily.with_context(from_controller=True).update_subfamily_from_controller(data)
       
        # Return success response
        return json.dumps({'success': True})