from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def fetch_endpoints(request):    
    endpoints = [
        {
            'authentication': [
                {
                    'login': {
                        'url': '/api/login', 
                        'type': 'POST',
                        'data_request': {
                            'email': 'string', 
                            'password': 'string'
                            },
                        'data_response': {
                            "token": "string",
                            "auth_user": {
                                "id": 'integer',
                                "information": {
                                    "id": 'integer',
                                    "name": "string",
                                    "phone": "string",
                                    "document": 'null',
                                    "photo": 'string',
                                    "created_at": "datetime",
                                    "user_auth": 'integer'
                                },
                                "password": "string",
                                "last_login": 'datetime',
                                "is_superuser": 'boolean',
                                "email": 'string',
                                "is_client": 'boolean',
                                "is_supplier": 'boolean',
                                "is_active": 'boolean',
                                "is_staff": 'boolean',
                                "groups": [],
                                "user_permissions": []
                            }
                        }
                    }
                },
                {
                    'signup': {
                        'url': '/api/signup', 
                        'type': 'POST',
                        'schema_request': {
                            'email': 'string', 
                            'password': 'string', 
                            'name': 'string', 
                            'phone': 'string'
                        },
                        'data_response': {
                             "token": "string",
                            "auth_user": {
                                "id": 'integer',
                                "information": {
                                    "id": 'integer',
                                    "name": "string",
                                    "phone": "string",
                                    "document": 'null',
                                    "photo": 'string',
                                    "created_at": "datetime",
                                    "user_auth": 'integer'
                                },
                                "password": "string",
                                "last_login": 'datetime',
                                "is_superuser": 'boolean',
                                "email": 'string',
                                "is_client": 'boolean',
                                "is_supplier": 'boolean',
                                "is_active": 'boolean',
                                "is_staff": 'boolean',
                                "groups": [],
                                "user_permissions": []
                            }
                        }
                    }
                },
                {
                    'logout': {
                        'url': '/api/logout',
                        'header': 'Authorization: Token <token>',
                        'type': 'POST',
                    }
                }
            ]
        },
        {
            'categories': [
                {
                    'structure': {
                        'url': '/api/structure',
                        'type': 'GET',
                        'data_response': {
                            "id": 'integer',
                            "name": "string",
                            "parent": "reference or null",
                            "active": 'boolean',
                            "children": [
                                {
                                    "id": 'integer',
                                    "name": "string",
                                    "parent": "reference or null",
                                    "active": 'boolean',
                                    "children": []
                                }
                            ]
                        }
                    }
                },
                {
                    'sectors': {
                        'url': '/api/sectors',
                        'type': 'GET',
                        'data_response': {
                            "id": 'integer',
                            "name": "string",
                            "parent": "integer or null",
                            "active": 'boolean',
                            "children": []
                        }
                    }
                },
                {
                    'categories': {
                        'url': '/categories',
                        'type': 'GET',
                        'data_response': {
                            "id": 'integer',
                            "name": "string",
                            "parent": "integer or null",
                            "active": 'boolean',
                            "children": []
                        }
                    }
                }
            ]
        },
        {
            'services': [
                {
                    'standard-services': {
                        'url': '/api/standard-services/{category_id}',
                        'type': 'GET',
                        'data_request': {
                            'category_id': 'integer'
                        },
                        'data_response': {
                            "id": 'integer',
                            "description": "string",
                            "category": 'reference'
                        }
                    }
                },
                {
                    'services-by-generalservice': {
                        'url': '/api/services-by-generalservice/{general_service_id}',
                        'type': 'GET',
                        'data_request': {
                            'standard_service_id': 'integer'
                        },
                        'data_response': {
                            "id": 'integer',
                            "supplier": {
                                "details": {
                                    "id": 'integer',
                                    "document_type": "string - CPF or CNPJ",
                                    "company_document_number": "string",
                                    "birthdate": "date",
                                    "company_name": "string",
                                    "company_name_show": "string",
                                    "owner_document_number": "string",
                                    "photo": "string",
                                    "term": 'boolean',
                                    "cnd": "string",
                                    "sign_at": "datetime",
                                    "segment": 'reference',
                                    "supplier": 'reference'
                                },
                                "address": {
                                    "id": 'integer',
                                    "street": "string",
                                    "number": "string",
                                    "complement": 'string',
                                    "neighborhood": "string",
                                    "city": "string",
                                    "state": "string",
                                    "postal_code": "string"
                                },
                                "owner_name": "string",
                                "email": "string",
                                "phone": "string",
                                "active": 'boolean',
                                "created_at": "datetime",
                                "updated_at": "datetime"
                            },
                            "price": "double",
                            "service_image": "string",
                            "requirements": "string",
                            "execution_time": 'integer',
                            "unit_of_execution": "string",
                            "active": 'boolean',
                            "created_at": "datetime",
                            "updated_at": 'datetime',
                            "general_service": 'reference',
                            "unit_for_service": 'reference',
                            "team": 'null or reference',
                            "workers": []
                        }
                    }
                },
                {
                    'service': '/api/service/{service_id}'
                }
            ]
        },
        {
            'suppliers': {
                'supplier': '/api/supplier/{supplier_id}',
                'supplier/services': '/api/supplier/{supplier_id}/services'
            }
        }
    ]
    
    
    
    return Response({'endpoints': endpoints}, status=200)