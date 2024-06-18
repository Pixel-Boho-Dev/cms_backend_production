# yourapp/middleware.py

import json
from django.utils.deprecation import MiddlewareMixin
import re

class NormalizeImagePathMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.get('Content-Type') == 'application/json':
            try:
                data = json.loads(response.content.decode('utf-8'))
                
                def normalize_path(path):
                    # Ensure the path starts with /cms_backend/
                    if path and path.startswith("http"):
                        match = re.search(r'(/cms_backend/.*)', path)
                        if match:
                            return match.group(1)
                    if path and not path.startswith('/cms_backend/'):
                        return f'/cms_backend/{path.lstrip("/")}'
                    return path

                def update_paths(obj):
                    if isinstance(obj, dict):
                        for key, value in obj.items():
                            if isinstance(value, str) and 'icon' in key:
                                obj[key] = normalize_path(value)
                            else:
                                update_paths(value)
                    elif isinstance(obj, list):
                        for item in obj:
                            update_paths(item)

                update_paths(data)
                response.content = json.dumps(data).encode('utf-8')
            except json.JSONDecodeError:
                pass

        return response
