# -*- coding: utf-8 -*-
{
    'name': "project_digitalis",

    'summary': """
        Estiende el modulo de proyecto para manejar clientes y sus estados""",

    'description': """
       Test de Odoo para la versión 14/13

        Desarrolle un módulo que agregue un nuevo tab en la aplicación de Proyecto que permita:
        - Agregar clientes
        - De cada cliente se desea tener el estado del mismo
        - Los estados posibles tienen que poder ser gestionados desde la aplicación de Proyecto
        - La edición de los estados de los clientes en el proyecto solo la puede hacer un usuario con permisos de administración
        - Los posibles estados de un cliente en un proyecto son propios de cada compañía 
    """,

    'author': "Ernesto Ruiz",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/menus.xml',
        'views/views.xml',
    
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
