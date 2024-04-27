from odoo import fields, models, api
import json
import base64
import logging as log


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        log.warning('create product temp ---------------')
        log.warning(vals)
        if not 'service_to_purchase' in vals:
            vals['service_to_purchase'] = False
        return super(ProductTemplate, self).create(vals)

class ProductProduct(models.Model):

    _inherit = 'product.product'

    id_exchange = fields.Integer()

    def update_product_from_controller(self, data):
        product = self.env['product.product']
        for dictt in data :
            #image_1920
            if "image_1920" in dictt  and dictt['image_1920']:
                dictt['image_1920'] = base64.decodebytes(dictt['image_1920'].encode('ascii'))

            #product_brand_id
            if "product_brand_id" in dictt  and dictt['product_brand_id']:
                brand = self.env['product.brand'].search([('id_exchange','=',dictt['product_brand_id'][0])])
                if not brand :
                    brand = self.env['product.brand'].create({'id_exchange': dictt['product_brand_id'][0],'name': dictt['product_brand_id'][1],
                                                            'logo':base64.decodebytes(dictt['product_brand_id'][2].encode('ascii'))})
                dictt['product_brand_id'] = brand.id

            #x_product_brand_id2
            if "x_product_brand_id2" in dictt  and dictt['x_product_brand_id2']:
                brand2 = self.env['product.brand'].search([('id_exchange','=',dictt['x_product_brand_id2'][0])])
                if not brand2 :
                    brand2 = self.env['product.brand'].create({'id_exchange': dictt['x_product_brand_id2'][0],'name': dictt['x_product_brand_id2'][1],
                                                            'logo': base64.decodebytes(dictt['x_product_brand_id2'][2].encode('ascii'))})
                dictt['x_product_brand_id2'] = brand2.id


            #intrastat_code_id
            if "intrastat_code_id" in dictt  and dictt['intrastat_code_id']:
                intrastat = self.env['account.intrastat.code'].search([('code','=',dictt['intrastat_code_id'])])
                dictt['intrastat_code_id'] = intrastat.id if intrastat else False

            #intrastat_origin_country_id
            if "intrastat_origin_country_id" in dictt  and dictt['intrastat_origin_country_id']:
                country = self.env['res.country'].search([('code','=',dictt['intrastat_origin_country_id'])])
                dictt['intrastat_origin_country_id'] = intrastat_origin_country_id.id if intrastat_origin_country_id else False
            

            #product_family_id
            if "product_family_id" in dictt  and dictt['product_family_id']:
                family = self.env['product.family'].search([('id_exchange','=',dictt['product_family_id'][0])])
                if not family :
                    family = self.env['product.family'].create({'id_exchange': dictt['product_family_id'][0],'name': dictt['product_family_id'][1]})
                dictt['product_family_id'] = family.id


            #product_sub_family_id
            if "product_sub_family_id" in dictt  and dictt['product_sub_family_id']:
                subfamily = self.env['product.sub.family'].search([('id_exchange','=',dictt['product_sub_family_id'][0])])
                if not subfamily :
                    subfamily = self.env['product.sub.family'].create({'id_exchange': dictt['product_sub_family_id'][0],'name': dictt['product_sub_family_id'][1]})
                dictt['product_sub_family_id'] = subfamily.id


            #container_ids
            if "container_ids" in dictt  and dictt['container_ids']:
                container = self.env['container'].search([('name','=',dictt['container_ids'])])
                if not container:
                    container = self.env['container'].create({'name': dictt['container_ids']})
                
                dictt['container_ids'] = container.id


            #shape_ids
            if "shape_ids" in dictt  and dictt['shape_ids']:
                shape = self.env['shape'].search([('name','=',dictt['shape_ids'])])
                if not shape:
                    shape = self.env['shape'].create({'name': dictt['shape_ids']})
                
                
                dictt['shape_ids'] = shape.id

            #label_ids
            if "label_ids" in dictt  and dictt['label_ids']:
                label = self.env['label'].search([('name','in',dictt['label_ids'])])
                if not label:
                    label = self.env['label'].create({'name': dictt['label_ids']})
                
                
                dictt['label_ids'] = label.id

            #categ_id
            if "categ_id" in dictt  and dictt['categ_id']:
                categ = self.env['product.category'].search([('id_exchange','=',dictt['categ_id'])])
                dictt['categ_id'] = categ.id

            #category2_id
            if "category2_id" in dictt  and dictt['category2_id']:
                categ = self.env['product.category'].search([('id_exchange','=',dictt['category2_id'])])
                dictt['category2_id'] = categ.id

            #category3_id
            if "category3_id" in dictt  and dictt['category3_id']:
                categ = self.env['product.category'].search([('id_exchange','=',dictt['category3_id'])])
                dictt['category3_id'] = categ.id

            #multi_categ_id
            if "multi_categ_id" in dictt  and dictt['multi_categ_id']:
                categ = self.env['product.category'].search([('id_exchange','in',dictt['multi_categ_id'])])
                dictt['multi_categ_id'] = [(6,0,categ.ids)]


            #capacity_ids
            if "capacity_ids" in dictt  and dictt['capacity_ids']:
                capacity = self.env['capacity'].search([('name','in',dictt['capacity_ids'])])

                missing_capacity_names = [capacity_name for capacity_name in dictt['capacity_ids'] if capacity_name not in set(capacity.mapped('name'))]
                for missing_capacity in missing_capacity_names:
                    capacity += self.env['capacity'].create({'name': missing_capacity})
       
                   
                dictt['capacity_ids'] = [(6,0,capacity.ids)] if capacity else False


            #color_ids
            if "color_ids" in dictt  and dictt['color_ids']:
                color = self.env['color'].search([('name','in',dictt['color_ids'])])

                missing_color_names = [color_name for color_name in dictt['color_ids'] if color_name not in set(color.mapped('name'))]
                for missing_color in missing_color_names:
                    color += self.env['color'].create({'name': missing_color})
               
                dictt['color_ids'] = [(6,0,color.ids)] if color else False

            
            #for_who_ids
            if "for_who_ids" in dictt  and dictt['for_who_ids']:
                for_who = self.env['for_who'].search([('name','in',dictt['for_who_ids'])])

                missing_for_who_names = [for_who_name for for_who_name in dictt['for_who_ids'] if for_who_name not in set(for_who.mapped('name'))]
                for missing_for_who in missing_for_who_names:
                    for_who += self.env['for_who'].create({'name': missing_for_who})
              
                dictt['for_who_ids'] = [(6,0,for_who.ids)] if for_who else False

            

            #taxes_id
            if "taxes_id" in dictt  and dictt['taxes_id']:
                taxes = self.env['account.tax'].search([('name','in',dictt['taxes_id'])])
   
                dictt['taxes_id'] = [(6,0,taxes.ids)] if taxes else False

            #supplier_taxes_id
            if "supplier_taxes_id" in dictt  and dictt['supplier_taxes_id']:
                taxes = self.env['account.tax'].search([('name','in',dictt['supplier_taxes_id'])])
   
                dictt['supplier_taxes_id'] = [(6,0,taxes.ids)] if taxes else False

            if "multi_barcode_ids" in dictt and dictt['multi_barcode_ids']:
                barcodes = self.env['product.multiple.barcodes']
                for val in dictt['multi_barcode_ids']:
                    exist = barcodes.search([('product_multi_barcode','=',val)])
                    if exist:
                        barcodes += exist
                    else :

                        barcodes += barcodes.create({'product_multi_barcode':val})
                dictt['multi_barcode_ids'] = [(6,0,barcodes.ids)] if barcodes else False

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

    def update_brand_from_controller(self, data):
        log.warning('in update_brand_from_controller')
        brand = self.env['product.brand']
        for dictt in data :
            if 'logo' in dictt and dictt['logo']:
                dictt['logo'] = base64.decodebytes(dictt['logo'].encode('ascii'))
                
            my_brand = brand.search([('id_exchange','=',dictt['id_exchange'])])  
            if my_brand :
                my_brand.write(dictt)
            else:
                brand.create(dictt)

        return True 




   
class ProductFamily(models.Model):

    _inherit = 'product.family'

    id_exchange = fields.Integer()

    def update_family_from_controller(self, data):
        log.warning('in update_family_from_controller')
        family = self.env['product.family']
        for dictt in data :
            if 'logo' in dictt and dictt['logo']:
                dictt['logo'] = base64.decodebytes(dictt['logo'].encode('ascii'))
                
            my_family = family.search([('id_exchange','=',dictt['id_exchange'])])  
            if my_family :
                my_family.write(dictt)
            else:
                family.create(dictt)

        return True 


class ProductFamily(models.Model):

    _inherit = 'product.sub.family'

    def update_subfamily_from_controller(self, data):
        log.warning('in update_subfamily_from_controller')
        subfamily = self.env['product.sub.family']
        for dictt in data :
            if 'logo' in dictt and dictt['logo']:
                dictt['logo'] = base64.decodebytes(dictt['logo'].encode('ascii'))
                
            my_subfamily = subfamily.search([('id_exchange','=',dictt['id_exchange'])])  
            if my_subfamily :
                my_subfamily.write(dictt)
            else:
                subfamily.create(dictt)

        return True 

    id_exchange = fields.Integer()