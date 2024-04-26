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

            #container_ids
            if dictt['container_ids']:
                container = self.env['container'].search([('name','=',dictt['container_ids'])])
                if not container:
                    container = self.env['container'].create({'name': dictt['container_ids']})
                
                dictt['container_ids'] = container.id

            #shape_ids
            if dictt['shape_ids']:
                shape = self.env['shape'].search([('name','=',dictt['shape_ids'])])
                if not shape:
                    shape = self.env['shape'].create({'name': dictt['shape_ids']})
                
                
                dictt['shape_ids'] = shape.id


            #capacity_ids
            if dictt['capacity_ids']:
                capacity = self.env['capacity'].search([('name','in',dictt['capacity_ids'])])

                missing_capacity_names = [capacity_name for capacity_name in dictt['capacity_ids'] if capacity_name not in set(capacity.mapped('name'))]
                for missing_capacity in missing_capacity_names:
                    capacity += self.env['capacity'].create({'name': missing_capacity})
       
                   
                dictt['capacity_ids'] = [(6,0,capacity.ids)] if capacity else False


            #color_ids
            if dictt['color_ids']:
                color = self.env['color'].search([('name','in',dictt['color_ids'])])

                missing_color_names = [color_name for color_name in dictt['color_ids'] if color_name not in set(color.mapped('name'))]
                for missing_color in missing_color_names:
                    color += self.env['color'].create({'name': missing_color})
               
                dictt['color_ids'] = [(6,0,color.ids)] if color else False

            
            #for_who_ids
            if dictt['for_who_ids']:
                for_who = self.env['for_who'].search([('name','in',dictt['for_who_ids'])])

                missing_for_who_names = [for_who_name for for_who_name in dictt['for_who_ids'] if for_who_name not in set(for_who.mapped('name'))]
                for missing_for_who in missing_for_who_names:
                    for_who += self.env['for_who'].create({'name': missing_for_who})
              
                dictt['for_who_ids'] = [(6,0,for_who.ids)] if for_who else False

            

            #taxes_id
            if dictt['taxes_id']:
                taxes = self.env['account.tax'].search([('name','in',dictt['taxes_id'])])
   
                   
                dictt['taxes_id'] = [(6,0,taxes.ids)] if taxes else False

            keys_to_delete = [key for key, value in dictt.items() if value is False]
            for key in keys_to_delete:
                del dictt[key]
            my_prod = product.search([('id_exchange','=',dictt['id_exchange'])])  
            log.warning('dictt===================')
            log.warning(dictt)
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