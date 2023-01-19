from typing import Dict
import base64
import json

from loguru import logger

class ByteConverter:

    @classmethod
    def serialize_to_bytes (cls, data: Dict) -> str:
        data_json = json.dumps(data)
        data_encoded = base64.b64encode(data_json.encode('ascii'))

        return data_encoded
    
    @classmethod
    def deserialize_to_dict (cls, encoded_bytes: str) -> Dict:

        try:
            
            data_bytes = base64.b64decode(encoded_bytes)
            data_json = data_bytes.decode('utf-8')
            data_dict = eval(data_json)

            return data_dict

        except UnicodeDecodeError as u:
            logger.error(f'Received error when trying to decode admin: {u}')