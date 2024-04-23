from odoo import fields, models, api
import logging as log

class ProductProduct(models.Model):

    _inherit = 'product.product'

    id_exchange = fields.Integer()

    def update_product_from_controller(self, data):
        product = self.env['product.product']
        for dictt in data :
            #product_brand_id
            if dictt['product_brand_id']:
                brand = self.env['product.brand'].search([('id_exchange','=',dictt['product_brand_id'][0])])
                if not brand :
                    brand = self.env['product.brand'].create({'id_exchange': dictt['product_brand_id'][0],'name': dictt['product_brand_id'][1],'logo': dictt['product_brand_id'][2]})
                dictt['product_brand_id'] = brand.id

            #x_product_brand_id2
            if dictt['x_product_brand_id2']:
                brand2 = self.env['product.brand'].search([('id_exchange','=',dictt['x_product_brand_id2'][0])])
                if not brand2 :
                    brand2 = self.env['product.brand'].create({'id_exchange': dictt['x_product_brand_id2'][0],'name': dictt['x_product_brand_id2'][1],'logo': dictt['x_product_brand_id2'][2]})
                dictt['x_product_brand_id2'] = brand2.id


            #intrastat_code_id
            if dictt['intrastat_code_id']:
                intrastat = self.env['account.intrastat.code'].search([('code','=',dictt['intrastat_code_id'])])
                dictt['intrastat_code_id'] = intrastat.id if intrastat else False

            #intrastat_origin_country_id
            if dictt['intrastat_origin_country_id']:
                country = self.env['res.country'].search([('code','=',dictt['intrastat_origin_country_id'])])
                dictt['intrastat_origin_country_id'] = intrastat_origin_country_id.id if intrastat_origin_country_id else False
            

            #product_family_id
            if dictt['product_family_id']:
                family = self.env['product.family'].search([('id_exchange','=',dictt['product_family_id'][0])])
                if not family :
                    family = self.env['product.family'].create({'id_exchange': dictt['product_family_id'][0],'name': dictt['product_family_id'][1]})
                dictt['product_family_id'] = family.id


            #product_sub_family_id
            if dictt['product_sub_family_id']:
                subfamily = self.env['product.family'].search([('id_exchange','=',dictt['product_sub_family_id'][0])])
                if not subfamily :
                    subfamily = self.env['product.family'].create({'id_exchange': dictt['product_sub_family_id'][0],'name': dictt['product_sub_family_id'][1]})
                dictt['product_sub_family_id'] = subfamily.id

            #categ_id
            if dictt['categ_id']:
                categ = self.env['product.category'].search([('id_exchange','=',dictt['categ_id'])])
                dictt['categ_id'] = categ.id


            #capacity_ids
            if dictt['capacity_ids']:
                capacity = self.env['capacity'].search([('name','in',dictt['capacity_ids'])])

                missing_capacity_names = [capacity_name for capacity_name in dictt['capacity_ids'] if capacity_name not in set(capacity.mapped('name'))]
                for missing_capacity in missing_capacity_names:
                    capacity += self.env['capacity'].create({'name': missing_capacity})
                if not capacity :
                    dictt['capacity_ids'] = False
                   
                dictt['capacity_ids'] = [(6,0,capacity.ids)]


            #color_ids
            if dictt['color_ids']:
                color = self.env['color'].search([('name','in',dictt['color_ids'])])

                missing_color_names = [color_name for color_name in dictt['color_ids'] if color_name not in set(color.mapped('name'))]
                for missing_color in missing_color_names:
                    color += self.env['color'].create({'name': missing_color})
                if not color :
                    dictt['color_ids'] = False
                   
                dictt['color_ids'] = [(6,0,color.ids)]

            #container_ids
            if dictt['container_ids']:
                container = self.env['container'].search([('name','in',dictt['container_ids'])])

                missing_container_names = [container_name for container_name in dictt['container_ids'] if container_name not in set(container.mapped('name'))]
                for missing_container in missing_container_names:
                    container += self.env['container'].create({'name': missing_container})
                if not container :
                    dictt['container_ids'] = False
                   
                dictt['container_ids'] = [(6,0,container.ids)]

            #for_who_ids
            if dictt['for_who_ids']:
                for_who = self.env['for_who'].search([('name','in',dictt['for_who_ids'])])

                missing_for_who_names = [for_who_name for for_who_name in dictt['for_who_ids'] if for_who_name not in set(for_who.mapped('name'))]
                for missing_for_who in missing_for_who_names:
                    for_who += self.env['for_who'].create({'name': missing_for_who})
                if not for_who :
                    dictt['for_who_ids'] = False
                   
                dictt['for_who_ids'] = [(6,0,for_who.ids)]

            #shape_ids
            if dictt['shape_ids']:
                shape = self.env['shape'].search([('name','in',dictt['shape_ids'])])

                missing_shape_names = [shape_name for shape_name in dictt['shape_ids'] if shape_name not in set(shape.mapped('name'))]
                for missing_shape in missing_shape_names:
                    shape += self.env['shape'].create({'name': missing_shape})
                if not shape :
                    dictt['shape_ids'] = False
                   
                dictt['shape_ids'] = [(6,0,shape.ids)]


            #taxes_id
            if dictt['taxes_id']:
                taxes = self.env['account.tax'].search([('name','in',dictt['taxes_id'])])
                if not taxes :
                    dictt['taxes_id'] = False
                   
                dictt['taxes_id'] = [(6,0,taxes.ids)]

            my_prod = product.search([('id_exchange','=',dictt['id_exchange'])])  
            if my_prod :
                my_prod.write(dictt)
            else:
                product.create(dictt)

        return True 

   
class ProductCategory(models.Model):

    _inherit = 'product.category'

    id_exchange = fields.Integer()


    def update_category_from_controller(self, data):
        log.warning('in update_category_from_controller')
        category = self.env['product.category']
        for dictt in data :
            if dictt['parent_id']:
                parent = category.search([('id_exchange', '=',dictt['parent_id'] )])
                dictt['parent_id'] = parent.id if parent else False
            my_categ = category.search([('id_exchange','=',dictt['id_exchange'])])  
            if my_categ :
                my_categ.write(dictt)
            else:
                category.create(dictt)

        return True 


   
class ProductBrand(models.Model):

    _inherit = 'product.brand'

    id_exchange = fields.Integer()




   
class ProductFamily(models.Model):

    _inherit = 'product.family'

    id_exchange = fields.Integer()