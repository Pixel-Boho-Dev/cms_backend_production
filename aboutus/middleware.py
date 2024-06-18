import json
import re
import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class NormalizeImagePathMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        content_type = response.get('Content-Type', '')

        if content_type.startswith('application/json'):
            try:
                data = json.loads(response.content.decode('utf-8'))

                def normalize_path(path):
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
                            if key == 'profile_pic' and isinstance(value, str):
                                logger.debug(f"Original profile_pic: {value}")
                                obj[key] = normalize_path(value)
                                logger.debug(f"Normalized profile_pic: {obj[key]}")
                            elif isinstance(value, (str, dict, list)):
                                update_paths(value)

                update_paths(data)
                response.content = json.dumps(data).encode('utf-8')
            except json.JSONDecodeError as e:
                logger.error(f"JSON decoding error: {e}")

        return response
